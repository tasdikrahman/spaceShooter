#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: tasdik
# @Contributers : Branden (Github: @bardlean86)
# @Date:   2016-01-17
# @Email:  prodicus@outlook.com  Github: @tasdikrahman
# @Last Modified by:   tasdik
# @Last Modified by:   Branden
# @Last Modified by:   Dic3
# @Last Modified time: 2016-10-16
# MIT License. You can find a copy of the License @ http://prodicus.mit-license.org

## Game music Attribution
##Frozen Jam by tgfcoder <https://twitter.com/tgfcoder> licensed under CC-BY-3 <http://creativecommons.org/licenses/by/3.0/>

## Additional assets by: Branden M. Ardelean (Github: @bardlean86)

from __future__ import division
import pygame
import random
from pykeyboard import PyKeyboard
from os import path
from time import sleep

## assets folder
img_dir = path.join(path.dirname(__file__), 'assets')
sound_folder = path.join(path.dirname(__file__), 'sounds')

###############################
## to be placed in "constant.py" later

GENERATIONCOUNT = 10 #The rate at which we kill off datasets
prevFitness = 0
genCount = 0
alphaScore = 0
NODENUM = 20
datOffSet = 0 #This will move with the player to insure learning based on the position of the player
species = 0
xnodePos = [[0 for x in range(NODENUM)] for y in range(NODENUM*3)]
ynodePos = [[0 for x in range(NODENUM)] for y in range(NODENUM*3)]
nodePos = list(zip(xnodePos,ynodePos))
shootDataSet = [[[False for z in range(NODENUM)] for y in range(NODENUM*3)] for x in range(GENERATIONCOUNT)]
leftDataSet = [[[False for z in range(NODENUM)] for y in range(NODENUM*3)] for x in range(GENERATIONCOUNT)]
rightDataSet = [[[False for z in range(NODENUM)] for y in range(NODENUM*3)] for x in range(GENERATIONCOUNT)]
alphaDataSet = [[[False for z in range(NODENUM)] for y in range(NODENUM*3)] for x in range(3)]
prevAlphaDataSet = [[[False for z in range(NODENUM)] for y in range(NODENUM*3)] for x in range(3)]
neatNodes = [[0 for x in range(NODENUM)] for y in range(NODENUM*3)]
WIDTH = 600
HEIGHT = 1080
GAMEHEIGHT = 600
FPS = 60
POWERUP_TIME = 5000
BAR_LENGTH = 100
BAR_HEIGHT = 10

# Define Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
for x in range(0, NODENUM):
    for y in range(0, NODENUM):
        if (x % 2 == 0):
            neatNodes[x][y] = GREEN
        else:
            neatNodes[x][y] = BLUE

###############################

###############################
## to placed in "__init__.py" later
## initialize pygame and create window
pygame.init()
pygame.mixer.init()  ## For sound
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Shooter")
clock = pygame.time.Clock()     ## For syncing the FPS
###############################

font_name = pygame.font.match_font('arial')

def main_menu():
    global screen

    menu_song = pygame.mixer.music.load(path.join(sound_folder, "menu.ogg"))
    pygame.mixer.music.play(-1)

    title = pygame.image.load(path.join(img_dir, "main.png")).convert()
    title = pygame.transform.scale(title, (WIDTH, HEIGHT), screen)

    screen.blit(title, (0,0))
    pygame.display.update()

    while True:
        ev = pygame.event.poll()
        if ev.type == pygame.KEYDOWN:
            if ev.key == pygame.K_RETURN:
                break
            elif ev.key == pygame.K_q:
                pygame.quit()
                quit()
        elif ev.type == pygame.QUIT:
                pygame.quit()
                quit()
        else:
            draw_text(screen, "Press [ENTER] To Begin", 30, WIDTH/2, HEIGHT/2)
            draw_text(screen, "or [Q] To Quit", 30, WIDTH/2, (HEIGHT/2)+40)
            pygame.display.update()

    #pygame.mixer.music.stop()
    pygame.display.update()

