#Imports
import sys
from telegram.ext import Updater
from telegram.ext import CommandHandler
from random import random
from random import choice
from random import randint
import pickle
import logging

#Telegram bot log
logging.basicConfig(
		format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
		level=logging.INFO)
logger = logging.getLogger(__name__)

#Dict with LocationTypeName : [all possible NPCs]	The enemies list is in order from weak to strong
locationTypes = {"Mountain": ['Worm', 'Moon Moon', 'Feral Frog', 'Feral Rock', 'Feral Cough', 'Squirrel', 'Flat Hat', 'Flop Hat', 'Old Computerscreen', 'Cloud', 'Fluffy Cloud', 'Head', 'Sneeze', 'Pile Of Snow', 'Old Summer Breeze', 'FatCat', 'Plofkip', 'Puppy', 'Kitten', 'Feral Slug', 'Feral Cat', 'Feral', 'Feral Hat', 'Goat', 'Hat', 'Rock', 'Ordinairy Rock', 'Pointy Stick', 'Big Snail', 'Lost Cyclist', 'Little Dwarf', 'Feral Dog', 'Brat', 'Red Hat', 'Mist', 'Falling Branch', 'Coyote', 'Flobglob', 'Lost Penguin', 'Snobtrobl', 'Dwarf', 'Feral ?', 'Feral Potato', 'Mad Brat', 'Broken Robot', 'Paperhat-Aeroplane', 'Black Dwarf', 'Feral Snake', 'Feral Tree', 'Saturday Music', 'Mountain Dog', 'Grass Monster', 'Small Wolf', 'Ginger Dwarf', 'Big Feral Cat', 'Goblin', 'Myst I', 'Blind Wolf', 'Armored Dwarf', 'Feral ??', 'Suare Hat', 'Hoblin', 'Moss Monster', 'Falling Tree', 'Pink Dwarft', 'Fat Dwarf', 'Big Feral Dog', 'Feral Owl', 'Froblin', 'Mean Teddybear', 'Magical Dwarf', 'Top Hat', 'Myst II', 'Rainy Cloud', 'Freddy', 'Master Dwarf', 'Feral ???', 'Troubled Dwarf', 'Angry Cucumber', 'King Dwarf', 'Feral Atomic Bomb', 'Rocky Snake', 'Robot', 'Wolf', 'Electric Dwarf', 'Flying Mittens', 'Mountain Goat', 'Rusty Moustache', 'Blood Wolf', 'Broblaglorb', 'Mad Trashcan', 'Evil Robot', 'Flying Zits', 'Evil Flower', 'Mechatronicon', 'Spaghetti Monster', 'Corrupted Hat'],
	"Field": ["Fieldguy 1-1", "Fieldguy 1-2", "Fieldguy 1-3", "Fieldguy 2-1", "Fieldguy 2-2", "Fieldguy 2-3", "Fieldguy 3-1", "Fieldguy 3-2", "Fieldguy 3-3"],
	"Road": ["Roadguy 1-1", "Roadguy 1-2", "Roadguy 1-3", "Roadguy 2-1", "Roadguy 2-2", "Roadguy 2-3", "Roadguy 3-1", "Roadguy 3-2", "Roadguy 3-3"]}

