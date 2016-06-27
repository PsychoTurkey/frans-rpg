#!/usr/bin/env python3
# Imports
from sys import argv
import json
from random import random, choice, randint
import pickle
import logging
from telegram.ext import Updater, CommandHandler

# Telegram bot log
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=15)
logger = logging.getLogger(__name__)

# Dict with LocationTypeName: [all possible NPCs] The enemies list is in order from weak to strong
locationTypes = {
    "Mountain": [
        'Worm', 'Moon Moon', 'Feral Frog', 'Feral Rock', 'Feral Cough', 'Squirrel', 'Flat Hat',
        'Flop Hat', 'Old Computerscreen', 'Cloud', 'Fluffy Cloud', 'Head', 'Sneeze',
        'Pile Of Snow', 'Old Summer Breeze', 'FatCat', 'Plofkip', 'Puppy', 'Kitten', 'Feral Slug',
        'Feral Cat', 'Feral', 'Feral Hat', 'Goat', 'Hat', 'Rock', 'Ordinairy Rock', 'Pointy Stick',
        'Big Snail', 'Lost Cyclist', 'Little Dwarf', 'Feral Dog', 'Brat', 'Red Hat', 'Mist',
        'Falling Branch', 'Coyote', 'Flobglob', 'Lost Penguin', 'Snobtrobl', 'Dwarf', 'Feral ?',
        'Feral Potato', 'Mad Brat', 'Broken Robot', 'Paperhat-Aeroplane', 'Black Dwarf',
        'Feral Snake', 'Feral Tree', 'Saturday Music', 'Mountain Dog', 'Grass Monster',
        'Small Wolf', 'Ginger Dwarf', 'Big Feral Cat', 'Goblin', 'Myst I', 'Blind Wolf',
        'Armored Dwarf', 'Feral ??', 'Suare Hat', 'Hoblin', 'Moss Monster', 'Falling Tree',
        'Pink Dwarft', 'Fat Dwarf', 'Big Feral Dog', 'Feral Owl', 'Froblin', 'Mean Teddybear',
        'Magical Dwarf', 'Top Hat', 'Myst II', 'Rainy Cloud', 'Freddy', 'Master Dwarf',
        'Feral ???', 'Troubled Dwarf', 'Angry Cucumber', 'King Dwarf', 'Feral Atomic Bomb',
        'Rocky Snake', 'Robot', 'Wolf', 'Electric Dwarf', 'Flying Mittens', 'Mountain Goat',
        'Rusty Moustache', 'Blood Wolf', 'Broblaglorb', 'Mad Trashcan', 'Evil Robot',
        'Flying Zits', 'Evil Flower', 'Mechatronicon', 'Spaghetti Monster', 'Corrupted Hat'
    ],
    "Field": [
        "Fieldguy 1-1", "Fieldguy 1-2", "Fieldguy 1-3", "Fieldguy 2-1", "Fieldguy 2-2",
        "Fieldguy 2-3", "Fieldguy 3-1", "Fieldguy 3-2", "Fieldguy 3-3"
    ],
    "Road": [
        "Roadguy 1-1", "Roadguy 1-2", "Roadguy 1-3", "Roadguy 2-1", "Roadguy 2-2", "Roadguy 2-3",
        "Roadguy 3-1", "Roadguy 3-2", "Roadguy 3-3"
    ]
}