def draw_neat(surf, size, x, y):
    for z in range(NODENUM, NODENUM*2):
        for c in range(0, NODENUM):
            pygame.draw.rect(screen, neatNodes[z][c], pygame.Rect(x + z * size, y + c * size, size, size))
            xnodePos[z][c] = x + z * size
            ynodePos[z][c] = y + c * size
    nodePos = list(zip(xnodePos,ynodePos))

def draw_neurons(surf,size, x, y):
    #Drawing Behaviour Circles
    draw_text(surf, "Left()", 15, x + 60, y - 10)
    pygame.draw.circle(screen, RED, (int(x), int(y)),size, 5)
    draw_text(surf, "Shoot()", 15, x + 60 , y - 70)
    pygame.draw.circle(screen, RED, (int(x), int(y) - 60),size, 5)
    draw_text(surf, "Right()", 15, x + 60, y -130)
    pygame.draw.circle(screen, RED, (int(x), int(y) - 120),size, 5)

    draw_text(screen, "Previous Fitness", 15, WIDTH/2, HEIGHT/2 +120)
    draw_text(screen, str(prevFitness), 15, WIDTH/2, HEIGHT/2 +150)

    draw_text(screen, "Fitness", 15, WIDTH/2 + 100, HEIGHT/2 +120)
    draw_text(screen, str(score), 15, WIDTH/2 + 100, HEIGHT/2 +150)

    draw_text(screen, "Species", 15, WIDTH/2 - 100, HEIGHT/2 +120)
    draw_text(screen, str(species), 15, WIDTH/2 - 100, HEIGHT/2 +150)

    draw_text(screen, "Alpha", 15, WIDTH/2 + 200, HEIGHT/2 +120)
    draw_text(screen, str(alphaScore), 15, WIDTH/2 + 200, HEIGHT/2 +150)

    draw_text(screen, "Gen", 15, WIDTH/2 - 200, HEIGHT/2 +120)
    draw_text(screen, str(genCount + 1), 15, WIDTH/2 - 200, HEIGHT/2 +150)

    #Drawing Combinations
    pygame.draw.circle(screen, RED, (int(x) - 50, int(y) - 30),int(size/1.5), 5)
    pygame.draw.circle(screen, RED, (int(x) - 50, int(y) - 90),int(size/1.5), 5)
    #Drawing Final Combination
    pygame.draw.circle(screen, RED, (int(x) - 90, int(y) - 60),int(size/2), 5)
    #Drawing Connections
    for c in range(NODENUM - datOffSet, NODENUM * 2 - datOffSet):
        for k in range(0, NODENUM):
            if(leftDataSet[species][c][k] and rightDataSet[species][c][k]):
                pygame.draw.line(surf, YELLOW, (int(x), int(y)), (int(x) - 50, int(y) - 30), 1)
                pygame.draw.line(surf, YELLOW, (int(x), int(y) - 120), (int(x) - 50, int(y) - 30), 1)
                pygame.draw.line(surf, YELLOW, (int(x), int(y)), (int(x) - 50, int(y) - 90), 1)
                pygame.draw.line(surf, YELLOW, (int(x), int(y) - 120), (int(x) - 50, int(y) - 90), 1)
                pygame.draw.line(surf, YELLOW, (int(x) - 50, int(y) - 30), (xnodePos[c+datOffSet][k], ynodePos[c+datOffSet][k]), 1)
                pygame.draw.line(surf, YELLOW, (int(x) - 50, int(y) - 90), (xnodePos[c+datOffSet][k], ynodePos[c+datOffSet][k]), 1)
            #elif(leftDataSet[species][c][k] and shootDataSet[species][c][k]):


            else:
                if (leftDataSet[species][c][k] == True):
                    pygame.draw.line(surf, YELLOW, (int(x), int(y)), (xnodePos[c+datOffSet][k], ynodePos[c+datOffSet][k]), 1)
                if (shootDataSet[species][c][k] == True):
                    pygame.draw.line(surf, YELLOW, (int(x), int(y) - 60), (xnodePos[c+datOffSet][k], ynodePos[c+datOffSet][k]), 1)
                if (rightDataSet[species][c][k] == True):
                    pygame.draw.line(surf, YELLOW, (int(x), int(y) - 120), (xnodePos[c+datOffSet][k], ynodePos[c+datOffSet][k]), 1)

