import pytmx, pygame, render, pyautogui, mapping

pygame.init()
 
WHITE = (255, 255, 255)
screenSize = int(pyautogui.size()[1]/1.5)
size = (screenSize, int(screenSize*.71))
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("My Game")
 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()

gameMap = mapping.map("test.tmx", 'character.png', (10,10))

moveX = 0
moveY = 0
velocity = 2

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                moveX = -velocity
            if event.key == pygame.K_d:
                moveX = velocity
            if event.key == pygame.K_w:
                moveY = -velocity
            if event.key == pygame.K_s:
                moveY = velocity
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                if moveX != velocity:
                    moveX = 0
            if event.key == pygame.K_d:
                if moveX != -velocity:
                    moveX = 0
            if event.key == pygame.K_w:
                if moveY != velocity:
                    moveY = 0
            if event.key == pygame.K_s:
                if moveY != -velocity:
                    moveY = 0
 
    # --- Game logic should go here
    gameMap.move(moveX, moveY)
 
    # --- Screen-clearing code goes here
    gameMap.drawMap(screen, "test.tmx")
 
    # --- Drawing code should go here
    gameMap.drawMainCharacter(screen)

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
 
# Close the window and quit.
pygame.quit()