# Lists with items and possible adjectives. Again, the items go from weak to strong.
healingItems = [
    'Arsenic', 'Dirt', 'Water', 'Bread', 'Corn', 'Frog', 'Fluorine', 'Potato', 'Not So Hot Dog',
    'Salad', 'Beans', 'Fish', 'Tooth Paste', 'Cucumber', 'Soda', 'Bunch Of Peas', 'Sandwich',
    'Brew', 'Draught', 'Chicken Wing', 'Icecream', 'Hamburger', 'Apple', 'Tomato', 'Coffee',
    'Cabbage', 'Cake', 'Honey', 'Portion Of French Fries', 'Mushroom', 'Canadian Bacon', 'Pancakes',
    'Ketchup', 'Cookie', 'Maple Syrup', 'Soup', 'Waffle', 'Lizard', 'Medicine', 'Tea', 'Remedy',
    'Potion', 'Cheese', 'Cupcake', 'Bacon', 'Chocolate', 'Strange Substance', 'Heroïn', 'Rice',
    'Hugs In A Bottle', 'Unicorn Blood', 'Dessert Eagle', 'Chocolate Milk', 'Elixir'
]
healingItemsAdj = [
    'Probably Poisonous', 'Awful', 'Diarrhea Inducing', 'Moldy', 'Sucky', 'Diseased', 'Gross',
    'Rotten', 'Bad', 'Wasted', 'From The Garbage Can', 'Fast Food', 'Dirty', 'Unhealthy',
    'Barely Acceptable', 'Best Before: Two Weeks Ago', 'Hate Filled', 'Mediocre',
    'Lacking Vitamins', 'Gay', 'Ok', 'Cheap', 'Nice', 'Fried', 'FDA Approved', 'Tasty', 'Fresh',
    'Gluten Free', 'Herbal', 'Average', 'Vegetarian', 'Good', 'Grilled', 'Shake Before Usage',
    'Ice Cold', 'Normal', 'Exhilarating', 'Moisturized', 'Catch Up', 'Standard', 'Filling',
    'Yummy Yummy In My Tummy', '0% Fats', 'Great', 'Open Here', 'Cooked', 'Roasted',
    'Love Infused', 'Cheesy', 'Chocolate', 'Super', 'Baked', 'Vegan', 'Special', 'Glowing',
    'Sundried', 'Heroic', 'Makes You Vomit Rainbows', 'Glorious', 'Marinated', 'Awesome',
    'Healthy', 'Exquisite'
]
weaponItems = [
    'Throwing Sand', 'Boots', 'Twig', 'Rock', 'Stone', 'Rubber Band', 'Butter Knife', 'Stick',
    'Scissors', 'Fork', 'Bone', 'Shovel', 'Wrench', 'Magnets', 'Catapult', 'Lasso', 'Water Gun',
    'Bear Hugs', 'Crowbar', 'Boxing Glove', 'Piece Of Glass', 'Bowling Ball', 'Chair', 'Club',
    'Hammer', 'Blowgun', 'Boomerang', 'Bear Hands', 'Cheese Rasp', 'Razor', 'Knife',
    'Baseball Bat', 'Saw', 'Tomahawk', 'Dagger', 'Axe', 'Machete', 'Bow And Arrow', 'Shuriken',
    'Sai', 'Spear', 'Staff', 'Guitar', 'Cutlass', 'Crossbow', 'Nunchucks', 'Poison', 'Sword',
    'Magic Wand', 'Rapier', 'Musket', 'Mace', 'Lance', 'Flail', 'Nail Gun', 'Blow Torch',
    'Flintlock Rifle', 'Katana', 'Mines', 'Battleaxe', 'Revolver', 'Tazer', 'Cannon', 'Bombs',
    'Bucket Of Lava', 'Piano String', 'Bubble Blaster', 'Bible', 'Thora', 'Koran', 'Pistol',
    'Mysterious Syringe', 'Lawn Mower', 'Unholy Tome', 'Flame Thrower', 'Shotgun',
    'Unidentified Weapon', 'Rifle', 'Sledge Hammer', 'Dynamite', 'Submachine Gun',
    'Radioactive Barrel', 'Grand Piano', 'Chainsaw', 'Machine Gun', 'Sniper Rifle', 'Grenade',
    'Spoon', 'Solar Flare', 'Excalibur', 'AK 47', 'Desert Eagle', 'Molotov Cocktail', 'Bazooka',
    'Microwave', "Dragon's Tail", 'Javelin', 'Grenade Launcher', 'RPG', 'Unicorn Horn', 'X-57613C',
    'Minigun', 'Gatling Gun', 'Tank'
]
weaponItemsAdj = [
    'Broken', 'Cardboard', 'Old', 'Toy', 'Dull', 'Weaponized', 'Plastic', 'Imaginary',
    'Implausible', 'Anticlimactic', 'Rusty', 'Lite', 'Inferior', 'N00by', 'Origami',
    'Dead Battery', 'Oil Leaking', 'Unreliable', 'Glass', 'Adorable', 'Wooden', 'Bolt Action',
    'Pocket', 'Light', 'Steam Powered', 'Not So Bad', 'Bloody', "Cowboy's", 'Wi-Fi Enabled',
    'Sharp', 'Spiked', 'Competent', 'Steel', "Gentleman's", 'Fearsome', 'Semi Automatic',
    'Waterproof', 'Hands Free', 'Good', 'Medieval', 'Adjustable', 'Flaming', 'Suspicious', 'Shiny',
    'Scoped', 'Dug Up', 'Dangerous', 'Stable', 'Steady', 'Mechanical', 'Environment Friendly',
    'Portable', 'Electrical', 'Powerful', 'Great', 'Shocking', 'Do It Yourself', 'Laser',
    'Shafting', 'Energized', 'Huge', 'Ninja', 'Accurate', 'Full Automatic', 'Ruby Inlaid',
    'White Hot', 'Blinding', 'Super', 'Dual', 'Intangible', 'Crushing', 'Heavy', 'Epic',
    'Stunning', 'Fear Powered', 'Digital', 'Melting', 'Special', 'Crippling', 'Holy', 'Invisible',
    'Precise', 'Rocket Propelled', 'Undefined', 'Explosive', 'Laser Guided', 'Head Popping',
    'Legendary', 'Smart', 'Plasma', 'Lovely', 'Hydrogen', 'Celestrial', 'Limited Edition',
    '.50 Cal', "Wizard's", "Rachmaninoff's", 'Magical', 'Majestic', 'Very Special', 'Sacred',
    'Demonic', 'Four Dimensional', 'Theoratical', 'Antimatter', 'Alien', "Master's",
    'Perfect'
]
armorItems = [
    'Underwear', 'Bra', 'Body Paint', 'Fierce Frown', 'Paper Shopping Bag Hat', 'Trousers',
    'Arm Protectors', 'Leg Protectors', 'Bikini', 'Sweater', 'Back Protectors', 'Hat', 'Earcuffs',
    'Chest Protectors', 'Water Wings', 'Cooking Pan Helmet', 'Head Protectors', 'Goggles',
    'Fake Mustache', 'Arm Plating', 'Cape', 'Hockey Mask', 'Leg Plating', 'Gloves',
    'Bucket Helmet', 'Back Plating', 'Kilt', 'Pumpkin Helmet', 'Chest Plating', 'Real Helmet',
    'Boots', 'Head Plating', 'Suit', 'Arm Armor', 'Garbage Can Lid Shield', 'Leg Armor', 'Crown',
    'Back Armor', 'Shield', 'Chest Armor', 'Vest', 'Head Armor', 'Power Suit', 'Arm Power Armor',
    'Turtle Shell', 'Leg Power Armor', 'Reactive Armor', 'Back Power Armor', 'Power Shield',
    "Fuck This Shit I'm Going Naked", 'Sarcasm', 'Top Hat', 'Chest Power Armor', 'Magical Barrier',
    'Head Power Armor', 'Tank'
]
armorItemsAdj = [
    'Old', 'Broken', 'Gross', 'Skin', 'Pre Historic', 'Ripped', 'Unwashed', 'Aluminum Foil',
    'Black', 'Wooden', 'Trashy', 'Implausible', 'Made In China', 'Brittle', 'Hole Filled',
    'Shabby', 'Cardboard', 'Inferior', 'Weak', 'Hide', 'Paper', 'Slippery', 'Falling Apart',
    'Leather', 'Slutty', 'Homemade', 'Light', 'Not So Bad', 'Duct Tape', "Gentleman's", 'Good',
    'Copper', 'Sneaking', 'Protective', 'Roman', 'Cool', 'Bronze', 'Feathered',
    'Makes You Look Skinny', 'Fireproof', 'Tough', 'Shiny', 'Huge', 'Analog', 'Iron',
    'Made In Germany', 'Special', 'Sparkling', 'Stunning', 'Super', 'White', 'Winged', 'Steel',
    'Heavy', 'Bulletproof', 'Holy', 'Invisible', 'Spock', 'Beautiful', 'Twinkling',
    'Emerald Inlaid', 'Legendary', 'Sacred', 'Ironic', 'Dragon Scales', 'Bad As Badass',
    'Fabulously Amazebaltastic', 'Futuristic', 'Unicorn Hide', 'Asian', "Master's",
    'Perfect'
]

# Players can't do anything if they can't fight. Useful when testing.
noWeaponDamage = 1
# Change for testing purposes: new characters start at this level.
initialLevel = 1
# Gold in the player's inventory when they create a character. Bank already has 10.
initialGold = 0

# Multidimensional dictionary with coordinates and their location objects {x : {y : object}}
locations = {}
# All creature id's and their objects {id : object}. Contains players as well.
creatures = {}
# Contains players, store and market, needed for when an item needs to find it's inventory.
inventories = {}
# Bank-stored gold for each player {id : amount}
bank = {}
# Remembers currently taken ids for items and NPCs, False means taken. Doesn't contain players.
ids = [True]
# Keeps track of number of send messages, saves after every 20.
messageCount = 0
items = {}  # Items dictionary {id : object}

# References to creatures, locations etc. cannot be real object-references because of troubles with
# saving to file. Instead, coordinates, id numbers or strings are used.

