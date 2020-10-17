"""THIS IS A TEXT BASED STORY RPG. THIS IS MY FIRST PROJECT USING PYTHON. I TRIED TO PUT ALL PYTHON TO USE
IN THIS PROJECT. USING NESTED DICTIONARY AND NESTED LOOPS TO GET A ROBUST GAME(IN ONLY TEXT FORMAT). THIS GAME IS
NEARLY COMPLETE, IF YOU HAVE AN SUGGESTIONS ON IMPROVEMENT, PLEASE FEEL FREE TO REACH OUT TO ME. THE PATH OF KNOWLEDGE
AND MASTERY IS NEVER FULLY REALISED AND IS ALWAYS A MOVING GOAL OF ENDLESS DEPTH..."""



###THIS GAME IS BEING CREATED AS AN ONGOING LEARNING PROJECT,

#IMPORTING ALL NEEDED MODS FOR THIS PROJECT..
#tryed to add os.system('clear') but it does not seem to work.

import random
import sys
import os
import time



#THIS IS A SETUP LIST FOR ALL THE GLOBAL VARIABLES WE NEED

fin = open('itemlist.txt')
board = {}
boxes = [x for x in range(99) if x%2==0] * 50
treasure_items = {}
boss_items ={'The Sword Of The Room':{'WIS': 20}, 'The Secret Key':{'HP': 20}, "Necklace 'La Rae The Beautiful' ":{
    'SP':20}}
UP = "up"
LEFT = 'left'
RIGHT = 'right'
DOWN = 'down'
##these global variables are used for started location on board.
starty = random.choice(range(26))
startx = random.choice(range(26))



#THIS CREATES OUR PARAMETERS FOR EACH STAT WE WANT OUR ITEMS TO HAVE
#THIS IS WHAT A FUNTION WILL USE TO CREATE OUR NESTED DICT, FOR ALL ITEMS IN GAME

HP = list(range(0, 10))
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

#####THIS LIST IS USED TO LOOP THROUGH AND ADD RANDOM NUMBERS AND STATS TO CREATE A TREASURE LIST

for line in fin:
    stat, attribute = random.choice(list(Char_Stats.items()))
    sorted_attri = random.choice(attribute)
    word = line.strip()
    treasure_items[word] = {}
    treasure_items[word][stat] = sorted_attri


#THIS CREATES A DICTIONARY THAT HAS THE DATA POINT OF EVERY USED DATA ON OUR MAP
#THIS IS USED TO PULL WHERE ON THE MAP WE WANT TO REPLACE FOR OUR PLAYER ICON (THE DICT. IS 50 LISTS OF 26 POINTS

for y in range(26):
    board[y] = {}

n_0 = 0
for y in range(26):
    for x in range(50):
        board[y][x] = boxes[n_0]
        n_0 += 1


############################################################################
############################################################################

####THIS CREATES THE GAME BOARD WE WILL BE USING.###########################
##these two funtions were created in large part by studing the code in "inventwithpython'-Sonar Treasure Hunt
##this funtion RETURNS the board, we it can be used in other funtions.
##The drawGame funtion print odd. It does not prints 26 '_|' 50 times. from left to right.

def getGame():
    board = []
    for x in range(50):
        board.append([])
        for y in range(26):
            board[x].append('_|')

    return board

def drawGame(getGame):
    for row in range(26):
        gameRow = ''
        for column in range(50):
            gameRow += getGame[column][row]
        print(gameRow)





####Treasure_room function returns a random item from the main item nestede dict

def Treasure_room():
    odds_of_treasure = random.choice(list(range(4)))
    treasure_keys = treasure_items.keys()
    treasure = random.choice(list(treasure_keys))
    if odds_of_treasure == 1:
        room_treasure = treasure
        print(game_graphics.TreasureChest())
        return room_treasure
    else:
        print('You look around the room and find no treasure')





############################################################################

