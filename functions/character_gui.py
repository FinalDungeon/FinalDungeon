import pygame as pg
import os

WIDTH = 1000    
HEIGHT = 700
FPS = 30

# define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
CYAN = (0,255,255)
MAGENTA = (255,0,255)
YELLOW = (255,255,0)

# initialize PyGame and create window
pg.init()
pg.mixer.init()
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption('Character GUI')
screen.fill(BLACK)
clock = pg.time.Clock()

font1_path = os.path.join(os.path.abspath('../fonts'),'Blackwood Castle.ttf')
font2_path = os.path.join(os.path.abspath('../fonts'),'BlackwoodCastleShadow.ttf')
normal_font = pg.font.Font(font1_path, 40)
shadow_font = pg.font.Font(font2_path, 40)
ability_scores = 'Strength', 'Dexterity', 'Constitution', 'Intelligence', 'Wisdom', 'Charisma'
text_images = []
for ability in ability_scores:
    text_images.append(normal_font.render(ability, True, BLACK))

scores = {'strength': 13, 'dexterity': 9, 'constitution': 10, 'intelligence': 18, 'widsom': 17, 'charisma': 14}
score_images = []
for ability, score in scores.items():
    score_images.append(shadow_font.render(str(score), True, BLACK))

pc_image = pg.image.load('../images/allura.png')
bg_image = pg.image.load('../images/bg.jpg')


# Game loop
running = True
while running:
    # keep loop running at the right speed
    clock.tick(FPS)
    # Process input (events)
    for event in pg.event.get():
        # check for closing window
        if event.type == pg.QUIT:
            running = False

    # Update
    font_loc = 10
    score_loc = 10
    circle_loc = 35

    # Draw / render
    screen.fill(BLACK)
    screen.blit(bg_image,(0,0))
    for image in text_images:
        screen.blit(image, (10,font_loc))
        font_loc += 50
        pg.draw.circle(screen, WHITE, (230,circle_loc), 25)
        circle_loc += 50
    for image in score_images:
        screen.blit(image, (210, score_loc))
        score_loc += 50

    screen.blit(pc_image, (300,10))

    # *after* drawing everything, flip the display
    pg.display.flip()

pg.quit()