# classes


class location:

    def __init__(self, x, y, locationType, level):
        """location(x, y, locationType, level)"""
        # Locations dict coordinates
        self.x = x
        self.y = y
        # Terrain type: Mountain, Field, etc.
        self.locationType = locationType
        self.level = level
        # Contains NPC ids
        self.population = []
        # Contains  player ids
        self.players = []

    # Add or remove a NPC or player from the lists:
    def populationAdd(self, id):
        if id not in self.population:
            self.population += [id]

    def populationRemove(self, id):
        if id in self.population:
            self.population.pop(self.population.index(id))

    def playerEnters(self, id):
        if id not in self.players:
            self.players += [id]

    def playerLeaves(self, id):
        if id in self.players:
            self.players.pop(self.players.index(id))

    def info(self):
        """Display its own stats"""
        message = "\n".join(line.lstrip() for line in "Terrain: {}\n\
        Coordinates: {}\n\
        Difficulty: {}".format(
            self.locationType, coordsFormat(self.x, self.y), getRating(self.level)
        ).split("\n"))
        # players and npc in the location:
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
        """creature(x, y, id, creatureType, level)"""
        # Initial location
        self.x = x
        self.y = y
        # Refer to the creature (ingame as well) with this number
        self.id = id
        locations[x][y].populationAdd(self.id)
        # Initial level
        self.level = level
        # The creature name, for players it's "Player" to distinct players and NPCs.
        self.creatureType = creatureType
        self.name = self.creatureType
        # Should it be reffered to with "a" or "an"?
        first = self.name[0].lower()

        if first == "a" or first == "e" or first == "i" or first == "o" or first == "u":
            self.n = "n"
        else:
            self.n = ""

        # hp cannot exceed this value, based the creature's level.
        self.maxHp = getLevelHp(level)
        self.hp = self.maxHp
        # NPCs get weapon and armor ratings as if they had weapons of their own level
        self.damage = getItemEffect("Weapon", level)
        self.armor = getItemEffect("Armor", level)

    def teleport(self, x, y):
        """Move to location x, y."""
        try:
            # It could happen that a creature is not actually in a location
            locations[self.x][self.y].populationRemove(self.id)
        except:
            pass

        locations[x][y].populationAdd(self.id)
        self.x = x
        self.y = y

    def die(self):
        """Respawn without gold and xp if it is a player, delete if it is a NPC."""
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

    def attack(self, targetId):
        """Checks if attack is possible, subtracts a certain damage, handles death and rewards."""
        fightBack = False
        if self.x == 0 and self.y == 0:
            # The return value is checked for the message and whether the victim fights back
            # (only if the victim is a NPC and doesn't die).
            return ["You can't fight when in Cromania. ", fightBack]

        # If the target is a player and in the right location...
        if targetId in locations[self.x][self.y].players:
            target = creatures[targetId]
            if self == target:
                self.die()
                return ["You commited suïcide and lost all your gold. ", fightBack]

            # Ignore if the damage isn't greater than the target's armor.
            if self.damage > target.armor:
                min = round((self.damage - target.armor) / 2)
                if min == 0:
                    # At least one damage point.
                    min = 1
                max = self.damage - target.armor
                damage = randint(min, max)
                target.hp -= damage
                message = self.name + " dealt " + str(damage) + " damage to " + target.name + ". "
                if target.hp <= 0:
                    message += self.name + " killed " + target.name + "! "
                    # If the attacker is a player:
                    if self.creatureType == "Player":
                        # Get victim's gold. Victim loses it througth their die() method.
                        self.gold += target.gold
                        # Keep track of the number of players someone killed.
                        self.playerKills += 1
                        message += "You took all gold ({}) from {}.".format(
                            target.gold, target.name
                        )
                    # Don't get xp when an enemy has a much lower level.
                    if self.creatureType == "Player" and target.level - self.level >= -4:
                        # Gain xp by some formula based on both levels
                        message += self.gainXp(round(0.5 * (target.level - self.level + 6) ** 1.5))
                    target.die()
                else:
                    message += target.name + " still has " + str(target.hp) + " health. "
            else:
                return [target.name + " absorbed all damage... ", fightBack]
        # ...or a NPC in the right location:
        elif targetId in locations[self.x][self.y].population:
            # If a NPC is attacked and does not die, it will attack back.
            fightBack = True
            target = creatures[targetId]
            if self.damage > target.armor:
                min = round((self.damage - target.armor) / 2)
                if min == 0:
                    min = 1

                max = self.damage - target.armor
                damage = randint(min, max)
                target.hp -= damage
                message = "{} dealt {} damage to the {}.".format(self.name, damage, target.name)
                if target.hp <= 0:
                    message += self.name + " killed the " + target.name + "! "
                    self.kills += 1
                    # Get a randomly generated reward base on the victim's level.
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
        """Add HP and reset if the result exceeds maxHp."""
        self.hp += amount
        if self.hp > self.maxHp:
            self.hp = self.maxHp

    def stats(self):
        """Print the creature's stats."""
        return "\n".join(line.lstrip() for line in "Name: {}\n\
    Id: {}\n\
    Level: {}\n\
    Hp: {}/{}\n\
    Damage: {}\n\
    Armor: {}\n\
    Coordinates: {}".format(
                self.name, self.id, self.level, self.hp, self.maxHp, self.damage,
                self.armor, coordsFormat(self.x, self.y)
            ).split("\n"))


class inventory:
    """A class that can manage items. Used for shop and players."""

    def __init__(self, id):
        """inventory(id)"""
        self.id = id
        # Holds the item ids
        self.inventory = []

    def gainItem(self, itemId):
        """Add or remove an item from this inventory:"""
        if itemId not in self.inventory:
            self.inventory += [itemId]

    def dropItem(self, itemId):
        if itemId in self.inventory:
            self.inventory.pop(self.inventory.index(itemId))

    def viewInventory(self):
        """Return nice format of every item in given inventory"""
        if self.inventory:
            message = ""
            itemNames = []
            for i in self.inventory:
                # Print level as well when it is armor or a weapon
                if items[i].itemType == "Armor" or items[i].itemType == "Weapon":
                    level = " level %s" % (items[i].level)
                else:
                    level = ""
                itemNames += ["{}{}: {} ({}), effect {}, value {}.\n".format(
                    items[i].itemType, level, items[i].name,
                    items[i].id, items[i].effect, items[i].value
                )]
            itemNames.sort()
            for i in itemNames:
                message += i
            return message
        else:
            return None