#Lists with items and possible adjectives. Again, the items go from weak to strong.
healingItems = ['Arsenic', 'Dirt', 'Water', 'Bread', 'Corn', 'Frog', 'Fluorine', 'Potato', 'Not So Hot Dog', 'Salad', 'Beans', 'Fish', 'Tooth Paste', 'Cucumber', 'Soda', 'Bunch Of Peas', 'Sandwich', 'Brew', 'Draught', 'Chicken Wing', 'Icecream', 'Hamburger', 'Apple', 'Tomato', 'Coffee', 'Cabbage', 'Cake', 'Honey', 'Portion Of French Fries', 'Mushroom', 'Canadian Bacon', 'Pancakes', 'Ketchup', 'Cookie', 'Maple Syrup', 'Soup', 'Waffle', 'Lizard', 'Medicine', 'Tea', 'Remedy', 'Potion', 'Cheese', 'Cupcake', 'Bacon', 'Chocolate', 'Strange Substance', 'Heroïn', 'Rice', 'Hugs In A Bottle', 'Unicorn Blood', 'Dessert Eagle', 'Chocolate Milk', 'Elixir']
healingItemsAdj = ['Probably Poisonous', 'Awful', 'Diarrhea Inducing', 'Moldy', 'Sucky', 'Diseased', 'Gross', 'Rotten', 'Bad', 'Wasted', 'From The Garbage Can', 'Fast Food', 'Dirty', 'Unhealthy', 'Barely Acceptable', 'Best Before: Two Weeks Ago', 'Hate Filled', 'Mediocre', 'Lacking Vitamins', 'Gay', 'Ok', 'Cheap', 'Nice', 'Fried', 'FDA Approved', 'Tasty', 'Fresh', 'Gluten Free', 'Herbal', 'Average', 'Vegetarian', 'Good', 'Grilled', 'Shake Before Usage', 'Ice Cold', 'Normal', 'Exhilarating', 'Moisturized', 'Catch Up', 'Standard', 'Filling', 'Yummy Yummy In My Tummy', '0% Fats', 'Great', 'Open Here', 'Cooked', 'Roasted', 'Love Infused', 'Cheesy', 'Chocolate', 'Super', 'Baked', 'Vegan', 'Special', 'Glowing', 'Sundried', 'Heroic', 'Makes You Vomit Rainbows', 'Glorious', 'Marinated', 'Awesome', 'Healthy', 'Exquisite']
weaponItems = ['Throwing Sand', 'Boots', 'Twig', 'Rock', 'Stone', 'Rubber Band', 'Butter Knife', 'Stick', 'Scissors', 'Fork', 'Bone', 'Shovel', 'Wrench', 'Magnets', 'Catapult', 'Lasso', 'Water Gun', 'Bear Hugs', 'Crowbar', 'Boxing Glove', 'Piece Of Glass', 'Bowling Ball', 'Chair', 'Club', 'Hammer', 'Blowgun', 'Boomerang', 'Bear Hands', 'Cheese Rasp', 'Razor', 'Knife', 'Baseball Bat', 'Saw', 'Tomahawk', 'Dagger', 'Axe', 'Machete', 'Bow And Arrow', 'Shuriken', 'Sai', 'Spear', 'Staff', 'Guitar', 'Cutlass', 'Crossbow', 'Nunchucks', 'Poison', 'Sword', 'Magic Wand', 'Rapier', 'Musket', 'Mace', 'Lance', 'Flail', 'Nail Gun', 'Blow Torch', 'Flintlock Rifle', 'Katana', 'Mines', 'Battleaxe', 'Revolver', 'Tazer', 'Cannon', 'Bombs', 'Bucket Of Lava', 'Piano String', 'Bubble Blaster', 'Bible', 'Thora', 'Koran', 'Pistol', 'Mysterious Syringe', 'Lawn Mower', 'Unholy Tome', 'Flame Thrower', 'Shotgun', 'Unidentified Weapon', 'Rifle', 'Sledge Hammer', 'Dynamite', 'Submachine Gun', 'Radioactive Barrel', 'Grand Piano', 'Chainsaw', 'Machine Gun', 'Sniper Rifle', 'Grenade', 'Spoon', 'Solar Flare', 'Excalibur', 'AK 47', 'Desert Eagle', 'Molotov Cocktail', 'Bazooka', 'Microwave', "Dragon's Tail", 'Javelin', 'Grenade Launcher', 'RPG', 'Unicorn Horn', 'X-57613C', 'Minigun', 'Gatling Gun', 'Tank']
weaponItemsAdj = ['Broken', 'Cardboard', 'Old', 'Toy', 'Dull', 'Weaponized', 'Plastic', 'Imaginary', 'Implausible', 'Anticlimactic', 'Rusty', 'Lite', 'Inferior', 'N00by', 'Origami', 'Dead Battery', 'Oil Leaking', 'Unreliable', 'Glass', 'Adorable', 'Wooden', 'Bolt Action', 'Pocket', 'Light', 'Steam Powered', 'Not So Bad', 'Bloody', "Cowboy's", 'Wi-Fi Enabled', 'Sharp', 'Spiked', 'Competent', 'Steel', "Gentleman's", 'Fearsome', 'Semi Automatic', 'Waterproof', 'Hands Free', 'Good', 'Medieval', 'Adjustable', 'Flaming', 'Suspicious', 'Shiny', 'Scoped', 'Dug Up', 'Dangerous', 'Stable', 'Steady', 'Mechanical', 'Environment Friendly', 'Portable', 'Electrical', 'Powerful', 'Great', 'Shocking', 'Do It Yourself', 'Laser', 'Shafting', 'Energized', 'Huge', 'Ninja', 'Accurate', 'Full Automatic', 'Ruby Inlaid', 'White Hot', 'Blinding', 'Super', 'Dual', 'Intangible', 'Crushing', 'Heavy', 'Epic', 'Stunning', 'Fear Powered', 'Digital', 'Melting', 'Special', 'Crippling', 'Holy', 'Invisible', 'Precise', 'Rocket Propelled', 'Undefined', 'Explosive', 'Laser Guided', 'Head Popping', 'Legendary', 'Smart', 'Plasma', 'Lovely', 'Hydrogen', 'Celestrial', 'Limited Edition', '.50 Cal', "Wizard's", "Rachmaninoff's", 'Magical', 'Majestic', 'Very Special', 'Sacred', 'Demonic', 'Four Dimensional', 'Theoratical', 'Antimatter', 'Alien', "Master's", 'Perfect']
armorItems = ['Underwear', 'Bra', 'Body Paint', 'Fierce Frown', 'Paper Shopping Bag Hat', 'Trousers', 'Arm Protectors', 'Leg Protectors', 'Bikini', "Fuck This Shit I'm Going Naked", 'Sweater', 'Back Protectors', 'Hat', 'Earcuffs', 'Chest Protectors', 'Water Wings', 'Cooking Pan Helmet', 'Head Protectors', 'Goggles', 'Fake Mustache', 'Arm Plating', 'Cape', 'Hockey Mask', 'Leg Plating', 'Gloves', 'Bucket Helmet', 'Back Plating', 'Kilt', 'Pumpkin Helmet', 'Chest Plating', 'Real Helmet', 'Boots', 'Head Plating', 'Suit', 'Arm Armor', 'Garbage Can Lid Shield', 'Leg Armor', 'Crown', 'Back Armor', 'Shield', 'Chest Armor', 'Vest', 'Head Armor', 'Power Suit', 'Arm Power Armor', 'Turtle Shell', 'Leg Power Armor', 'Reactive Armor', 'Back Power Armor', 'Power Shield', 'Sarcasm', 'Top Hat', 'Chest Power Armor', 'Magical Barrier', 'Head Power Armor', 'Tank']
armorItemsAdj = ['Old', 'Broken', 'Gross', 'Skin', 'Pre Historic', 'Ripped', 'Unwashed', 'Aluminum Foil', 'Black', 'Wooden', 'Trashy', 'Implausible', 'Made In China', 'Brittle', 'Hole Filled', 'Shabby', 'Cardboard', 'Inferior', 'Weak', 'Hide', 'Paper', 'Slippery', 'Falling Apart', 'Leather', 'Slutty', 'Homemade', 'Light', 'Not So Bad', 'Duct Tape', "Gentleman's", 'Good', 'Copper', 'Sneaking', 'Protective', 'Roman', 'Cool', 'Bronze', 'Feathered', 'Makes You Look Skinny', 'Fireproof', 'Tough', 'Shiny', 'Huge', 'Analog', 'Iron', 'Made In Germany', 'Special', 'Sparkling', 'Stunning', 'Super', 'White', 'Winged', 'Steel', 'Heavy', 'Bulletproof', 'Holy', 'Invisible', 'Spock', 'Beautiful', 'Twinkling', 'Emerald Inlaid', 'Legendary', 'Sacred', 'Ironic', 'Dragon Scales', 'Bad As Badass', 'Fabulously Amazebaltastic', 'Futuristic', 'Unicorn Hide', 'Asian', "Master's", 'Perfect']