##THIS IS A LIST OF ALL TEXT BASED GRAPHICS THAT WILL BE USED FOR THE GAME

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
        print()

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
        print()

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
######CLASSES FOR THE GAME & PLAYER
#Character is where items effect the players stats

class Player:
    def __init__(self, Name, Role, EXP_P, INVENTORY, CHARACTER, LV_P, HP_P, SP_P, WIS_P):
        self.Name = Name
        self.Role = Role
        self.EXP_P = EXP_P
        self.LOCATION = []
        self.INVENTORY = INVENTORY
        self.CHARACTER = CHARACTER
        self.LV_P = LV_P
        self.HP_P = HP_P
        self.SP_P = SP_P
        self.WIS_P = WIS_P


class Thief(Player):
    def __init__(self):
        super().__init__(Name='')

    Role = 'Thief'
    HP_P = 8
    SP_P = 12
    INVENTORY = {}
    WIS_P = 10
    EXP_P = 0
    LV_P = 1
    CHARACTER = {}


class StrongMan(Player):
    def __init__(self):
        super().__init__(Name='')

    Role = 'StrongMan'
    HP_P = 12
    SP_P = 10
    INVENTORY = {}
    WIS_P = 8
    EXP_P = 0
    LV_P = 1
    CHARACTER = {}


class Pacifist(Player):
    def __init__(self):
        super().__init__(Name='')

    Role = 'Pacifist'
    HP_P = 10
    SP_P = 10
    INVENTORY = {}
    WIS_P = 10
    EXP_P = 0
    LV_P = 1
    CHARACTER = {}


class Scientist(Player):
    def __init__(self):
        super().__init__(Name='')

    Role = 'Scientist'
    HP_P = 8
    SP_P = 8
    INVENTORY = {}
    WIS_P = 15
    EXP_P = 0
    LV_P = 1
    CHARACTER = {}



###Easy class for building enemies

class Enemies:
    def __init__(self):
        self.HP = 0
        self.Items = ''
        self.Attack = 0
        self.EXP = 0


##THIS WILL BE USED TO CONNECT USER TO PLAYER CLASS AND RETURN THEIR CLASS

def player_hero():
    print('Here are the 4 class for this game.')
    print()
    print('Thief: They are masters of speed and stealth. (Low Health, Moderate Wisdom, High Speed)')
    print()
    print('Strongman: Kick the door down first, and think later (Low Wisdom, Moderate Speed, High Health')
    print()
    print('Scientist: They use their mind to solve problems. (Low Health, Low Speed, Very High Wisdom')
    print()
    print('Pasifist: No special abilities. Avoids confrontations. (Moderate Health, Moderate Wisdom, Moderate Speed')
    print()
    p_pick = input(' What ability do you have? \n >>> ')

    if p_pick.lower().startswith('t'):
        Hero = Thief
        return Hero
    if p_pick.lower() == 'strongman':
        Hero = StrongMan
        return Hero
    if p_pick.lower() == 'scientist':
        Hero = Scientist
        return Hero
    if p_pick.lower().startswith('p'):
        Hero = Pacifist
        return Hero

    else:
        print('Please pick Thief, Strongman, Scientist, or Pasifist')
        player_hero()



#THIS FUNCTION HELP CREATE THE EFFECT OF OUR PLAYER MOVING OF THE BOARD.
#THIS FUNTIONS WORKS WITH GETGAME AND USER_MAP_INPUT TO CREATE THE EFFECT.
###The only bug is when you move off the board it takes two moves to move back.

def Moving_On_Map(getGame,y,x):
    if y >= 0 and y < 50 and x >= 0 and x < 26:
        getGame[y][x] = 'XX'
        Player.LOCATION = [y, x]
        drawGame(getGame)
    else:
        return False



#it prints 26 '_|' 50 times from left to right. So what you think should be moving left is moving up.
##THIS IS ALSO USED TO RANDOMLY GENERATE ITEMS IN EACH ROOM.