class player(creature, inventory):
    # Todo: sepparate ids and names

    def __init__(self, id):
        """player(id)"""
        # Starts in Cromania
        self.x = 0
        self.y = 0
        locations[0][0].playerEnters(id)
        # How to refer to this player
        self.id = id
        # Distinct from creatures
        self.creatureType = "Player"
        # Used for messages
        self.name = id
        # Start at level 1, max 100
        self.level = initialLevel
        # Level up when a player reaches a certain xp amount, amount increases per level.
        self.xp = 0
        self.maxHp = getLevelHp(self.level)
        self.hp = self.maxHp
        # Initial stats
        self.damage = noWeaponDamage
        self.armor = 0
        # Gold that the player currently has on them. One loses it on death.
        self.gold = initialGold
        # Money that is safe from dangers.
        bank[id] = 10
        # Remember how many players someone has killed.
        self.playerKills = 0
        # Remember how many NPCs someone has killed.
        self.kills = 0
        # Remember how often someone has died.
        self.deaths = 0
        # Id's of items in inventory.
        self.inventory = []
        # Id's of equipped items: [weapon, armor]. -1 means nothing equiped.
        self.equipped = [-1, -1]

    def move(self, args):
        """Move between locations, checks for valid input,
        can move in 8 directions, distance multiplier is limeted to one's level.
        Eg: "/m se 5" moves some 5 locations south, 5 locations east."""

        # First user input ("/m" base command is ignored)
        direction = str(args[0])
        if not (
                direction == "n"
                or direction == "s"
                or direction == "w"
                or direction == "e"
                or direction == "ne"
                or direction == "nw"
                or direction == "se"
                or direction == "sw"):
            # Valid direction?
            return "You passed an invalid direction! "
        # The more enemies and the higher their levels, the lower the chance to be able to move.
        # The chance is "player levels / sum of enemy levels".
        fleeChance = 0

        for i in locations[self.x][self.y].population:
            # Get all creature levels
            fleeChance += creatures[i].level

        if not fleeChance:
            # 1 if there is no creature
            fleeChance = 1
        fleeChance = self.level / fleeChance

        # Random chance
        if fleeChance > random():
            # If no multiplier variable is given, move only one.
            multiplier = 1
            try:
                # Second user input, see if it is a valid number and <= player level
                multiplier = int(args[1])
                if multiplier > self.level:
                    return "The multiplier can only be as high as your level."
            # Error if multiplier cannot be converted
            except ValueError:
                return "Invalid multiplier. "
            # Ignore if no multiplier is given
            except IndexError:
                pass
            # Leave old location
            locations[self.x][self.y].playerLeaves(self.id)

            # Calculate new coordinates
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

            # Create new a new location if it doesn't exist,
            # newLocation() returns a message with info of the location.
            if self.x not in locations:
                message = newLocation(
                    self.x, self.y, choice(list(locationTypes.keys())),
                    abs(self.level + randint(-2, 2))
                )
            elif self.y not in locations[self.x]:
                message = newLocation(
                    self.x, self.y, choice(list(locationTypes.keys())),
                    abs(self.level + randint(-2, 2))
                )
            # Or tell what already discovered location a player is in:
            else:
                message = "Terrain: {}.".format(locations[self.x][self.y].locationType)

            locations[self.x][self.y].playerEnters(self.id)
            return "You now are in {}. {}".format(coordsFormat(self.x, self.y), message)
        # If one fails to move, it is attacked by a random creature in the location.
        else:
            # The first thing in the list is the attack message, the second the fightBack boolean.
            return "You failed to flee and were attacked! {}".format(
                creatures[choice(locations[self.x][self.y].population)].attack(self.id)[0]
            )

    def gainXp(self, xp):
        """Handle xp rewards, level ups and max level."""
        # Ignore if no xp
        if xp <= 0:
            return
        # Ignore if already level 100
        if self.level < 100:
            # End with a space for ongoing messages.
            message = "You gained " + str(xp) + " XP. "
            self.xp += xp
            # getLevelXp() gives the amount xp needed to level up.
            # Keep leveling up when total xp is greater than this value.
            while self.xp >= getLevelXp(self.level):
                self.xp -= getLevelXp(self.level)
                self.level += 1
                # The only thing that directly changes when leveling up is maxHp.
                self.maxHp = getLevelHp(self.level)
                self.hp = self.maxHp
                message += "You leveled up! You are now level " + str(self.level) + ". "

            if self.level >= 100:
                self.xp = 0
                # Ignore previous message.
                return self.name + " reached level 100!!! You can no longer gain XP. "
            message += "You now have " + str(self.xp) + " XP. "
            return message
        else:
            return ""

    def teleport(self, x, y):
        """Locations use different methods when a player moves then when a NPC does."""
        try:
            locations[self.x][self.y].playerLeaves(self.id)
        except Exception:
            pass
        locations[x][y].playerEnters(self.id)
        self.x = x
        self.y = y

    def stats(self):
        """All the player's stats"""
        return "\n".join(line.lstrip() for line in "Id: {}\n\
    Level: {}\n\
    Xp: {}/{}\n\
    Hp: {}/{}\n\
    Damage: {}\n\
    Armor: {}\n\
    Gold: {}\n\
    Bank: {}\n\
    Coordinates: {}\n\
    Player kills: {}\n\
    NPC kills: {}\n\
    Deaths: {}".format(
                self.name, self.level, self.xp, getLevelXp(self.level),
                self.hp, self.maxHp, self.damage, self.armor, self.gold,
                bank[self.id], coordsFormat(self.x, self.y),
                self.playerKills, self.kills, self.deaths
            ).split("\n"))

    def venture(self):
        """When venturing, something happens within the location."""
        # Easier reference
        curLoc = locations[self.x][self.y]
        # Can't venture in Cromania
        if curLoc.locationType == "Cromania":
            return "Not much is happening here in Cromania..."
        # The same chance calculation as when moving (player level / sum of enemy levels)
        ventureChance = 0
        for i in curLoc.population:
            ventureChance += creatures[i].level
        if not ventureChance:
            ventureChance = 1
        ventureChance = self.level / ventureChance
        if ventureChance > random():
            # If venturing succeeds, 25% chance to find a chest with random reward:
            if random() < 0.25:
                return "You found a chest! " + getReward(self, 2 * curLoc.level)
            else:
                # Or spawn a random enemy.
                enemyId = getId()
                level = curLoc.level + randint(-2, 2)
                if level <= 0:
                    level = 1
                if level > 100:
                    level = 100
                lower = round(level / 100 * len(locationTypes[curLoc.locationType])) - 3
                # What if upper too high?
                upper = round(level / 100 * len(locationTypes[curLoc.locationType])) + 3
                if lower < 0:
                    lower = 0
                if upper >= len(locationTypes[curLoc.locationType]):
                    # Upper can be the actual length because the slice in the next line excludes it.
                    lower = len(locationTypes[curLoc.locationType]) - 10
                creatures[enemyId] = creature(
                    self.x, self.y, enemyId,
                    choice(locationTypes[curLoc.locationType][lower:upper]), level
                )
                return "You encountered a {} {} with id {}.".format(
                    creatures[enemyId].n, creatures[enemyId].name, enemyId
                )
        else:
            return "You were attacked! {}".format(
                creatures[choice(locations[self.x][self.y].population)].attack(self.id)[0]
            )

    def equip(self, itemId, effect):
        """Equip an item and adjust stats."""
        if itemId in self.equipped:
            self.equipped[self.equipped.index(itemId)] = -1
            itemtype = items[itemId].itemType
            if itemtype == "Armor":
                self.armor = 0
            elif itemtype == "Weapon":
                self.damage = noWeaponDamage
            return "You unequipped {}.".format(items[itemId].name)

        if items[itemId].level <= self.level:
            if items[itemId].itemType == "Weapon":
                self.equipped[0] = itemId
                self.damage = effect
                return "You are now using {}!".format(items[itemId].name)
            elif items[itemId].itemType == "Armor":
                self.equipped[1] = itemId
                self.armor = effect
                return "You are now wearing {}!".format(items[itemId].name)
        else:
            # Items have level caps
            return "You have to be at least level {} to use this item.".format(items[itemId].level)

    def unequip(self, itemId):
        """Unequip an item and adjust stats."""
        if items[itemId].itemType == "Weapon":
            # -1 means unequipped.
            self.equipped[0] = -1
            # Always at least some damage.
            self.damage = noWeaponDamage
        elif items[itemId].itemType == "Armor":
            self.equipped[1] = -1
            self.armor = 0


