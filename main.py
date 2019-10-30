# ALL IMPORTS AND ALL GLOBAL VARIABLES
import pygame
from pikachu import Pikachu
import random
#import math # NOT USED YET
#import random # NOT USED YET
#import pygame.gfxdraw  # NOT USED YET
#from pygame.locals import * # NOT USED YET

# INITIALIZE PYGAME AND GLOBAL DISPLAY VARIABLES
pygame.init()
global displayWidth
displayWidth = 1080
global displayHeight
displayHeight = 720
global display
display = pygame.display.set_mode((displayWidth, displayHeight))
pygame.display.set_caption('EECS448 Project 3: Pokemon Battle Simulator')

# GLOBAL TEXT OBJECT VARIABLES
global BLACK
BLACK = pygame.Color(0, 0, 0)
global WHITE
WHITE = pygame.Color(255, 255, 255)
global RED
RED = pygame.Color(255, 0, 0)
global font
font = pygame.font.Font('freesansbold.ttf', 32)
global smallText
smallText = pygame.font.Font('freesansbold.ttf', 36)
global mediumText
mediumText = pygame.font.Font('freesansbold.ttf', 48)
global largeText
largeText = pygame.font.Font('freesansbold.ttf', 65)

# GLOBAL PLAYER POKEMON VARIABLES
global pokemonP1
pokemonP1 = ""
global pokemonAI
pokemonAI = ""

# CREATES A TEXT OBJECT
def createTextObject(textToDisplay, fontToUse):
    textSurface = font.render(textToDisplay, True, BLACK)
    return textSurface, textSurface.get_rect()

# CHECKS IF (x, y) IS INSIDE OF (rect.x, rect.y)
def isPointInRect(x, y, rect):
    if x < rect.x + rect.width and x > rect.x and y < rect.y + rect.height and y > rect.y:
        return True # (x, y) IS INSIDE OF (rect.x, rect.y)
    return False # (x, y) IS NOT INSIDE OF (rect.x, rect.y)

# (UNFINISHED) TRACKS IF THE PLAY BUTTON IS CLICKED
def trackPlayButton():
    global pokemonP1
    global pokemonAI
    mouse = pygame.mouse.get_pos() # GETS (x, y) COORDINATES OF MOUSE
    #print("mouse(x, y): ", mouse[0], ",", mouse[1]) # TESTER CODE
    if displayWidth * 0.45 + 110 > mouse[0] > displayWidth * 0.45 and displayHeight * 0.805 + 40 > mouse[1] > displayHeight * 0.805: # VALID LOCATION OF PLAY BUTTON
        pygame.draw.rect(display, RED, (displayWidth * 0.45, displayHeight * 0.805, 110, 40), 5) # BOX AROUND PLAY ON MOUSE-HOVER
        if pygame.mouse.get_pressed() == (1, 0, 0): # MOUSE CLICK DETECTED
            if pokemonP1 != "" and pokemonAI != "": # IF PLAYER 1 AND PLAYER AI HAVE POKEMON SELECTED
                if isPointInRect(mouse[0], mouse[1], pygame.Rect(displayWidth * 0.45, displayHeight * 0.805, 110, 40)): # MOUSE CLICK IS IN VALID LOCATION FOR PLAY BUTTON
                    # (UNFINISHED) THIS IS WHERE WINDOW SWITCH SHOULD OCCUR
                    print("MOUSE CLICK DETECTED ON PLAY BUTTON") # TESTER CODE
                    fightScreen(1) # (UNFINISHED) LET HUMAN = 1; AI = 2
            else: # (UNFINISHED) PLAYER 1 AND/OR PLAYER AI HAVE NOT SELECTED THEIR POKEMON
                print("FAILURE ON POKEMON SELECTION") # TESTER CODE

# (UNFINISHED) TRACKS IF PLAYER 1'S PIKACHU BUTTON IS CLICKED
def trackPikachuButton_P1():
    global pokemonP1
    mouse = pygame.mouse.get_pos() # GETS (x, y) COORDINATES OF MOUSE
    #print("mouse(x, y): ", mouse[0], ",", mouse[1]) # TESTER CODE
    if displayWidth * 0.19 + 130 > mouse[0] > displayWidth * 0.19 and displayHeight * 0.17 + 40 > mouse[1] > displayHeight * 0.17: # VALID LOCATION OF PLAYER 1'S PIKACHU BUTTON
        pygame.draw.rect(display, RED, (displayWidth * 0.19, displayHeight * 0.17, 130, 40), 5) # BOX AROUND PLAYER 1'S PIKACHU ON MOUSE-HOVER
        if pygame.mouse.get_pressed() == (1, 0, 0): # MOUSE CLICK DETECTED
            if isPointInRect(mouse[0], mouse[1], pygame.Rect(displayWidth * 0.19, displayHeight * 0.17, 130, 40)): # MOUSE CLICK IS IN VALID LOCATION FOR PLAYER 1'S PIKACHU BUTTON
                print("MOUSE CLICK DETECTED ON PLAYER 1'S PIKACHU BUTTON") # TESTER CODE
                pokemonP1 = "Pikachu" # GLOBAL pokemonP1 VARIABLE
                print("pokemonP1", pokemonP1) # TESTER CODE