def user_map_input(playerinput,treasure):
    enemy_odds = random.choice(list(range(1, 50)))
    item_stats = []

    try:
        item_stats = treasure_items[treasure]
        print('You look around the room and find a treasure chest! You open it to find a: ')
        if playerinput.lower().startswith('u'):
            Player.LOCATION = [Player.LOCATION[0], (Player.LOCATION[1]) - 1]
            print(treasure)
            game_player.INVENTORY[treasure] = item_stats
            if enemy_odds < 25:
                Enemy(enemy_odds)
            if enemy_odds > 47:
                Enemy(-1)
            if enemy_odds == 18:
                story_line(3)
        if playerinput.lower().startswith('d'):
            Player.LOCATION = [Player.LOCATION[0], (Player.LOCATION[1]) + 1]
            print(treasure)
            game_player.INVENTORY[treasure] = item_stats
            if enemy_odds < 25:
                Enemy(enemy_odds)
            if enemy_odds > 47:
                Enemy(-1)
            if enemy_odds == 18:
                story_line(3)
        if playerinput.lower().startswith('l'):
            Player.LOCATION = [(Player.LOCATION[0]) - 1, Player.LOCATION[1]]
            print(treasure)
            game_player.INVENTORY[treasure] = item_stats
            if enemy_odds < 25:
                Enemy(enemy_odds)
            if enemy_odds > 47:
                Enemy(-1)
            if enemy_odds == 18:
                story_line(3)
        if playerinput.lower().startswith('r'):
            Player.LOCATION = [(Player.LOCATION[0]) + 1, Player.LOCATION[1]]
            print(treasure)
            game_player.INVENTORY[treasure] = item_stats
            if enemy_odds < 25:
                Enemy(enemy_odds)
            if enemy_odds > 47:
                Enemy(-1)
            if enemy_odds == 18:
                story_line(3)

    except KeyError:
        print('You look around the room and find no other items in the room.')
        if playerinput.lower().startswith('u'):
            Player.LOCATION = [Player.LOCATION[0], (Player.LOCATION[1]) - 1]
            if enemy_odds < 25:
                Enemy(enemy_odds)
            if enemy_odds > 47:
                Enemy(-1)
            if enemy_odds == 18:
                story_line(3)
        if playerinput.lower().startswith('d'):
            Player.LOCATION = [Player.LOCATION[0], (Player.LOCATION[1]) + 1]
            if enemy_odds < 25:
                Enemy(enemy_odds)
            if enemy_odds > 47:
                Enemy(-1)
            if enemy_odds == 18:
                story_line(3)
        if playerinput.lower().startswith('l'):
            Player.LOCATION = [(Player.LOCATION[0]) - 1, Player.LOCATION[1]]
            if enemy_odds < 25:
                Enemy(enemy_odds)
            if enemy_odds > 47:
                Enemy(-1)
            if enemy_odds == 18:
                story_line(3)
        if playerinput.lower().startswith('r'):
            Player.LOCATION = [(Player.LOCATION[0]) + 1, Player.LOCATION[1]]
            if enemy_odds < 25:
                Enemy(enemy_odds)
            if enemy_odds > 47:
                Enemy(-1)
            if enemy_odds == 18:
                story_line(3)




# LARGE FUNCTION THAT DEALS WITH ALL BATTLES
#there are 3 options normal battle, boss battle, and first battle


