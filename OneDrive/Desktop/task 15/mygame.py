# I have adapted this code from the example provided for this task

import pygame # Imports a game library that lets you use specific functions in your program.
import random # Import to generate random numbers. 

# Initialize the pygame modules to get everything started.

pygame.init() 

# The screen that will be created needs a width and a height.

screen_width = 1400
screen_height = 700
screen = pygame.display.set_mode((screen_width,screen_height)) # This creates the screen and gives it the width and height specified as a 2 item sequence.

# variables created and images loaded to create players and enemies 

player = pygame.image.load("player.jpg")

enemy = pygame.image.load("enemy.png")

prize = pygame.image.load("prize.jpg")

enemy_two = pygame.image.load("monster.jpg")

enemy_three = pygame.image.load("monster.jpg")

# Get the width and height of the images in order to do boundary detection 

image_height = player.get_height()
image_width = player.get_width()

enemy_height = enemy.get_height()
enemy_width = enemy.get_width()

prize_height = prize.get_height()
prize_width = prize.get_width()

enemy_two_height = enemy_two.get_height()
enemy_two_width = enemy_two.get_width()

enemy_three_height = enemy_three.get_height()
enemy_three_width = enemy_three.get_width()

print("This is the height of the player image: " +str(image_height))
print("This is the width of the player image: " +str(image_width))

# players positions stored in variables

playerXPosition = 100
playerYPosition = 50

# variables created to make the enemy start off screen

enemyXPosition =  screen_width
enemyYPosition =  random.randint(0, screen_height - enemy_height)

enemy_two_x_position = random.randint(0, screen_width - enemy_two_width)
enemy_two_y_position = random.randint(0, screen_height - enemy_two_height)


enemy_three_x_position =  random.randint(0, screen_width - enemy_two_width)
enemy_three_y_position =  random.randint(0, screen_height - enemy_three_height)


prize_x_position = 900
prize_y_position = 100


# This checks if the up, down, left and right key is pressed.
# Boolean values are set to Flase 

keyUp= False
keyDown = False
keyRight = False
keyLeft = False

# This is the game loop.
# In games you will need to run the game logic over and over again.
# You need to refresh/update the screen window and apply changes to 
# represent real time game play. 

while 1: # This is a looping structure that will loop the indented code until you tell it to stop

    screen.fill(0) # Clears the screen.
    screen.blit(player, (playerXPosition, playerYPosition))# This draws the player image to the screen at the postion specfied.
    screen.blit(enemy, (enemyXPosition, enemyYPosition))
    screen.blit(enemy_two, (enemy_two_x_position, enemy_two_y_position))
    screen.blit(enemy_three, (enemy_three_x_position, enemy_three_y_position))
    screen.blit(prize, (prize_x_position, prize_y_position))
    pygame.display.flip()# This updates the screen. 
    
    # This loops through events in the game.
    
    for event in pygame.event.get():
    
        # This event checks if the user quits the program, then if so it exits the program. 
        
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)
            
        # This event checks if the user press a key down.
        
        if event.type == pygame.KEYDOWN:
        
            # Test if the key pressed is the one we want.
            
            if event.key == pygame.K_UP: # pygame.K_UP represents a keyboard key constant. 
                keyUp = True
                
            if event.key == pygame.K_DOWN: # pygame.K_DOWN represents a keyboard key constant.
                keyDown = True
                
            if event.key == pygame.K_RIGHT:# pygame.K_RIGHT represents a keyboard key constant.
                keyRight = True
                
            if event.key == pygame.K_LEFT:# pygame.K_LEFT represents a keyboard key constant.
                keyLeft = True
    
        # This event checks if the key is up
        
        if event.type == pygame.KEYUP:
        
            # Test if the key released is the one we want.
            
            if event.key == pygame.K_UP:
                keyUp = False
                
            if event.key == pygame.K_DOWN:
                keyDown = False
                
            if event.key == pygame.K_RIGHT:
                keyRight = False
                
            if event.key == pygame.K_LEFT:
                keyLeft = False
            
    # After events are checked for in the for loop above and values are set,
    # check key pressed values and move player accordingly.
    
    # The coordinate system of the game window(screen) is that the top left corner is (0, 0).
    # This means that if you want the player to move down you will have to increase the y position. 
    
    if keyUp == True:
        if playerYPosition > 0 : # This makes sure that the user does not move the player above the window.
            playerYPosition -= 1
            
    if keyDown == True:
        if playerYPosition < screen_height - image_height:# This makes sure that the user does not move the player below the window.
            playerYPosition += 1
            
    if keyRight == True:
        if playerXPosition > 0 : 
            playerXPosition += 1
            
    if keyLeft == True:
        if playerXPosition < screen_width - image_width:  
            playerXPosition -= 1
    
    # Check for collision of the enemy with the player.
    # To do this we need bounding boxes around the images of the player and enemy.
    # We the need to test if these boxes intersect. If they do then there is a collision.
    
    # Bounding box for the player:
    
    playerBox = pygame.Rect(player.get_rect())
    
    # The following updates the playerBox position to the player's position,
    # in effect making the box stay around the player image. 
    
    playerBox.top = playerYPosition
    playerBox.left = playerXPosition
    
    # Bounding box for the enemy:
    
    enemyBox = pygame.Rect(enemy.get_rect())
    enemyBox.top = enemyYPosition
    enemyBox.left = enemyXPosition

    enemy_two_box = pygame.Rect(enemy_two.get_rect())
    enemy_two_box.top = enemy_two_y_position
    enemy_two_box.left = enemy_two_x_position

    enemy_three_box = pygame.Rect(enemy_three.get_rect())
    enemy_three_box.top = enemy_three_y_position
    enemy_three_box.left = enemy_three_x_position

    prize_box = pygame.Rect(prize.get_rect())
    prize_box.top = prize_y_position
    prize_box.left = prize_x_position
    
    # Test collision of the boxes:
    
    if playerBox.colliderect(enemyBox):
    
        # Display losing status to the user: 
        
        print("You lose!")
       
        # Quite game and exit window: 
        
        pygame.quit()
        exit(0)

     # Test collision of the boxes:
    
    if playerBox.colliderect(enemy_two_box):
    
        # Display losing status to the user: 
        
        print("You lose!")
       
        # Quite game and exit window: 
        
        pygame.quit()
        exit(0)

    if playerBox.colliderect(enemy_three_box):
    
        # Display losing status to the user: 
        
        print("You lose!")
       
        # Quite game and exit window: 
        
        pygame.quit()
        exit(0)
        
    # If the enemy is off the screen the user wins the game:
    
    if enemyXPosition < 0 - enemy_width:
    
        # Display wining status to the user: 
        
        print("You win!")
        
        # Quite game and exit window: 
        pygame.quit()
        
        exit(0)

    if playerBox.colliderect(prize_box):

        print("You Win!")

        pygame.quit()

        exit(0)
 
    
    # Make enemy approach the player.
    
    enemyXPosition -= 0.15

    enemy_two_x_position -= 0.15

    enemy_three_x_position -= 0.15

