#!/usr/bin/env python3

from random import randint
from random import choice

healingItems = ['Arsenic', 'Dirt', 'Water', 'Bread', 'Corn', 'Frog', 'Fluorine', 'Potato', 'Not So Hot Dog', 'Salad', 'Beans', 'Fish', 'Tooth Paste', 'Cucumber', 'Soda', 'Bunch Of Peas', 'Sandwich', 'Brew', 'Draught', 'Chicken Wing', 'Icecream', 'Hamburger', 'Apple', 'Tomato', 'Coffee', 'Cabbage', 'Cake', 'Honey', 'Portion Of French Fries', 'Mushroom', 'Canadian Bacon', 'Pancakes', 'Ketchup', 'Cookie', 'Maple Syrup', 'Soup', 'Waffle', 'Lizard', 'Medicine', 'Tea', 'Remedy', 'Potion', 'Cheese', 'Cupcake', 'Bacon', 'Chocolate', 'Strange Substance', 'Heroïn', 'Rice', 'Hugs In A Bottle', 'Unicorn Blood', 'Dessert Eagle', 'Chocolate Milk', 'Elixir']
healingItemsAdj = ['Probably Poisonous', 'Awful', 'Diarrhea Inducing', 'Moldy', 'Sucky', 'Diseased', 'Gross', 'Rotten', 'Bad', 'Wasted', 'From The Garbage Can', 'Fast Food', 'Dirty', 'Unhealthy', 'Barely Acceptable', 'Best Before: Two Weeks Ago', 'Hate Filled', 'Mediocre', 'Lacking Vitamins', 'Gay', 'Ok', 'Cheap', 'Nice', 'Fried', 'FDA Approved', 'Tasty', 'Fresh', 'Gluten Free', 'Herbal', 'Average', 'Vegetarian', 'Good', 'Grilled', 'Shake Before Usage', 'Ice Cold', 'Normal', 'Exhilarating', 'Moisturized', 'Catch Up', 'Standard', 'Filling', 'Yummy Yummy In My Tummy', '0% Fats', 'Great', 'Open Here', 'Cooked', 'Roasted', 'Love Infused', 'Cheesy', 'Chocolate', 'Super', 'Baked', 'Vegan', 'Special', 'Glowing', 'Sundried', 'Heroic', 'Makes You Vomit Rainbows', 'Glorious', 'Marinated', 'Awesome', 'Healthy', 'Exquisite']
weaponItems = ['Throwing Sand', 'Boots', 'Twig', 'Rock', 'Stone', 'Rubber Band', 'Butter Knife', 'Stick', 'Scissors', 'Fork', 'Bone', 'Shovel', 'Wrench', 'Magnets', 'Catapult', 'Lasso', 'Water Gun', 'Bear Hugs', 'Crowbar', 'Boxing Glove', 'Piece Of Glass', 'Bowling Ball', 'Chair', 'Club', 'Hammer', 'Blowgun', 'Boomerang', 'Bear Hands', 'Cheese Rasp', 'Razor', 'Knife', 'Baseball Bat', 'Saw', 'Tomahawk', 'Dagger', 'Axe', 'Machete', 'Bow And Arrow', 'Shuriken', 'Sai', 'Spear', 'Staff', 'Guitar', 'Cutlass', 'Crossbow', 'Nunchucks', 'Poison', 'Sword', 'Magic Wand', 'Rapier', 'Musket', 'Mace', 'Lance', 'Flail', 'Nail Gun', 'Blow Torch', 'Flintlock Rifle', 'Katana', 'Mines', 'Battleaxe', 'Revolver', 'Tazer', 'Cannon', 'Bombs', 'Bucket Of Lava', 'Piano String', 'Bubble Blaster', 'Bible', 'Thora', 'Koran', 'Pistol', 'Mysterious Syringe', 'Lawn Mower', 'Unholy Tome', 'Flame Thrower', 'Shotgun', 'Unidentified Weapon', 'Rifle', 'Sledge Hammer', 'Dynamite', 'Submachine Gun', 'Radioactive Barrel', 'Grand Piano', 'Chainsaw', 'Machine Gun', 'Sniper Rifle', 'Grenade', 'Spoon', 'Solar Flare', 'Excalibur', 'AK 47', 'Desert Eagle', 'Molotov Cocktail', 'Bazooka', 'Microwave', "Dragon's Tail", 'Javelin', 'Grenade Launcher', 'RPG', 'Unicorn Horn', 'X-57613C', 'Minigun', 'Gatling Gun', 'Tank']
weaponItemsAdj = ['Broken', 'Cardboard', 'Old', 'Toy', 'Dull', 'Weaponized', 'Plastic', 'Imaginary', 'Implausible', 'Anticlimactic', 'Rusty', 'Lite', 'Inferior', 'N00by', 'Origami', 'Dead Battery', 'Oil Leaking', 'Unreliable', 'Glass', 'Adorable', 'Wooden', 'Bolt Action', 'Pocket', 'Light', 'Steam Powered', 'Not So Bad', 'Bloody', "Cowboy's", 'Wi-Fi Enabled', 'Sharp', 'Spiked', 'Competent', 'Steel', "Gentleman's", 'Fearsome', 'Semi Automatic', 'Waterproof', 'Hands Free', 'Good', 'Medieval', 'Adjustable', 'Flaming', 'Suspicious', 'Shiny', 'Scoped', 'Dug Up', 'Dangerous', 'Stable', 'Steady', 'Mechanical', 'Environment Friendly', 'Portable', 'Electrical', 'Powerful', 'Great', 'Shocking', 'Do It Yourself', 'Laser', 'Shafting', 'Energized', 'Huge', 'Ninja', 'Accurate', 'Full Automatic', 'Ruby Inlaid', 'White Hot', 'Blinding', 'Super', 'Dual', 'Intangible', 'Crushing', 'Heavy', 'Epic', 'Stunning', 'Fear Powered', 'Digital', 'Melting', 'Special', 'Crippling', 'Holy', 'Invisible', 'Precise', 'Rocket Propelled', 'Undefined', 'Explosive', 'Laser Guided', 'Head Popping', 'Legendary', 'Smart', 'Plasma', 'Lovely', 'Hydrogen', 'Celestrial', 'Limited Edition', '.50 Cal', "Wizard's", "Rachmaninoff's", 'Magical', 'Majestic', 'Very Special', 'Sacred', 'Demonic', 'Four Dimensional', 'Theoratical', 'Antimatter', 'Alien', "Master's", 'Perfect']
armorItems = ['Underwear', 'Bra', 'Body Paint', 'Fierce Frown', 'Paper Shopping Bag Hat', 'Trousers', 'Arm Protectors', 'Leg Protectors', 'Bikini', "Fuck This Shit I'm Going Naked", 'Sweater', 'Back Protectors', 'Hat', 'Earcuffs', 'Chest Protectors', 'Water Wings', 'Cooking Pan Helmet', 'Head Protectors', 'Goggles', 'Fake Mustache', 'Arm Plating', 'Cape', 'Hockey Mask', 'Leg Plating', 'Gloves', 'Bucket Helmet', 'Back Plating', 'Kilt', 'Pumpkin Helmet', 'Chest Plating', 'Real Helmet', 'Boots', 'Head Plating', 'Suit', 'Arm Armor', 'Garbage Can Lid Shield', 'Leg Armor', 'Crown', 'Back Armor', 'Shield', 'Chest Armor', 'Vest', 'Head Armor', 'Power Suit', 'Arm Power Armor', 'Turtle Shell', 'Leg Power Armor', 'Reactive Armor', 'Back Power Armor', 'Power Shield', 'Sarcasm', 'Top Hat', 'Chest Power Armor', 'Magical Barrier', 'Head Power Armor', 'Tank']
armorItemsAdj = ['Old', 'Broken', 'Gross', 'Skin', 'Pre Historic', 'Ripped', 'Unwashed', 'Aluminum Foil', 'Black', 'Wooden', 'Trashy', 'Implausible', 'Made In China', 'Brittle', 'Hole Filled', 'Shabby', 'Cardboard', 'Inferior', 'Weak', 'Hide', 'Paper', 'Slippery', 'Falling Apart', 'Leather', 'Slutty', 'Homemade', 'Light', 'Not So Bad', 'Duct Tape', "Gentleman's", 'Good', 'Copper', 'Sneaking', 'Protective', 'Roman', 'Cool', 'Bronze', 'Feathered', 'Makes You Look Skinny', 'Fireproof', 'Tough', 'Shiny', 'Huge', 'Analog', 'Iron', 'Made In Germany', 'Special', 'Sparkling', 'Stunning', 'Super', 'White', 'Winged', 'Steel', 'Heavy', 'Bulletproof', 'Holy', 'Invisible', 'Spock', 'Beautiful', 'Twinkling', 'Emerald Inlaid', 'Legendary', 'Sacred', 'Ironic', 'Dragon Scales', 'Bad As Badass', 'Fabulously Amazebaltastic', 'Futuristic', 'Unicorn Hide', 'Asian', "Master's", 'Perfect']


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
    itemLower = round(level / 100 * len(itemsNouns)) - 3 #Ratio of current level to max level -> ratio of nth healing item to all healing items
    itemUpper = round(level / 100 * len(itemsNouns)) + 3
    if itemLower < 0:
        itemLower = 0
    if itemUpper > len(itemsNouns):
        itemLower = len(itemsNouns) - 10 #Extra items when near max level

    adjLower = round(level / 100 * len(itemsAdj)) - 5
    adjUpper = round(level / 100 * len(itemsAdj)) + 5
    if adjLower < 0:
        adjLower = 0
    if adjUpper > len(itemsAdj):
        adjLower = len(itemsAdj) - 15 #Extra Adj near when max level
    adj = ""
    for i in range(randint(1, 2) + round(level / 33)): #Min 1, max 5 Adj
        while adj in name:
            adj = choice(itemsAdj[adjLower : adjUpper])
        name += adj + " "
    name += choice(itemsNouns[itemLower : itemUpper])
    return name

for i in range(100):
    print(i, newItemName("Healing Item", i))
