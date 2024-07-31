import pygame 
import os       #This os module allows Python to access your files and directories on your computer - like making folders, renaming files, or delete files.

pygame.init()   #This is to initiates all the modules required by Pygame that you will need for your game. 

screen_height = 600
screen_width = 1100
screen = pygame.display.set_mode((screen_width, screen_height)) #This will define where the game will be shown

#Since there will be two dinosaur running you can make the images and it being implemented into a list if there are more than one pictures.
#Dinosaur movements
running = [pygame.image.load(os.path.join("Assets/Dino", "DinoRun1.png")),                #Storing all the T-Rex images running 
        pygame.image.load(os.path.join("Assets/Dino", "DinoRun2.png"))]                      #This is telling the computer to go through the path and get all the pictures it needs
jumping = pygame.image.load(os.path.join("Assets/Dino", "DinoJump.png"))
ducking = [pygame.image.load(os.path.join("Assets/Dino", "DinoDuck1.png")),
           pygame.image.load(os.path.join("Assets/Dino", "DinoDuck2.png"))]

#Cactus
small_cactus = [pygame.image.load(os.path.join("Assets/Cactus", "SmallCactus1.png")),
                pygame.image.load(os.path.join("Assets/Cactus", "SmallCactus2.png")),
                pygame.image.load(os.path.join("Assets/Cactus", "SmallCactus3.png"))]
large_cactus = [pygame.image.load(os.path.join("Assets/Cactus", "LargeCactus1.png")),
                pygame.image.load(os.path.join("Assets/Cactus", "LargeCactus2.png")),
                pygame.image.load(os.path.join("Assets/Cactus", "LargeCactus3.png"))]

#Birds
bird = [pygame.image.load(os.path.join("Assets/Bird", "Bird1.png")),
        pygame.image.load(os.path.join("Assets/Bird", "Bird2.png"))]

#Clouds for the background 
cloud = pygame.image.load(os.path.join("Assets/Others", "Cloud.png"))

back_ground = pygame.image.load(os.path.join("Asstes/Others", "Track.png"))


class Dinosaur:
    x_pos = 80      #These two variables basically positioning the dinosaur 
    y_pos = 310
#Now creating an init method (function) which will initialize the dinosaur whenever the object of this class is created
    def __init__(self):     #This first init method will be including all the images of the dinosaur
        self.duck_img = ducking
        self.run_img = running
        self.jump_img = jumping
#When we first initialize the Dinosaur, first we just want it to run only
        self.duck_img = False
        self.run_img = True         #These will only telling the code to just run for the Dinosaur
        self.jump_img = False 

        self.step_index = 0  #This is keeping track of which steps the dinosaur is on
        self.image = self.run_img[0]   #this will initialize the first image of the dinosaur when the game has been created
        self.dino_rect = self.image.get_rect() #This will create a rectangle around the dinosaur as a hitbox 

        #now setting the x and y rectangle coordinates on the dinosaur
        self.dino_rect.x = self.x_pos
        self.dino_rect.y = self.y_pos

    #Creating an update function that will updates the dinosaur on every while loop iteration by getting the user input
    def update(self, userInput):
        #The first block will be checking the states of the dinosaur
        if self.dino_duck:
            self.duck()
        elif self.dino_run:
            self.run()
        elif self.dino_jump:
            self.jump()

        elif self.step_index >= 10:         #This will be reset every 10 steps and allow us to animate the dinosaur later on
            self.step_index = 0 

        if userInput[pygame.K_UP] and not self.dino_jump:
        elif userInput[pygame.K_UP] and not self.dino_jump:
        elif not (self.dino_jump or userInput [pygame.K_DOWN]:
        
#The main loop will be in here
def main(): #It will become super helpful later down in the coding
    run = True #This will be the switch for our while loop (starts the loop)
    clock = pygame.time.Clock()         #This is a clock that is used to control the game's frame rate
    player = Dinosaur()         #This is adding the player into the game and this is the instances of the class Dinosaur

#Here's the main loop
    while run:      #This will allow the player to exits the game safely 
        for event in pygame.event.get():
            if event.type == pygame.QUIT: #So in order to enter this conditional statement, the player must exit out of the window or QUIT
                run = False     #This is set to false whenever the player press on the x on window or page

        screen.fill((255, 255, 255))        #This "screen.fill" will filled everything in the color white on every while loop iteration
        userInput = pygame.key.get_pressed() #This is detecting all the keys are being pressed that are used to control the game

        player.draw(screen)     #this function will be drawing the dinosaur onto the screen
        player.update(userInput)    #this function will update the dinosaur every while loop iteration or updates the player's state based on the current user input

        clock.tick(30)      #This is setting the frame rate to 30 frames per second, making the game run smoothly
        pygame.display.update()     #This will updates the display with everything drawn since the last update (in other words, putting all images in the game)
main()