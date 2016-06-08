"""
To do:
"""

from telegram import Updater
from random import random
from random import choice
from random import randint
import pickle
import logging

logging.basicConfig(
		format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
		level=logging.INFO)
logger = logging.getLogger(__name__)

locationTypes = {"Mountain": ['Worm', 'Moon Moon', 'Feral Frog', 'Feral Rock', 'Feral Cough', 'Squirrel', 'Flat Hat', 'Flop Hat', 'Old Computerscreen', 'Cloud', 'Fluffy Cloud', 'Head', 'Sneeze', 'Pile Of Snow', 'Old Summer Breeze', 'FatCat', 'Plofkip', 'Puppy', 'Kitten', 'Feral Slug', 'Feral Cat', 'Feral', 'Feral Hat', 'Goat', 'Hat', 'Rock', 'Ordinairy Rock', 'Pointy Stick', 'Big Snail', 'Lost Cyclist', 'Little Dwarf', 'Feral Dog', 'Brat', 'Red Hat', 'Mist', 'Falling Branch', 'Coyote', 'Flobglob', 'Lost Penguin', 'Snobtrobl', 'Dwarf', 'Feral ?', 'Feral Potato', 'Mad Brat', 'Broken Robot', 'Paperhat-Aeroplane', 'Black Dwarf', 'Feral Snake', 'Feral Tree', 'Saturday Music', 'Mountain Dog', 'Grass Monster', 'Small Wolf', 'Ginger Dwarf', 'Big Feral Cat', 'Goblin', 'Myst I', 'Blind Wolf', 'Armored Dwarf', 'Feral ??', 'Suare Hat', 'Hoblin', 'Moss Monster', 'Falling Tree', 'Pink Dwarft', 'Fat Dwarf', 'Big Feral Dog', 'Feral Owl', 'Froblin', 'Mean Teddybear', 'Magical Dwarf', 'Top Hat', 'Myst II', 'Rainy Cloud', 'Freddy', 'Master Dwarf', 'Feral ???', 'Troubled Dwarf', 'Angry Cucumber', 'King Dwarf', 'Feral Atomic Bomb', 'Rocky Snake', 'Robot', 'Wolf', 'Electric Dwarf', 'Flying Mittens', 'Mountain Goat', 'Rusty Moustache', 'Blood Wolf', 'Broblaglorb', 'Mad Trashcan', 'Evil Robot', 'Flying Zits', 'Evil Flower', 'Mechatronicon', 'Spaghetti Monster', 'Corrupted Hat'],
	"Field": ["Fieldguy 1-1", "Fieldguy 1-2", "Fieldguy 1-3", "Fieldguy 2-1", "Fieldguy 2-2", "Fieldguy 2-3", "Fieldguy 3-1", "Fieldguy 3-2", "Fieldguy 3-3"],
	"Road": ["Roadguy 1-1", "Roadguy 1-2", "Roadguy 1-3", "Roadguy 2-1", "Roadguy 2-2", "Roadguy 2-3", "Roadguy 3-1", "Roadguy 3-2", "Roadguy 3-3"]}
