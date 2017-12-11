#/uvsr/bin/env python
# -*- coding: utf-8 -*-
# @Author: tasdik
# @Contributers : Branden (Github: @bardlean86)
# @Date:   2016-01-17
# @Email:  prodicus@outlook.com  Github: @tasdikrahman
# @Last Modified by:   tasdik
# @Last Modified by:   Branden
# @Last Modified time: 2016-01-26
# MIT License. You can find a copy of the License @ http://prodicus.mit-license.org

## Game music Attribution
##Frozen Jam by tgfcoder <https://twitter.com/tgfcoder> licensed under CC-BY-3 <http://creativecommons.org/licenses/by/3.0/>

## Additional assets by: Branden M. Ardelean (Github: @bardlean86)

from __future__ import division
import pygame
import random
from os import path

## assets folder
## 게임에 필요한 이미지, 사운드 파일이 들어있는 파일을 불러온다
img_dir = path.join(path.dirname(__file__), 'assets')
sound_folder = path.join(path.dirname(__file__), 'sounds')

###############################
## to be placed in "constant.py" later
## 게임이 실행될때 화면의 초기 설정
WIDTH = 480
HEIGHT = 600
FPS = 60
POWERUP_TIME = 5000
BAR_LENGTH = 100
BAR_HEIGHT = 10

## 게임에 쓰이는 색들을 정의 되어있는 부분
# Define Colors 
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
###############################

###############################
## to placed in "__init__.py" later
## initialize pygame and create window
pygame.init() ## pygame초기화 부분
pygame.mixer.init()  ## For sound ## pygame sound 초기화
screen = pygame.display.set_mode((WIDTH, HEIGHT)) ## 화면을 설정 
pygame.display.set_caption("Space Shooter") ## 위도우 창의 위 부분의 제목 
clock = pygame.time.Clock()     ## For syncing the FPS ##FPS 감도 설정?? 이부분은 검색이 필요할듯
###############################

## 글자 폰트 설정
font_name = pygame.font.match_font('arial')

## 메인 메뉴를 구현한 함수
def main_menu():
    ## 스크린을 전역 변수로 선언
    global screen
    
	## 처음 시작하고 페이지 화면의 음악
    menu_song = pygame.mixer.music.load(path.join(sound_folder, "menu.ogg"))
	## 소리에 관하여 처리해주는 
    pygame.mixer.music.play(-1)
	
	## 메인 이미지를 로드
    title = pygame.image.load(path.join(img_dir, "main.png")).convert()
    ## 스크린 설정 
    title = pygame.transform.scale(title, (WIDTH, HEIGHT), screen)
	
	## 스크린에 그려준다.
    screen.blit(title, (0,0))
	## >?? 검색 필요
    pygame.display.update()
	
	## 무한정으로 입령이 들어올때까지 반복하는 반복문
    while True:
		## 입력받은 이벤트를 ev에 저장
        ev = pygame.event.poll()
		## 입력이 생기면 if문 안으로 들어가고 안하면 else로 들어감
        if ev.type == pygame.KEYDOWN:
			## 입력이 생기면 입력 받은 키가 엔터이면 while문을 빠져나간다
            if ev.key == pygame.K_RETURN:
                break
			## 이력된 키가 q이면 게임을 끝낸다
            elif ev.key == pygame.K_q:
                pygame.quit()
                quit()
		## 입력이 없으면 안내문을 뛰워주고 스크리을 업데이트 해준다.
        else:
            draw_text(screen, "Press [ENTER] To Begin", 30, WIDTH/2, HEIGHT/2)
            draw_text(screen, "or [Q] To Quit", 30, WIDTH/2, (HEIGHT/2)+40)
            pygame.display.update()
	
	## while문을 빠져나오면 
    #pygame.mixer.music.stop()
	## 음악을 바꿔주고 플레이한다
    ready = pygame.mixer.Sound(path.join(sound_folder,'getready.ogg'))
    ready.play()
	## 화면을 검정색으로 만들고
    screen.fill(BLACK)
	## get ready 문구를 뛰워준다
    draw_text(screen, "GET READY!", 40, WIDTH/2, HEIGHT/2)
	## 화면을 업데이트 해준다
    pygame.display.update()

