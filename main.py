import os
import time
import colorama
import keyboard
import random
#import playsound
#import subprocess
pewPewBullets = [None,None]
score = 100
spaceShipCoords = [19,28]
bombCoords = [None,None]
spawnIncrement = 1
import colorama
from colorama import Fore,Back
from colorama import init
init()

def createBomb():
    global bombCoords
    bombCoords = [random.randint(1,38),2]
    
def render():
    global spaceShipCoords
    for i in range(30):
        if i == 0 or i == 29: 
            print(Fore.WHITE+'-'*40)
        else:
            print(Fore.WHITE+'|', end='')
            for n in range(38):
                #print(f'n: {n}')
                #print(f'i: {i}')
                if n == spaceShipCoords[0] and i == spaceShipCoords[1]:
                    print(Fore.BLUE+'^', end='')
                elif n == pewPewBullets[0] and i == pewPewBullets[1]:
                    print(Fore.GREEN+'|', end='')
                #'''
                #[somthing for i in something_else if predicate]
                #if pewPewBullets != []:
                #    for i in range(len(pewPewBullets)):
                #        if n == pewPewBullets[i][1] and i == pewPewBullets[i][0]:
                #            print('.',end='')
                #        else:
                #            print(' ',end='')
                #'''
                elif n == bombCoords[0] and i == bombCoords[1]:
                    print(Fore.RED+'x', end='')
                else:
                    print(' ',end='')
            print(Fore.WHITE+'|')
lives = 2
def legend():
    print('''
------------
|Legend    |
|^ = You   |
|x = Bomb  |
|| = Bullet|
------------
Note: You can only shoot one bullet at a time!!!
''')
    print(f'Score: {score}')
    print(f'Lives: {lives}')
os.system('clear')
createBomb()
print(bombCoords)
render()
legend()
print(f'Spacship Co-ordinates: {spaceShipCoords}')
createBomb()

while True:
    #print(f'{bombCoords[0]},{bombCoords[1]}')
    if pewPewBullets != [None,None]:
        time.sleep(0.0001)
        pewPewBullets[1] -= 1
        time.sleep(0.0001)
        os.system('clear')
        render()
        legend()
        print(f'Spacship Co-ordinates: {spaceShipCoords}')
    if bombCoords != [None,None]:
        time.sleep(0.02)
        bombCoords[1] += 1
        time.sleep(0.02)
        os.system('clear')
        render()
        legend()
        print(f'Spacship Co-ordinates: {spaceShipCoords}')
    if keyboard.is_pressed('left'):
        if spaceShipCoords[0] != 0:
            spaceShipCoords[0] -= 1
            if pewPewBullets == [None,None]:
                time.sleep(0.03)
            os.system('clear')
            render()
            legend()
            print(f'Spacship Co-ordinates: {spaceShipCoords}')
    if keyboard.is_pressed('right'):
        if spaceShipCoords[0] != 37:
            spaceShipCoords[0] += 1
            if pewPewBullets == [None,None]:
                time.sleep(0.05)
            os.system('clear')
            render()
            legend()
            print(f'Spacship Co-ordinates: {spaceShipCoords}')
    if keyboard.is_pressed('space'):
        if pewPewBullets == [None,None]:
            pewPewBullets[0] = spaceShipCoords[0]
            pewPewBullets[1] = spaceShipCoords[1]-1
            #winsound.Beep(500, 100)
            #playsound.playsound('pew.m4a')
            #playsound.playsound('pew.mp3', True)
        time.sleep(0.1)
        os.system('clear')
        render()
        legend()
        print(f'Spacship Co-ordinates: {spaceShipCoords}')
    if pewPewBullets[1] == 1:
        pewPewBullets = [None,None]
        time.sleep(0.05)
        os.system('clear')
        render()
        legend()
        print(f'Spacship Co-ordinates: {spaceShipCoords}')
    if bombCoords == pewPewBullets or (bombCoords[0] == pewPewBullets[0] and bombCoords[1]>pewPewBullets[1] and bombCoords[1]-pewPewBullets[1] == 1):
        pewPewBullets = [None,None]
        bombCoords = [None,None]
        createBomb()
        score += 28-bombCoords[1]
    if bombCoords[1] == 29:
        bombCoords = [None,None]
        createBomb()
    if bombCoords == spaceShipCoords:
        lives -= 1
        if lives == 0:
            os.system('clear')
            print("""
  _____                         ____                 
 / ____|                       / __ \                
| |  __  __ _ _ __ ___   ___  | |  | |_   _____ _ __ 
| | |_ |/ _` | '_ ` _ \ / _ \ | |  | \ \ / / _ \ '__|
| |__| | (_| | | | | | |  __/ | |__| |\ V /  __/ |   
 \_____|\__,_|_| |_| |_|\___|  \____/  \_/ \___|_|  

""")
            print(f'Your score {score}')
            exit()
    #if score%100 == 0:
    #    time.sleep(0.1)
    #    bombCoords.append([random.randint(1,38),1])

    