healingItems = ['Arsenic', 'Dirt', 'Water', 'Bread', 'Corn', 'Frog', 'Fluorine', 'Potato', 'Not So Hot Dog', 'Salad', 'Beans', 'Fish', 'Tooth Paste', 'Cucumber', 'Soda', 'Bunch Of Peas', 'Sandwich', 'Brew', 'Draught', 'Chicken Wing', 'Icecream', 'Hamburger', 'Apple', 'Tomato', 'Coffee', 'Cabbage', 'Cake', 'Honey', 'Portion Of French Fries', 'Mushroom', 'Canadian Bacon', 'Pancakes', 'Ketchup', 'Cookie', 'Maple Syrup', 'Soup', 'Waffle', 'Lizard', 'Medicine', 'Tea', 'Remedy', 'Potion', 'Cheese', 'Cupcake', 'Bacon', 'Chocolate', 'Strange Substance', 'Heroïn', 'Rice', 'Hugs In A Bottle', 'Unicorn Blood', 'Dessert Eagle', 'Chocolate Milk', 'Elixir']
healingItemsAdj = ['Probably Poisonous', 'Awful', 'Diarrhea Inducing', 'Moldy', 'Sucky', 'Diseased', 'Gross', 'Rotten', 'Bad', 'Wasted', 'From The Garbage Can', 'Fast Food', 'Dirty', 'Unhealthy', 'Barely Acceptable', 'Best Before: Two Weeks Ago', 'Hate Filled', 'Mediocre', 'Lacking Vitamins', 'Gay', 'Ok', 'Cheap', 'Nice', 'Fried', 'FDA Approved', 'Tasty', 'Fresh', 'Gluten Free', 'Herbal', 'Average', 'Vegetarian', 'Good', 'Grilled', 'Shake Before Usage', 'Ice Cold', 'Normal', 'Exhilarating', 'Moisturized', 'Catch Up', 'Standard', 'Filling', 'Yummy Yummy In My Tummy', '0% Fats', 'Great', 'Open Here', 'Cooked', 'Roasted', 'Love Infused', 'Cheesy', 'Chocolate', 'Super', 'Baked', 'Vegan', 'Special', 'Glowing', 'Sundried', 'Heroic', 'Makes You Vomit Rainbows', 'Glorious', 'Marinated', 'Awesome', 'Healthy', 'Exquisite']
weaponItems = ['Throwing Sand', 'Boots', 'Twig', 'Rock', 'Stone', 'Rubber Band', 'Butter Knife', 'Stick', 'Scissors', 'Fork', 'Bone', 'Shovel', 'Wrench', 'Magnets', 'Catapult', 'Lasso', 'Water Gun', 'Bear Hugs', 'Crowbar', 'Boxing Glove', 'Piece Of Glass', 'Bowling Ball', 'Chair', 'Club', 'Hammer', 'Blowgun', 'Boomerang', 'Bear Hands', 'Cheese Rasp', 'Razor', 'Knife', 'Baseball Bat', 'Saw', 'Tomahawk', 'Dagger', 'Axe', 'Machete', 'Bow And Arrow', 'Shuriken', 'Sai', 'Spear', 'Staff', 'Guitar', 'Cutlass', 'Crossbow', 'Nunchucks', 'Poison', 'Sword', 'Magic Wand', 'Rapier', 'Musket', 'Mace', 'Lance', 'Flail', 'Nail Gun', 'Blow Torch', 'Flintlock Rifle', 'Katana', 'Mines', 'Battleaxe', 'Revolver', 'Tazer', 'Cannon', 'Bombs', 'Bucket Of Lava', 'Piano String', 'Bubble Blaster', 'Bible', 'Thora', 'Koran', 'Pistol', 'Mysterious Syringe', 'Lawn Mower', 'Unholy Tome', 'Flame Thrower', 'Shotgun', 'Unidentified Weapon', 'Rifle', 'Sledge Hammer', 'Dynamite', 'Submachine Gun', 'Radioactive Barrel', 'Grand Piano', 'Chainsaw', 'Machine Gun', 'Sniper Rifle', 'Grenade', 'Spoon', 'Solar Flare', 'Excalibur', 'AK 47', 'Desert Eagle', 'Molotov Cocktail', 'Bazooka', 'Microwave', "Dragon's Tail", 'Javelin', 'Grenade Launcher', 'RPG', 'Unicorn Horn', 'X-57613C', 'Minigun', 'Gatling Gun', 'Tank']
weaponItemsAdj = ['Broken', 'Cardboard', 'Old', 'Toy', 'Dull', 'Weaponized', 'Plastic', 'Imaginary', 'Implausible', 'Anticlimactic', 'Rusty', 'Lite', 'Inferior', 'N00by', 'Origami', 'Dead Battery', 'Oil Leaking', 'Unreliable', 'Glass', 'Adorable', 'Wooden', 'Bolt Action', 'Pocket', 'Light', 'Steam Powered', 'Not So Bad', 'Bloody', "Cowboy's", 'Wi-Fi Enabled', 'Sharp', 'Spiked', 'Competent', 'Steel', "Gentleman's", 'Fearsome', 'Semi Automatic', 'Waterproof', 'Hands Free', 'Good', 'Medieval', 'Adjustable', 'Flaming', 'Suspicious', 'Shiny', 'Scoped', 'Dug Up', 'Dangerous', 'Stable', 'Steady', 'Mechanical', 'Environment Friendly', 'Portable', 'Electrical', 'Powerful', 'Great', 'Shocking', 'Do It Yourself', 'Laser', 'Shafting', 'Energized', 'Huge', 'Ninja', 'Accurate', 'Full Automatic', 'Ruby Inlaid', 'White Hot', 'Blinding', 'Super', 'Dual', 'Intangible', 'Crushing', 'Heavy', 'Epic', 'Stunning', 'Fear Powered', 'Digital', 'Melting', 'Special', 'Crippling', 'Holy', 'Invisible', 'Precise', 'Rocket Propelled', 'Undefined', 'Explosive', 'Laser Guided', 'Head Popping', 'Legendary', 'Smart', 'Plasma', 'Lovely', 'Hydrogen', 'Celestrial', 'Limited Edition', '.50 Cal', "Wizard's", "Rachmaninoff's", 'Magical', 'Majestic', 'Very Special', 'Sacred', 'Demonic', 'Four Dimensional', 'Theoratical', 'Antimatter', 'Alien', "Master's", 'Perfect']
armorItems = ['Underwear', 'Bra', 'Body Paint', 'Fierce Frown', 'Paper Shopping Bag Hat', 'Trousers', 'Arm Protectors', 'Leg Protectors', 'Bikini', 'Sweater', 'Back Protectors', 'Hat', 'Earcuffs', 'Chest Protectors', 'Water Wings', 'Cooking Pan Helmet', 'Head Protectors', 'Goggles', 'Fake Mustache', 'Arm Plating', 'Cape', 'Hockey Mask', 'Leg Plating', 'Gloves', 'Bucket Helmet', 'Back Plating', 'Kilt', 'Pumpkin Helmet', 'Chest Plating', 'Real Helmet', 'Boots', 'Head Plating', 'Suit', 'Arm Armor', 'Garbage Can Lid Shield', 'Leg Armor', 'Crown', 'Back Armor', 'Shield', 'Chest Armor', 'Vest', 'Head Armor', 'Power Suit', 'Arm Power Armor', 'Turtle Shell', 'Leg Power Armor', 'Reactive Armor', 'Back Power Armor', 'Power Shield', "Fuck This Shit I'm Going Naked", 'Sarcasm', 'Top Hat', 'Chest Power Armor', 'Magical Barrier', 'Head Power Armor', 'Tank']
armorItemsAdj = ['Old', 'Broken', 'Gross', 'Skin', 'Pre Historic', 'Ripped', 'Unwashed', 'Aluminum Foil', 'Black', 'Wooden', 'Trashy', 'Implausible', 'Made In China', 'Brittle', 'Hole Filled', 'Shabby', 'Cardboard', 'Inferior', 'Weak', 'Hide', 'Paper', 'Slippery', 'Falling Apart', 'Leather', 'Slutty', 'Homemade', 'Light', 'Not So Bad', 'Duct Tape', "Gentleman's", 'Good', 'Copper', 'Sneaking', 'Protective', 'Roman', 'Cool', 'Bronze', 'Feathered', 'Makes You Look Skinny', 'Fireproof', 'Tough', 'Shiny', 'Huge', 'Analog', 'Iron', 'Made In Germany', 'Special', 'Sparkling', 'Stunning', 'Super', 'White', 'Winged', 'Steel', 'Heavy', 'Bulletproof', 'Holy', 'Invisible', 'Spock', 'Beautiful', 'Twinkling', 'Emerald Inlaid', 'Legendary', 'Sacred', 'Ironic', 'Dragon Scales', 'Bad As Badass', 'Fabulously Amazebaltastic', 'Futuristic', 'Unicorn Hide', 'Asian', "Master's", 'Perfect']