# (UNFINISHED) TRACKS IF PLAYER 1'S CHARIZARD BUTTON IS CLICKED
def trackCharizardButton_P1():
    global pokemonP1
    mouse = pygame.mouse.get_pos() # GETS (x, y) COORDINATES OF MOUSE
    #print("mouse(x, y): ", mouse[0], ",", mouse[1]) # TESTER CODE
    if displayWidth * 0.173 + 170 > mouse[0] > displayWidth * 0.173 and displayHeight * 0.235 + 40 > mouse[1] > displayHeight * 0.235: # VALID LOCATION OF PLAYER 1'S CHARIZARD BUTTON
        pygame.draw.rect(display, RED, (displayWidth * 0.173, displayHeight * 0.235, 170, 40), 5) # BOX AROUND PLAYER 1'S CHARIZARD ON MOUSE-HOVER
        if pygame.mouse.get_pressed() == (1, 0, 0): # MOUSE CLICK DETECTED
            if isPointInRect(mouse[0], mouse[1], pygame.Rect(displayWidth * 0.173, displayHeight * 0.235, 170, 40)): # MOUSE CLICK IS IN VALID LOCATION FOR PLAYER 1'S CHARIZARD BUTTON
                print("MOUSE CLICK DETECTED ON PLAYER 1'S CHARIZARD BUTTON") # TESTER CODE
                pokemonP1 = "Charizard" # GLOBAL pokemonP1 VARIABLE
                print("pokemonP1", pokemonP1) # TESTER CODE

# (UNFINISHED) TRACKS IF PLAYER AI'S PIKACHU BUTTON IS CLICKED
def trackPikachuButton_AI():
    global pokemonAI
    mouse = pygame.mouse.get_pos() # GETS (x, y) COORDINATES OF MOUSE
    #print("mouse(x, y): ", mouse[0], ",", mouse[1]) # TESTER CODE
    if displayWidth * 0.71 + 130 > mouse[0] > displayWidth * 0.71 and displayHeight * 0.17 + 40 > mouse[1] > displayHeight * 0.17: # VALID LOCATION OF PLAYER AI'S PIKACHU BUTTON
        pygame.draw.rect(display, RED, (displayWidth * 0.71, displayHeight * 0.17, 130, 40), 5) # BOX AROUND PLAYER AI'S PIKACHU ON MOUSE-HOVER
        if pygame.mouse.get_pressed() == (1, 0, 0): # MOUSE CLICK DETECTED
            if isPointInRect(mouse[0], mouse[1], pygame.Rect(displayWidth * 0.71, displayHeight * 0.17, 130, 40)): # MOUSE CLICK IS IN VALID LOCATION FOR PLAYER AI'S PIKACHU BUTTON
                print("MOUSE CLICK DETECTED ON PLAYER AI'S PIKACHU BUTTON") # TESTER CODE
                pokemonAI = "Pikachu" # GLOBAL pokemonAI VARIABLE
                print("pokemonAI", pokemonAI) # TESTER CODE

# (UNFINISHED) TRACKS IF PLAYER AI'S CHARIZARD BUTTON IS CLICKED
def trackCharizardButton_AI():
    global pokemonAI
    mouse = pygame.mouse.get_pos() # GETS (x, y) COORDINATES OF MOUSE
    #print("mouse(x, y): ", mouse[0], ",", mouse[1]) # TESTER CODE
    if displayWidth * 0.69 + 170 > mouse[0] > displayWidth * 0.69 and displayHeight * 0.235 + 40 > mouse[1] > displayHeight * 0.235: # VALID LOCATION OF PLAYER AI'S CHARIZARD BUTTON
        pygame.draw.rect(display, RED, (displayWidth * 0.69, displayHeight * 0.235, 170, 40), 5) # BOX AROUND PLAYER AI'S CHARIZARD ON MOUSE-HOVER
        if pygame.mouse.get_pressed() == (1, 0, 0): # MOUSE CLICK DETECTED
            if isPointInRect(mouse[0], mouse[1], pygame.Rect(displayWidth * 0.69, displayHeight * 0.235, 170, 40)): # MOUSE CLICK IS IN VALID LOCATION FOR PLAYER AI'S CHARIZARD BUTTON
                print("MOUSE CLICK DETECTED ON PLAYER AI'S CHARIZARD BUTTON") # TESTER CODE
                pokemonAI = "Charizard" # GLOBAL pokemonAI VARIABLE
                print("pokemonAI", pokemonAI) # TESTER CODE