class item:
    """Parent class for healing items, gear."""

    def __init__(self, id, name, itemType, value, ownerId, inventoryId):
        """item(id, name, itemType, value, ownerId, inventoryId)"""
        # Uses same id system as NPCs
        self.id = id
        self.name = name
        # Healing item, weapon etc.
        self.itemType = itemType
        # Price in gold
        self.value = value
        # id of the shop or player that owns it. Used for market.
        self.ownerId = ownerId
        # Inventory it's in.
        self.inventoryId = inventoryId

    def changeInventory(self, newId, newOwner=False):
        """Changes the inventory the item is in to newId,
        and if newOwner is True change the owner as well."""
        inventories[self.inventoryId].dropItem(self.id)
        self.inventoryId = newId
        inventories[self.inventoryId].gainItem(self.id)
        if newOwner:
            self.ownerId = newId

    def destroy(self):
        """Delete the item, remove it from an inventory"""
        ids[self.id] = True
        inventories[self.inventoryId].dropItem(self.id)
        del items[self.id]

    # Move to market with a player-chosen price: other players can buy it,
    # but the seller can't use it anymore.s
    # def market(self, price)


class healingItem(item):
    """Use to regenerate health."""

    def __init__(self, id, name, value, effect, ownerId, inventoryId):
        """healinItem(id, name, value, effect, ownerId, inventoryId)"""
        item.__init__(self, id, name, "Healing Item", value, ownerId, inventoryId)
        # The parentclass item doesn't have effect because future items may not need it.
        self.effect = effect

    def use(self, userId):
        """Actually use the item"""
        creatures[userId].heal(self.effect)
        message = "You used {} healing {}.".format(self.name, self.effect)
        self.destroy()  # Single use
        return message


class armor(item):
    """armor(id, name, level, value, effect, ownerId, inventoryId)"""

    def __init__(self, id, name, level, value, effect, ownerId, inventoryId):
        item.__init__(self, id, name, "Armor", value, ownerId, inventoryId)
        # Minimum required level to equip this item
        self.level = level
        # Armor points
        self.effect = effect

    def use(self, userId):
        """Toggle equip"""
        if self.id in creatures[userId].equipped:
            creatures[userId].unequip(self.id)
            return "You unequipped the " + self.name + ". "
        else:
            creatures[userId].equip(self.id)
            return "You equipped the " + self.name + ". "


class weapon(armor):
    """Really the only difference is the itemType"""

    def __init__(self, id, name, level, value, effect, ownerId, inventoryId):
        """weapon(id, name, level, value, effect, ownerId, inventoryId)"""
        item.__init__(self, id, name, "Weapon", value, ownerId, inventoryId)
        self.level = level
        self.effect = effect

# Functions accessable by players


def start(bot, update):
    """Initial message"""
    # sendMessage() sends a message back to the one that used the command.
    # bot and update gives that information.
    sendMessage(bot, update, "Welcome to FransRPG! Type '/help' for instructions. ")


def help(bot, update):
    """Lists player commands"""
    message = "Type '/help' for this message.\n\
    Type '/start' to see the welcome message.\n\
    Type '/stats [id]' to see that creature's stats.  Player id's are their names. Enter no id for your own stats.\n\
    Type '/location [id]' to get info about that creature's current location.\n\
    Type '/players' to see all players and their locations.\n\
    Type '/join' to create a character.\n\
    Type '/attack [id]' to attack the creature with that id.\n\
    Type '/move [direction] [multiplier]' to move in any of directions n, ne, e, se, s, sw, w or nw. Multiplier is limited to your level.\n\
    Type '/venture' to explore your current location.\n\
    Type '/deposit [amount]' or '/withdraw [amount]' to move your gold when in Cromania.\n\
    Type '/give [amount] [playername]' to bring that amount of gold to someone's bank.\n\
    Type '/shop' to see the content of the shop.\n\
    Type '/inventory' to see the items in your inventory.\n\
    Type '/buy [id]' to buy an item.\n\
    Type '/use [id]' to use, equip or unequip an item.\n\
    Type '/drop [id]' to drop an item.\n\
    Type '/save' to save the game to file. Autosave will occur after every 20 send messages.\n\
    Type '/load [filename]' to load the game from the given file. Legit filenames are 'save',\n\
    'autosave' and 'reset'.\n\
    Items and shop and fill do not work yet."
    message = "\n".join(line.lstrip() for line in message.split("\n"))
    sendMessage(bot, update, message)


def stats(bot, update, args):
    """Get info about a player or creature"""
    if args:
        id = args[0]
        try:
            # Try to make a creature id out of the argument. Player ids stay strings.
            id = int(id)
        except ValueError:
            pass
        if id in creatures:
            sendMessage(bot, update, creatures[id].stats())
        else:
            # Players are creatures as well
            sendMessage(bot, update, "There is no creature with that id...")
    else:
        # If there is no argument, give info about the player itself.
        id = getName(update)
        if id in creatures:
            sendMessage(bot, update, creatures[id].stats())
        else:
            sendMessage(bot, update, "You do not have a character yet! Create one with /join.")