def draw_text(surf, text, size, x, y):
    ## selecting a cross platform font to display the score
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, WHITE)       ## True denotes the font to be anti-aliased
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)


def draw_shield_bar(surf, x, y, pct):
    # if pct < 0:
    #     pct = 0
    pct = max(pct, 0)
    ## moving them to top
    # BAR_LENGTH = 100
    # BAR_HEIGHT = 10
    fill = (pct / 100) * BAR_LENGTH
    outline_rect = pygame.Rect(x, y, BAR_LENGTH, BAR_HEIGHT)
    fill_rect = pygame.Rect(x, y, fill, BAR_HEIGHT)
    pygame.draw.rect(surf, GREEN, fill_rect)
    pygame.draw.rect(surf, WHITE, outline_rect, 2)


def draw_lives(surf, x, y, lives, img):
    for i in range(lives):
        img_rect= img.get_rect()
        img_rect.x = x + 30 * i
        img_rect.y = y
        surf.blit(img, img_rect)

def checkAlpha():
    if (score > prevFitness):
        alphaScore = score
        print(alphaScore)
        for x in range(NODENUM, NODENUM * 2):
            for y in range(0, NODENUM):
                alphaDataSet[0][x][y] = leftDataSet[species][x][y]
                alphaDataSet[1][x][y] = rightDataSet[species][x][y]
                alphaDataSet[2][x][y] = shootDataSet[species][x][y]

def breedAlpha():
    offspring = [[[False for z in range(NODENUM)] for y in range(NODENUM*3)] for x in range(3)]
    for x in range(NODENUM, NODENUM * 2):
        for y in range(0, NODENUM):
            if (alphaDataSet[0][x][y] and y % 2 == 0):
                offspring[0][x][y] = True
            if (alphaDataSet[1][x][y] and y % 2 == 0):
                offspring[1][x][y] = True
            if (alphaDataSet[2][x][y] and y % 2 == 0):
                offspring[2][x][y] = True
            if (prevAlphaDataSet[0][x][y] and y % 2 != 0):
                offspring[0][x][y] = True
            if (prevAlphaDataSet[1][x][y] and y % 2 != 0):
                offspring[1][x][y] = True
            if (prevAlphaDataSet[2][x][y] and y % 2 != 0):
                offspring[2][x][y] = True
    leftDataSet[0] = offspring[0]
    shootDataSet[0] = offspring[1]
    rightDataSet[0] = offspring[2]



def moveLeftForN(keyboard):
    keyboard.press_key("Left")
    keyboard.release_key("Left")

def moveRightForN(keyboard):
    keyboard.press_key("Right")
    keyboard.release_key("Right")

def newmob():
    mob_element = Mob()
    all_sprites.add(mob_element)
    mobs.add(mob_element)

def act():
    for x in range(NODENUM, NODENUM * 2):
        for y in range(0, NODENUM):
            if (neatNodes[x+datOffSet][y] == GREEN and leftDataSet[species][x+datOffSet][y] == True):
                moveLeftForN(keyboard)
            if (neatNodes[x+datOffSet][y] == GREEN and rightDataSet[species][x+datOffSet][y] == True):
                moveRightForN(keyboard)
            if (neatNodes[x+datOffSet][y] == GREEN and shootDataSet[species][x+datOffSet][y] == True):
                player.shoot()