## main_menu 함수는일단 게임의 첫페이지를 담당하고 있고 사운드가 플레이되고 사용자의 입력(이벤트)를 기다리고 있다.
## 실행을 하지 말지 결정하는 단계이다.
    
## 텍스트를 그리는 함수
def draw_text(surf, text, size, x, y):
    ## selecting a cross platform font to display the score
	## 폰트 , 사이즈를 설정
    font = pygame.font.Font(font_name, size)
	## 폰트를 흰색으로 렌더 하고 anti-aliasesd를 사용 
    text_surface = font.render(text, True, WHITE)       ## True denotes the font to be anti-aliased 
    ## 가상의 폰트가 들어가는 사각형을 할당하고 사각형을 위치하고
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
	## 화면에 텍스트를 그린다
    surf.blit(text_surface, text_rect)


## 플레이어 우주선에  쉴드 게이지를 나타네는 바
def draw_shield_bar(surf, x, y, pct):
    # if pct < 0:
    #     pct = 0
	## >>>>??pct
    pct = max(pct, 0) 
    ## moving them to top
    # BAR_LENGTH = 100
    # BAR_HEIGHT = 10
	## 얼마나 채워져있는지 
	## 바의 크기를
    fill = (pct / 100) * BAR_LENGTH
	## outline_rect 쉴드 게이지 바의 아웃라인을 그려준다
    outline_rect = pygame.Rect(x, y, BAR_LENGTH, BAR_HEIGHT)
	## 쉘드게이지바가 얼마나 채워졌는지
    fill_rect = pygame.Rect(x, y, fill, BAR_HEIGHT)
	## 쉘드게이지바를 그려주고
    pygame.draw.rect(surf, GREEN, fill_rect)
	## 아웃라인을 그려주고
    pygame.draw.rect(surf, WHITE, outline_rect, 2)


## 플레이어 생명 수
def draw_lives(surf, x, y, lives, img):
    ## 생명 수 만큼 아이톤을 출력해준다
    for i in range(lives):
		## 이미지를 넣어주고
        img_rect= img.get_rect()
		##  x의 위치를 설정
        img_rect.x = x + 30 * i
		## y의 위치를 설졍
        img_rect.y = y
		## 화면에 그려준다
        surf.blit(img, img_rect)


## 장해물??
def newmob():
    ## 장해물을 생성하는 것 같음
    mob_element = Mob()
    ## 
    all_sprites.add(mob_element)
    mobs.add(mob_element)

## 폭발하는 기능을 보여주는 class 
class Explosion(pygame.sprite.Sprite):
    #pygame.sprite.Sprite는 object를 화면에 보이게 하는 class
    # init은 초기화는거 생성자 같은거
    def __init__(self, center, size):
		##pygame.sprite.Sprite을 초기화
        pygame.sprite.Sprite.__init__(self)
		## 사이즈를 설정
        self.size = size
		## 폭발하는 이미지 설정
        self.image = explosion_anim[self.size][0]
		## 이미지의 사각형을 설정
        self.rect = self.image.get_rect()
		## 사각형의 중앙을 잠고
        self.rect.center = center
		##??
        self.frame = 0 
		## 업데이트를 해주고
        self.last_update = pygame.time.get_ticks()
    
        self.frame_rate = 75
	## 초기화한 걸로 update
    def update(self):
        ## 시간을 넣어줌 
        now = pygame.time.get_ticks()
        ## last_update 이해가 안감
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