locations = {} #Multidimensional dictionary with coordinates and their objects {x : {y : object}}
creatures = {} #All creature id's and their objects {id : object}
bank = {} #Bank-stored gold for each player {id : amount}
ids = [True] #Remembers currently taken id's, False means taken.
messageCount = 0 #Keeps track of number of send messages, saves after every 20.
items = {} #Items dictionary {id : object}

#classes
class location:
	def __init__(self, x, y, locationType, level):
		self.x = x
		self.y = y
		self.locationType = locationType
		self.level = level
		self.population = []
		self.players = []
	
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
		
	def info(self):
		message = "Terrain: " + self.locationType + \
			"\nCoordinates: " + coordsFormat(self.x, self.y) + \
			"\nDifficulty: " + getRating(self.level)
		if bool(self.population):
			message += "\nCreatures: "
			for i in self.population:
				message += "\n" + creatures[i].name + " (" + str(creatures[i].id) + ")"
		message += "\nPlayers: "
		for i in self.players:
			message += "\n" + creatures[i].id
		return message

class creature:
	def __init__(self, x, y, id, creatureType, level):	
		self.x = x
		self.y = y
		self.id = id
		self.level = level
		locations[x][y].populationAdd(self.id)
		rating = randint(0, round(level / 100 * len(locationTypes[locations[x][y].locationType])))
		self.creatureType = creatureType
		self.name = self.creatureType
		first = self.name[0].lower()
		if first == "a" or first == "e" or first == "i" or first == "o" or first == "u":
			self.n = "n"
		else:
			self.n = ""
		self.maxHp = getLevelHp(level)
		self.hp = self.maxHp
		self.damage = getItemEffect("Weapon", level)
		self.armor = getItemEffect("Armor", level)
			

	def teleport(self, x, y):
		try:
			locations[self.x][self.y].populationRemove(self.id)
		except Exception: #Excess
			pass
		locations[x][y].populationAdd(self.id)
		self.x = x
		self.y = y
		
	def die(self):
		if self.creatureType == "Player":
			if not self.rememberXp:
				self.xp = 0
			self.gold = 0
			self.hp = self.maxHp
			self.deaths += 1
			self.teleport(0, 0)

		else:
			ids[self.id] = True
			locations[self.x][self.y].populationRemove(self.id)
			del creatures[self.id]
			
	def attack(self, targetId):
		fightBack = False
		if self.x == 0 and self.y == 0:
			return ["You can't fight when in Cromania. ", fightBack]
		if targetId in locations[self.x][self.y].players:
			target = creatures[targetId]
			if self == target:
				self.die()
				return ["You commited suïcide and lost all your gold. ", fightBack]
			if self.damage > target.armor:
				min = round((self.damage - target.armor)/2)
				if min == 0:
					min = 1
				max = self.damage - target.armor
				damage = randint(min, max) #What if max == 0?
				target.hp -= damage
				message = self.name + " dealt " + str(damage) + " damage to " + target.name + ". "
				if target.hp <= 0:
					message += self.name + " killed " + target.name + "! "
					if self.creatureType == "Player":
						self.gold += target.gold
						self.playerKills += 1
						message += "You took all gold (" + str(target.gold) + ") from " + target.name + ". "
					if self.creatureType == "Player" and target.level - self.level >= -4:
						message += self.gainXp(round(0.5 * (target.level - self.level + 6) ** 1.5))
					target.die()
				else:
					message += target.name + " still has " + str(target.hp) + " health. "
			else:
				return [target.name + " absorbed all damage... ", fightBack]
		
		elif targetId in locations[self.x][self.y].population:
			fightBack = True
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
					message += getReward(self, target.level)
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
		
	def heal(self, amount):
		self.hp += amount
		if self.hp > self.maxHp:
			self.hp = maxHp
	
	def stats(self):
		return "Name: " + self.name + \
			"\nId: " + str(self.id) + \
			"\nLevel: " + str(self.level) + \
			"\nHp: " + str(self.hp) + "/" + str(self.maxHp) + \
			"\nDamage: " + str(self.damage) + \
			"\nArmor: " + str(self.armor) + \
			"\nCoordinates: " + coordsFormat(self.x, self.y)

