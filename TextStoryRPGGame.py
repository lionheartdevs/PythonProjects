"""THIS IS A TEXT BASED STORY RPG. THIS IS MY FIRST PROJECT USING PYTHON. I TRIED TO PUT ALL PYTHON TO USE
IN THIS PROJECT. USING NESTED DICTIONARY AND NESTED LOOPS TO GET A ROBUST GAME(IN ONLY TEXT FORMAT). THIS GAME IS
NOT YET COMPLETE, IF YOU HAVE AN SUGGESTIONS, PLEASE FEEL FREE TO REACH OUT TO ME. THE PATH OF KNOWLEDGE AND MASTERY
IS NEVER FULLY REALISED AND IS ALWAYS A MOVING GOAL OF ENDLESS DEPTH..."""

###THIS GAME IS ONLY HALF COMPLETE AND IS BEING CREATED AS AN ONGOING LEARNING PROJECT,

#IMPORTING ALL OUR NEEDED MODS.

import random
import sys
import os
import time


####all global variables and funtions work###dont alter###
#THIS IS A SETUP LIST FOR ALL THE GLOBAL VARIABLES WE NEED

fin = open('largewordslist.txt')
letters = ("abcdefghijklmnopqurtuvwxyz")
letter = [i for i in list(letters.upper())]
numbers = [i for i in range(1, 50)]
board = {}
boxes = []
treasure_items = {}


#THIS CREATES OUR PARAMETERS FOR EACH STAT WE WANT FOR ITEMS
#THIS CREATES A LIST FOR THE TREASURE FUNCTION TO LATER USE
#####THIS WORKS, DO NOT ALTER##########

HP = list(range(0, 100))
SP = list(range(0, 10))
WIS = list(range(0, 10))
LV = list(range(0, 3))
Char_Stats = {'HP':[], 'SP':[], 'WIS':[], 'LV':[]}
number_gen_HP = 0
while number_gen_HP < 1000:
    Char_Stats['HP'] += [random.choice(HP)]
    number_gen_HP += 1
number_gen_SP = 0
while number_gen_SP < 1000:
    Char_Stats['SP'] += [random.choice(SP)]
    number_gen_SP += 1
number_gen_WIS = 0
while number_gen_WIS < 1000:
    Char_Stats['WIS'] += [random.choice(WIS)]
    number_gen_WIS += 1
number_gen_LV = 0
while number_gen_LV < 1000:
    Char_Stats['LV'] += [random.choice(LV)]
    number_gen_LV += 1

#THIS CREATES A NESTED DICTIONARY THAT HAS THE DATA POINT OF EVERY SINGLE UNDERSCORE ON OUR MAP(OVER 1000)
#THIS WILL HELP CREATE THE ILLUSION THAT OUR CHAR. IS MOVING ON THE TEXT MAP
#####THIS WORKS DONT TOUCH IT###############################


for x in range(203, 5278):
    if x % 2 != 0:
        boxes.append(x)

for y in letter:
    board[y] = {}

n_0 = 0
for y in letter:
    for i in numbers:
        board[y][i] = boxes[n_0]
        n_0 += 1


############################################################################
############################################################################
############################################################################
##THIS IS A LIST OF ALL TEST BASED GRAPHICS FOR THE GAME###################
####needs to be adjusted and improved as the game comes together#######

class game_graphics:

    def Enemy():
        print('#################')
        print('    __________   ')
        print('   /  `    `  \  ')
        print('  /   0  ^  0  \ ')
        print('  \   /^^^^^\  / ')
        print('   |  |vvvvv| |  ')
        print('    \________/   ')
        print('                 ')
        print('#################')
        print('#################')
        print()
        print('You encountered a monster!')

    def Boss():

        print('$$$$$$$$$$$$$$$$$$$$$$$$$$')
        print('$$$$$$$$$$$$$$$$$$$$$$$$$$')
        print('$$$$$$$$$$$$$$$$$$$$$$$$$$')
        print('$$$$$$$$$$$$$$$$$$$$$$$$$$')
        print('    ~~~~~~~~~~~~~~~~~~    ')
        print('   /   {0}    {0}     \   ')
        print('   |        V         |   ')
        print('   | | ^^^^^^^^^^^ |  |   ')
        print('   | |_VVVVVVVVVVV_|  |   ')
        print('   | | ____________|  |   ')
        print('    \ \___________/  /    ')
        print('     ****************     ')
        print('$$$$$$$$$$$$$$$$$$$$$$$$$$')
        print('$$$$$$$$$$$$$$$$$$$$$$$$$$')
        print('$$$$$$$$$$$$$$$$$$$$$$$$$$')
        print('$$$$$$$$$$$$$$$$$$$$$$$$$$')

    def TreasureChest():
        print('@@@@@@@@@@@@@@@@@@@@@')
        print('        _____        ')
        print(' _______/---\______  ')
        print(' |IIIIIIIIIIIIIIII|  ')
        print(' |     | (o) |    |  ')
        print(' |IIIIIIIIIIIIIIII|  ')
        print(' |^^^^^^^^^^^^^^^^|  ')
        print(' ~~~~~~~~~~~~~~~~~~  ')
        print('@@@@@@@@@@@@@@@@@@@@@')

    def StartScreen():
        print('##############################')
        print('##############################')
        print('            START             ')
        print('            HELP              ')
        print('            QUIT              ')
        print('##############################')
        print('##############################')

    def GameTitle():
        print('##############################')
        time.sleep(0.3)
        print('##############################')
        time.sleep(0.3)
        print('#########THE ROOM#############')
        time.sleep(0.3)
        print('#####created by Chris#########')
        time.sleep(0.3)
        print('###all rights reserved 2019###')
        time.sleep(0.3)
        print('##############################')
        time.sleep(0.3)
        print('##############################')