## 플레이어 
class Player(pygame.sprite.Sprite):
    ##플레이어를 초기화해준다
    def __init__(self):
        ## 앞에 뛰어주는 걸 초기화
        pygame.sprite.Sprite.__init__(self)
        ## scale the player img down
        ## 우준선 이미지를 가지고오다
        ## 이미지의 크기를 다시 설정해준다
        self.image = pygame.transform.scale(player_img, (50, 38))
        ## 이미지의 키 값을 블랙으로 설정한다
        self.image.set_colorkey(BLACK)
        ## 이미지의 사각형의 크기를 받아오고
        self.rect = self.image.get_rect()
        ## 반지름을 20으로 설정
        self.radius = 20
        ## 사각형의 중심 x 좌표
        self.rect.centerx = WIDTH / 2
        ## 사각형의 밑부분을 설정
        self.rect.bottom = HEIGHT - 10
        ## ?? 이거 정말 모르겠다
        ## 속도값
        self.speedx = 0 
        ## 쉴드 게이지를 설정
        self.shield = 100
        ## 발사체가 나가는데 딜레이
        self.shoot_delay = 250
        ## 마지막으로 발사한 발사채의 발사시간
        self.last_shot = pygame.time.get_ticks()
        ## 생명
        self.lives = 3
        ##??? 처음에 죽고나서 잠깐 히든?? 되는건?
        self.hidden = False
        ## 히든 되어있는 시간을 설정
        self.hide_timer = pygame.time.get_ticks()
        ## 파워 아이템을 먹은 개수... 처음에는 1로 초기화
        self.power = 1
        ## 파워의 지속 시간
        self.power_timer = pygame.time.get_ticks()

    ## player의 객체를 업데이트 하는거
    def update(self):
        
        ## time out for powerups
        ## 파워를 먹고 시간이 지나면 파워를 하나를 깍는다
        if self.power >=2 and pygame.time.get_ticks() - self.power_time > POWERUP_TIME:
            self.power -= 1
            ## 파워 시간을 다시초기화
            self.power_time = pygame.time.get_ticks()

        ## 히든이 왜있는거지??
        ## 잘모르겠당///
        ## 히든 되고 나서 몇초있다 히든이 풀리는 부분을 제어하는것 같다.
        ## unhide 
        if self.hidden and pygame.time.get_ticks() - self.hide_timer > 1000:
            self.hidden = False
            self.rect.centerx = WIDTH / 2
            self.rect.bottom = HEIGHT - 30
        
        ##??????????????????????
        ## 위치 해있는 좌표를 0으로 초기화하는 것 같음
        self.speedx = 0     ## makes the player static in the screen by default. 
        # then we have to check whether there is an event hanlding being done for the arrow keys being 
        ## pressed 

        ## 키에 따라 반응 업데이트 하는 부분
        ## will give back a list of the keys which happen to be pressed down at that moment
        ## 무슨 키를 눌렀는지 Keystate에 저장
        keystate = pygame.key.get_pressed()
        ## LEFT는 -5만큼 이동     
        if keystate[pygame.K_LEFT]:
            self.speedx = -5
        ## RIGHT는 5만큼 이동
        elif keystate[pygame.K_RIGHT]:
            self.speedx = 5

        ## 스페이를 눌렀으면 발사체 발사
        #Fire weapons by holding spacebar
        if keystate[pygame.K_SPACE]:
            self.shoot()

        ##  ???? 이부분은 잘모르겠음
        ## check for the borders at the left and right
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0

        ## 이미지를 움직인 만큼 옮겨준다
        self.rect.x += self.speedx

    ## 발사하는 함수
    def shoot(self):
        ## 시간을 업데이트 하고
        ## to tell the bullet where to spawn
        now = pygame.time.get_ticks()
        ## 마지막으로 쏜 시간과 현재시간을 빼서 딜레이 만큼 지났으면 발살체를 발사하는 효과로 넘어가게 해준다
        if now - self.last_shot > self.shoot_delay:
            ##마지막 발사 시간을 업데이트 해준다.
            self.last_shot = now
            ## 우주선의 파워가 1일면
            if self.power == 1:
                ## 발사체의 위치를 설정해준다
                bullet = Bullet(self.rect.centerx, self.rect.top)
                ## 화면에 보여지게 하는 부분에 설정해주고
                all_sprites.add(bullet)
                ## ???
                bullets.add(bullet)
                ## 소리를 플레이해준다
                shooting_sound.play()
            ## 파워 2개
            if self.power == 2:
                bullet1 = Bullet(self.rect.left, self.rect.centery)
                bullet2 = Bullet(self.rect.right, self.rect.centery)
                all_sprites.add(bullet1)
                all_sprites.add(bullet2)
                bullets.add(bullet1)
                bullets.add(bullet2)
                shooting_sound.play()

            ## 파워 3개 
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
    ## 파워 아이템을 먹었을때 
    def powerup(self):
        self.power += 1
        self.power_time = pygame.time.get_ticks()
    ## 죽었다 다시 살았을때??
    ## 그런것 같음..
    def hide(self):
        self.hidden = True
        self.hide_timer = pygame.time.get_ticks()
        self.rect.center = (WIDTH / 2, HEIGHT + 200)