class inventory:
	def __init__(self, id):
			self.id = id
			self.inventory = []
			
	def gainItem(self, itemId):
		if not itemId in self.inventory:
			self.inventory += itemId

	def dropItem(self, itemId):
		if itemId in self.inventory:
			self.inventory.pop(self.inventory.index(id))
		
class player(creature, inventory):
	def __init__(self, id):
		self.x = 0
		self.y = 0
		locations[0][0].playerEnters(id)
		self.id = id
		self.creatureType = "Player"
		self.name = id
		self.level = 1
		self.hp = 10
		self.damage = 4
		self.armor = 0
		self.xp = 0
		self.gold = 0
		self.playerKills = 0
		self.kills = 0
		self.deaths = 0
		self.rememberXp = False
		self.maxHp = 10
		bank[id] = 10
		self.inventory = [] #Id's of items in inventory
		self.equipped = [-1, -1] #Id's of equipped items: weapon, armor
	
	def move(self, args):
		direction = str(args[0])
		if not(direction == "n" or direction == "s" or direction == "w" or direction == "e" or direction == "ne" or direction == "nw" or direction == "se" or direction == "sw"):
			return "You passed an invalid direction! "
		fleeChance = 0
		for i in locations[self.x][self.y].population:
			fleeChance += creatures[i].level 
		if not fleeChance:
			fleeChance = 1
		fleeChance = self.level / fleeChance
		if fleeChance > random():
			multiplier = 1
			try:
				multiplier = int(args[1])
				if multiplier > self.level:
					return "The multiplier can only be as high as your level."
			except ValueError:
				return "Invalid multiplier. "
			except IndexError:
				pass
			
			locations[self.x][self.y].playerLeaves(self.id)
			
			if direction == "n":
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
				
			if not self.x in locations:
				message = newLocation(self.x, self.y, choice(list(locationTypes.keys())), abs(self.level + randint(-2, 2)))
			elif not self.y in locations[self.x]:
				message = newLocation(self.x, self.y, choice(list(locationTypes.keys())), abs(self.level + randint(-2, 2)))
			else:
				message = "Terrain: " + locations[self.x][self.y].locationType + ". "
			locations[self.x][self.y].playerEnters(self.id)
			return "You now are in " + coordsFormat(self.x, self.y) + ". " + message
		else:
			return "You failed to flee and were attacked! " + creatures[choice(locations[self.x][self.y].population)].attack(self.id)[0]
	
	def gainXp(self, xp):
		if xp <= 0:
			return
		if self.level < 100:
			message = "You gained " + str(xp) + " XP. "
			self.xp += xp
			while self.xp >= getLevelXp(self.level):
				self.xp -= getLevelXp(self.level)
				self.level += 1
				self.maxHp = getLevelHp()
				message += "You leveled up! You are now level " + str(self.level) + ". "
			if self.level >= 100:
				self.xp = 0
				return self.name + " reached level 100!!! You can no longer gain XP. "
			message += "You now have " + str(self.xp) + " XP. "
			return message
		else:
			return ""
	
	def teleport(self, x, y):
		try:
			locations[self.x][self.y].playerLeaves(self.id)
		except Exception:
			pass
		locations[x][y].playerEnters(self.id)
		self.x = x
		self.y = y
	
	def stats(self):
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
			
	def venture(self):
		curLoc = locations[self.x][self.y]
		if curLoc.locationType == "Cromania":
			return "Not much is happening here in Cromania..."
		ventureChance = 0
		for i in curLoc.population:
			ventureChance += creatures[i].level
		if not ventureChance:
			ventureChance = 1
		ventureChance = self.level / ventureChance
		if ventureChance > random():
			if random() < 0.25:
				return "You found a chest! " + getReward(self, 2 * curLoc.level)
			else:
				enemyId = getId()
				level = curLoc.level + randint(-2, 2)
				if level <= 0:
					level = 1
				if level > 100:
					level = 100
				lower = round(level / 100 * len(locationTypes[curLoc.locationType])) - 3
				upper = round(level / 100 * len(locationTypes[curLoc.locationType])) + 3 #What if upper too high?
				if lower < 0:
					lower = 0
				creatures[enemyId] = creature(self.x, self.y, enemyId, choice(locationTypes[curLoc.locationType][lower : upper]), level)
				return "You encountered a" + creatures[enemyId].n + " " + creatures[enemyId].name + " with id " + str(enemyId) + ". "
		else:
			return "You were attacked! " + choice(self.location.population).attack(self.id)[0]
						
	def equip(self, itemId):
		if items[itemId].level <= self.level:
			if items[itemId].itemType == "Weapon":
				self.equipped[0] = itemId
				self.damage = items[itemId].effect
			elif items[itemId].itemType == "Armor":
				self.equipped[1] = itemId
				self.armor = items[itemId].effect
		else:
			return "You have to be at least level " + str(items[itemId].level) + " to use this item."
	
	def unequip(self, itemId):
		if items[itemId].itemType == "Weapon":
			self.equipped[0] = -1
			self.damage = 0
		elif items[itemId].itemType == "Armor":
			self.equipped[1] = -1
			self.armor = 0
			