noWeaponDamage = 4 #Players can't do anything if they can't fight. Useful when testing.

locations = {} #Multidimensional dictionary with coordinates and their location objects {x : {y : object}}
creatures = {} #All creature id's and their objects {id : object}. Contains players as well.
bank = {} #Bank-stored gold for each player {id : amount}
ids = [True] #Remembers currently taken ids for items and NPCs, False means taken. Doesn't contain players. 
messageCount = 0 #Keeps track of number of send messages, saves after every 20.
items = {} #Items dictionary {id : object}

#References to creatures, locations etc. cannot be real object-references because of troubles with saving to file. Instead, coordinates, id numbers or strings are used.

#classes
class location:
	def __init__(self, x, y, locationType, level):
		self.x = x #Locations dict coordinates
		self.y = y
		self.locationType = locationType #Terrain type: Mountain, Field, etc.
		self.level = level
		self.population = [] #Contains NPC ids
		self.players = [] # " player
	
	#Add or remove a NPC or player from the lists:
	def populationAdd(self, id):
		if not id in self.population:
			self.population += [id]
	
	def populationRemove(self, id):
		if id in self.population:
			self.population.pop(self.population.index(id))
	
	def playerEnters(self, id):
		if not id in self.players:
			self.players += [id]
	
	def playerLeaves(self, id):
		if id in self.players:
			self.players.pop(self.players.index(id))
		
	#Display its own stats:
	def info(self):
		message = ("Terrain: " + self.locationType + 
			"\nCoordinates: " + coordsFormat(self.x, self.y) +  #A fancier format of the coordinates
			"\nDifficulty: " + getRating(self.level)) #easy, hard etc. instead of level number
		if bool(self.population): #players and npc in the location:
			message += "\nCreatures: "
			for i in self.population:
				message += "\n" + creatures[i].name + " (" + str(creatures[i].id) + ")"
		message += "\nPlayers: "
		for i in self.players:
			message += "\n" + creatures[i].id
		return message

class creature:
	def __init__(self, x, y, id, creatureType, level):	
		self.x = x #Initial location
		self.y = y
		locations[x][y].populationAdd(self.id)
		self.id = id #Refer to the creature (ingame as well) with this number
		self.level = level #Initial level
		self.creatureType = creatureType #The creature name, for players it's "Player" to distinct players and NPCs.
		self.name = self.creatureType
		first = self.name[0].lower() #Should it be reffered to with "a" or "an"?
		if first == "a" or first == "e" or first == "i" or first == "o" or first == "u":
			self.n = "n"
		else:
			self.n = ""
		self.maxHp = getLevelHp(level) #hp cannot exceed this value, based the creature's level.
		self.hp = self.maxHp
		self.damage = getItemEffect("Weapon", level) #NPCs get weapon and armor ratings as if they had weapons of their own level
		self.armor = getItemEffect("Armor", level)
			

	def teleport(self, x, y): #Move to location x, y. 
		try:
			locations[self.x][self.y].populationRemove(self.id) #It could happen that a creature is not actually in a location
		except:
			pass
		locations[x][y].populationAdd(self.id)
		self.x = x
		self.y = y
		
	def die(self): #Respawn without gold and xp if it is a player, delete if it is a NPC.
		if self.creatureType == "Player":
			self.xp = 0
			self.gold = 0
			self.hp = self.maxHp
			self.deaths += 1
			self.teleport(0, 0)

		else:
			ids[self.id] = True
			locations[self.x][self.y].populationRemove(self.id)
			del creatures[self.id]
			
	def attack(self, targetId): #Checks if attack is possible, subtracts a certain damage, handles death and rewards.
		if self.x == 0 and self.y == 0:
			return ["You can't fight when in Cromania. ", False] #The return value is checked for the message and whether the victim fights back (only if the victim is a NPC and doesn't die).
		if targetId in locations[self.x][self.y].players: #If the target is a player and in the right location...
			target = creatures[targetId]
			if self == target:
				self.die()
				return ["You commited suïcide and lost all your gold. ", False]
			if self.damage > target.armor: #Ignore if the damage isn't greater than the target's armor.
				min = round((self.damage - target.armor)/2)
				if min == 0:
					min = 1 #At least one damage point.
				max = self.damage - target.armor
				damage = randint(min, max)
				target.hp -= damage
				message = self.name + " dealt " + str(damage) + " damage to " + target.name + ". "
				if target.hp <= 0:
					message += self.name + " killed " + target.name + "! "
					if self.creatureType == "Player": #If the attacker is a player:
						self.gold += target.gold #Get victim's gold. Victim loses it througth their die() method.
						self.playerKills += 1 #Keep track of the number of players someone killed.
						message += "You took all gold (" + str(target.gold) + ") from " + target.name + ". "
					if self.creatureType == "Player" and target.level - self.level >= -4: #Don't get xp when an enemy has a much lower level.
						message += self.gainXp(round(0.5 * (target.level - self.level + 6) ** 1.5)) #Gain xp by some formula based on both levels
					target.die()
				else:
					message += target.name + " still has " + str(target.hp) + " health. "
			else:
				return [target.name + " absorbed all damage... ", False]
		
		elif targetId in locations[self.x][self.y].population: #...or a NPC in the right location:
			fightBack = True #If a NPC is attacked and does not die, it will attack back.
			target = creatures[targetId]
			if self.damage > target.armor:
				min = round((self.damage - target.armor)/2)
				if min == 0:
					min = 1
				max = self.damage - target.armor
				damage = randint(min, max)
				target.hp -= damage
				message = self.name + " dealt " + str(damage) + " damage to the " + target.name + ". "
				if target.hp <= 0:
					message += self.name + " killed the " + target.name + "! "
					self.kills += 1
					message += getReward(self, target.level) #Get a randomly generated reward base on the victim's level.
					fightBack = False
					if self.creatureType == "Player" and target.level - self.level >= -4:
						message += self.gainXp(round(0.5 * (target.level - self.level + 6) ** 1.5))
					target.die()
				else:
					message += "The " + target.name + " still has " + str(target.hp) + " health. "
					fightBack = True
			else:
				return ["The " + target.name + " absorbed all damage... ", fightBack]
		else:
			return ["Target doesn't exist in this location. ", fightBack]
		return [message, fightBack]
		
	def heal(self, amount): #Add HP and reset if the result exceeds maxHp.
		self.hp += amount
		if self.hp > self.maxHp:
			self.hp = maxHp
	
	def stats(self): #Print the creature's stats.
		return "Name: " + self.name + \
			"\nId: " + str(self.id) + \
			"\nLevel: " + str(self.level) + \
			"\nHp: " + str(self.hp) + "/" + str(self.maxHp) + \
			"\nDamage: " + str(self.damage) + \
			"\nArmor: " + str(self.armor) + \
			"\nCoordinates: " + coordsFormat(self.x, self.y)