def locationInfo(bot, update, args):
    """Gives info about the location a creature (players are creatures as well) is in."""
    if len(args) == 1:
        id = args[0]
        try:
            id = int(id)
        except ValueError:
            pass

        if id in creatures:
            # Find location and use build-in info() method
            sendMessage(bot, update, locations[creatures[id].x][creatures[id].y].info())
        else:
            sendMessage(bot, update, "There is no creature with that id...")
    elif len(args) == 2:
        try:
            y = int(args[0])
            x = int(args[1])
            message = locations[x][y].info()
            sendMessage(bot, update, message)
        except KeyError:
            sendMessage(bot, update, "That location is not yet discovered.")
        except ValueError:
            sendMessage(bot, update, "You passed an invalid value!")

    else:
        # No argument gives info about the location of the player itself
        id = getName(update)
        if id in creatures:
            sendMessage(bot, update, locations[creatures[id].x][creatures[id].y].info())
        else:
            sendMessage(bot, update, "You do not have a character yet! Create one with /join.")


def listPlayers(bot, update):
    """View all players and their coordinates."""
    message = ""
    for creature in list(creatures.values()):
        if creature.creatureType == "Player":
            message += "{} level {}: {}\n".format(
                creature.name, creature.level, coordsFormat(creature.x, creature.y)
            )
    sendMessage(bot, update, message)


def join(bot, update):
    """Create a character to join the game!"""
    # Extracts user name from the update class.
    id = getName(update)
    if id not in creatures:
        creatures[id] = player(id)
        inventories[id] = creatures[id]
        # Give a player a beginning weapon with level 2 stats
        start_weapon_id = getId()
        start_weapon_effect = getItemEffect("Weapon", 2)
        start_weapon_value = getItemValue("Weapon", start_weapon_effect)
        start_weapon_name = newItemName("Weapon", 1)
        items[start_weapon_id] = weapon(
            id, start_weapon_name, 1, start_weapon_value, start_weapon_effect, id, id
        )
        creatures[id].equip(start_weapon_id, start_weapon_effect)
        # Give a player a beginning armor with level 1 stats
        start_armor_id = getId()
        start_armor_efffect = getItemEffect("Armor", 1)
        start_armor_value = getItemValue("Armor", start_armor_efffect)
        start_armor_name = newItemName("Weapon", 1)
        items[start_armor_id] = armor(
            id, start_armor_name, 1, start_armor_value, start_armor_efffect, id, id
        )
        creatures[id].equip(start_armor_id, start_armor_efffect)
        sendMessage(bot, update, "You joined the game! Your name is " + id + ".")
        fillStore(bot, update)
    else:
        sendMessage(bot, update, "You already have a character...")


def move(bot, update, args):
    """Move between locations, first argument is direction and optional second is multiplier."""
    id = getName(update)
    if id in creatures:
        sendMessage(bot, update, creatures[id].move(args))
    else:
        sendMessage(bot, update, "You do not have a character yet! Create one with /join.")


def attack(bot, update, args):
    """Attack creature with this id. Only allowed in group chats."""
    id = getName(update)
    if args:
        # Target id
        target = str(args[0])
        if target in creatures:
            # Not allowed in private chat
            if (
                    creatures[target].creatureType == "Player"
                    and update.message.chat.type == "private"
                    and not id == target):
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
        # If figthBack is True, make the victim attack back.
        if returnValue[1]:
            sendMessage(bot, update, str(creatures[target].attack(id)[0]))
    else:
        sendMessage(bot, update, "You do not have a character yet! Create one with /join.")


def venture(bot, update):
    """Adventure in the location, with a chance on loot or enemies."""
    id = getName(update)
    if id in creatures:
        sendMessage(bot, update, creatures[id].venture())
    else:
        sendMessage(bot, update, "You do not have a character yet! Create one with /join.")


def deposit(bot, update, args):
    """Transfer gold to bank."""
    id = getName(update)
    if creatures[id].x != 0 or creatures[id].y != 0:  # Only allowed in Cromania
        sendMessage(bot, update, "You have to be in Cromania to do that.")
        return
    if id in creatures:
        if args:
            try:
                # Valid value?
                amount = int(args[0])
                # Enough money?
                if amount <= creatures[id].gold:
                    sendMessage(bot, update, "Deposited " + str(amount) + " gold.")
                    bank[id] += amount
                    creatures[id].gold -= amount
                else:
                    sendMessage(bot, update, "You do not have that amount of money!")
            except ValueError:
                sendMessage(bot, update, "You passed an invalid value!")
        else:
            amount = creatures[id].gold
            sendMessage(bot, update, "Deposited {} gold.".format(amount))
            bank[id] += amount
            creatures[id].gold = 0
    else:
        sendMessage(bot, update, "You do not have a character yet! Create one with /join.")


def withdraw(bot, update, args):
    """Transfer gold from the bank"""
    id = getName(update)
    if creatures[id].x != 0 or creatures[id].y != 0:
        sendMessage(bot, update, "You have to be in Cromania to do that.")
        return
    if id in creatures:
        if args:
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
        else:
            amount = bank[id]
            sendMessage(bot, update, "Withdrew {} gold.".format(amount))
            creatures[id].gold += amount
            bank[id] = 0
    else:
        sendMessage(bot, update, "You do not have a character yet! Create one with /join.")


def giveMoney(bot, update, args):
    """Transfer gold (inventory gold, not bank gold) to another player's bank."""
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
            sendMessage(bot, update, "That creature does not exist...")
    else:
        sendMessage(bot, update, "You do not have a character yet! Create one with /join.")


def save(bot, update, filename="save"):
    """Save all creatures, items, locations etc. to file [filename].pkl."""
    with open(filename + ".pkl", "wb") as output:
        pickle.dump(creatures, output, pickle.HIGHEST_PROTOCOL)
        pickle.dump(inventories, output, pickle.HIGHEST_PROTOCOL)
        pickle.dump(items, output, pickle.HIGHEST_PROTOCOL)
        pickle.dump(locations, output, pickle.HIGHEST_PROTOCOL)
        pickle.dump(ids, output, pickle.HIGHEST_PROTOCOL)
        pickle.dump(bank, output, pickle.HIGHEST_PROTOCOL)
        sendMessage(bot, update, "Saved to '{}'.".format(filename))


def load(bot, update, args):
    """Load all creatures, items, locations etc. from file [filename].pkl."""
    try:
        with open(args[0] + ".pkl", "rb") as input:
            global creatures
            global inventories
            global items
            global locations
            global ids
            global bank
            creatures = pickle.load(input)
            inventories = pickle.load(input)
            items = pickle.load(input)
            locations = pickle.load(input)
            ids = pickle.load(input)
            bank = pickle.load(input)

            for inv in inventories:
                if inv in creatures:
                    inventories[inv] = creatures[inv]

            sendMessage(bot, update, "Loaded from '" + args[0] + "'. ")
    except Exception:
        sendMessage(bot, update, "Unable to load. Did you spell the filename right?")