class item:
	def __init__(self, id, name, itemType, value, owner, inventoryId): #No effect? No level?
		self.id = id
		self.name = name
		self.value = value
		self.effect = effect #No level?
		self.owner = owner
		self.inventoryId = inventoryId
	
	def destroy(self):
		ids[self.id] = True
		creatures[self.inventoryId].dropItem(self.id)
		del items[self.id]
	
	#def market(self, price):

class healingItem(item):
	def __init__(self, id, name, level, value, effect, owner, inventoryId): #Excess level?
		item.__init__(self, id, name, "Healing Item", value, owner, inventoryId)
		self.effect = effect #Double effect?
		
	def use(self, userId):
		if userId == inventoryId:
			creatures[userId].heal(self.effect)
			self.destroy()
			return "You used " + self.name + " healing " + str(self.effect) + ". "
		else:
			return self.name + " is not in your inventory!"

class armor(item):
	def __init__(self, id, name, level, value, effect, owner, inventoryId):
		item.__init__(self, id, name, "Armor", value, owner, inventoryId)
		self.level = level #Double level?
		self.effect = effect #Double effect?
		
	def use(self, userId):
		if userId == inventoryId:
			if self.id in creatures[userId].equipped:
				creatures[userId].unequip(self.id)
			else:
				creatures[userId].equip(self.id)
				
