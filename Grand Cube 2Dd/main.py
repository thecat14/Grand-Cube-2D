
import time as t
import random as rd
print(" .----------------.  .----------------.  .----------------.  .-----------------. .----------------.   .----------------.  .----------------.  .----------------.  .----------------.   .----------------.  .----------------. ")
print("| .--------------. || .--------------. || .--------------. || .--------------. || .--------------. | | .--------------. || .--------------. || .--------------. || .--------------. | | .--------------. || .--------------. |")
print("| |    ______    | || |  _______     | || |      __      | || | ____  _____  | || |  ________    | | | |     ______   | || | _____  _____ | || |   ______     | || |  _________   | | | |    _____     | || |  ________    | |")
print("| |  .' ___  |   | || | |_   __ \    | || |     /  \     | || ||_   \|_   _| | || | |_   ___ `.  | | | |   .' ___  |  | || ||_   _||_   _|| || |  |_   _ \    | || | |_   ___  |  | | | |   / ___ `.   | || | |_   ___ `.  | |")
print("| | / .'   \_|   | || |   | |__) |   | || |    / /\ \    | || |  |   \ | |   | || |   | |   `. \ | | | |  / .'   \_|  | || |  | |    | |  | || |    | |_) |   | || |   | |_  \_|  | | | |  |_/___) |   | || |   | |   `. \ | |")
print("| | | |    ____  | || |   |  __ /    | || |   / ____ \   | || |  | |\ \| |   | || |   | |    | | | | | |  | |         | || |  | '    ' |  | || |    |  __'.   | || |   |  _|  _   | | | |   .'____.'   | || |   | |    | | | |")
print("| | \ `.___]  _| | || |  _| |  \ \_  | || | _/ /    \ \_ | || | _| |_\   |_  | || |  _| |___.' / | | | |  \ `.___.'\  | || |   \ `--' /   | || |   _| |__) |  | || |  _| |___/ |  | | | |  / /____     | || |  _| |___.' / | |")
print("| |  `._____.'   | || | |____| |___| | || ||____|  |____|| || ||_____|\____| | || | |________.'  | | | |   `._____.'  | || |    `.__.'    | || |  |_______/   | || | |_________|  | | | |  |_______|   | || | |________.'  | |")
print("| '--------------' || '--------------' || '--------------' || '--------------' || '--------------' | | '--------------' || '--------------' || '--------------' || '--------------' | | '--------------' || '--------------' |")
print("'----------------'  '----------------'  '----------------'  '----------------'  '----------------'   '----------------'  '----------------'  '----------------'  '----------------'   '----------------'  '----------------' ")

input("press enter to start... ")
def img_ak47():
    f = open("weapons/ak47_image", 'r')
    print(f.read())
    print("☭☭☭☭☭☭☭☭☭☭☭☭☭☭☭☭☭☭☭☭☭☭☭☭☭☭☭☭☭☭☭☭☭☭☭☭☭☭☭☭☭☭☭☭☭☭☭☭☭☭☭☭☭☭")
    t.sleep(5)
def img_ar15():
    f = open("weapons/ar15_image", 'r')
    print(f.read())
    t.sleep(5)
def img_spas12():
    f = open("weapons/spas12_image", 'r')
    print(f.read())
    t.sleep(5)
def img_colt1911():
    f = open("weapons/col1911_image", 'r')
    print(f.read())
    t.sleep(5)



