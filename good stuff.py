import pygame
import random
from threading import Timer
import sys
# import pygame_textinput

def button():
    pygame.init()
    
    # screen dimensions
    screen_width = 1000
    screen_height = 600
    screen = pygame.display.set_mode([screen_width, screen_height])
    

    WHITE = (255,255,255)
    GREY = (128, 128, 128)

    #Display text
    font = pygame.font.SysFont('Calibri', 50, True, False)
    text = font.render("Title",True,WHITE)
    text = font.render("Your Game " , True, WHITE)
    screen.blit(text, [400, 30])
    pygame.display.flip()

    # screen into a variable
    widthQuit = 850
    widthAvoid = 850
    widthEat= 850
    
    # stores the heightQuit of the
    # screen into a variable
    heightQuit = 1100
    heightAvoid = 900
    heightEat = 700
    
    smallfont = pygame.font.SysFont('Corbel',35)
    

    quitBtn = smallfont.render("Quit" , True , WHITE)
    avoidBtn = smallfont.render("Avoid" , True , WHITE)
    eatBtn = smallfont.render("Eat" , True , WHITE)
    
    while True:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()

            #checks if a mouse is clicked
            if event.type == pygame.MOUSEBUTTONDOWN:

                #if the mouse is clicked on the
                # button the game is terminated
                if widthQuit/2 <= mouse[0] <= widthQuit/2+140 and heightQuit/2 <= mouse[1] <= heightQuit/2+40:
                    pygame.quit()
                if widthAvoid/2 <= mouse[0] <= widthAvoid/2+140 and heightAvoid/2 <= mouse[1] <= heightAvoid/2+40:
                    pygame.quit()
                    avoidBlocks()
                if widthEat/2 <= mouse[0] <= widthEat/2+140 and heightEat/2 <= mouse[1] <= heightEat/2+40:
                    pygame.quit()
                    eatBlocks()

        # xy coordinates of mouse
        mouse = pygame.mouse.get_pos()

        # Background color for buttons
        pygame.draw.rect(screen,GREY,[widthQuit/2,heightQuit/2,140,40])
        pygame.draw.rect(screen,GREY,[widthAvoid/2,heightAvoid/2,140,40])
        pygame.draw.rect(screen,GREY,[widthEat/2,heightEat/2,140,40])
    
        # placing the quitBtn onto button
        screen.blit(quitBtn , (widthQuit/2+50,heightQuit/2))
        screen.blit(avoidBtn , (widthAvoid/2+50,heightAvoid/2))
        screen.blit(eatBtn , (widthEat/2+50,heightEat/2))  

        font = pygame.font.SysFont('Calibri', 100, True, False)
        text = font.render("Score: ", True, WHITE)

        pygame.display.update()


def eatBlocks():

    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)
    YELLOW = (255, 255, 0)

    # starting coordinates of player block
    x1 = 0
    y1 = 0

    # hold values of player block when moving
    x1_change = 0       
    y1_change = 0

    score = 0


    # class for all blocks in the game
    class Block(pygame.sprite.Sprite):
    
        def __init__(self, WHITE, width, height):
        
            # Call the parent class (Sprite) constructor
            super().__init__()

            # Create an image of the block, and fill it with a WHITE.
            # This could also be an image loaded from the disk.
            self.image = pygame.Surface([width, height])
            self.image.fill(WHITE)

            # Fetch the rectangle object that has the dimensions of the image
            # image.
            # Update the position of this object by setting the values
            # of rect.x and rect.y
            self.rect = self.image.get_rect()

    pygame.init()

    screen_width = 1000
    screen_height = 600
    screen = pygame.display.set_mode([screen_width, screen_height])

    block_list = pygame.sprite.Group()

    all_sprites_list = pygame.sprite.Group()

    for i in range(50):

        food = Block(YELLOW, 20, 15)

        # Set a random location for the block
        food.rect.x = random.randrange(screen_width)
        food.rect.y = random.randrange(screen_height)

        # Add the block to the list of objects
        block_list.add(food)
        all_sprites_list.add(food)
    # green player 
    player = Block(RED, 20, 20)
    all_sprites_list.add(player)
    # Loop until the user clicks the close button.
    loop = True
    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()
    # -------- Main Program Loop -----------
    while loop:
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                loop = False
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a and score >= 10:
                    x1_change = -10
                    y1_change = 0
                elif event.key == pygame.K_d and score >= 10:
                    x1_change = 10
                    y1_change = 0
                elif event.key == pygame.K_w and score >= 10:
                    y1_change = -10
                    x1_change = 0
                elif event.key == pygame.K_s and score >= 10:
                    y1_change = 10
                    x1_change = 0
                elif event.key == pygame.K_a:
                    x1_change = -5
                    y1_change = 0
                elif event.key == pygame.K_d:
                    x1_change = 5
                    y1_change = 0
                elif event.key == pygame.K_w:
                    y1_change = -5
                    x1_change = 0
                elif event.key == pygame.K_s:
                    y1_change = 5
                    x1_change = 0
        # Positioning of player block updates after key is pressed
        x1 += x1_change
        y1 += y1_change

        # If player block hits walls, game over
        if x1 >= screen_width or x1 < 0 or y1 >= screen_height or y1 < 0:
            loop = False
            print ("Game over")
        # Clear the screen
        screen.fill(BLACK)
        # player block positioning which updates after x1, y1 change is applied
        player.rect.x = x1
        player.rect.y = y1
        # See if the player block has collided with anything.
        blocks_hit_list = pygame.sprite.spritecollide(player, block_list, True)
        # Check the list of collisions.
        for block in blocks_hit_list:
            score +=1
            print(score)
        # Check for win
        if score == 50:
            print("You won!")
            loop = False
        # Draw all the spites
        all_sprites_list.draw(screen)
        # Score stuff                             bold #Italic
        font = pygame.font.SysFont('Calibri', 25, True, False)
        text = font.render("Score: " + str(score), True, WHITE)
        screen.blit(text, [350, 10])
        #Update the screen with drawing.
        pygame.display.flip()
        # 60 FPS
        clock.tick(60)
    print("quit")
    pygame.quit()

