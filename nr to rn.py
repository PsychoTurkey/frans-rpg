#[["guy", 1], ["guy2", 1], ["guy3", 3]]
#[["guy", "guy2"], [], ["guy3"]]

length = len([["Goat",2],["Mad Brat",4],["Brat",3],["Goblin",6],["Squirel",1],["Angry Cucumber",11],["Rocky Snake",12],["Flat Hat",1],["Flop Hat",1],["Hat",2],["Suare Hat",7],["Red Hat",3],["Top Hat",9],["Froblin",8],["Hoblin",7],["Old Computerscreen",1],["Mist",3],["Myst I",6],["Myst II",9],["Cloud",1],["Fluffy Cloud",1],["Rainy Cloud",9],["Rock",2],["Ordinairy Rock",2],["Moss Monster",7],["Mad Trashcan",18],["Saturday Music",5],["Flying Zits",19],["Faling Branch",3],["Faling Tree",7],["A Head",1],["Robot",12],["Broken Robot",4],["Evil Robot",18],["Mechatronicon",22],["Pointy Stick",2],["Worm",0],["Big Snail",2],["Sneeze",1],["Snow",1],["Mountain Goat",14],["Coyote",3],["Mountain Dog",5],["Moon Moon",0],["Wolf",12],["Blood Wolf",15],["Spagetii Monster",23],["Blind Wolf",6],["Corrupted Hat",28],["Old Summer Breeze",1],["Evil Flower",21],["FatCat",1],["A lost cyclist",2],["Mean Teddybear",8],["Freddy",9],["Paperhat-aeroplane",4],["Grassmonster",5],["Flobglob",3],["Plofkip",1],["A lost Penguin",3],["Small Wolf",5],["Puppy",1],["Kitten",1],["Flying mittens",13],["a Rusty Moustache",14],["Broblaglorb",16],["Snobtrobl",3],["Dwarf",3],["Black Dwarf",4],["Ginger Dwarf",5],["Armored Dwarf",6],["Pink Dwarft",7],["Magical Dwarf",8],["Master Dwarf",9],["Troubled Dwarf",10],["King Dwarf",11],["Little Dwarf",2],["Electric Dwarf",12],["Fat Dwarf",7],["Feral Slug",1],["Feral Cat",1],["Big Feral Cat",5],["Feral Dog",2],["Big Feral Dog",7],["Feral Snake",4],["Feral Frog",0],["Feral Owl",7],["Feral",1],["Feral ?",3],["Feral ??",6],["Feral ???",9],["Feral Hat",1],["Feral Rock",0],["Feral Potato",3],["Feral Tree",4],["Feral Atomic Bomb",11],["Feral Cough",0]])
convert = [[0 for x in range(2)] for x in range(length)]
convert = [["Goat",2],["Mad Brat",4],["Brat",3],["Goblin",6],["Squirel",1],["Angry Cucumber",11],["Rocky Snake",12],["Flat Hat",1],["Flop Hat",1],["Hat",2],["Suare Hat",7],["Red Hat",3],["Top Hat",9],["Froblin",8],["Hoblin",7],["Old Computerscreen",1],["Mist",3],["Myst I",6],["Myst II",9],["Cloud",1],["Fluffy Cloud",1],["Rainy Cloud",9],["Rock",2],["Ordinairy Rock",2],["Moss Monster",7],["Mad Trashcan",18],["Saturday Music",5],["Flying Zits",19],["Faling Branch",3],["Faling Tree",7],["A Head",1],["Robot",12],["Broken Robot",4],["Evil Robot",18],["Mechatronicon",22],["Pointy Stick",2],["Worm",0],["Big Snail",2],["Sneeze",1],["Snow",1],["Mountain Goat",14],["Coyote",3],["Mountain Dog",5],["Moon Moon",0],["Wolf",12],["Blood Wolf",15],["Spagetii Monster",23],["Blind Wolf",6],["Corrupted Hat",28],["Old Summer Breeze",1],["Evil Flower",21],["FatCat",1],["A lost cyclist",2],["Mean Teddybear",8],["Freddy",9],["Paperhat-aeroplane",4],["Grassmonster",5],["Flobglob",3],["Plofkip",1],["A lost Penguin",3],["Small Wolf",5],["Puppy",1],["Kitten",1],["Flying mittens",13],["a Rusty Moustache",14],["Broblaglorb",16],["Snobtrobl",3],["Dwarf",3],["Black Dwarf",4],["Ginger Dwarf",5],["Armored Dwarf",6],["Pink Dwarft",7],["Magical Dwarf",8],["Master Dwarf",9],["Troubled Dwarf",10],["King Dwarf",11],["Little Dwarf",2],["Electric Dwarf",12],["Fat Dwarf",7],["Feral Slug",1],["Feral Cat",1],["Big Feral Cat",5],["Feral Dog",2],["Big Feral Dog",7],["Feral Snake",4],["Feral Frog",0],["Feral Owl",7],["Feral",1],["Feral ?",3],["Feral ??",6],["Feral ???",9],["Feral Hat",1],["Feral Rock",0],["Feral Potato",3],["Feral Tree",4],["Feral Atomic Bomb",11],["Feral Cough",0]]

maxlvl = 0
for i in convert:
    if i[1] > maxlvl:
        maxlvl = i[1]

result = [[0] for x in range(maxlvl + 1)]

for i in convert:
    if result[i[1]] == [0]:
        result[i[1]] = [i[0]]
    else:
        result[i[1]] += [i[0]]
print(result)