class weapon(armor):
	def __init__(self, id, name, level, value, effect, owner, inventoryId):
		item.__init__(self, id, name, "Weapon", level, value, effect, owner, inventoryId)
				
#player functions
def start(bot, update):
	sendMessage(bot, update, "Welcome to FransRPG! Type '/?' for instructions. ")

def stats(bot, update, args):
	if args:
		id = args[0]
		try:
			id = int(id)
		except ValueError:
			pass
		if id in creatures:
			sendMessage(bot, update, creatures[id].stats())
		else:
			sendMessage(bot, update, "There is no creature with that id...")
	else:
		id = getName(update)
		if id in creatures:
			sendMessage(bot, update, creatures[id].stats())
		else:
			sendMessage(bot, update, "You do not have a character yet! Create one with /join.")
	
def locationInfo(bot, update, args): #Individual locations?
	if args:
		id = args[0]
		if id in creatures:
			sendMessage(bot, update, locations[creatures[id].x][creatures[id].y].info())
		elif id in locations: #???
			sendMessage(bot, update, locations[id].info())
		else:
			sendMessage(bot, update, "There is no player named like that.")
		
	else:
		id = getName(update)
		if id in creatures:
			sendMessage(bot, update, locations[creatures[id].x][creatures[id].y].info())
		else:
			sendMessage(bot, update, "You do not have a character yet! Create one with /join.")
	
def listPlayers(bot, update):
	message = ""
	for i in list(creatures.values()):
		if i.creatureType == "Player":
			message += i.name + ": " + coordsFormat(i.x, i.y) + "\n" 
	sendMessage(bot, update, message)
	
def help(bot, update):
	sendMessage(bot, update, "Type '/?' for this message.\
	\nType '/stats [id]' to see that creature's stats. Player id's are their names. No id for yourself.\
	\nType '/location [id]' to get info about your current location.\
	\nType '/listPlayers' to see the location of all players.\
	\nType '/join' to create a character.\
	\nType '/attack [id]' to attack the creature with that id.\
	\nType '/move [direction] [multiplier]' to move in any of directions n, ne, e, se, s, sw, w or nw. Multiplier is limited to your level.\
	\nType '/venture' to explore your current location.\
	\nType '/deposit [amount]' or '/withdraw [amount]' to move your gold when in Cromania.\
	\nType '/giveMoney [amount] [playername]' to bring that gold to someone's bank.\
	\nType '/fillStore' to reset the store's items.\
	\nType '/viewStore' to see the content of the store.\
	\nType '/save' to save the game to file. Autosave will occur after every 20 send messages.\
	\nType '/load' to load the game from file.")

def join(bot, update):
	id = getName(update)
	if not id in creatures:
		creatures[id] = player(id)
		sendMessage(bot, update, "You joined the game! Your name is " + id + ".")
	else:
		sendMessage(bot, update, "You already have a character...")