############################################################################
############################################################################
############################################################################
############################################################################
############################################################################

#THIS IS A TEXT BASED RPG WITH STORY ELEMENTS.
#BELOW IS THE CLASSES, METHODS, AND FUNCTIONS FOR THE GAME


######CLASSES FOR THE GAME###################
####all classes need to be worked on########

class Classes:
    def __init__(self, Name, HP, SP, LV, WIS):
        self.Name = Name
        self.HP = HP
        self.SP = SP
        self.LV = LV
        self.WIS = WIS

####NEED TO REWORK THIS#######

class Thief(Classes):
    def __init__(self):
        super().__init__(Name=input('What is the name of your Char ?', HP=10, SP=10, LV=1, WIS=6))

    role = 'Thief'



class StrongMan(Classes):
    def __init__(self):
        super().__init__(Name=input('What is the name of your Char ?', HP=8, SP=10, LV=1, WIS=6))

    role = 'StrongMan'


class Pacifist(Classes):
    def __init__(self):
        super().__init__(Name=input('What is the name of your Char ?', HP=8, SP=10, LV=1, WIS=6))

    role = 'Pacifist'


class Scientist(Classes):
    def __init__(self):
        super().__init__(Name=input('What is the name of your Char ?', HP=8, SP=10, LV=1, WIS=6))

    role = 'Scientist'


####player needs to be worked on###############

class Player:
    def __init__(self):
        self.Role = ''
        self.EXP = 0
        self.LOCATION = []
        self.INVENTORY = {} # where items are held
        self.CHAR = {} # where items are put on to effect player
        self.LV = 0

    def Charactor(self):
        pass


############need to add deeper elements to ememies, attack, inventory, etc.

class Enemies:
    def __init__(self):
        self.HP = 0
        self.Items = ''
        self.Attack = 0
        self.EXP = 0

#######################################################################
####this needs to be reworked####

def pickingclass():
    CPick = input(' What class are you? \n >>> ')
    if CPick == 'Thief':
         Player.Role = Thief()
    elif CPick == 'Strongman':
        Player.Role = StrongMan()
    if CPick == 'Scientist':
        Player.Role = Scientist()
    if CPick == 'Pasifist':
        Player.Role = Pacifist()
    else:
        print('Please pick Thief, Strongman, Scientist, or Pasifist')
        pickingclass()
    print('Your class is ' + CPick)
    return CPick

#pickingclass()
#####THIS FUNTION CREATES THE MAP WE SEE
######DO NOT ALTER MAP############
def Create_Map():
    printed_board = ("")
    for i in range(1, 6):
        printed_board += ("                   " + str(i))
    printed_board += '\n'
    printed_board += ("0 1 2 3 4 5 6 7 8 9 " * 5)
    printed_board += '\n'
    alpha = list(letters.upper())
    for i in range(26):
        printed_board += (alpha[i])
        printed_board += ("_|" * len(range(49)))
        printed_board += '\n'
    print(printed_board)

##########This Works#############################
def Moving_On_Map(y, x):
    if y in letter and [x for x in list(range(1, 49))]:
        print('The move is correct!!' + y + x + ' is your move')
        #need to replace the '_' with "C" when player has been to location on map.
        ####when dict. index for all underscores are completed, add the funtion here
    else:
        print('Not working')

#####This keeps track of the current location of the char.######################
###need to be worked on######
def last_player_move():
    return Player.LOCATION[-1]

class Room:
    ####Treasure should work#####
    ####need to test method####
    ####Needs 'Room_Items' a dict. of items found in room
    #####needs to be worked on###########almost there####
    def Treasure(self):
        odds_of_treasure = random.randint(0, 2)
        treasure_keys = treasure_items.keys()
        treasure = random.shuffle(treasure_keys)
        if odds_of_treasure == 1:
            room_treasure = list(my_dict.keys())[0]
        return Room_Items[odds_of_treasure]
    def Enemy(self):
        pass
#####THIS LIST WILL BE USED TO LOOP THROUGH AND ADD RANDOM NUMBERS AND STATS TO CREATE A VERY LARGE TREASURE LIST####
###THIS FUNTION WORKS####DONT CHANGE IT#############################
####This adds random stat and random stat attribute to a word(for a 100,000+ game item list#####
def Treasure():

    for line in fin:
        stat, attribute = random.choice(list(Char_Stats.items()))
        sorted_attri = random.choice(attribute)
        word = line.strip()
        treasure_items[word] = {}
        treasure_items[word][stat] = sorted_attri
    return treasure_items

###^^^^^This works, dont change it##############################

####Needs to be worked on################
def Game():
    Graphics.game_graphics.GameTitle()
    time.sleep(0.5)
    print()
    Graphics.game_graphics.StartScreen()
    if input('> ') == 'start':
        print('Welcome to your quest.')
        print('Choose your class (Strongman, Thief, Pacifist, Scientist')
        # pickingclass()
    elif input() == 'quit':
        sys.exit()

    ###Should put code here to clear screen
    while True:
        Create_Map()
        print('This is your game map. You will need to find the secret room...and survive during the process.')
        #print('Where would you like to start at. Type the letter (to the left), and the number on the top')
        Moving_On_Map(input('What letter?'), input('What number?'))
        #need to figure if this works



Game()