def attack():
    global life_player
    global npc_life
    line_attacked_npc = input("In wich line is the NPC ?! :   ")
    case_attacked_npc = input("In wich case is the NPC ?! :   ")
    npcs_img = "NPCs\\NPC1", "NPCs\\NPC2", "NPCs\\NPC3"
    f = open(rd.choice(npcs_img), 'r')

    for a in range(0, len(MAP)):
        current_line = MAP[a]
        if "웃" in MAP[a]:
            print("NPC IN LINE : " + str(a))
            npc_x_pos = a
            for b in range(0, len(current_line)):
                if "웃" in current_line[b]:
                    print("NPC IN CASE : " + str(b))
                    npc_y_pos = b
                    print("npc found")
        else:
            print()
    print(npc_x_pos)
    print(npc_y_pos)
    npc_cr = ["Has a gun", "He is Conor McGregor", "He is an ex-military", "1.15m height", "He is fat", "He is blind"]
    if line_attacked_npc == str(npc_x_pos):
        if case_attacked_npc == str(npc_y_pos):
            arnold_f = open("arnold.txt", 'r')
            vs_f = open("VS", 'r')
            print(arnold_f.read())
            print(vs_f.read())
            print(f.read())

            current_cr = rd.choice(npc_cr)
            print(current_cr)
            choice = input("Are you sure you want to attack this guy ?  1.Yes  2.No")
            if current_cr == npc_cr[0]:
                npc_deg = 30
                life_player = life_player - npc_deg

            if current_cr == npc_cr[1]:
                npc_deg = 99
                life_player = life_player - npc_deg

            if current_cr == npc_cr[2]:
                npc_deg = 40
                life_player = life_player - npc_deg

            if current_cr == npc_cr[3]:
                npc_deg = 20
                life_player = life_player - npc_deg

            if current_cr == npc_cr[4]:
                npc_deg = 25
                life_player = life_player - npc_deg

            if current_cr == npc_cr[4]:
                npc_deg = -5
                life_player = life_player - npc_deg

            if equiped_weapon == "AK-47":
                npc_life = npc_life - ak47_deg
            if equiped_weapon == "AR-15":
                npc_life = npc_life - ar15_deg
            if equiped_weapon == "Colt 1911":
                npc_life = npc_life - colt1911_deg
            if equiped_weapon == "SPAS-12":
                npc_life = npc_life - spas12_deg

            if npc_life < 1:
                MAP[npc_x_pos][npc_y_pos] = "☠"
                t.sleep(5)
            else:
                print("The attacked NPC has : " + str(npc_life) + "HP")

            if life_player < 1:
                while True:
                    input("YOU ARE DEAD !!!!!!!!!!!!!!")

def see_weapons():
    global equiped_weapon
    print("You have this weapons:   1.AK-47: " + str(ak47) + "   2.AR-15 : " + str(ar15) + "   3.Colt 1911 : " + str(
        colt1911) + "   4.SPAS-12 : " + str(spas12))
    choosed_weapon = input("Choose your weapon :   ")
    if choosed_weapon == "1":
        if ak47 == True:
            equiped_weapon = "AK-47"
        else:
            print("You do not have this weapon...")
            t.sleep(1)

    if choosed_weapon == "2":
        if ar15 == True:
            equiped_weapon = "AR-15"
        else:
            print("You do not have this weapon...")
            t.sleep(1)

    if choosed_weapon == "3":
        if colt1911 == True:
            equiped_weapon = "Colt 1911"
        else:
            print("You do not have this weapon...")
            t.sleep(1)

    if choosed_weapon == "4":
        if spas12 == True:
            equiped_weapon = "SPAS-12"
        else:
            print("You do not have this weapon...")
            t.sleep(1)

def ammunation():
    global ak47
    global ar15
    global spas12
    global colt1911
    global money
    print("                                            __  .__               ")
    print("_____    _____   _____  __ __  ____ _____ _/  |_|__| ____   ____  ")
    print("\__  \  /     \ /     \|  |  \/    \\__  \\   __\  |/  _ \ /    \ ")
    print(" / __ \|  Y Y  \  Y Y  \  |  /   |  \/ __ \|  | |  (  <_> )   |  \ ")
    print("(____  /__|_|  /__|_|  /____/|___|  (____  /__| |__|\____/|___|  /")
    print("     \/      \/      \/           \/     \/                    \/ ")

    print("You have :" + str(money) + "$")
    weapons = ["1. AK-47 : 3000$    ", "2. AR-15 : 2000$    ", "3.Colt 1911 : 250$    ", "4.SPAS-12 : 1500$"]
    print(weapons)
    weapon_choice = input("Which weapon do you want to buy ? (press enter to exit...):   ")

    if weapon_choice == "1":
        price = 3000
        if money > price:
            money = money - price
            print("You have :" + str(money) + "$")
            ak47 = True
            print("You bought an AK-47 ! ")
            img_ak47()
        else:
            print("you do not have enough money")
            t.sleep(1)

    if weapon_choice == "2":
        price = 2000
        if money > price:
            money = money - price
            print("You have :" + str(money) + "$")
            ar15 = True
            print("You bought an AR-15 ! ")
            img_ar15()
        else:
            print("you do not have enough money")
            t.sleep(1)

    if weapon_choice == "3":
        price = 250
        if money > price:
            money = money - price
            print("You have :" + str(money) + "$")
            colt1911 = True
            print("You bought a Colt 1911 ! ")
            img_colt1911()
        else:
            print("you do not have enough money")
            t.sleep(1)

    if weapon_choice == "4":
        price = 1500
        if money > price:
            money = money - price
            print("You have :" + str(money) + "$")
            spas12 = True
            print("You bought a SPAS-12 ! ")
            img_spas12()
        else:
            print("you do not have enough money")
            t.sleep(1)