# (UNFINISHED) DISPLAYS THE START SCREEN
def startScreen():
    # PLAYER 1'S POKEMON OPTIONS
    textPlayer1, textPlayer1_RECT = createTextObject("Player 1's Pokemon", largeText)
    textPlayer1_RECT.center = (displayWidth / 4, displayHeight / 8)

    # PLAYER 1'S POKEMON BUTTONS
    textPikachu1, textPikachu1_RECT = createTextObject("Pikachu", mediumText)
    textPikachu1_RECT.center = (displayWidth / 4, displayHeight / 5)
    textCharizard1, textCharizard1_RECT = createTextObject("Charizard", mediumText)
    textCharizard1_RECT.center = (displayWidth / 4, displayHeight / 3.8)

    # PLAYER 2'S POKEMON OPTIONS
    textPlayer2, textPlayer2_RECT = createTextObject("Player 2's Pokemon", largeText)
    textPlayer2_RECT.center = (displayWidth / 1.3, displayHeight / 8)

    # PLAYER 2'S POKEMON BUTTONS
    textPikachu2, textPikachu2_RECT = createTextObject("Pikachu", mediumText)
    textPikachu2_RECT.center = (displayWidth / 1.3, displayHeight / 5)
    textCharizard2, textCharizard2_RECT = createTextObject("Charizard", mediumText)
    textCharizard2_RECT.center = (displayWidth / 1.3, displayHeight / 3.8)

    # PLAY BUTTON
    textPlay, textPlay_RECT = createTextObject("PLAY", largeText)
    textPlay_RECT.center = (displayWidth / 2, displayHeight / 1.2)

    #Pokemon Image Icons
#     imagePikachu = pygame.image.load('Pikachu.jpg')
#     imagePikachu_RECT = imagePikachu.get_rect()
#     imagePikachu_RECT.center = (displayWidth / 6, displayHeight / 5.5)
#     imageChar = pygame.image.load('Charizard.jpg')
#     imageChar_RECT = imageChar.get_rect()
#     imageChar_RECT.center = (displayWidth / 7.5, displayHeight / 3.8)
#     imagePikachu2 = pygame.image.load('Pikachu.jpg')
#     imagePikachu2_RECT = imagePikachu2.get_rect()
#     imagePikachu2_RECT.center = (displayWidth / 1.45, displayHeight / 5.5)
#     imageChar2 = pygame.image.load('Charizard.jpg')
#     imageChar2_RECT = imageChar2.get_rect()
#     imageChar2_RECT.center = (displayWidth / 1.52, displayHeight / 3.8)

    playGame = True # MAIN GAME LOOP BOOLEAN VARIABLE
    while playGame == True: # MAIN GAME LOOP
        display.fill(WHITE) # MAKES BACKGROUND OF START SCREEN WHITE
#         display.blit(imagePikachu, imagePikachu_RECT)
#         display.blit(imageChar, imageChar_RECT)
#         display.blit(imagePikachu2, imagePikachu2_RECT)
#         display.blit(imageChar2, imageChar2_RECT)
        display.blit(textPlayer1, textPlayer1_RECT) # DISPLAYS PLAYER 1'S POKEMON
        display.blit(textPikachu1, textPikachu1_RECT) # DISPLAYS PIKACHU FOR PLAYER 1
        display.blit(textCharizard1, textCharizard1_RECT) # DISPLAYS CHARIZARD FOR PLAYER 1
        display.blit(textPlayer2, textPlayer2_RECT) # DISPLAYS PLAYER AI'S POKEMON
        display.blit(textPikachu2, textPikachu2_RECT) # DISPLAYS PIKACHU FOR PLAYER AI
        display.blit(textCharizard2, textCharizard2_RECT) # DISPLAYS CHARIZARD FOR PLAYER AI
        display.blit(textPlay, textPlay_RECT) # DISPLAYS PLAY
        for event in pygame.event.get(): # FOR-LOOP TO HANDLE ALL PYGAME EVENTS
            if event.type == pygame.QUIT: # IF PYGAME EVENT IS QUIT
                playGame = False # STOP RUNNING THE PROGRAM
                pygame.quit() # QUIT PYGAME
                quit() # QUIT PYTHON3
            trackPikachuButton_P1() # TRACKS IF PIKACHU BUTTON IS CLICKED BY PLAYER 1
            trackCharizardButton_P1() # TRACKS IF CHARIZARD BUTTON IS CLICKED BY PLAYER 1
            trackPikachuButton_AI() # TRACKS IF PIKACHU BUTTON IS CLICKED BY PLAYER AI
            trackCharizardButton_AI() # TRACKS IF CHARIZARD BUTTON IS CLICKED BY PLAYER AI
            trackPlayButton() # TRACKS IF PLAY BUTTON IS CLICKED
            pygame.display.update() # UPDATE THE PYGAME DISPLAY