class inventory: #A class that can manage items. Used for shop and players.
	def __init__(self, id):
			self.id = id
			self.inventory = [] #Holds the item ids
			
	def gainItem(self, itemId): #Add or remove an item from this inventory:
		if not itemId in self.inventory:
			self.inventory += itemId

	def dropItem(self, itemId):
		if itemId in self.inventory:
			self.inventory.pop(self.inventory.index(id))
		
class player(creature, inventory):
	def __init__(self, id): #Todo: sepparate ids and names
		self.x = 0 #Starts in Cromania
		self.y = 0
		locations[0][0].playerEnters(id)
		self.id = id #How to refer to this player
		self.creatureType = "Player" #Distinct from creatures
		self.name = id #Used for messages
		self.level = 1 #Start at level 1, max 100
		self.xp = 0 #Level up when a player reaches a certain xp amount, amount increases per level.
		self.maxHp = 10
		self.hp = 10 #Initial hp
		self.damage = noWeaponDamage #Initial stats
		self.armor = 0
		self.gold = 0 #Gold that the player currently has on them. One loses it on death.
		bank[id] = 10 #Money that is safe from dangers.
		self.playerKills = 0 #Remember how many players someone has killed.
		self.kills = 0 #Remember how many NPCs someone has killed.
		self.deaths = 0 #Remember how often someone has died.
		self.inventory = [] #Id's of items in inventory.
		self.equipped = [-1, -1] #Id's of equipped items: [weapon, armor]. -1 means nothing equiped.
	
	def move(self, args): #Move between locations, checks for valid input, can move in 8 directions, distance multiplier is limeted to one's level. Eg: "/m se 5" moves some 5 locations south, 5 locations east.
		direction = str(args[0]) #First user input ("/m" base command is ignored)
		if not(direction == "n" or direction == "s" or direction == "w" or direction == "e" or direction == "ne" or direction == "nw" or direction == "se" or direction == "sw"):
			return "You passed an invalid direction! " #Valid direction?
		fleeChance = 0 #The more enemies and the higher their levels, the lower the chance to be able to move. The chance is "player levels / sum of enemy levels".
		for i in locations[self.x][self.y].population:
			fleeChance += creatures[i].level #Get all creature levels
		if not fleeChance:
			fleeChance = 1 #1 if there is no creature
		fleeChance = self.level / fleeChance #
		if fleeChance > random(): #Random chance
			multiplier = 1 #If no multiplier variable is given, move only one.
			try:
				multiplier = int(args[1]) #Second user input, see if it is a valid number and <= player level 
				if multiplier > self.level:
					return "The multiplier can only be as high as your level."
			except ValueError: #Error if multiplier cannot be converted
				return "Invalid multiplier. "
			except IndexError: #Ignore if no multiplier is given
				pass
			
			locations[self.x][self.y].playerLeaves(self.id) #Leave old location
			
			if direction == "n": #Calculate new coordinates
				self.y += multiplier
			elif direction == "s":
				self.y -= multiplier
			elif direction == "w":
				self.x -= multiplier
			elif direction == "e": 
				self.x += multiplier
			elif direction == "ne":
				self.y += multiplier
				self.x += multiplier
			elif direction == "nw":
				self.y += multiplier
				self.x -= multiplier
			elif direction == "se": 
				self.y -= multiplier
				self.x += multiplier
			else:
				self.y -= multiplier
				self.x -= multiplier
				
			if not self.x in locations: #Create new a new location if it doesn't exist, newLocation() returns a message with info of the location.
				message = newLocation(self.x, self.y, choice(list(locationTypes.keys())), abs(self.level + randint(-2, 2)))
			elif not self.y in locations[self.x]:
				message = newLocation(self.x, self.y, choice(list(locationTypes.keys())), abs(self.level + randint(-2, 2)))
			else:
				message = "Terrain: " + locations[self.x][self.y].locationType + ". " #Or tell what already discovered location a player is in:
			locations[self.x][self.y].playerEnters(self.id)
			return "You now are in " + coordsFormat(self.x, self.y) + ". " + message
		else: #If one fails to move, it is attacked by a random creature in the location.
			return "You failed to flee and were attacked! " + creatures[choice(locations[self.x][self.y].population)].attack(self.id)[0] #The first thing in the list is the attack message, the second the fightBack boolean.
	
	def gainXp(self, xp): #Handle xp rewards, level ups and max level.
		if xp <= 0: #Ignore if no xp
			return
		if self.level < 100: #Ignore if already level 100
			message = "You gained " + str(xp) + " XP. " #End with a space for ongoing messages.
			self.xp += xp
			while self.xp >= getLevelXp(self.level): #getLevelXp() gives the amount xp needed to level up. Keep leveling up when total xp is greater than this value.
				self.xp -= getLevelXp(self.level)
				self.level += 1
				self.maxHp = getLevelHp() #The only thing that directly changes when leveling up is maxHp. 
				message += "You leveled up! You are now level " + str(self.level) + ". "
			if self.level >= 100:
				self.xp = 0
				return self.name + " reached level 100!!! You can no longer gain XP. " #Ignore previous message.
			message += "You now have " + str(self.xp) + " XP. "
			return message
		else:
			return ""
	
	def teleport(self, x, y): #Locations use different methods when a player moves then when a NPC does
		try:
			locations[self.x][self.y].playerLeaves(self.id)
		except Exception:
			pass
		locations[x][y].playerEnters(self.id)
		self.x = x
		self.y = y
	
	def stats(self): #All the player's stats
		return "Id: " + self.name + \
			"\nLevel: " + str(self.level) + \
			"\nXp: " + str(self.xp) + "/" + str(getLevelXp(self.level)) + \
			"\nHp: " + str(self.hp) + "/" + str(self.maxHp) + \
			"\nDamage: " + str(self.damage) + \
			"\nArmor: " + str(self.armor) + \
			"\nGold: " + str(self.gold) + \
			"\nBank: " + str(bank[self.id]) + \
			"\nCoordinates: " + coordsFormat(self.x, self.y) + \
			"\nPlayer kills: " + str(self.playerKills) + \
			"\nNPC kills: " + str(self.kills) + \
			"\nDeaths: " + str(self.deaths)
			
	def venture(self): #When venturing, something happens within the location.
		curLoc = locations[self.x][self.y] #Easier reference
		if curLoc.locationType == "Cromania": #Can't venture in Cromania
			return "Not much is happening here in Cromania..."
		ventureChance = 0 #The same chance calculation as when moving (player level / sum of enemy levels)
		for i in curLoc.population:
			ventureChance += creatures[i].level
		if not ventureChance:
			ventureChance = 1
		ventureChance = self.level / ventureChance
		if ventureChance > random():
			if random() < 0.25: #If venturing succeeds, 25% chance to find a chest with random reward:
				return "You found a chest! " + getReward(self, 2 * curLoc.level)
			else:
				enemyId = getId() #Or spawn a random enemy.
				level = curLoc.level + randint(-2, 2)
				if level <= 0:
					level = 1
				if level > 100:
					level = 100
				lower = round(level / 100 * len(locationTypes[curLoc.locationType])) - 3
				upper = round(level / 100 * len(locationTypes[curLoc.locationType])) + 3 #What if upper too high?
				if lower < 0:
					lower = 0
				if upper >= len(locationTypes[curLoc.locationType]):
					upper = len(locationTypes[curLoc.locationType]) #Upper can be the actual length because the slice in the next line excludes it.
				creatures[enemyId] = creature(self.x, self.y, enemyId, choice(locationTypes[curLoc.locationType][lower : upper]), level)
				return "You encountered a" + creatures[enemyId].n + " " + creatures[enemyId].name + " with id " + str(enemyId) + ". "
		else:
			return "You were attacked! " + choice(self.location.population).attack(self.id)[0]
						
	def equip(self, itemId): #Equip an item and adjust stats.
		if items[itemId].level <= self.level:
			if items[itemId].itemType == "Weapon":
				self.equipped[0] = itemId
				self.damage = items[itemId].effect
			elif items[itemId].itemType == "Armor":
				self.equipped[1] = itemId
				self.armor = items[itemId].effect
		else:
			return "You have to be at least level " + str(items[itemId].level) + " to use this item." #Items have level caps
	
	def unequip(self, itemId): #Unequip an item and adjust stats.
		if items[itemId].itemType == "Weapon":
			self.equipped[0] = -1 #-1 means unequipped.
			self.damage = noWeaponDamage #Always at least some damage.
		elif items[itemId].itemType == "Armor":
			self.equipped[1] = -1
			self.armor = 0
			