l1 = ["█", "█", "█", "█", "█", "█", "█", "█", "E", "░"]
l2 = ["█", "█", "█", "█", "█", "█", "█", "█", "░", "░"]
l3 = ["█", "█", "█", "█", "█", "█", "█", "█", "█", "█"]
l4 = ["█", "█", "█", "█", "█", "█", "█", "█", "█", "█"]
l5 = ["█", "█", "█", "█", "█", "█", "█", "█", "█", "█"]
l6 = ["█", "█", "█", "█", "█", "█", "█", "█", "█", "█"]
l7 = ["█", "█", "█", "█", "█", "█", "█", "█", "█", "█"]
l8 = ["█", "█", "█", "█", "█", "█", "█", "█", "█", "█"]
l9 = ["█", "█", "█", "█", "█", "█", "█", "█", "█", "█"]
l10 = ["█", "█", "█", "█", "█", "█", "█", "█", "█", "█"]

player = "☺"
npc = "웃"

l1[0] = player
l5[5] = npc
money = 15000

ak47 = False
ar15 = False
colt1911 = False
spas12 = False

ak47_deg = 80
ar15_deg = 60
colt1911_deg = 25
spas12_deg = 45

equiped_weapon = ""

life_player = 100
npc_life = 100

while True:

    MAP = [l1, l2, l3, l4, l5, l6, l7, l8, l9, l10]

    command = input("1.right   2.left   3.up   4.down    W.see weapons   A.attack:   ")

    #  get the current position of the player
    for line in range(0, len(MAP)):
        if player in MAP[line]:
            current_line = MAP[line]
            x_pos = line

            for colons in range(0, len(current_line)):
                if current_line[colons] == player:
                    y_pos = colons

    coordinates = x_pos, y_pos

    #  detect the commands

    if command == "W":
        see_weapons()
    if command == "A":
        attack()
    if command == "1":
        y_pos = y_pos + 1
        MAP[x_pos][y_pos] = player
        MAP[x_pos][y_pos - 1] = "█"

    if command == "2":
        y_pos = y_pos - 1
        MAP[x_pos][y_pos] = player
        MAP[x_pos][y_pos + 1] = "█"

    if command == "4":
        x_pos = x_pos + 1
        MAP[x_pos][y_pos] = player
        MAP[x_pos - 1][y_pos] = "█"

    if command == "3":
        x_pos = x_pos - 1
        MAP[x_pos][y_pos] = player
        MAP[x_pos + 1][y_pos] = "█"

    print("_________________________________________________________")
    print("_________________________________________________________")
    print("_________________________________________________________")
    if coordinates == (0, 7):
        print("you entered a building")
        ammunation()
    print("your coordinates are : "+str(coordinates))
    print("You have :" + str(money) + "$")
    print("Your life is " + str(life_player))
    print("You have equiped an : " + equiped_weapon)
    l1[9] = "░"
    l1[8] = "E"
    l1[9] = "░"
    l1[8] = "░"

    print(l1)
    print(l2)
    print(l3)
    print(l4)
    print(l5)
    print(l6)
    print(l7)
    print(l8)
    print(l9)
    print(l10)