def do(bot, update, args):
    """Execute a Python command. Only allowed for certain players."""
    # See if the id of the user matches one in the json file (which would mean the user is an admin)
    if getTelegramId(update) in admins:
        try:
            # Try to execute the command.
            text = str(eval(str(" ".join(args))))
        except:
            text = "Invalid command."
        sendMessage(bot, update, text)
    else:
        sendMessage(bot, update, "You have to be an admin for that.")


def reset(bot, update):
    """Delete everything and start from the beginning. Only allowed for certain players."""
    if getTelegramId(update) in admins:
        global creatures
        global inventories
        global items
        global locations
        global ids
        global bank
        global messageCount
        # Save a backup
        save(bot, update, "reset")
        # Delete everything
        creatures = {}
        inventories = {}
        items = {}
        locations = {}
        bank = {}
        # Reset ids
        ids = [True]
        messageCount = 0
        # Create initial location.
        newLocation(0, 0, "Cromania", 1)
        inventories["storeObjectId"] = inventory("storeObjectId")
        sendMessage(bot, update, "Reset all game data! Type '/load reset' to undo.")
    else:
        sendMessage(bot, update, "You have to be an admin for that.")


def viewStore(bot, update):
    """Lists all items in the shop"""
    id = getName(update)
    # Only allowed in Cromania
    if creatures[id].x != 0 or creatures[id].y != 0:
        sendMessage(bot, update, "You have to be in Cromania to do that.")
        return
    content = inventories["storeObjectId"].viewInventory()
    if content:
        sendMessage(bot, update, content)
    else:
        sendMessage(bot, update, "The shop is currently empty!")


def buy(bot, update, args):
    """Buy an item from the shop and move it to a players inventory"""
    playerId = getName(update)
    # Only allowed in Cromania
    if creatures[playerId].x != 0 or creatures[playerId].y != 0:
        sendMessage(bot, update, "You have to be in Cromania to do that.")
        return
    if playerId in creatures:
        try:
            # Create usable id from the given args
            itemId = int(args[0])
        except Exception:
            sendMessage(bot, update, "You passed an invalid value!")
            return
        if itemId in inventories["storeObjectId"].inventory:
            if creatures[playerId].gold >= items[itemId].value:
                creatures[playerId].gold -= items[itemId].value
                items[itemId].changeInventory(playerId, True)
                sendMessage(bot, update, "You bought the {}!".format(items[itemId].name))
            else:
                sendMessage(bot, update, "You do not have that amount of money!")
        else:
            sendMessage(bot, update, "That item is not in the shop.")
    else:
        sendMessage(bot, update, "You do not have a character yet! Create one with /join.")


def use(bot, update, args):
    """Use a healing item or toggle equip of armor and weapons."""
    playerId = getName(update)
    if playerId in creatures:
        try:
            # Create usable id from the given args
            itemId = int(args[0])
        except Exception:
            sendMessage(bot, update, "You passed an invalid value!")
            return
        if itemId in creatures[playerId].inventory:
            if items[itemId].itemType == "Healing Item":
                # Universal for healingItem(), armor() and weapon().
                sendMessage(bot, update, items[itemId].use(playerId))
            else:
                sendMessage(bot, update, creatures[playerId].equip(itemId, items[itemId].effect))
        else:
            sendMessage(bot, update, "That item is not in your inventory.")
    else:
        sendMessage(bot, update, "You do not have a character yet! Create one with /join.")


def drop(bot, update, args):
    """Destroy an item in a player's inventory."""
    playerId = getName(update)
    if playerId in creatures:
        try:
            itemId = int(args[0])
        except Exception:
            sendMessage(bot, update, "You passed an invalid value!")
            return
        if itemId in creatures[playerId].inventory:
            sendMessage(bot, update, "You dropped the " + items[itemId].name + "!")
            # Takes care of everything
            items[itemId].destroy()
        else:
            sendMessage(bot, update, "That item is not in your inventory.")
    else:
        sendMessage(bot, update, "You do not have a character yet! Create one with /join.")


def viewPlayerInventory(bot, update):
    """List all items in the caller's inventory"""
    id = getName(update)
    if id in creatures:
        content = inventories[id].viewInventory()
        if content:
            sendMessage(bot, update, content)
        else:
            sendMessage(bot, update, "There is nothing in your inventory.")
    else:
        sendMessage(bot, update, "You do not have a character yet! Create one with /join.")

# Various functions for formatting, calculating values, creating etc.


def newLocation(x, y, locationType, level):
    """Create a new location instance and return a message describing it."""
    if x not in locations:
        locations[x] = {}
        locations[x][y] = location(x, y, locationType, level)
    else:
        locations[x][y] = location(x, y, locationType, level)
    return "New " + getRating(level) + " location discovered: " + locationType + ". "


def newItemName(type, level):
    """Generates an item name. Number of adjectives based on the level,
    and adjectives and names are chosen the higher the level,
    the higher in the lists."""
    # Choose list:
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
    # Ratio of current level to max level -> ratio of nth item to all items
    itemLower = round(level / 100 * len(itemsNouns)) - 3
    itemUpper = round(level / 100 * len(itemsNouns)) + 3
    if itemLower < 0:
        itemLower = 0
    if itemUpper > len(itemsNouns):
        # Choice from extra items when near max level
        itemLower = len(itemsNouns) - 10
        # itemsUpper can be left unchanged because the slice at the end of function will ignore it,
        # if it is to high

    adjLower = round(level / 100 * len(itemsAdj)) - 5
    adjUpper = round(level / 100 * len(itemsAdj)) + 5
    if adjLower < 0:
        adjLower = 0

    if adjUpper > len(itemsAdj):
        # Same as at itemsUpper
        adjLower = len(itemsAdj) - 15
    adj = ""
    # At least 1 and at most 5 adjectives
    for i in range(randint(1, 2) + round(level / 33)):
        # Pick a new adjective when it was already chosen
        while adj in name:
            adj = choice(itemsAdj[adjLower:adjUpper])
        name += adj + " "
    name += choice(itemsNouns[itemLower:itemUpper])
    return name