# 장애물에 대한 정보저장
# defines the enemies
class Mob(pygame.sprite.Sprite):
    #mob class에 현재 게임 화면에 대한 정보를 줌
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        ##게임화면에 몹에대한정보를 초기화시켜주고
        self.image_orig = random.choice(meteor_images)
        ##운석의 이미지를 랜덤으로 지정
        self.image_orig.set_colorkey(BLACK)
        ##운석의base color를 검정으로설정
        self.image = self.image_orig.copy()
        ##몹클래스에 아까받은 이미지를 복사
        self.rect = self.image.get_rect()
        self.radius = int(self.rect.width *.90 / 2)
        self.rect.x = random.randrange(0, WIDTH - self.rect.width)
        self.rect.y = random.randrange(-150, -100)
        self.speedy = random.randrange(5, 20)        ## for randomizing the speed of the Mob
        ##몹의 이동속도를 조정

        ## 몹의이동경로를 더자세하게 표현하기위함? 
        self.speedx = random.randrange(-3, 3)

        ## 몹의위치와새로운몹을만들어냄
        self.rotation = 0
        self.rotation_speed = random.randrange(-8, 8)
        self.last_update = pygame.time.get_ticks()  ## time when the rotation has to happen
        
    def rotate(self):
        time_now = pygame.time.get_ticks()
        ##진행된게임시간을불러옴??
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
        ##몹들을 이동시킴

        if (self.rect.top > HEIGHT + 10) or (self.rect.left < -25) or (self.rect.right > WIDTH + 20):
            self.rect.x = random.randrange(0, WIDTH - self.rect.width)
            self.rect.y = random.randrange(-100, -40)
            self.speedy = random.randrange(1, 8)        ## for randomizing the speed of the Mob
        ##몹의이동스피드도랜덤으로설정하게함
## 폭팔관련클래스(터지는효과)
## defines the sprite for Powerups
class Pow(pygame.sprite.Sprite):
    def __init__(self, center):
        pygame.sprite.Sprite.__init__(self)
        ##화면에클래스연동
        self.type = random.choice(['shield', 'gun'])
        ##타입에 shield나 gun을랜덤으로추가해줌
        self.image = powerup_images[self.type]
        ##이미지추가
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        ## place the bullet according to the current position of the player
        self.rect.center = center
        ##가운데에위치시킴
        self.speedy = 2
        ##속도를2로조정

    ##바뀐정보를 업데이트 해 줌
    def update(self):
        """should spawn right in front of the player"""
        self.rect.y += self.speedy
        ## kill the sprite after it moves over the top border
        if self.rect.top > HEIGHT:
            self.kill()

    ##만약 화면의끝에 폭팔이닿으면 현재의것을 없앤다??    


##날아다니는총알에대한정보
## defines the sprite for bullets
class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        ##총알을 초기화 시켜주고
        pygame.sprite.Sprite.__init__(self)
        self.image = bullet_img
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        ## place the bullet according to the current position of the player
        self.rect.bottom = y 
        self.rect.centerx = x
        ##날아갈위치를정해주고
        self.speedy = -10
        ##위방향으로 10의속도로 진행
        
    ##바뀐내용을업데이트
    def update(self):
        """should spawn right in front of the player"""
        self.rect.y += self.speedy
        ##x좌표는 고정 시키고 y좌표만 이동시킨다.
        ## kill the sprite after it moves over the top border
        if self.rect.bottom < 0:
            self.kill()
        ##만약총알이화면끝에닿으면총알제거
        ## now we need a way to shoot
        ## lets bind it to "spacebar".
        ## adding an event for it in Game loop