def Enemy(number):
    """This function does a lot. We are breaking up the treasure_item list to randomly select a key.
    Once we select a key (example 'sword') we extract the randomly generated stats attached to the item.
    We put that value in 'item_stats'. This way we can put it all into the char slot if he wins the battle.
    the default is 'if number > 0: ' the else statement is for the opening fight"""

    if number > 0:
        item_stats = {}
        Enemies.HP = random.choice(range(20, 80))
        Enemies.EXP = random.choice(range(10, 40))
        Enemies.Attack = int(Enemies.HP / Enemies.EXP)
        Enemies.Items = random.choice(list(treasure_items.keys()))
        item_stats = treasure_items[Enemies.Items]
        game_graphics.Enemy()
        print('You have encountered a monster!')
        Health = Enemies.HP
        Health_Player = game_player.HP_P
        while Health > 0 or Health_Player > 0:
            print('Monster HP: ' + str(Health))
            attack_player = int((game_player.HP_P / game_player.SP_P) + 3)
            enemy_attack = Enemies.Attack
            player_input = input('What did you want to do? (attack or run)')
            if player_input.lower().startswith('a'):
                Health = Health - attack_player
                print('You hit monster for: ' + str(attack_player) + ' damage!')
                print('Monster current HP is at: ' + str(Health))
                game_graphics.Enemy()
                Health_Player = Health_Player - enemy_attack
                print('Your got hit for ' + str(enemy_attack) + ' damage!')
                print('Your current HP is at: ' + str(Health_Player))
                if Health <= 0:
                    print('You defeated the monster!')
                    print('You gained ' + str(Enemies.EXP) + ' experience points from the fallen monster')
                    game_player.EXP_P += Enemies.EXP
                    game_graphics.TreasureChest()
                    print('You picked up a ' + Enemies.Items + ' from the fallen monster!')
                    game_player.INVENTORY[Enemies.Items] = item_stats
                    return False
                if Health_Player <= 0:
                    print("Sorry, you died. Your story was forgotten, and your did not make it out of the room...")
                    sys.exit()
            if player_input.lower() == 'run':
                print('You decide to run for this monster')
                if int(Enemies.HP) < float(game_player.SP_P + game_player.WIS_P):
                    print('The run around the monster, leaving it confused and dazed')
                    break
                else:
                    print('You are not able to escape the monster; you must confront it.')




    if number == -1:
        item_stats = {}
        Enemies.HP = random.choice(range(100, 150))
        Enemies.EXP = random.choice(range(75, 100))
        Enemies.Attack = int(Enemies.HP / 6)
        Enemies.Items = random.choice(list(boss_items.keys()))
        item_stats = boss_items[Enemies.Items]
        game_graphics.Boss()
        print('You have encountered the Boss!')
        Health = Enemies.HP
        Health_Player = game_player.HP_P
        story_line(1)
        while Health > 0 or Health_Player > 0:
            print('Boss HP: ' + str(Health))
            attack_player = int((game_player.HP_P / game_player.SP_P) + 3)
            enemy_attack = Enemies.Attack
            player_input = input('What did you want to do? (attack or run)')
            if player_input.lower() == 'run':
                print("You can not run away from this battle")
            if player_input.lower().startswith('a'):
                Health = Health - attack_player
                print('You hit monster for: ' + str(attack_player) + ' damage!')
                print('Monster current HP is at: ' + str(Health))
                game_graphics.Boss()
                Health_Player = Health_Player - enemy_attack
                print('Your got hit for ' + str(enemy_attack) + ' damage!')
                print('Your current HP is at: ' + str(Health_Player))
                if Health <= 0:
                    print('You defeated the Boss!!!')
                    print('You gained ' + str(Enemies.EXP) + ' experience points from the fallen monster')
                    game_player.EXP_P += Enemies.EXP
                    game_graphics.TreasureChest()
                    print('You picked up a ' + Enemies.Items + ' from the fallen monster!')
                    game_player.INVENTORY[Enemies.Items] = item_stats
                    story_line(2)
                if Health_Player <= 0:
                    print("Sorry, you died. Your story was forgotten, and your did not make it out of the room...")
                    sys.exit()
    else:
        item_stats = {}
        Enemies.HP = 10
        Enemies.EXP = random.choice(range(10, 40))
        Enemies.Attack = int(Enemies.HP / Enemies.EXP)
        Enemies.Items = random.choice(list(treasure_items.keys()))
        item_stats = treasure_items[Enemies.Items]
        game_graphics.Enemy()
        print("You will see many of these monsters in 'The Room'. A monsters HP is their health points. "
              "you need to get their HP to 0 in order to defeat them.")
        time.sleep(2)
        print("You can run, but you need to have high wisdom and speed to do so.")
        Health = Enemies.HP
        Health_Player = game_player.HP_P
        while Health > 0 or Health_Player > 0:
            print('Monster HP: ' + str(Health))
            attack_player = int((game_player.HP_P / game_player.SP_P) + 2)
            enemy_attack = Enemies.Attack + 2
            player_input = input('What did you want to do? (attack or run)')
            if player_input.lower() == 'run':
                print("You can not run away from this battle")
            if player_input.lower().startswith('a'):
                Health = Health - attack_player
                print('You hit monster for: ' + str(attack_player) + ' damage!')
                print('Monster current HP is at: ' + str(Health))
                game_graphics.Enemy()
                Health_Player = Health_Player - enemy_attack
                print('Your got hit for ' + str(enemy_attack) + ' damage!')
                print('Your current HP is at: ' + str(Health_Player))
                if Health <= 0:
                    print('You defeated the monster! Great job!')
                    print('You gained ' + str(Enemies.EXP) + ' experience points from the fallen monster')
                    game_player.EXP_P += Enemies.EXP
                    game_graphics.TreasureChest()
                    print('You picked up a ' + Enemies.Items + ' from the fallen monster!')
                    game_player.INVENTORY[Enemies.Items] = item_stats
                    print("Keep in mind that if you die, you lose. No saves, no restarts, no second chances."
                          "Find out why you are here, who wants you dead, and get out alive.")
                    print("Remember to check your inventory often and put on items that help you.")
                    return False
                if Health_Player <= 0:
                    print("Sorry, you died. Your story was forgotten, and your did not make it out of the room...")
                    sys.exit()