def avoidBlocks():
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)
    YELLOW = (255, 255, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 250)
    
    # starting coordinates of player block
    x1 = 0
    y1 = 0
    blockDimensionX = 20
    blockDimensionY = 20

    # Hold updating values of x and y values
    x1_change = 0       
    y1_change = 0

    # Variables
    score = 0

    # class for all blocks in the game
    class Block(pygame.sprite.Sprite):
    
        def __init__(self, WHITE, width, height):
        
            # Call the parent class (Sprite) constructor
            super().__init__()

            # Create an image of the block, and fill it with a WHITE.
            # This could also be an image loaded from the disk.
            self.image = pygame.Surface([width, height])
            self.image.fill(WHITE)

            # Fetch the rectangle object that has the dimensions of the image
            # image.
            # Update the position of this object by setting the values
            # of rect.x and rect.y
            self.rect = self.image.get_rect()

    # Initialize Pygame
    pygame.init()

    screen_width = 1000
    screen_height = 600

    screen = pygame.display.set_mode([screen_width, screen_height])


    block_list_avoid = pygame.sprite.Group()
    block_list_collectCoins = pygame.sprite.Group()


    all_sprites_list = pygame.sprite.Group()


    player = Block(RED, blockDimensionX, blockDimensionY)
    all_sprites_list.add(player)

    loop = True

    clock = pygame.time.Clock()

    for i in range(50):

        obstacle = Block(BLUE, 20, 15)

        obstacle.rect.x = random.randrange(screen_width)
        obstacle.rect.y = random.randrange(screen_height)

        block_list_avoid.add(obstacle)
        all_sprites_list.add(obstacle)
   
    # -------- Main Program Loop -----------
    while loop:
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                loop = False
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a and score >= 3:
                    x1_change = -3
                    y1_change = 0
                elif event.key == pygame.K_d and score >= 3:
                    x1_change = 3
                    y1_change = 0
                elif event.key == pygame.K_w and score >= 3:
                    y1_change = -3
                    x1_change = 0
                elif event.key == pygame.K_s and score >= 3:
                    y1_change = 3
                    x1_change = 0

                elif event.key == pygame.K_a:
                    x1_change = -3
                    y1_change = 0
                elif event.key == pygame.K_d:
                    x1_change = 3
                    y1_change = 0
                elif event.key == pygame.K_w:
                    y1_change = -3
                    x1_change = 0
                elif event.key == pygame.K_s:
                    y1_change = 3
                    x1_change = 0
        # Positioning of player block updates after key is pressed
        x1 += x1_change
        y1 += y1_change 

        # If player block hits walls, game over
        if x1 >= screen_width or x1 < 0 or y1 >= screen_height or y1 < 0:
            loop = False
            print ("Game over")

        # Clear the screen
        screen.fill(BLACK)

        coins = Block(YELLOW, 20, 15)


        # player block positioning which updates after x1, y1 change is applied
        player.rect.x = x1
        player.rect.y = y1

        # See if the player block has collided with anything.
        blocks_hit_list_avoid = pygame.sprite.spritecollide(player, block_list_avoid, True)
        block_hit_list_collectCoins = pygame.sprite.spritecollide(player, block_list_collectCoins, True)

        # for i in range(1):
        for block in block_hit_list_collectCoins:
            if block_hit_list_collectCoins:
                score += 1
                coins.rect.x = random.randrange(screen_width)
                coins.rect.y = random.randrange(screen_height)

        # Add the block to the list of objects
        block_list_collectCoins.add(coins)
        all_sprites_list.add(coins)


        # Check the list of collisions
        
        for block in blocks_hit_list_avoid:
            print("Game Over")
            pygame.quit() 
            

        # Check for win
        if score == 50:
            print("You won!")
            loop = False

        # Draw all the spites
        all_sprites_list.draw(screen)

        # Score stuff                             bold #Italic
        font = pygame.font.SysFont('Calibri', 25, True, False)
        text = font.render("Score: " + str(score), True, WHITE)
        screen.blit(text, [350, 10])

        #Update the screen with drawing.
        pygame.display.flip()

        # 60 FPS
        clock.tick(60)

    print("quit")

    pygame.quit()

button()