def move(bot, update, args):
	id = getName(update)
	if id in creatures:
		sendMessage(bot, update, creatures[id].move(args))
	else:
		sendMessage(bot, update, "You do not have a character yet! Create one with /join.")

def attack(bot, update, args):
	id = getName(update)
	if args:
		target = str(args[0])
		if target in creatures:
			if creatures[target].creatureType == "Player" and update.message.chat.type == "private" and not id == target:
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
		if returnValue[1]:
			sendMessage(bot, update, str(creatures[target].attack(id)[0]))
	else:
		sendMessage(bot, update, "You do not have a character yet! Create one with /join.")
			
def venture(bot, update):
	id = getName(update)
	if id in creatures:
		sendMessage(bot, update, creatures[id].venture())
	else:
		sendMessage(bot, update, "You do not have a character yet! Create one with /join.")
	
def deposit(bot, update, args):
	id = getName(update)
	if creatures[id].x != 0 or creatures[id].y != 0:
		sendMessage(bot, update, "You have to be in Cromania to do that.")
		return
	if id in creatures:
		try:
			amount = int(args[0])
			if amount <= creatures[id].gold:
				sendMessage(bot, update, "deposited " + str(amount) + " gold.")
				bank[id] += amount
				creatures[id].gold -= amount
			else:
				sendMessage(bot, update, "You do not have that amount of money!")
		except ValueError:
				sendMessage(bot, update, "You passed an invalid value!")
	else:
		sendMessage(bot, update, "You do not have a character yet! Create one with /join.")

def withdraw(bot, update, args):
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

def giveMoney(bot, update, args):
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
		
def save(bot, update):
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

def load(bot, update):
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
		
		try: #Don't send message if load() if there's no update or bot
			sendMessage(bot, update, "Loaded from file.")
		except:
			pass
		
def do(bot, update, args):
	if getName(update) == "Storm": #id instead of name
		try:
			text = str(eval(str(" ".join(args))))
		except:
			text = "Invalid command."
		sendMessage(bot, update, text)
	else:
		sendMessage(bot, update, "You have to be Storm for that.")
	
def reset(bot, update):
	if getName(update) == "Storm": #Id instead of name
		global creatures
		global items
		global locations
		global ids
		global bank
		global storeObject
		global messageCount
		save(bot, update)
		creatures = {}
		items = {}
		locations = {}
		bank = {}
		ids = [True]
		storeObject = inventory(getId())
		messageCount = 0
		newLocation(0, 0, "Cromania", 1)
		creatures[storeObject.id] = storeObject
		sendMessage(bot, update, "Reset all game data! Type '/save' to make permanent or '/load' to undo.")
	else:
		sendMessage(bot, update, "You have to be Storm for that.")

def fillStore(bot, update):
	for i in storeObject.inventory:
		items[i].destroy()
	for i in creatures:
		if creatures[i].type == "Player":
			for j in range(5):
				level = creatures[i].level + randint(-3, 1)
				if level <= 0:
					level = 1
				if level > 100:
					level = 100
				id = getId()
				item = choice(["Healing Item", "Weapon", "Armor"])
				name = newItemName(item, level)
				effect = getItemEffect(item, level + 2)
				if item == "Healing Item":
					value = round(0.02 * effect ** 2 + 0.5 * effect - 2)
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

def viewStore(bot, update):
	message = ""
	if storeObject.inventory:
		for i in storeObject.inventory:
			if items[i].itemType == "Armor" or items[i].itemType == "Weapon":
				message += "Level %s " % (items[i].level)
			message += "%s: %s (%s), %s\n" % (items[i].itemType, items[i].name, items[i].id, items[i].effect)
		sendMessage(bot, update, message)
	else:
		sendMessage(bot, update, "The store is currently empty.")
		
	
#tools
def newLocation(x, y, locationType, level):
	if not x in locations:
		locations[x] = {}
		locations[x][y] = location(x, y, locationType, level)
	else:
		locations[x][y] = location(x, y, locationType, level)
	return "New " + getRating(level) + " location discovered: " + locationType + ". "