##THIS IS USED FOR THE STORY AND THE PATHS ARE ENTERED AT KEY LOCATIONS

def story_line(path):
    if path == 0:
        print(game_player.Name + ' wakes up in a room, dazed and confused he looks around.')
        time.sleep(2.5)
        print("Mystery Voice 'Welcome young warrior, to The Rooms. I hope you had a safe travel.'")
        time.sleep(2.5)
        print(game_player.Name + " 'Where am I?'")
        time.sleep(2.5)
        print("Mystery Voice 'Where you are is not important; how will you get out and survive is the question.")
        time.sleep(2.5)
        print("I have a few question before we begin. Your name is: " + game_player.Name + " is that correct?'")
        time.sleep(2.5)
        print(game_player.Name + " 'How do you..'")
        time.sleep(2.5)
        print("Mystery Voice 'You seem to have an ability as " + game_player.Role + " , that will come into handy.")
        time.sleep(2.5)
        print(" Well, seems like we have everything in order.")
        time.sleep(2.5)
        print("I would say good luck; but...")
        time.sleep(3)
        print("no one has ever escaped alive.")
        time.sleep(2)
        print("The speaker on the wall goes silent, and you hear a noise coming from the other side of the room")

    if path == 1:
        print(game_player.Name + ' enters a room that looks different than all the others, behind the large '
                                 'monster he sees his escape.')
        time.sleep(2.5)
        print("A man walks down the set of stairs behind the monster, he starts to clap.")
        time.sleep(2.5)
        print("Mystery Man: 'Well done!, I must admit there was some close calls. I never thought you would "
              "make it this far.' ")
        time.sleep(2.5)
        print(game_player.Name + "'I am getting out of here! You cant spot me!'")
        time.sleep(3)
        print("Mystery Man: 'We will see...'")
        time.sleep(2.5)
        print("The man steps back and the large monster lunges toward you.")

    if path == 2:
        print("After the beast falls, the dust in the room begins to settle.")
        time.sleep(2.5)
        print("You look up at the man, and his face has no emotion; but you detect a small sense of...happiness.")
        time.sleep(2.5)
        print(game_player.Name + " 'I won your stupid game.")
        time.sleep(2.5)
        print("Mystery Man: ' I had to be sure, and you are the one we have been looking for. My name is Eldren'")
        time.sleep(2.5)
        print("Eldren walk toward you, and his demeanor has changed to one of fulfilment and contentment.'")
        time.sleep(2.5)
        print("You step back, readying your battle position")
        time.sleep(2.5)
        print("Eldren: 'I mean you no harm my boy. You are the one the Guardians have been waiting for.")
        time.sleep(2.5)
        print(game_player.Name + " 'What are you talking about?' ")
        time.sleep(3)
        print("Eldren: 'Let me show you.'")
        time.sleep(4)
        print("Thank you for playing 'The Room' by Chris Norman. All right reserved.")
        game_graphics.GameTitle()
        sys.exit()

    if path == 3:
        item_stats = []
        print('You find a room like no other. Walls decorated in gold.')
        time.sleep(2.0)
        print('You see a treasure chest like no other.')
        time.sleep(2)
        print('You walk up to it and open it.')
        game_graphics.TreasureChest()
        time.sleep(3)
        Enemies.Items = random.choice(list(boss_items.keys()))
        item_stats = boss_items[Enemies.Items]
        print('You picked up a ' + Enemies.Items + ' from the golden chest!')
        game_player.INVENTORY[Enemies.Items] = item_stats