# (UNFINISHED) SETS UP GRAPHICS FOR THE FIGHT SCREEN
def fightScreen(playerTurn):
    print("fightScreen") # TESTER CODE
    display.fill(BLACK)
    pygame.display.update()

def playerTurn():
    # WILL CONTAIN EVERYTHING DONE IN ONE TURN (WILL CALL OTHER FUNCTIONS SUCH AS attack, attack_AI, checkForWin, etc.)
    #has to begin by tracking "fight", "bag", "run", etc (needs to be a different function probably)

    playerMove = "variable that contains ATTACK or USE_POTION ... can add others" #ex: clicking "attack" in GUI would then set this string to ATTACK

    if(playerMove == "ATTACK"): #or ----- if (FIGHT == True):
        #depends on which attack P1 chooses; ex if P1 is pikachu & they chppse... pokemonP1.ThunderBoltAttack()
        pokemonP1.ThunderBoltAttack(pokemonP1, pokemonAI);
        #now we should display some sort of window/message for the user saying if they hit or not
        #update AI's health in the UI

        # if pokemonAI.checkAlive() == False
        #     pokemonAI.faint()
        #     fight over

    elif(playerMove == "BAG"):
        if (pokemonP1.bagEmpty()):
            print("This player has nothing in their bad")   #Display some message to the player "BAG IS EMPTY"
        else:
            #change the player UI to ask what they want to do
            pokemonP1.useHealthPotion() #for this implementation, all we can use is health potions
            AIBagTrack += 1 #lets AI track how many items you've use from your bag so it can be more AI-ish

    elif(playerMove == "RUN"):
        # DISPLAY SOME SORT OF MESSAGE SAYING THE THIS PLAYER CHOSE TO RUN
        pygame.quit()

    elif(playerMove == "POKEMON"):  #nothing for this is done, just an example
        pokemonP1.switchPokemon()


    AITurn()    #after player's turn is over, let AI go



def AITurn():
<<<<<<< HEAD
    # AIMove = random.randint(1,101)
    # if (AIMove <= 90): #90% chance to attack
    #     #attack
    #     chosenAttack, result = playerAI.AIAttack() #chosenAttack will be the string of which attack was used, result was whether it worked or not
    #     #display 3 second popup window of which attack was chosen and whether it worked
    #     #checkForWin, if game over then exit this function and display victory screen
    # else if (AIMove <= 98 and playerAI.hasItem()): #8% chance to use item
    #     playerAI.useHealthPotion()
    #     #use item
    # #add 2% chance to run, need a run function to end the game

    # FOR BETA-VERSION (PROJECT 3 VERSION)
    # MAKE SOME VARIABLE/DEF THAT SAYS IF POKEMON IS IN CRITICAL CONDITION
    if(pokemonP1.currentHealth == critical):    #if P1 currently set-up pokemon is in critical condition - attack them
        pokemonAI.AIAttack(pokemonAI, pokemonP1)
        #now we should display some sort of window/message for the user saying if they hit or not
        #update player's health in the UI
    elif(pokemonAI.currentHealth == critical and pokemonAI.bagEmpty):   #this should be the AI's last option - AI is going to die if it's hit again
        # DISPLAY SOME SORT OF MESSAGE SAYING THE THIS PLAYER CHOSE TO RUN
        pygame.quit()

    elif(pokemonAI.currentHealth == critical):  #if AI is low, it will use potion
        pokemonAI.useHealthPotion()

    else:   # if pokemonP1 is not low and AI is not low, then all we can do is attack the other player
        pokemonAI.AIAttack(pokemonAI, pokemonP1)
        #now we should display some sort of window/message for the user saying if they hit or not
        #update player's health in the UI

    playerTurn()    #after turn is over, let the player go
=======
    AIMove = random.randint(1,101)
    if (AIMove <= 90): #90% chance to attack
        #attack
        chosenAttack, result = playerAI.AIAttack() #chosenAttack will be the string of which attack was used, result was whether it worked or not
        #display 3 second popup window of which attack was chosen and whether it worked
        #checkForWin, if game over then exit this function and display victory screen
    #else if (AIMove <= 98 and playerAI.hasItem()): #8% chance to use item
        #use item
    #add 2% chance to run, need a run function to end the game
>>>>>>> 85293fb5527f72fcf8823f58ddc5c1b5f94a4a7f

# MAIN
if __name__ == "__main__":
    startScreen() # CALL startScreen TO LOAD THE START SCREEN

    #playerTest = Pikachu() # TESTER CODE
    #player1 = Pikachu() # CHOOSE PLAYER1'S POKEMON
    #playerAI = # CHOOSE AI POKEMON