class Explosion(pygame.sprite.Sprite):
    def __init__(self, center, size):
        pygame.sprite.Sprite.__init__(self)
        self.size = size
        self.image = explosion_anim[self.size][0]
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.frame = 0
        self.last_update = pygame.time.get_ticks()
        self.frame_rate = 75

    def update(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > self.frame_rate:
            self.last_update = now
            self.frame += 1
            if self.frame == len(explosion_anim[self.size]):
                self.kill()
            else:
                center = self.rect.center
                self.image = explosion_anim[self.size][self.frame]
                self.rect = self.image.get_rect()
                self.rect.center = center


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        ## scale the player img down
        self.image = pygame.transform.scale(player_img, (50, 38))
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.radius = 20
        self.rect.centerx = WIDTH / 2
        self.rect.bottom = GAMEHEIGHT - 40
        self.speedx = 0
        self.shield = 100
        self.shoot_delay = 250
        self.last_shot = pygame.time.get_ticks()
        self.lives = 1 #changed lives to 1 to make neuro evolution faster
        self.hidden = False
        self.hide_timer = pygame.time.get_ticks()
        self.power = 1
        self.power_timer = pygame.time.get_ticks()

    def update(self):
        ## time out for powerups
        if self.power >=2 and pygame.time.get_ticks() - self.power_time > POWERUP_TIME:
            self.power -= 1
            self.power_time = pygame.time.get_ticks()

        ## unhide
        if self.hidden and pygame.time.get_ticks() - self.hide_timer > 1000:
            self.hidden = False
            self.rect.centerx = WIDTH / 2
            self.rect.bottom = GAMEHEIGHT - 30

        self.speedx = 0     ## makes the player static in the screen by default.
        # then we have to check whether there is an event hanlding being done for the arrow keys being
        ## pressed

        ## will give back a list of the keys which happen to be pressed down at that moment
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
            self.moveLeft()
        elif keystate[pygame.K_RIGHT]:
            self.moveRight()

        #Fire weapons by holding spacebar
        if keystate[pygame.K_SPACE]:
            self.shoot()

        ## check for the borders at the left and right
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0

        self.rect.x += self.speedx

    def moveRight(self):
        self.speedx += 10
    def moveLeft(self):
        self.speedx += -10

    def shoot(self):
        ## to tell the bullet where to spawn
        now = pygame.time.get_ticks()
        if now - self.last_shot > self.shoot_delay:
            self.last_shot = now
            if self.power == 1:
                bullet = Bullet(self.rect.centerx, self.rect.top)
                all_sprites.add(bullet)
                bullets.add(bullet)
                shooting_sound.play()
            if self.power == 2:
                bullet1 = Bullet(self.rect.left, self.rect.centery)
                bullet2 = Bullet(self.rect.right, self.rect.centery)
                all_sprites.add(bullet1)
                all_sprites.add(bullet2)
                bullets.add(bullet1)
                bullets.add(bullet2)
                shooting_sound.play()

            """ MOAR POWAH """
            if self.power >= 3:
                bullet1 = Bullet(self.rect.left, self.rect.centery)
                bullet2 = Bullet(self.rect.right, self.rect.centery)
                missile1 = Missile(self.rect.centerx, self.rect.top) # Missile shoots from center of ship
                all_sprites.add(bullet1)
                all_sprites.add(bullet2)
                all_sprites.add(missile1)
                bullets.add(bullet1)
                bullets.add(bullet2)
                bullets.add(missile1)
                shooting_sound.play()
                missile_sound.play()

    def powerup(self):
        self.power += 1
        self.power_time = pygame.time.get_ticks()

    def hide(self):
        self.hidden = True
        self.hide_timer = pygame.time.get_ticks()
        self.rect.center = (WIDTH / 2, GAMEHEIGHT + 200)


# defines the enemies
class Mob(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image_orig = random.choice(meteor_images)
        self.image_orig.set_colorkey(BLACK)
        self.image = self.image_orig.copy()
        self.rect = self.image.get_rect()
        self.radius = int(self.rect.width *.90 / 2)
        self.rect.x = random.randrange(0, WIDTH - self.rect.width)
        self.rect.y = random.randrange(-150, -100)
        self.speedy = random.randrange(20, 30)        ## for randomizing the speed of the Mob, INCREASED METEOR SPEED

        ## randomize the movements a little more
        self.speedx = random.randrange(-3, 3)

        ## adding rotation to the mob element
        self.rotation = 0
        self.rotation_speed = random.randrange(-8, 8)
        self.last_update = pygame.time.get_ticks()  ## time when the rotation has to happen

    def rotate(self):
        time_now = pygame.time.get_ticks()
        if time_now - self.last_update > 50: # in milliseconds
            self.last_update = time_now
            self.rotation = (self.rotation + self.rotation_speed) % 360
            new_image = pygame.transform.rotate(self.image_orig, self.rotation)
            old_center = self.rect.center
            self.image = new_image
            self.rect = self.image.get_rect()
            self.rect.center = old_center

    def update(self):
        self.rotate()
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        ## now what if the mob element goes out of the screen

        if (self.rect.top > GAMEHEIGHT + 10) or (self.rect.left < -25) or (self.rect.right > WIDTH + 20):
            self.rect.x = random.randrange(0, WIDTH - self.rect.width)
            self.rect.y = random.randrange(-100, -40)
            self.speedy = random.randrange(1, 8)        ## for randomizing the speed of the Mob

## defines the sprite for Powerups
class Pow(pygame.sprite.Sprite):
    def __init__(self, center):
        pygame.sprite.Sprite.__init__(self)
        self.type = random.choice(['shield', 'gun'])
        self.image = powerup_images[self.type]
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        ## place the bullet according to the current position of the player
        self.rect.center = center
        self.speedy = 2

    def update(self):
        """should spawn right in front of the player"""
        self.rect.y += self.speedy
        ## kill the sprite after it moves over the top border
        if self.rect.top > GAMEHEIGHT:
            self.kill()

## defines the sprite for bullets
class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = bullet_img
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        ## place the bullet according to the current position of the player
        self.rect.bottom = y
        self.rect.centerx = x
        self.speedy = -10

    def update(self):
        """should spawn right in front of the player"""
        self.rect.y += self.speedy
        ## kill the sprite after it moves over the top border
        if self.rect.bottom < 0:
            self.kill()

        ## now we need a way to shoot
        ## lets bind it to "spacebar".
        ## adding an event for it in Game loop

## FIRE ZE MISSILES
class Missile(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = missile_img
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
        self.speedy = -10

    def update(self):
        """should spawn right in front of the player"""
        self.rect.y += self.speedy
        if self.rect.bottom < 0:
            self.kill()


###################################################
## Load all game images

background = pygame.image.load(path.join(img_dir, 'starfield.png')).convert()
background_rect = background.get_rect()
## ^^ draw this rect first

player_img = pygame.image.load(path.join(img_dir, 'playerShip1_orange.png')).convert()
player_mini_img = pygame.transform.scale(player_img, (25, 19))
player_mini_img.set_colorkey(BLACK)
bullet_img = pygame.image.load(path.join(img_dir, 'laserRed16.png')).convert()
missile_img = pygame.image.load(path.join(img_dir, 'missile.png')).convert_alpha()
# meteor_img = pygame.image.load(path.join(img_dir, 'meteorBrown_med1.png')).convert()
meteor_images = []
meteor_list = [
    'meteorBrown_big1.png',
    'meteorBrown_big2.png',
    'meteorBrown_med1.png',
    'meteorBrown_med3.png',
    'meteorBrown_small1.png',
    'meteorBrown_small2.png',
    'meteorBrown_tiny1.png'
]

for image in meteor_list:
    meteor_images.append(pygame.image.load(path.join(img_dir, image)).convert())

## meteor explosion
explosion_anim = {}
explosion_anim['lg'] = []
explosion_anim['sm'] = []
explosion_anim['player'] = []
for i in range(9):
    filename = 'regularExplosion0{}.png'.format(i)
    img = pygame.image.load(path.join(img_dir, filename)).convert()
    img.set_colorkey(BLACK)
    ## resize the explosion
    img_lg = pygame.transform.scale(img, (75, 75))
    explosion_anim['lg'].append(img_lg)
    img_sm = pygame.transform.scale(img, (32, 32))
    explosion_anim['sm'].append(img_sm)

    ## player explosion
    filename = 'sonicExplosion0{}.png'.format(i)
    img = pygame.image.load(path.join(img_dir, filename)).convert()
    img.set_colorkey(BLACK)
    explosion_anim['player'].append(img)

## load power ups
powerup_images = {}
powerup_images['shield'] = pygame.image.load(path.join(img_dir, 'shield_gold.png')).convert()
powerup_images['gun'] = pygame.image.load(path.join(img_dir, 'bolt_gold.png')).convert()


###################################################


###################################################
### Load all game sounds
shooting_sound = pygame.mixer.Sound(path.join(sound_folder, 'pew.wav'))
missile_sound = pygame.mixer.Sound(path.join(sound_folder, 'rocket.ogg'))
expl_sounds = []
for sound in ['expl3.wav', 'expl6.wav']:
    expl_sounds.append(pygame.mixer.Sound(path.join(sound_folder, sound)))
## main background music
#pygame.mixer.music.load(path.join(sound_folder, 'tgfcoder-FrozenJam-SeamlessLoop.ogg'))
pygame.mixer.music.set_volume(0.2)      ## simmered the sound down a little

player_die_sound = pygame.mixer.Sound(path.join(sound_folder, 'rumble1.ogg'))
###################################################

## TODO: make the game music loop over again and again. play(loops=-1) is not working
# Error :
# TypeError: play() takes no keyword arguments
#pygame.mixer.music.play()

#############################
## Game loop
running = True
menu_display = True
while running:
    if menu_display:
        main_menu()
        #pygame.time.wait(3000)

        #Stop menu music
        pygame.mixer.music.stop()
        #Play the gameplay music
        pygame.mixer.music.load(path.join(sound_folder, 'tgfcoder-FrozenJam-SeamlessLoop.ogg'))
        pygame.mixer.music.play(-1)     ## makes the gameplay sound in an endless loop

        menu_display = False

        keyboard = PyKeyboard()

        ## group all the sprites together for ease of update
        all_sprites = pygame.sprite.Group()
        player = Player()
        all_sprites.add(player)

        ## spawn a group of mob
        mobs = pygame.sprite.Group()
        for i in range(8):      ## 8 mobs
            # mob_element = Mob()
            # all_sprites.add(mob_element)
            # mobs.add(mob_element)
            newmob()

        ## group for bullets
        bullets = pygame.sprite.Group()
        powerups = pygame.sprite.Group()

        #### Score board variable
        score = 0

    #1 Process input/events
    clock.tick(FPS)     ## will make the loop run at the same speed all the time
    for event in pygame.event.get():        # gets all the events which have occured till now and keeps tab of them.
        ## listening for the the X button at the top
        if event.type == pygame.QUIT:
            running = False

        ## Press ESC to exit game
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
        # ## event for shooting the bullets
        # elif event.type == pygame.KEYDOWN:
        #     if event.key == pygame.K_SPACE:
        #         player.shoot()      ## we have to define the shoot()  function

    #2 Update
    all_sprites.update()


    ## check if a bullet hit a mob
    ## now we have a group of bullets and a group of mob
    hits = pygame.sprite.groupcollide(mobs, bullets, True, True)
    ## now as we delete the mob element when we hit one with a bullet, we need to respawn them again
    ## as there will be no mob_elements left out
    for hit in hits:
        score += 50 - hit.radius         ## give different scores for hitting big and small metoers
        random.choice(expl_sounds).play()
        # m = Mob()
        # all_sprites.add(m)
        # mobs.add(m)
        expl = Explosion(hit.rect.center, 'lg')
        all_sprites.add(expl)
        if random.random() > 0.9:
            pow = Pow(hit.rect.center)
            all_sprites.add(pow)
            powerups.add(pow)
        newmob()        ## spawn a new mob

    ## ^^ the above loop will create the amount of mob objects which were killed spawn again
    #########################

    ## check if the player collides with the mob
    hits = pygame.sprite.spritecollide(player, mobs, True, pygame.sprite.collide_circle)        ## gives back a list, True makes the mob element disappear
    for hit in hits:
        player.shield = 0#hit.radius * 2
        expl = Explosion(hit.rect.center, 'sm')
        all_sprites.add(expl)
        newmob()
        if player.shield <= 0:
            player_die_sound.play()
            death_explosion = Explosion(player.rect.center, 'player')
            all_sprites.add(death_explosion)
            # running = False     ## GAME OVER 3:D
            player.hide()
            player.lives -= 1
            player.shield = 100

    ## if the player hit a power up
    hits = pygame.sprite.spritecollide(player, powerups, True)
    for hit in hits:
        if hit.type == 'shield':
            player.shield += random.randrange(10, 30)
            if player.shield >= 100:
                player.shield = 100
        if hit.type == 'gun':
            player.powerup()

    ## if player died and the explosion has finished, end game
    if player.lives == 0:
        checkAlpha()
        prevFitness = score
        score = 0
        if (species >= GENERATIONCOUNT - 1):
            genCount += 1
            species = 0
            alphaScore = 0
            breedAlpha()
            prevAlphaDataSet = alphaDataSet
        species += 1
        player.lives +=1
        try:
            leftDataSet[species][random.randint(NODENUM+1,NODENUM*3)][random.randint(0, NODENUM)] = True
            leftDataSet[species][random.randint(NODENUM+1,NODENUM*3)][random.randint(0, NODENUM)] = False
            rightDataSet[species][random.randint(NODENUM+1,NODENUM*3)][random.randint(0, NODENUM)] = True
            rightDataSet[species][random.randint(NODENUM+1,NODENUM*3)][random.randint(0, NODENUM)] = False
            shootDataSet[species][random.randint(NODENUM+1,NODENUM*3)][random.randint(0, NODENUM)] = True
            shootDataSet[species][random.randint(NODENUM+1,NODENUM*3)][random.randint(0, NODENUM)] = False
        except: IndexError
        #running = False
        # menu_display = True
        pygame.display.update()
        if (prevFitness == 0):
            moveRightForN(keyboard)

    #3 Draw/render
    screen.fill(BLACK)
    ## draw the stargaze.png image
    screen.blit(background, background_rect)

    all_sprites.draw(screen)

    for x in range(NODENUM, NODENUM*2):
        for y in range(NODENUM):
            if (player.rect.center[0] > WIDTH/NODENUM * (x - NODENUM) and player.rect.center[0] < WIDTH/NODENUM * ((x -NODENUM)+1)): #if player collides with a hitbox
                neatNodes[x][NODENUM-1] = RED
                datOffSet= x - NODENUM * 2
            else:
                neatNodes[x][NODENUM-1] = BLUE
            for z in range(len(mobs.sprites())):
                if (mobs.sprites()[z].rect.center[0] > WIDTH/NODENUM * (x - NODENUM) and mobs.sprites()[z].rect.center[0] < WIDTH/NODENUM * ((x -NODENUM)+1) and mobs.sprites()[z].rect.center[1] > WIDTH/NODENUM * (y-1) and mobs.sprites()[z].rect.center[1] < WIDTH/NODENUM * y):
                    neatNodes[x][y] = GREEN
                elif(neatNodes[x][y] != RED):
                    neatNodes[x][y] = BLUE
                if(neatNodes[x][y] == GREEN):
                    break;

    size = 10
    draw_neat(screen, size, WIDTH / 2 - 500, (GAMEHEIGHT + HEIGHT)/2 - 100)
    draw_neurons(screen, 20, WIDTH/2 + 200, (GAMEHEIGHT + HEIGHT)/2 + 50)
    draw_text(screen, str(score), 18, WIDTH / 2, 10)     ## 10px down from the screen
    draw_shield_bar(screen, 5, 5, player.shield)
    act()

    # Draw lives
    draw_lives(screen, WIDTH - 100, 5, player.lives, player_mini_img)

    ## Done after drawing everything to the screen
    pygame.display.flip()

pygame.quit()