class item: #Parent class for healing items, gear.
	def __init__(self, id, name, itemType, value, owner, inventoryId):
		self.id = id #Uses same id system as NPCs
		self.name = name
		self.itemType = itemType #Healing item, weapon etc.
		self.value = value #Price in gold
		self.owner = owner #id of the shop or player that owns it. Used for market.
		self.inventoryId = inventoryId #Inventory it's in.
	
	def destroy(self): #Delete the item, remove it from an inventory
		ids[self.id] = True
		creatures[self.inventoryId].dropItem(self.id)
		del items[self.id]
	
	#def market(self, price): #Move to market with a player-chosen price: other players can buy it, but the seller can't use it anymore.s

class healingItem(item): #Use to regenerate health.
	def __init__(self, id, name, value, effect, owner, inventoryId):
		item.__init__(self, id, name, "Healing Item", value, owner, inventoryId)
		self.effect = effect #The parentclass item doesn't have effect because future items may not need it. 
		
	def use(self, userId): #Actually use the item
		if userId == inventoryId:
			creatures[userId].heal(self.effect)
			self.destroy() #Single use
			return "You used " + self.name + " healing " + str(self.effect) + ". "
		else:
			return self.name + " is not in your inventory!"

class armor(item):
	def __init__(self, id, name, level, value, effect, owner, inventoryId):
		item.__init__(self, id, name, "Armor", value, owner, inventoryId)
		self.level = level #Minimum required level to equip this item
		self.effect = effect #armor points
		
	def use(self, userId): #Toggle equip
		if userId == inventoryId:
			if self.id in creatures[userId].equipped:
				creatures[userId].unequip(self.id)
			else:
				creatures[userId].equip(self.id)
				
class weapon(armor): #Really the only difference is the itemType
	def __init__(self, id, name, level, value, effect, owner, inventoryId):
		item.__init__(self, id, name, "Weapon", value, owner, inventoryId)
		self.level = level
		self.effect = effect
				
#Functions accessable by players
def start(bot, update): #Initial message
	sendMessage(bot, update, "Welcome to FransRPG! Type '/help' for instructions. ") #sendMessage() sends a message back to the one that used the command. bot and update gives that information.