def fillStore(bot, update):
    """Create 5 items per player, with about their level."""
    # inventory list gets smaller when deleting items and the for loop gets confused:
    # Use temporary list instead.
    tempInv = [i for i in inventories["storeObjectId"].inventory]
    # Clear old store inventory
    for i in tempInv:
        items[i].destroy()
    levels = []
    for i in creatures:
        if creatures[i].creatureType == "Player":
            if creatures[i].level not in levels:
                # A few items per different level that players have
                levels += [creatures[i].level]

    for i in levels:
        for j in range(6):
            # Random level with middle slightly below player level
            level = i + randint(-3, 1)
            # But between 1 and 100
            if level <= 0:
                level = 1
            if level > 100:
                level = 100
            id = getId()
            # Any of these items
            item = choice(["Healing Item", "Healing Item", "Healing Item", "Weapon", "Armor"])
            # Random name generator, based on the level.
            name = newItemName(item, level)
            # Formula for effect per item per level
            effect = getItemEffect(item, level + 2)
            if item == "Healing Item":
                # Value based on effect
                value = getItemEffect(item, effect)
                items[id] = healingItem(id, name, value, effect, "storeObjectId", "storeObjectId")
                inventories["storeObjectId"].gainItem(id)
            elif item == "Weapon":
                value = getItemValue(item, effect)
                items[id] = weapon(id, name, level, value, effect, "storeObjectId", "storeObjectId")
                inventories["storeObjectId"].gainItem(id)
            elif item == "Armor":
                value = getItemValue(item, effect)
                items[id] = armor(id, name, level, value, effect, "storeObjectId", "storeObjectId")
                inventories["storeObjectId"].gainItem(id)
    sendMessage(
        bot, update, "The shop content has been reset! Type '/shop' to see the new content."
    )


def getReward(player, rating):
    """Get some gold based on the rating.
    Gives a fair amount when the rating equals the level of a killed NPC."""
    max = round(0.05 * rating ** 2 + 0.5 * rating)
    amount = randint(round(max / 2), max)
    if amount == 0:
        # Always at least 1 gold.
        amount = 1
    player.gold += amount
    return "Your loot is {} gold.".format(amount)


def getName(update):
    """Update contains information about who used a command.
    This extracts the user's name from it."""
    return str(update.message.from_user.first_name)


def getTelegramId(update):
    return str(update.message.from_user.id)


def coordsFormat(x, y):
    """Returns a fancier representation of coordinates."""
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
    """Calculates xp needed for players to level up, per level."""
    return round(level ** 1.1) + 9


def getLevelHp(level):
    """Calculates the max hp of creatues, per level."""
    return int(0.3 * level ** 1.65 + level + 9)


def getItemEffect(item, level):
    """Gives amount of hp healed, damage or armor based on an item's level."""
    if item == "Healing Item":
        return randint(
            round(0.9 * getLevelHp(level) / (0.1 * level + 2)),
            round(1.1 * getLevelHp(level) / (0.1 * level + 2))
        )
    elif item == "Weapon":
        return randint(
            round(getLevelHp(level) / 15 * 1.1), round(getLevelHp(level) / 12 * 1.1)
        ) + 1
    elif item == "Armor":
        return randint(
            round(getLevelHp(level) / 30 * 1.1), round(getLevelHp(level) / 15 * 1.1)
        ) + 1


def getItemValue(item, effect):
    """Gives amount of gold you have to pay for a certain item"""
    if item == "Healing Item":
        return round(0.02 * effect ** 2 + 0.5 * effect - 2)
    if item == "Weapon":
        return round(0.15 * effect ** 2 + 3 * effect)
    if item == "Armor":
        return round(0.15 * (2.5 * effect) ** 2 + 3 * (2.5 * effect))


def getRating(level):
    """Convert location levels to this range."""
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
    """Returns first unoccupied id and marks it as occupied."""
    global ids
    for i in range(len(ids)):
        if ids[i]:
            ids[i] = False
            return i
    ids += [False]
    return len(ids) - 1


def sendMessage(bot, update, message):
    """Sends a message to Telegram, keeps track of autosave, adresses user."""
    global messageCount
    bot.sendMessage(chat_id=update.message.chat_id,
                    text=("@{}\n{}".format(getName(update), message))
                    )
    messageCount += 1
    if messageCount % 20 == 0:
        save(bot, update, "autosave")
    if messageCount % 30 == 0:
        fillStore(bot, update)

# main


def main():
    # The store, with items for purchase. The ID needs to be universal through saves.
    inventories["storeObjectId"] = inventory("storeObjectId")
    global admins
    # Try to load admin ids and bot token
    configfile = json.load(open(argv[1]))
    try:
        admins = configfile["superpowers"]
    except:
        pass

    # Load the token from the json file.
    token = configfile["token"]
    # Something important for the Telegram interface. argv[1] should be the bot token
    updater = Updater(token=token)

    # The same
    dispatcher = updater.dispatcher

    # Commands accessable by players:
    start_handler = CommandHandler("start", start)
    dispatcher.add_handler(start_handler)
    help_handler = CommandHandler("help", help)
    dispatcher.add_handler(help_handler)
    players_handler = CommandHandler("players", listPlayers)
    dispatcher.add_handler(players_handler)
    location_handler = CommandHandler("location", locationInfo, pass_args=True)
    dispatcher.add_handler(location_handler)
    stats_handler = CommandHandler("stats", stats, pass_args=True)
    dispatcher.add_handler(stats_handler)
    join_handler = CommandHandler("join", join)
    dispatcher.add_handler(join_handler)
    move_handler = CommandHandler("move", move, pass_args=True)
    dispatcher.add_handler(move_handler)
    attack_handler = CommandHandler("attack", attack, pass_args=True)
    dispatcher.add_handler(attack_handler)
    venture_handler = CommandHandler("venture", venture)
    dispatcher.add_handler(venture_handler)
    deposit_handler = CommandHandler("deposit", deposit, pass_args=True)
    dispatcher.add_handler(deposit_handler)
    withdraw_handler = CommandHandler("withdraw", withdraw, pass_args=True)
    dispatcher.add_handler(withdraw_handler)
    give_handler = CommandHandler("give", giveMoney, pass_args=True)
    dispatcher.add_handler(give_handler)
    store_handler = CommandHandler("shop", viewStore)
    dispatcher.add_handler(store_handler)
    buy_handler = CommandHandler("buy", buy, pass_args=True)
    dispatcher.add_handler(buy_handler)
    use_handler = CommandHandler("use", use, pass_args=True)
    dispatcher.add_handler(use_handler)
    drop_handler = CommandHandler("drop", drop, pass_args=True)
    dispatcher.add_handler(drop_handler)
    inventory_handler = CommandHandler("inventory", viewPlayerInventory)
    dispatcher.add_handler(inventory_handler)
    do_handler = CommandHandler("do", do, pass_args=True)
    dispatcher.add_handler(do_handler)
    save_handler = CommandHandler("save", save)
    dispatcher.add_handler(save_handler)
    load_handler = CommandHandler("load", load, pass_args=True)
    dispatcher.add_handler(load_handler)
    reset_handler = CommandHandler("reset", reset)
    dispatcher.add_handler(reset_handler)

    #  Create home city with level 1
    newLocation(0, 0, "Cromania", 1)

    #  Start waiting for commands
    updater.start_polling()

if __name__ == '__main__':
    # Start main() on start
    main()