##미사일에대한정보가담겨있음
## FIRE ZE MISSILES
class Missile(pygame.sprite.Sprite):
    def __init__(self, x, y):
        ##초기화에관한내용
        pygame.sprite.Sprite.__init__(self)
        self.image = missile_img
        ##미사일의 이미지를 추가한다.
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        ##미사일의 발사 위치를 설정하고
        self.rect.bottom = y
        self.rect.centerx = x
        ##위로10의 속도 만큼 진행시킨다.
        self.speedy = -10
    ##다시그려줌. bullet클래스의내용과동일.
    def update(self):
        """should spawn right in front of the player"""
        self.rect.y += self.speedy
        if self.rect.bottom < 0:
            self.kill()


###################################################
## Load all game images
##게임 이미지를 로드하기 위한 부분.

background = pygame.image.load(path.join(img_dir, 'starfield.png')).convert()
background_rect = background.get_rect()
## ^^ draw this rect first 
##배경화면불러오기
player_img = pygame.image.load(path.join(img_dir, 'playerShip1_orange.png')).convert()
##플레이어이미지를불러옴
player_mini_img = pygame.transform.scale(player_img, (25, 19))
##위에뜨는목숨에관한정보
##플레이어이미지를축소화시키고 목숨의개수만큼불러오기위해 저렇게만든듯?
player_mini_img.set_colorkey(BLACK)
bullet_img = pygame.image.load(path.join(img_dir, 'laserRed16.png')).convert()
##레이저이미지
missile_img = pygame.image.load(path.join(img_dir, 'missile.png')).convert_alpha()
#미사일이미지
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
##운석의이미지인데 랜덤으로불러오기위해배열을사용
for image in meteor_list:
    meteor_images.append(pygame.image.load(path.join(img_dir, image)).convert())
##모든이미지를로드함
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
##게임사운드를 불러옴.
shooting_sound = pygame.mixer.Sound(path.join(sound_folder, 'pew.wav'))##발사할때마다불러오는듯
missile_sound = pygame.mixer.Sound(path.join(sound_folder, 'rocket.ogg'))##미사일발사할때.
expl_sounds = []
for sound in ['expl3.wav', 'expl6.wav']:##폭팔사운드인듯
    expl_sounds.append(pygame.mixer.Sound(path.join(sound_folder, sound)))
## main background music
#pygame.mixer.music.load(path.join(sound_folder, 'tgfcoder-FrozenJam-SeamlessLoop.ogg'))
pygame.mixer.music.set_volume(0.2)      ## simmered the sound down a little
##사운드의크기를작게..

##죽을때 소리ㅋ
player_die_sound = pygame.mixer.Sound(path.join(sound_folder, 'rumble1.ogg'))
###################################################

## group all the sprites together for ease of update
all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)
##이모든정보를 초기화시키는역할인듯?(화면에 java frame 같은역할인가..)
## spawn a group of mob
##몹을랜덤으로생성함(운석)
score = 0

mobs = pygame.sprite.Group()
init_count = 2
for i in range(init_count):      ## 2 mobs
    newmob()
##총알하고 파워업에대한배열
## group for bullets ,
bullets = pygame.sprite.Group()
powerups = pygame.sprite.Group()
##점수. 당연히 0점부터시작.
#### Score board variable

level = 0

## TODO: make the game music loop over again and again. play(loops=-1) is not working
# Error : 
# TypeError: play() takes no keyword arguments
#pygame.mixer.music.play()

