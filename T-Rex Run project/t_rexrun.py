import pygame 
import os       #This os module allows Python to access your files and directories on your computer - like making folders, renaming files, or delete files.
import random


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

back_ground = pygame.image.load(os.path.join("Assets/Others", "Track.png"))


class Dinosaur:
    x_pos = 80      #These two variables basically positioning the dinosaur 
    y_pos = 310
    y_pos_duck = 340    #The y coordinate is higher because the dinosaur is ducking 
    jump_vel = 8.5  #This will determine the velocity of how high the dinosaur will be jumping
 #Now creating an init method (function) which will initialize the dinosaur whenever the object of this class is created
    def __init__(self):     #This first init method will be including all the images of the dinosaur
        self.duck_img = ducking
        self.run_img = running
        self.jump_img = jumping

        self.is_ducking = False       #When we first initialize the Dinosaur, first we just want it to run only
        self.is_running = True         #These will only telling the code to just run for the Dinosaur
        self.is_jumping = False

        self.step_index = 0  #This is keeping track of which steps the dinosaur is on
        self.jump_height = self.jump_vel        #This will initiate the jumping velocity that we have just define in the Dinosaur class before this function
        self.image = self.run_img[0]   #this will initialize the first image of the dinosaur when the game has been created
        self.dino_rect = self.image.get_rect() #This will create a rectangle around the dinosaur as a hitbox 
        self.dino_rect.x = self.x_pos   #now setting the x and y rectangle hitbox coordinates on the dinosaur
        self.dino_rect.y = self.y_pos

    #Creating an update function that will updates the dinosaur on every while loop iteration by getting the user input
    def update(self, userInput):
        #The first block will be checking the states of the dinosaur
        if self.is_ducking:
            self.duck()
        elif self.is_running:
            self.run()
        elif self.is_jumping:
            self.jump()

        elif self.step_index >= 10:         #This will be reset every 10 steps and allow us to animate the dinosaur later on
            self.step_index = 0 

        if userInput[pygame.K_UP] and not self.is_jumping:
            self.is_jumping = True
            self.is_running = False       #This block will detect jumping whenever you press the up key (it will be able to tell from userInput)
            self.is_ducking = False
        elif userInput[pygame.K_DOWN] and not self.is_jumping:
            self.is_ducking = True 
            self.is_jumping = False      #This block will detect ducking whenever you press the down key (it will be able to detect from userInput)
            self.is_running = False
        elif not (self.is_jumping or userInput [pygame.K_DOWN]):
            self.is_running = True
            self.is_ducking = False      #This block is saying that if dinosaur is jumping or ducking then we want to just set running to True and everything else False
            self.is_jumping = False
    #Now we are going to create seperate function for each movement


    def jump(self):
        self.image = self.jump_img #This is declaring the jumping image that we will be using
        if self.is_jumping:  #If the state of the dinosaur is set to jumping, then we would want to decrease the y position to allow the dinosaur to move up to our screen
            self.dino_rect.y -= self.jump_vel * 4       #This is determining how high the dinosaur is jumping and the higher the number is the higher the dinosaur jump
            self.jump_vel -= 0.8 #This will be decreasing the velocity for the Dinosaur to jump

        if self.jump_vel < -self.jump_height: #This will keep track if the jumping velocity does reach negative 8.5 
            self.is_jumping = False     #Stop the jump
            self.jump_vel = self.jump_height    #This will be reset the Dinosaur jump
            self.dino_rect.y = self.y_pos


    def run(self):
        self.image = self.run_img[self.step_index // 5]     #This is grabbing the dinosaur image running and implementing the step index #This will be rotating through the images of the dinosaur running, think of it like a gif, just two images at a fast frame rate
        self.dino_rect = self.image.get_rect()  #We will also need the rectangular hitbox
        self.dino_rect.x = self.x_pos       #Setting the position of the rectangule to where the dinosaur is
        self.dino_rect.y = self.y_pos
        self.step_index += 1            #The step index will be increment everytime the function is being called
        self.step_index %= 10


    def duck(self):
        self.image = self.duck_img[self.step_index // 5]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.x_pos
        self.dino_rect.y = self.y_pos_duck
        self.step_index += 1
        self.step_index %= 10


    def draw(self, screen):
        screen.blit(self.image, (self.dino_rect.x, self.dino_rect.y))

class Obstacles:    #This is the parent class that all obstacles will be going to
    def __init__(self, image, type):
        self.image = image      #All the images of the cactus
        self.type = type        #This will be putting types from small or large cactus separately. All cactus will determine with numbers 0 to 2
        self.rect = self.image[self.type].get_rect()    #Getting the rectangle coordinates of the image
        self.rect.x = screen_width      #Setting all obstacles applying with the screen width as it being created, all obstacles will appear just off right of the screen

    def update(self):   #It will allow the obstacles to be moving across the screen
        self.rect.x -= game_speed   #Decreasing the x-coordinate of the rectangle of the image by the game speed
        if self.rect.x < -self.rect.width:      #This if statement will remove any off obstacles that goes off the screen on the left hand side
            obstacles.pop()


    def draw(self, screen):
        screen.blit(self.image[self.type], self.rect)

class SmallCactus(Obstacles):
    def __init__(self, image): #Taking the image as a parameter
        self.type = random.randint(0, 2)
        super().__init__(image, self.type)
        self.rect.y = 325

class LargeCactus(Obstacles):
    def __init__(self, image):
        self.type = random.randint(0, 2)
        super().__init__(image, self.type)
        self.rect.y = 300


class Bird(Obstacles):      #Somewhat similar to the cacti classes but in the Bird class there are two images
    def __init__(self, image):
        self.type = 0
        super().__init__(image, self.type)
        self.rect.y = 250 #This is where the bird position will be 
        self.index = 0

        #now we need to override the type in the Obstacles class since the bird is animated
    
    def draw(self, screen):
        if self.index >= 9:
            self.index = 0      #This if statement will reset the index once it has reach the value of 9
        screen.blit(self.image[self.index // 5], self.rect)     #Showing the image on the screen
        self.index += 1


class Cloud:    #This class will be containing 3 functions or methods
    def __init__(self):
        self.x = screen_width + random.randint(800, 1000)   #These two will be telling us about the cloud coordinates when it is created
        self.y = random.randint(50, 100)
        self.image = cloud
        self.width = self.image.get_width()     #The width of the cloud

    def update(self):   #This functions/methods will be making the cloud move from the right to the left
        self.x -= game_speed    #This will be subtracting the x coordinates of the cloud
        if self.x < -self.width:       #This if statement will be resetting the cloud coordinates whenever it goes off the screen for it to show up again
            self.x = screen_width + random.randint(2500, 3000)
            self.y = random.randint(50, 100)
    
    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))

#The main loop will be in here
def main(): #It will become super helpful later down in the coding
    global game_speed, x_pos_bg, y_pos_bg, points, obstacles       #This line will tell the whole main function here that these can be use anywhere
    run = True #This will be the switch for our while loop (starts the loop)
    clock = pygame.time.Clock()         #This is a clock that is used to control the game's frame rate
    player = Dinosaur()         #This is adding the player into the game and this is the instances of the class Dinosaur
    cloud = Cloud()     #This will be calling up the Cloud class
    game_speed = 14
    x_pos_bg = 0        #Determines the background position (of the land that the dinosaur will be running on)
    y_pos_bg = 380
    points = 0 #At the start of the game, the points will always start at 0
    font = pygame.font.Font("freesansbold.ttf", 20)
    obstacles = []
    
    def score():
        global points, game_speed
        points += 1
        if points % 100 == 0:       #This statement will be checking that whenever the multiples is 100 then the game speed will be increment to 1, making it faster the longer the player live
            game_speed += 1

        text = font.render("Points: " + str(points), True, (0, 0, 0))   #This will be displaying the text of our points on the screen
        textrect = text.get_rect()          #This will be getting the coordinates the rectangle from within where the points are being display
        textrect.center = (1000, 40)        #This is positioning of where the points will be showing up
        screen.blit(text, textrect)


    def background():
        global x_pos_bg, y_pos_bg
        image_width = back_ground.get_width()
        screen.blit(back_ground, (x_pos_bg, y_pos_bg))
        screen.blit(back_ground, (image_width + x_pos_bg, y_pos_bg))
        if x_pos_bg <= -image_width:                #This if statement is just basically telling Python when one image moves off the screen, it reset and include the next image
            screen.blit(back_ground, (image_width + x_pos_bg, y_pos_bg))
            x_pos_bg = 0
        x_pos_bg -= game_speed


    #Here's the main loop
    while run:      #This will allow the player to exits the game safely 
        for event in pygame.event.get():
            if event.type == pygame.QUIT: #So in order to enter this conditional statement, the player must exit out of the window or QUIT
                run = False     #This is set to false whenever the player press on the x on window or page

        screen.fill((255, 255, 255))        #This "screen.fill" will filled everything in the color white on every while loop iteration
        userInput = pygame.key.get_pressed() #This is detecting all the keys are being pressed that are used to control the game

        player.draw(screen)     #this function will be drawing the dinosaur onto the screen
        player.update(userInput)    #this function will update the dinosaur every while loop iteration or updates the player's state based on the current user input

        if len(obstacles) == 0:
            if random.randint(0, 2) == 0:
                obstacles.append(SmallCactus(small_cactus))
            elif random.randint(0, 2) == 1:
                obstacles.append(LargeCactus(large_cactus))
            elif random.randint(0, 2) == 2:
                obstacles.append(Bird(bird))

        for obstacle in obstacles:
            obstacle.draw(screen)
            obstacle.update() 
            if player.dino_rect.colliderect(obstacle.rect):        #This if statement will be detecting whenever the dinosaur run pass a obstacles the hitbox will become red
                pygame.draw.rect(screen, (255, 0, 0), player.dino_rect, 2)      
        background()

        cloud.draw(screen)      #These two will be calling the update and drawing on the cloud
        cloud.update() 

        score()     

        clock.tick(30)      #This is setting the frame rate to 30 frames per second, making the game run smoothly
        pygame.display.update()     #This will updates the display with everything drawn since the last update (in other words, putting all images in the game)


main()