def newItemName(type, level):
	if type == "Healing Item":
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
		itemLower = len(itemsNouns) - 10 #Extra items when near max level
			#itemUpper = len(itemsNouns)?? 

	adjLower = round(level / 100 * len(itemsAdj)) - 5
	adjUpper = round(level / 100 * len(itemsAdj)) + 5
	if adjLower < 0:
		adjLower = 0
	if adjUpper > len(itemsAdj):
		adjLower = len(itemsAdj) - 15 #Extra Adj near when max level
		#same as at itemsUpper
	adj = ""
	for i in range(randint(1, 2) + round(level / 33)): #Min 1, max 5 Adj
		while adj in name:
			adj = choice(itemsAdj[adjLower : adjUpper])
		name += adj + " "
	name += choice(itemsNouns[itemLower : itemUpper])
	return name
	
def getReward(player, rating):
	max = round(0.05 * rating ** 2 + 0.5 * rating)
	amount = randint(round(max / 2), max)
	if amount == 0:
		amount = 1
	player.gold += amount
	return "Your loot is " + str(amount) + " gold. "
	
def getName(update):
	return str(update.message.from_user.first_name)
	
def coordsFormat(x, y):
	if y >= 0:
		yText = str(y) + "N, "
	else:
		yText = str(-y) + "S, "
	if x <= 0:
		xText = str(-x) + "W"
	else:
		xText = str(x) + "E"
	return yText + xText
	
def getLevelXp(level):
	return (round(level ** 1.1)+9)
	
def getLevelHp(level):
	return int(0.5 * level ** 2 + 0.5 * level + 9)
	
def getItemEffect(item, level):
	if item == "Healing Item":
		return randint(round(0.9 * getLevelHp(level) / (0.1 * level + 2)), round(1.1 * getLevelHp(level) / (0.1 * level + 2)))
	elif item == "Weapon":
		return randint(round(getLevelHp(level) / 15 * 1.1), round(getLevelHp(level) / 12 * 1.1))
	elif item == "Armor":
		return randint(round(getLevelHp(level) / 60 * 1.1), round(getLevelHp(level) / 30 * 1.1))
		
def getRating(level):
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

def getId():
	global ids
	for i in range(len(ids)):
		if ids[i]:
			ids[i] = False
			return i
	ids += [False]
	return len(ids) - 1
	
def sendMessage(bot, update, message):
	global messageCount
	bot.sendMessage(update.message.chat_id, text = ("@" + getName(update) + "\n" + message))
	messageCount += 1
	if messageCount >= 10:
		save(bot, update)
		messageCount = 0

#probs make global in main or inv above
storeObject = inventory(getId())

#main
def main():
	updater = Updater(sys.argv[1])
	
	dispatcher = updater.dispatcher
	
	#load(None, None) #Don't send message
	
	dispatcher.addTelegramCommandHandler("start", start)
	dispatcher.addTelegramCommandHandler("location", locationInfo)
	dispatcher.addTelegramCommandHandler("stats", stats)
	dispatcher.addTelegramCommandHandler("?", help)
	dispatcher.addTelegramCommandHandler("join", join)
	dispatcher.addTelegramCommandHandler("move", move)
	dispatcher.addTelegramCommandHandler("attack", attack)
	dispatcher.addTelegramCommandHandler("venture", venture)
	dispatcher.addTelegramCommandHandler("deposit", deposit)
	dispatcher.addTelegramCommandHandler("withdraw", withdraw)
	dispatcher.addTelegramCommandHandler("giveMoney", giveMoney)
	dispatcher.addTelegramCommandHandler("givemoney", giveMoney)
	dispatcher.addTelegramCommandHandler("do", do)
	dispatcher.addTelegramCommandHandler("save", save)
	dispatcher.addTelegramCommandHandler("load", load)
	dispatcher.addTelegramCommandHandler("reset", reset)
	dispatcher.addTelegramCommandHandler("listPlayers", listPlayers)
	dispatcher.addTelegramCommandHandler("listplayers", listPlayers)
	dispatcher.addTelegramCommandHandler("fillStore", fillStore)
	dispatcher.addTelegramCommandHandler("fillstore", fillStore)
	dispatcher.addTelegramCommandHandler("viewStore", viewStore)
	dispatcher.addTelegramCommandHandler("viewstore", viewStore)
	
	newLocation(0, 0, "Cromania", 1)
	getId #???
	creatures[storeObject.id] = storeObject #??? Does this work?
	
	updater.start_polling()

if __name__ == '__main__':
	main()