#############################
## Game loop
##메인게임루프
running = True
#쓰레드를돌아가게설정하고
menu_display = True
#메뉴화면을먼저보여줌
while running:
    if menu_display:
        main_menu()
        pygame.time.wait(3000)
        #메뉴화면이켜지고 3000ms 즉5초동안 메뉴화면을보여줌
    
        #Stop menu music
        pygame.mixer.music.stop()
        #메뉴음악을끄고 게임음악을불러옴
        #Play the gameplay music
        pygame.mixer.music.load(path.join(sound_folder, 'tgfcoder-FrozenJam-SeamlessLoop.ogg'))
        pygame.mixer.music.play(-1)     ## makes the gameplay sound in an endless loop
        #메뉴화면을끔
        menu_display = False
        
    #1 Process input/events
    #화면프레임체크? 항상같이돌아야함. 프레임이 고정적이지못하면 보이는화면이 지저분해짐
    clock.tick(FPS)     ## will make the loop run at the same speed all the time
    for event in pygame.event.get():        # gets all the events which have occured till now and keeps tab of them.
        ## listening for the the X button at the top
        if event.type == pygame.QUIT:
            running = False
        #ECS를누르면게임에서나가짐
        ## Press ESC to exit game
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
                ##쓰레드루프를종료시킴
        # ## event for shooting the bullets
        # elif event.type == pygame.KEYDOWN:
        #     if event.key == pygame.K_SPACE:
        #         player.shoot()      ## we have to define the shoot()  function

    #2 Update
        ##모든화면에표시될것들을 업데이트시켜줌
    all_sprites.update()


    ## check if a bullet hit a mob
    ## now we have a group of bullets and a group of mob
    ##만약에 몹에 맞을경우
    hits = pygame.sprite.groupcollide(mobs, bullets, True, True)
    ## now as we delete the mob element when we hit one with a bullet, we need to respawn them again
    ## as there will be no mob_elements left out 
    #
    for hit in hits:
        score += 50 - hit.radius        ## give different scores for hitting big and small metoers
        if(score>1000*level*level):
            newmob()
            level = level + 1
        random.choice(expl_sounds).play()
        ##폭발사운드를랜덤으로불러옴
        # m = Mob()
        # all_sprites.add(m)
        # mobs.add(m)
        expl = Explosion(hit.rect.center, 'lg')
        all_sprites.add(expl)
        ##띠용??
        if random.random() > 0.9:
            pow = Pow(hit.rect.center)
            all_sprites.add(pow)
            powerups.add(pow)
        newmob()
        ## spawn a new mob
        ##새로운몹을생성

    ## ^^ the above loop will create the amount of mob objects which were killed spawn again
    #########################

    ## check if the player collides with the mob
    hits = pygame.sprite.spritecollide(player, mobs, True, pygame.sprite.collide_circle)        ## gives back a list, True makes the mob element disappear
    for hit in hits:
        ##플레이어가 운석에맞을때.
        player.shield -= hit.radius * 2
        ##쉴드의 개수를 지움.
        expl = Explosion(hit.rect.center, 'sm')
        ##폭팔이미지추가  
        all_sprites.add(expl)
        ##다시그리기. 폭발을추가해서.
        newmob()
        ##새로운몹추가.
        if player.shield <= 0:
            ##플레이어의 쉴드가 0보다 크면
            player_die_sound.play()
            ##죽는사운드.
            death_explosion = Explosion(player.rect.center, 'player')
            ##죽는폭발추가?
            all_sprites.add(death_explosion)
            # running = False     ## GAME OVER 3:D
            player.hide()
            player.lives -= 1
            player.shield = 100
            ##플레이어를지움.

    ##플레이어가파워업아이템을 맟추면
    ## if the player hit a power up
    hits = pygame.sprite.spritecollide(player, powerups, True)
    for hit in hits:
        if hit.type == 'shield':
            player.shield += random.randrange(10, 30)
            if player.shield >= 100:
                player.shield = 100
        if hit.type == 'gun':
            player.powerup()
    ##만약플레이어가죽으면.
    ## if player died and the explosion has finished, end game
    if player.lives == 0 and not death_explosion.alive():
        running = False
        ##쓰레드종료.
        # menu_display = True
        # pygame.display.update()

    #3 Draw/render
    ##검정색화면으로그리기.
    screen.fill(BLACK)
    ## draw the stargaze.png image
    screen.blit(background, background_rect)
    ##화면다시그리기.
    all_sprites.draw(screen)
    draw_text(screen, str(score), 18, WIDTH / 2, 10)     ## 10px down from the screen
    draw_shield_bar(screen, 5, 5, player.shield)
    
    # Draw lives
    draw_lives(screen, WIDTH - 100, 5, player.lives, player_mini_img)
    
    ## Done after drawing everything to the screen
    pygame.display.flip()       
##게임종료.
pygame.quit()