def help(bot, update): #Lists player commands
	sendMessage(bot, update, "Type '/help' for this message.\
	\nType '/stats [id]' to see that creature's stats. Player id's are their names. Enter no id for your own stats.\
	\nType '/location [id]' to get info about that creature's current location.\
	\nType '/players' to see all players and their locations.\
	\nType '/join' to create a character.\
	\nType '/attack [id]' to attack the creature with that id.\
	\nType '/move [direction] [multiplier]' to move in any of directions n, ne, e, se, s, sw, w or nw. Multiplier is limited to your level.\
	\nType '/venture' to explore your current location.\
	\nType '/deposit [amount]' or '/withdraw [amount]' to move your gold when in Cromania.\
	\nType '/give [amount] [playername]' to bring that amount of gold to someone's bank.\
	\nType '/fill' to reset the store's items.\
	\nType '/store' to see the content of the store.\
	\nType '/save' to save the game to file. Autosave will occur after every 20 send messages.\
	\nType '/load' to load the game from file.")

def stats(bot, update, args): #Get info about a player or creature
	if args:
		id = args[0]
		try:
			id = int(id) #Try to make a creature id out of the argument. Player ids stay strings.
		except ValueError:
			pass
		if id in creatures:
			sendMessage(bot, update, creatures[id].stats())
		else:
			sendMessage(bot, update, "There is no creature with that id...") #Players are creatures as well
	else:
		id = getName(update) #If there is no argument, give info about the player itself.
		if id in creatures:
			sendMessage(bot, update, creatures[id].stats())
		else:
			sendMessage(bot, update, "You do not have a character yet! Create one with /join.")
	
def locationInfo(bot, update, args): #Gives info about the location a creature (players are creatures as well) is in.
	if args:
		id = args[0]
		if id in creatures:
			sendMessage(bot, update, locations[creatures[id].x][creatures[id].y].info()) #Find location and use build-in info() method
		else:
			sendMessage(bot, update, "There is no creature with that id...")
		
	else:
		id = getName(update) #No argument gives info about the location of the player itself
		if id in creatures:
			sendMessage(bot, update, locations[creatures[id].x][creatures[id].y].info())
		else:
			sendMessage(bot, update, "You do not have a character yet! Create one with /join.")
	
def listPlayers(bot, update): #View all players and their coordinates.
	message = ""
	for i in list(creatures.values()):
		if i.creatureType == "Player":
			message += i.name + ": " + coordsFormat(i.x, i.y) + "\n" 
	sendMessage(bot, update, message)
	

def join(bot, update): #Create a character to join the game!
	id = getName(update) #Extracts user name from the update class.
	if not id in creatures:
		creatures[id] = player(id)
		sendMessage(bot, update, "You joined the game! Your name is " + id + ".")
	else:
		sendMessage(bot, update, "You already have a character...")

def move(bot, update, args): #Move between locations, first argument is direction and optional second is multiplier.
	id = getName(update)
	if id in creatures:
		sendMessage(bot, update, creatures[id].move(args))
	else:
		sendMessage(bot, update, "You do not have a character yet! Create one with /join.")

def attack(bot, update, args): #Attack creature with this id. Only allowed in group chats.
	id = getName(update)
	if args:
		target = str(args[0]) #Target id
		if target in creatures:
			if creatures[target].creatureType == "Player" and update.message.chat.type == "private" and not id == target: #Not allowed in private chat
				sendMessage(bot, update, "You cannot attack other players in private chat!")
				return
	else:
		sendMessage(bot, update, "You must give an id.")
		return
	try:
		target = int(target)
	except ValueError:
		pass
	if id in creatures:
		returnValue = creatures[id].attack(target)
		sendMessage(bot, update, str(returnValue[0]))
		if returnValue[1]: #If figthBack is True, make the victim attack back.
			sendMessage(bot, update, str(creatures[target].attack(id)[0]))
	else:
		sendMessage(bot, update, "You do not have a character yet! Create one with /join.")
			
def venture(bot, update): #Adventure in the location, with a chance on loot or enemies.
	id = getName(update)
	if id in creatures:
		sendMessage(bot, update, creatures[id].venture())
	else:
		sendMessage(bot, update, "You do not have a character yet! Create one with /join.")
	
def deposit(bot, update, args): #Transfer gold to bank
	id = getName(update)
	if creatures[id].x != 0 or creatures[id].y != 0: #Only allowed in Cromania
		sendMessage(bot, update, "You have to be in Cromania to do that.")
		return
	if id in creatures:
		try:
			amount = int(args[0]) #Valid value?
			if amount <= creatures[id].gold: #Enough money?
				sendMessage(bot, update, "deposited " + str(amount) + " gold.")
				bank[id] += amount
				creatures[id].gold -= amount
			else:
				sendMessage(bot, update, "You do not have that amount of money!")
		except ValueError:
				sendMessage(bot, update, "You passed an invalid value!")
	else:
		sendMessage(bot, update, "You do not have a character yet! Create one with /join.")

def withdraw(bot, update, args): #Transfer gold from the bank
	id = getName(update)
	if creatures[id].x != 0 or creatures[id].y != 0:
		sendMessage(bot, update, "You have to be in Cromania to do that.")
		return
	if id in creatures:
		try:
			amount = int(args[0])
			if amount <= bank[id]:
				sendMessage(bot, update, "Withdrew " + str(amount) + " gold.")
				creatures[id].gold += amount
				bank[id] -= amount
			else:
				sendMessage(bot, update, "You do not have that amount of money!")
		except ValueError:
			sendMessage(bot, update, "You passed an invalid value!")
			pass
	else:
		sendMessage(bot, update, "You do not have a character yet! Create one with /join.")