#THIS DEALS WITH PLAYER LEVEL. I COULD HAVE MADE A LOOP OR SOMETHING FANCY, BUT THIS DOES THE TRICK.

def player_level(Level, Experience):
    if Level == 1 and Experience > 50:
        print("You leveled up! You are now Level 2")
        game_player.LV_P += 1
        game_player.SP_P += 1
        game_player.WIS_P += 1
        game_player.HP_P += 2
    if Level == 2 and Experience > 150:
        print("You leveled up! You are now Level 3")
        game_player.LV_P += 1
        game_player.SP_P += 2
        game_player.WIS_P += 2
        game_player.HP_P += 4
    if Level == 3 and Experience > 350:
        print("You leveled up! You are now Level 4")
        game_player.LV_P += 1
        game_player.SP_P += 2
        game_player.WIS_P += 2
        game_player.HP_P += 4
    if Level == 4 and Experience > 550:
        print("You leveled up! You are now Level 5")
        game_player.LV_P += 1
        game_player.SP_P += 2
        game_player.WIS_P += 2
        game_player.HP_P += 4
    if Level == 5 and Experience > 700:
        print("You leveled up! You are now Level 6")
        game_player.LV_P += 1
        game_player.SP_P += 3
        game_player.WIS_P += 3
        game_player.HP_P += 6






#THIS IS WHAT RUNS THE WHOLE GAME AND PUTS EVERYTHING TOGETHER.
#game.player = player_hero()..i hate the location..will fix it soon.