def giveMoney(bot, update, args): #Transfer gold (inventory gold, not bank gold) to another player's bank.
	id = getName(update)
	target = str(args[1])
	if creatures[id].x != 0 or creatures[id].y != 0:
		sendMessage(bot, update, "You have to be in Cromania to do that.")
		return
	if id in creatures:
		if target in creatures:
			if creatures[target].creatureType == "Player":
				try:
					amount = int(args[0])
					if amount <= creatures[id].gold:
						sendMessage(bot, update, "Gave " + str(amount) + " gold.")
						bank[target] += amount
						creatures[id].gold -= amount
					else:
						sendMessage(bot, update, "You do not have that amount of money!")
				except ValueError:
						sendMessage(bot, update, "You passed an invalid value!")
			else:
				sendMessage(bot, update, "That creature is not a player...")
		else:
			sendMessage(bot, update, "That character does not exsist...")
	else:
		sendMessage(bot, update, "You do not have a character yet! Create one with /join.")
		
def save(bot, update): #Save all creatures, items, locations etc. to file. Reset autosave. 
	with open("fransrpg.pkl", "wb") as output:
		global messageCount
		pickle.dump(creatures, output, pickle.HIGHEST_PROTOCOL)
		pickle.dump(items, output, pickle.HIGHEST_PROTOCOL)
		pickle.dump(locations, output, pickle.HIGHEST_PROTOCOL)
		pickle.dump(ids, output, pickle.HIGHEST_PROTOCOL)
		pickle.dump(bank, output, pickle.HIGHEST_PROTOCOL)
		pickle.dump(storeObject, output, pickle.HIGHEST_PROTOCOL)
		messageCount = 0
		sendMessage (bot, update, "Saved to file.")

def load(bot, update): #Load all creatures, items, locations etc. from file. Reset autosave. 
	with open("fransrpg.pkl", "rb") as input:
		global creatures
		global items
		global locations
		global ids
		global bank
		global storeObject
		global messageCount
		creatures = pickle.load(input)
		items = pickle.load(input)
		locations = pickle.load(input)
		ids = pickle.load(input)
		bank = pickle.load(input)
		storeObject = pickle.load(input)
		messageCount = 0
		
		sendMessage(bot, update, "Loaded from file.")

		
def do(bot, update, args): #Execute a Python command. Only allowed for certain players.
	if getName(update) == "Storm":
		try:
			text = str(eval(str(" ".join(args)))) #Try to execute the command.
		except:
			text = "Invalid command."
		sendMessage(bot, update, text)
	else:
		sendMessage(bot, update, "You have to be Storm for that.")
	
def test(bot, update, args):
	print (args)

def reset(bot, update): #Delete everything and start from the beginning. Only allowed for certain players.
	if getName(update) == "Storm": #Id instead of name
		global creatures
		global items
		global locations
		global ids
		global bank
		global storeObject
		global messageCount
		save(bot, update) #Save a back up
		creatures = {} #Delete everything
		items = {}
		locations = {}
		bank = {}
		ids = [True] #Reset ids
		storeObject = inventory(getId()) #Create store.
		messageCount = 0
		newLocation(0, 0, "Cromania", 1) #Create initial location.
		creatures[storeObject.id] = storeObject
		sendMessage(bot, update, "Reset all game data! Type '/save' to make permanent or '/load' to undo.")
	else:
		sendMessage(bot, update, "You have to be Storm for that.")

def fillStore(bot, update): #Create 5 items per player, with about their level.
	for i in storeObject.inventory: #Clear old store inventory
		items[i].destroy()
	for i in creatures:
		if creatures[i].type == "Player":
			for j in range(5):
				level = creatures[i].level + randint(-3, 1) #Random level with middle slightly below player level
				if level <= 0: #But between 1 and 100
					level = 1
				if level > 100:
					level = 100
				id = getId()
				item = choice(["Healing Item", "Weapon", "Armor"]) #Any of these items
				name = newItemName(item, level) #Random name generator, based on the level.
				effect = getItemEffect(item, level + 2) #Formula for effect per item per level
				if item == "Healing Item":
					value = round(0.02 * effect ** 2 + 0.5 * effect - 2) #Value based on effect
					items[id] = weapon(id, name, level, value, effect, storeObject.id, storeObject.id)
					storeObject.gainItem(id)
				elif item == "Weapon":
					value = round(0.15 * effect ** 2 + 3 * effect)
					items[id] = weapon(id, name, level, value, effect, storeObject.id, storeObject.id)
					storeObject.gainItem(id)
				elif item == "Armor":
					value = round(0.15 * (2.5 * effect) ** 2 + 3 * (2.5 * effect))
					items[id] = weapon(id, name, level, value, effect, storeObject.id, storeObject.id)
					storeObject.gainItem(id)

def viewStore(bot, update): #Print all items currently in the store
	if storeObject.inventory:
		message = ""
		for i in storeObject.inventory:
			if items[i].itemType == "Armor" or items[i].itemType == "Weapon": #Print level as well when it is armor or a weapon
				message += "Level %s " % (items[i].level)
			message += "%s: %s (%s), %s\n" % (items[i].itemType, items[i].name, items[i].id, items[i].effect)
		sendMessage(bot, update, message)
	else:
		sendMessage(bot, update, "The store is currently empty.")
		
	
#Various functions for formatting, calculating values, creating etc.
def newLocation(x, y, locationType, level): #Create a new location instance and return a message describing it.
	if not x in locations:
		locations[x] = {}
		locations[x][y] = location(x, y, locationType, level)
	else:
		locations[x][y] = location(x, y, locationType, level)
	return "New " + getRating(level) + " location discovered: " + locationType + ". "