game_player = player_hero()
player_equip_limit = 10
def Game():
    game_graphics.GameTitle()
    time.sleep(0.5)
    print()
    game_graphics.StartScreen()
    opening = input('--> ')
    if opening.lower().startswith('s'):
        game_player.Name = input('What is the name of your player? \n -->')
    elif opening.lower() == 'quit':
        sys.exit()
    elif opening.lower().startswith('h'):
        print("This is a game that requires strategy to complete")
        print("Tip 1: After every battle make sure you equip any items you have so you can survive longer")
        print("Tip 2: If you have the Wisdom and Speed you can run from a battle. You keep items in treasure chests")
        print('Tip 3: When you die you lose everything. A good start in items helps with end game.')
        print('Have Fun!')
        Game()
    else:
        game_graphics.StartScreen()
        opening = input('--> ')
        if opening.lower().startswith('s'):
            game_player.Name = input('What is the name of your player? \n -->')
        elif opening.lower() == 'quit':
            sys.exit()
    story_line(0)
    input("Press Enter To Continue...")
    Enemy(0)
    input("Press Enter To Continue...")
    print('This is your game map. You will need to find the secret room...and survive during the process.')
    print('This is your starting location')
    Moving_On_Map(getGame(), starty, startx)
    while True:
        player_level(game_player.LV_P, game_player.EXP_P)
        game_player.HP_P += 1
        print('What direction did you want to move? (up, down, left, right)')
        print("         |Inventory(I)| |Character Slots(C)| |Exit| ")
        player_input = input('>>> ')
        if player_input.lower().startswith('u'):
            user_map_input(player_input, Treasure_room())
            Moving_On_Map(getGame(), (Player.LOCATION[0]), (Player.LOCATION[1]))
        if player_input.lower().startswith('d'):
            user_map_input(player_input, Treasure_room())
            Moving_On_Map(getGame(), (Player.LOCATION[0]), (Player.LOCATION[1]))
        if player_input.lower().startswith('l'):
            user_map_input(player_input, Treasure_room())
            Moving_On_Map(getGame(), (Player.LOCATION[0]), (Player.LOCATION[1]))
        if player_input.lower().startswith('r'):
            user_map_input(player_input, Treasure_room())
            Moving_On_Map(getGame(), (Player.LOCATION[0]), (Player.LOCATION[1]))
        if player_input == 'I':
            print('Your current items in your inventory are: ')
            items = list(game_player.INVENTORY)
            for i in items:
                print(str(i) + ' with ' + str(game_player.INVENTORY[i]) + ' stats on it')
            if len(list(game_player.CHARACTER.keys())) <= player_equip_limit:
                print("Would you like to add any of these items to your character? (or 'End' to go back to room)")
                print("Your have room for: " + str(player_equip_limit - len(list(game_player.CHARACTER.keys()))))
                equip_input = input('>>> ')
                if equip_input == i:
                    equip = i
                    game_player.CHARACTER[i] = treasure_items[i]
                    print('Your added a ' + i + ' to your character')
                    del game_player.INVENTORY[equip]
            if len(list(game_player.CHARACTER.keys())) > player_equip_limit:
                print('You have no room to add anymore items to your character.')
        if player_input == 'C':
            if len(list(game_player.CHARACTER.keys())) <= player_equip_limit:
                print("Your have room for: " + str(player_equip_limit - len(list(game_player.CHARACTER.keys()))))
                print('Your current stats are: ')
                print('LV: ' + str(game_player.LV_P) + ' EXP: ' + str(game_player.EXP_P))
                print('|HP: ' + str(game_player.HP_P) + ' |SP: ' + str(game_player.SP_P) + ' | WIS: ' + str(
                    game_player.WIS_P))
                print('These are the items currently on your character: (type name of item to remove it(removing perm'
                      'anently removes item)')
                print(game_player.CHARACTER)
                for i in game_player.CHARACTER.keys():
                    char_stats = game_player.CHARACTER[i]
                    for x in char_stats:
                        if x == 'HP':
                            game_player.HP_P += char_stats[x]
                        if x == 'WIS':
                            game_player.WIS_P += char_stats[x]
                        if x == 'SP':
                            game_player.SP_P += char_stats[x]
                if input('>>> ') == [i for i in list(game_player.CHARACTER.keys())]:
                    del game_player.CHARACTER[i]
            if len(list(game_player.CHARACTER.keys())) > player_equip_limit:
                print('You have no room for more items. You need to remove items to add more')
                print('Your current stats are: ')
                print('LV: ' + str(game_player.LV_P) + ' EXP: ' + str(game_player.EXP_P))
                print('|HP: ' + str(game_player.HP_P) + ' |SP: ' + str(game_player.SP_P) + ' | WIS: ' + str(
                    game_player.WIS_P))
                print('These are the items currently on your character: (type name of item to remove it(removing '
                      'permanently removes item)')
                print(game_player.CHARACTER)
                if input('>>> ') == [i for i in list(game_player.CHARACTER.keys())]:
                    del game_player.CHARACTER[i]
        if player_input == 'Exit':
            print('Thanks for playing')
            sys.exit()



Game()