def newItemName(type, level): #Generates an item name. Number of adjectives based on the level, and adjectives and names are chosen the higher the level, the higher in the lists.
	if type == "Healing Item": #Choose list:
		itemsNouns = healingItems
		itemsAdj = healingItemsAdj
	elif type == "Weapon":
		itemsNouns = weaponItems
		itemsAdj = weaponItemsAdj
	elif type == "Armor":
		itemsNouns = armorItems
		itemsAdj = armorItemsAdj
	name = ""
	itemLower = round(level / 100 * len(itemsNouns)) - 3 #Ratio of current level to max level -> ratio of nth item to all items
	itemUpper = round(level / 100 * len(itemsNouns)) + 3
	if itemLower < 0:
		itemLower = 0
	if itemUpper > len(itemsNouns):
		itemLower = len(itemsNouns) - 10 #Choice from extra items when near max level
			#itemsUpper can be left unchanged because the slice at the end of function will ignore it if it is to high

	adjLower = round(level / 100 * len(itemsAdj)) - 5
	adjUpper = round(level / 100 * len(itemsAdj)) + 5
	if adjLower < 0:
		adjLower = 0
	if adjUpper > len(itemsAdj):
		adjLower = len(itemsAdj) - 15
		#same as at itemsUpper
	adj = ""
	for i in range(randint(1, 2) + round(level / 33)): #At least 1 and at most 5 adjectives
		while adj in name: #Pick a new adjective when it was already chosen
			adj = choice(itemsAdj[adjLower : adjUpper])
		name += adj + " "
	name += choice(itemsNouns[itemLower : itemUpper])
	return name
	
def getReward(player, rating): #Get some gold based on the rating. Gives a fair amount when the rating equals the level of a killed NPC.
	max = round(0.05 * rating ** 2 + 0.5 * rating)
	amount = randint(round(max / 2), max)
	if amount == 0:
		amount = 1 #Always at least 1 gold.
	player.gold += amount
	return "Your loot is " + str(amount) + " gold. "
	
def getName(update): #update contains information about who used a command. This extracts the user's name from it.
	return str(update.message.from_user.first_name)
	
def coordsFormat(x, y): #Returns a fancier representation of coordinates.
	if y >= 0:
		yText = str(y) + "N, "
	else:
		yText = str(-y) + "S, "
	if x <= 0:
		xText = str(-x) + "W"
	else:
		xText = str(x) + "E"
	return yText + xText
	
def getLevelXp(level): #Calculates xp needed for players to level up, per level.
	return (round(level ** 1.1)+9)
	
def getLevelHp(level): #Calculates the max hp of creatues, per level.
	return int(0.5 * level ** 2 + 0.5 * level + 9)
	
def getItemEffect(item, level): #Gives amount of hp healed, damage or armor based on an item's level.
	if item == "Healing Item":
		return randint(round(0.9 * getLevelHp(level) / (0.1 * level + 2)), round(1.1 * getLevelHp(level) / (0.1 * level + 2)))
	elif item == "Weapon":
		return randint(round(getLevelHp(level) / 15 * 1.1), round(getLevelHp(level) / 12 * 1.1))
	elif item == "Armor":
		return randint(round(getLevelHp(level) / 60 * 1.1), round(getLevelHp(level) / 30 * 1.1))
		
def getRating(level): #Convert location levels to this range.
	if level <= 10:
		return "very easy"
	elif level <= 20:
		return "easy"
	elif level <= 30:
		return "quite easy"
	elif level <= 40:
		return "not so easy"
	elif level <= 50:
		return "medium"
	elif level <= 60:
		return "not so hard"
	elif level <= 70:
		return "quite hard"
	elif level <= 80:
		return "hard"
	elif level <= 90:
		return "very hard"
	else:
		return "insane"

def getId(): #Returns first unoccupied id and marks it as occupied.
	global ids
	for i in range(len(ids)):
		if ids[i]:
			ids[i] = False
			return i
	ids += [False]
	return len(ids) - 1
	
def sendMessage(bot, update, message): #Sends a message to Telegram, keeps track of autosave, adresses user.
	global messageCount
	bot.sendMessage(chat_id = update.message.chat_id, text = ("@" + getName(update) + "\n" + message))
	messageCount += 1
	if messageCount >= 10:
		save(bot, update)
		messageCount = 0

storeObject = inventory(getId()) #The store, with items for purchase.

#main
def main():
	updater = Updater(token = sys.argv[1]) #Something important for the Telegram interface. argv[1] should be the bot token
	
	dispatcher = updater.dispatcher #The same
	
	#Commands accessable by players:
	start_handler = CommandHandler("start", start)
	dispatcher.add_handler(start_handler)
	help_handler = CommandHandler("help", help)
	dispatcher.add_handler(help_handler)
	players_handler = CommandHandler("players", listPlayers)
	dispatcher.add_handler(players_handler)
	location_handler = CommandHandler("location", locationInfo)
	dispatcher.add_handler(location_handler)
	stats_handler = CommandHandler("stats", stats)
	dispatcher.add_handler(stats_handler)
	join_handler = CommandHandler("join", join)
	dispatcher.add_handler(join_handler)
	move_handler = CommandHandler("move", move)
	dispatcher.add_handler(move_handler)
	attack_handler = CommandHandler("attack", attack)
	dispatcher.add_handler(attack_handler)
	venture_handler = CommandHandler("venture", venture)
	dispatcher.add_handler(venture_handler)
	deposit_handler = CommandHandler("deposit", deposit)
	dispatcher.add_handler(deposit_handler)
	withdraw_handler = CommandHandler("withdraw", withdraw)
	dispatcher.add_handler(withdraw_handler)
	give_handler = CommandHandler("give", giveMoney)
	dispatcher.add_handler(give_handler)
	fill_handler = CommandHandler("fill", fillStore)
	dispatcher.add_handler(fill_handler)
	store_handler = CommandHandler("store", viewStore)
	dispatcher.add_handler(store_handler)
	do_handler = CommandHandler("do", do)
	dispatcher.add_handler(do_handler)
	test_handler = CommandHandler("test", test)
	dispatcher.add_handler(test_handler)
	save_handler = CommandHandler("save", save)
	dispatcher.add_handler(save_handler)
	load_handler = CommandHandler("load", load)
	dispatcher.add_handler(load_handler)
	reset_handler = CommandHandler("reset", reset)
	dispatcher.add_handler(reset_handler)
	
	newLocation(0, 0, "Cromania", 1) #Create home city with level 1

	creatures[storeObject.id] = storeObject #Make storeObject possible to be found in the creatures list
	
	updater.start_polling() #Start waiting for commands

if __name__ == '__main__':
	main() #Start main() on start