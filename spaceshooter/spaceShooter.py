#!/usr/bin/env python #시스템 환경 변수를 파이썬으로 합니다.
# -*- coding: utf-8 -*- #인코딩 방식은 utf-8을 이용합니다.
# @Author: tasdik #저작자: tasdik
# @Contributers : Branden (Github: @bardlean86) #컨트리뷰터(기여자): Branden
# @Date:   2016-01-17 #날짜: 2016-01-17
# @Email:  prodicus@outlook.com  Github: @tasdikrahman #이메일 주소 
# @Last Modified by:   tasdik #최근 수정자 
# @Last Modified by:   Branden #최근 수정자
# @Last Modified by:   Dic3 #최근 수정자
# @Last Modified time: 2016-10-16 ##최근 수정 시간 
# MIT License. You can find a copy of the License @ http://prodicus.mit-license.org MIT 라이센스. 당신은 위 주소에서 라이센스 사본을 볼 수 있습니다.
 
## Game music Attribution #게임음악 속성은 아래와 같습니다.
##Frozen Jam by tgfcoder <https://twitter.com/tgfcoder> licensed under CC-BY-3 <http://creativecommons.org/licenses/by/3.0/>
 
## Additional assets by: Branden M. Ardelean (Github: @bardlean86)
 
from __future__ import division #파이썬2에서 3로 넘어갈 때 잘 작동하도록 하기 위한 기능을 도와주는 브릿지 패키지입니다. division은 숫자의 (나눗셈 등)연산결과가 실수가 나오도록 해줍니다. 
import pygame #pygame 모듈을 import합니다.
import random #random 모듈을 import합니다.
from os import path #os모듈내의 path를 이용합니다.
 
## assets folder #assets(자산) 폴더 
img_dir = path.join(path.dirname(__file__), 'assets') #이미지 폴더 
sound_folder = path.join(path.dirname(__file__), 'sounds') #사운드 폴더 
 
###############################
## to be placed in "constant.py" later #constant.py 파일에 놓이게 될것들 입니다. 
WIDTH = 480 #넓이 480
HEIGHT = 600 #높이 600
FPS = 60 #프레임 =60 
POWERUP_TIME = 5000 #파워를 받는 시간 = 5000
BAR_LENGTH = 100 #체력 바 길이 100
BAR_HEIGHT = 10 #체력 바 높이 10
 
# Define Colors # 색 정의 (튜플로 표기되었습니다.)
ALPHA_BLACK = (0, 0, 0, 0.45) #배경화면을 위한 색
WHITE = (255, 255, 255) #흰색 
BLACK = (0, 0, 0) #검정색 
RED = (255, 0, 0) #빨강 
GREEN = (0, 255, 0) #초록 
BLUE = (0, 0, 255) #파랑 
YELLOW = (255, 255, 0) #노랑 
###############################
 
###############################
## to placed in "__init__.py" later #초기화 기능들입니다. 
## initialize pygame and create window #pygame을 초기화합니다. 그리고 새로운 창을 엽니다.
pygame.init() #파이게임 초기화 
pygame.mixer.init()  ## For sound #mixer는 노래를 이용할 때 쓰입니다. 그것을 초기화 시켜줍니다.
screen = pygame.display.set_mode((WIDTH, HEIGHT)) #창의 규격을 설정합니다. 
pygame.display.set_caption("Space Shooter") #맨위 제목 캡션에 Space Shooter이라고 표기해줍니다.
clock = pygame.time.Clock()     ## For syncing the FPS #FPS와 동기화 시키기 위해 시간을 맞춥니다.
###############################
 
font_name = pygame.font.match_font('arial') #폰트는 arial을 이용합니다.
 
def main_menu(): #메인 메뉴 함수를 정의합니다. 
    global screen #전역 변수로 위에서 정의된 screen을 호출합니다.
 
    menu_song = pygame.mixer.music.load(path.join(sound_folder, "menu.ogg")) #첫 메뉴에서 뜨는 음악입니다.
    pygame.mixer.music.play(-1) #음수값이 있으므로 종료시까지 계속 반복하게 됩니다.
 
    title = pygame.image.load(path.join(img_dir, "main.png")).convert() #메인화면을 불러드립니다.
    title = pygame.transform.scale(title, (WIDTH, HEIGHT), screen) #title과 좌우 넓이를 규정한 창을 title로 합니다. 
 
    screen.blit(title, (0,0)) #영상을 화면에 표시합니다.(표시할때 0(가로: 위에서 부터 시작합니다.),0(높이: 위에서 부터 시작합니다.)위치부터 쏘아줍니다.)
    pygame.display.update() #화면 전체를 다시한번 업데이트 합니다.
 
    while True: #참이라면(무한 루프)
        ev = pygame.event.poll() #ev를 사용자가 입력하는 이벤트 받는 것으로 한다.
        if ev.type == pygame.KEYDOWN: #만약 키가 눌렸다면 
            if ev.key == pygame.K_RETURN: #키가 엔터키가 눌렸을 경우
                break #break
            elif ev.key == pygame.K_q: #q키가 눌렸을 경우
                pygame.quit() #게임을 끄도록 합니다.
                quit() # 나갑니다. 
        elif ev.type == pygame.QUIT: #윈도우의 닫기 버튼을 클릭했을 경우 
                pygame.quit() #게임을 끄도록 합니다.
                quit() #나갑니다. 
        else: #메인 메뉴에서 아래와 같은 text를 출력하게 해줌
            draw_text(screen, "Press [ENTER] To Begin", 30, WIDTH/2, HEIGHT/2) #글자를 출력합니다.
            draw_text(screen, "and [P] To Pause", 30, WIDTH/2, (HEIGHT/2)+40) 
            draw_text(screen, "or [Q] To Quit", 30, WIDTH/2, (HEIGHT/2)+80)
            pygame.display.update() #화면 전체를 다시한번 업데이트 합니다. 
 
    #pygame.mixer.music.stop() 
    ready = pygame.mixer.Sound(path.join(sound_folder,'getready.ogg')) #준비하라는 소리를 틀어줍니다.
    ready.play() #ready사운드를 틀어줍니다.
    screen.fill(BLACK) #화면 전체 색을 검은색으로 합니다.
    draw_text(screen, "GET READY!", 40, WIDTH/2, HEIGHT/2) #get ready라는 글자를 써줍니다.
    pygame.display.update() #화면 전체를 다시한번 업데이트 합니다. 
    
 
def draw_text(surf, text, size, x, y): #draw_text라는 함수를 정의합니다.
    ## selecting a cross platform font to display the score
    font = pygame.font.Font(font_name, size) #폰트 변수를 정의합니다.
    text_surface = font.render(text, True, WHITE) #폰트를 하얀색,트루타입으로 해줍니다. ## True denotes the font to be anti-aliased 
    text_rect = text_surface.get_rect()  #text_surface객체가 그려질 위치와 크기를 나타냅니다.
    text_rect.midtop = (x, y) #주어진 x,y좌표를 위치로 선정합니다.
    surf.blit(text_surface, text_rect) #화면에 뿌려줍니다.
 
 
def draw_shield_bar(surf, x, y, pct): #체력바와 관련된 함수를 정의합니다.
    # if pct < 0: 
    #     pct = 0
    pct = max(pct, 0) #pct와 0중 최대값을 가져옵니다.
    ## moving them to top
    # BAR_LENGTH = 100
    # BAR_HEIGHT = 10
    fill = (pct / 100) * BAR_LENGTH #fill을 정의합니다.
    outline_rect = pygame.Rect(x, y, BAR_LENGTH, BAR_HEIGHT) #체력 바의 아웃라인을 그립니다.
    fill_rect = pygame.Rect(x, y, fill, BAR_HEIGHT) #체력 바 안쪽을 그려줍니다.
    pygame.draw.rect(surf, GREEN, fill_rect) #체력바 안쪽을 초록색으로 그려줍니다.
    pygame.draw.rect(surf, WHITE, outline_rect, 2) #체력바 아웃라인을 흰색으로 그려줍니다.
 
 
def draw_lives(surf, x, y, lives, img): #여기서 img는 플레이어인 비행기를 의미합니다. 즉 플레이어의 삶과 관련된 함수입니다.
    for i in range(lives): #몫의 개수를 알수 있습니다.
        img_rect= img.get_rect() #몫이 그려질 위치와 크기를 나타냅니다.
        img_rect.x = x + 30 * i #x좌표에서 몫이 표시되는 위치입니다.
        img_rect.y = y #y좌료에서 몫이 표시되는 위치입니다.
        surf.blit(img, img_rect) #화면에 몫을 보여줍니다.
 
 
 
def newmob(): #새로운 몹에대한 함수입니다. (운석)
    mob_element = Mob() #mob_element를 Mob으로 정의합니다.
    all_sprites.add(mob_element) #전체 스프라이트에 mob_element를 추가를 합니다.
    mobs.add(mob_element) #mobs에 mob_element를 추가해줍니다.

class Explosion(pygame.sprite.Sprite): #Explosion 스프라이트 클래스입니다.
    def __init__(self, center, size): #초기화 함수입니다.
        pygame.sprite.Sprite.__init__(self) #pygame의 스프라이트를 초기화합니다.
        self.size = size #사이즈를 정의합니다.
        self.image = explosion_anim[self.size][0] #폭발 애니메이션을 우리가 정의한 크기로 해줍니다. 0부터 시작하게 해줍니다.
        self.rect = self.image.get_rect() #사각형 위치 설정을 어디로 할지 정합니다.
        self.rect.center = center #중앙으로 정해줍니다.
        self.frame = 0 #frame을 0으로 시작 합니다. 숫자조정을 하면 화면이 끊깁니다.
        self.last_update = pygame.time.get_ticks() #last update시간을 알려줍니다. 계속해야 됩니다. 안그러면 화면이 멈춥니다.
        self.frame_rate = 75 #프레임수를 정합니다. 0에 가까울수록 빠르게 터지는 모습을 볼수 있습니다. 각 프레임간 얼마나 기다려야하는지 정합니다.
 
    def update(self): #업데이트 함수입니다. 이미지들이 바뀌는 역할을 해줍니다.
        now = pygame.time.get_ticks() #tick을 해줍니다. 계속해야 됩니다. 안그러면 화면이 멈춥니다.
        if now - self.last_update > self.frame_rate: #위에서 정의한 변수중 이 조건을 충족한다면 
            self.last_update = now #pygame.time.get_ticks()를 호출합니다.
            self.frame += 1 #프레임을 하나 올립니다.
            if self.frame == len(explosion_anim[self.size]): #전체 애니메이션의 끝까지 왔다면 
                self.kill() #종료합니다. (폭발애니메이션의 끝입니다.)
            else:
                center = self.rect.center #중앙으로 위치 해줍니다.
                self.image = explosion_anim[self.size][self.frame] #어떤 이미지를 쓸지 정해줍니다.
                self.rect = self.image.get_rect() #사각형 위치 설정을 어디로 할지 정합니다.
                self.rect.center = center #중앙으로 위치 설정을 해줍니다.
 
 
class Player(pygame.sprite.Sprite): #Player 스프라이트 클래스입니다. 
    def __init__(self): #초기화 함수입니다.
        pygame.sprite.Sprite.__init__(self) #스프라이트 초기화입니다.
        ## scale the player img down
        self.image = pygame.transform.scale(player_img, (50, 38)) #비행체의 보이는 이미지 크기를 정해줍니다.
        self.image.set_colorkey(BLACK) 
        self.rect = self.image.get_rect() #사각형 위치 설정을 어디로 할지 정합니다.
        self.radius = 20 #플레이 대상의 외부 한계선을 정해줍니다.(값이 커지면 비행체가 먼곳에 있어도 운석에 맞은 판정을 받습니다.)(값이 적을수록 비행체 중심에 가야 운석 맞음 판정을 받습니다.)
        self.rect.centerx = WIDTH / 2 #첫 객체의 생성위치는 넓이의 2분의 1인 중앙으로 지정합니다.
        self.rect.bottom = HEIGHT - 10 #첫 객체생성의 높이를 설정해줍니다. 아래에서 10정도 띄어져 있습니다.
        self.speedx = 0 #이동과 관련됩니다. 음수는 좌측, 양수는 우측입니다.
        self.shield = 100 #객체가 처음 생성시 체력을 100으로 해줍니다.
        self.shoot_delay = 250 #발사하는 미사일의 딜레이를 250줍니다. 숫자가 낮을수록 더 빠르게 미사일을 발사할 수 있습니다.
        self.last_shot = pygame.time.get_ticks()
        self.lives = 3 #플레이어의 몫을 설정합니다.
        self.hidden = False #숨기는것을 일단 하지않습니다.
        self.hide_timer = pygame.time.get_ticks() 
        self.power = 1 #파위가 0이면 미사일 자체가 발사되지 않습니다. 발사와 관련되어있습니다.
        self.power_timer = pygame.time.get_ticks()
        background1_rect.top = -600 #움직이는 배경중 뒷부분 첫 설정입니다.
        
    def update(self): #업데이트 함수입니다.
        ## time out for powerups
        if self.power >=2 and pygame.time.get_ticks() - self.power_time > POWERUP_TIME: #이것을 통해 파워시간이 다되면 파워가 줄어들도록 합니다.
            self.power -= 1 #파워가 1씩 줄어듭니다.
            self.power_time = pygame.time.get_ticks()
 
        ## unhide  
        if self.hidden and pygame.time.get_ticks() - self.hide_timer > 1000: #숨김을 푸는 것과 관련이 있습니다.
            self.hidden = False #숨김을 거짓(드러남)으로 바꿉니다.
            self.rect.centerx = WIDTH / 2 #죽고난뒤에 살아남는 위치가 정해집니다.
            self.rect.bottom = HEIGHT - 30 #죽고난뒤에 살아남는 위치가 정해집니다.
 
        self.speedx = 0     ## makes the player static in the screen by default. 
        # then we have to check whether there is an event hanlding being done for the arrow keys being 
        ## pressed 
        self.speedy = 0  
        ## will give back a list of the keys which happen to be pressed down at that moment
        keystate = pygame.key.get_pressed()   #키의 현재상태를 나타냅니다.  
        if keystate[pygame.K_LEFT]: #왼쪽키라면 
            self.speedx = -5 #좌로
        elif keystate[pygame.K_RIGHT]: #오른쪽키라면
            self.speedx = 5 #우측
        elif keystate[pygame.K_UP]: #up 키라면
            self.speedy= -5
        elif keystate[pygame.K_DOWN]: #down 키라면
            self.speedy= 5
            
        #Fire weapons by holding spacebar
        if keystate[pygame.K_SPACE]: #키가 스페이스가 눌리면
            self.shoot() #발사

        if keystate[pygame.K_p]: #게임중 p키를 누르면
            self.pause() #pause함수를 불러옴
            
 
        #왼쪽과 오른쪽 테두리를 확인합니다.
        if self.rect.right > WIDTH: #우측이 너비보다 크면 
            self.rect.right = WIDTH #동일시합니다.
        if self.rect.left < 0:  #좌측이 0보다 작으면 
            self.rect.left = 0 #0과 동일 시 합니다.
        if self.rect.top < 0:  #화면 위쪽을 못 벗어나게 합니다.
            self.rect.top = 0 
        if self.rect.top > 560:  #아래 화면 못벋어나게 합니다.  
            self.rect.top = 560 
        self.rect.x += self.speedx #x좌표 변화율입니다. 
        self.rect.y += self.speedy #y좌표 변화율입니다.
        # 이거 찍으면 위치 추적 됩니다. print(self.rect)

    '''사용자가 p키를 눌러 pause를 할 수 있게 만들어 주는 함수로 함수를 부르자 마자 paused가 True가 됨으로써
    일시정지가 되고 pause인 상태에서 c키를 누르면 paused가 False가 되면서 게임을 계속 진행할 수 있고 q키를 누르게 된다면 
    게임이 바로 종료되며 위에서 선언한 ALPHA_BLACK으로 화면을 바꿔주고 draw_text를 통해 text를 출력하여
    어떤 버튼을 눌러야 하는지를 알려준다.
    '''
    def pause(self):
        paused = True 
        while paused:
            ev = pygame.event.poll()
            if ev.type == pygame.KEYDOWN:
                if ev.key == pygame.K_c:
                    paused = False
                elif ev.key == pygame.K_q:
                    pygame.quit()
                    quit()

            screen.fill(ALPHA_BLACK)
            draw_text(screen, "Paused", 30, WIDTH/2, HEIGHT/2 - 70)
            draw_text(screen, "Press [C] to contiune and [Q] to exit!", 20, WIDTH/2, HEIGHT/2 + 10)
            pygame.display.update()
      
       
    def shoot(self): #미사일 발사와 관련된 함수입니다.
        ## to tell the bullet where to spawn
        now = pygame.time.get_ticks()
        if now - self.last_shot > self.shoot_delay: #now - 마지막 슛 시간이 슛 딜레이보다 크면 
            self.last_shot = now 
            if self.power == 1: #파워가 1일겨우 
                bullet = Bullet(self.rect.centerx, self.rect.top)
                all_sprites.add(bullet) #총알을 추가합니다.
                bullets.add(bullet)  #총알을 추가합니다.
                shooting_sound.play() #슛 소리를 냅니다. 
            if self.power == 2: #파워가 2일경우 
                bullet1 = Bullet(self.rect.left, self.rect.centery)
                bullet2 = Bullet(self.rect.right, self.rect.centery)
                all_sprites.add(bullet1)  #총알을 추가합니다.
                all_sprites.add(bullet2)  #2번째 총알을 추가합니다.
                bullets.add(bullet1)  #총알을 추가합니다.
                bullets.add(bullet2) #2번째 총알을 추가합니다.
                shooting_sound.play() #슛 소리를 냅니다.
 
            """ MOAR POWAH """
            if self.power == 3: #파워가 3일 경우
                bullet1 = Bullet(self.rect.left, self.rect.centery)  #총알을 추가합니다.
                bullet2 = Bullet(self.rect.right, self.rect.centery) #2번째 총알을 추가합니다.
                missile1 = Missile(self.rect.centerx, self.rect.top) # Missile shoots from center of ship
                all_sprites.add(bullet1) #총알을 추가합니다.
                all_sprites.add(bullet2) #2번째 총알을 추가합니다.
                all_sprites.add(missile1) #3번째 미사일을 추가합니다.
                bullets.add(bullet1) #총알을 추가합니다.
                bullets.add(bullet2) #2번째 총알을 추가합니다.
                bullets.add(missile1) #3번째 미사일을 추가합니다.
                shooting_sound.play() #슛 소리를 냅니다.
                missile_sound.play() #미사일 소리를 냅니다.

            if self.power == 4: #파워가 4일 경우
                missile1 = Missile(self.rect.left, self.rect.centery) #미사일 추가
                missile2 = Missile(self.rect.right, self.rect.centery) #미사일 추가
                bullet1 = Bullet(self.rect.centerx, self.rect.top) #총알
                all_sprites.add(missile1) #1번째 미사일 
                all_sprites.add(missile2) #2번째 미사일
                all_sprites.add(bullet1)
                bullets.add(missile1) #1번째 미사일 
                bullets.add(missile2) #2번째 미사일
                bullets.add(bullet1)
                shooting_sound.play()
                missile_sound.play() #미사일 소리를 낸다

            if self.power >= 5:
                missile1 = Missile(self.rect.left, self.rect.centery) #미사일 추가 왼쪽 방향
                missile2 = Missile(self.rect.right, self.rect.centery) #미사일 추가 오른쪽 방향
                missile3 = Missile(self.rect.centerx, self.rect.top) #미사일 추가 가운데 방향
                all_sprites.add(missile1) #1번째 미사일 
                all_sprites.add(missile2) #2번째 미사일
                all_sprites.add(missile3) #3번째 미사일
                bullets.add(missile1) #1번째 미사일
                bullets.add(missile2) #2번째 미사일
                bullets.add(missile3) #3번째 미사일
                missile_sound.play() #미사일 소리를 낸다

    def powerup(self): #파워업 함수입니다.
        self.power += 1 #파워업을 먹을 시에는 파워가 1씩 증가합니다.
        self.power_time = pygame.time.get_ticks() #파워업된 시간이 들어갑니다.
 
    def hide(self): #숨김 함수입니다.
        self.hidden = True 
        self.hide_timer = pygame.time.get_ticks() 
        self.rect.center = (WIDTH / 2, HEIGHT + 200) 
 

# 적(운석)에 관한 클래스.
class Mob(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self) # pygame 내 sprite 초기화 / 추가 합니다.
        self.image_orig = random.choice(meteor_images)  # 운석 이미지를 랜덤으로 로드합니다.
        self.image_orig.set_colorkey(BLACK) # 나머지 부분의 배경색을 설정힙니다.
        self.image = self.image_orig.copy() # 선택된 운석 이미지로 복사하여 설정합니다.
        self.rect = self.image.get_rect() # 이미지에 대한 위치 및 너비 높이 정보를 로드합니다.
        self.radius = int(self.rect.width *.90 / 2) # 너비를 구합니다.
        self.rect.x = random.randrange(0, WIDTH - self.rect.width)  ## 움직일 수 있는 가로 및 
        self.rect.y = random.randrange(-150, -100)                  ## 세로 길이를 randomize 합니다.
        self.speedy = random.randrange(5, 20)       # 운석의 움직임을 속도를 이용해 randomize 합니다.
        self.speedx = random.randrange(-3, 3)
        
        # 운석 이 자체에 대한 순환을 설정합니다.
        self.rotation = 0
        self.rotation_speed = random.randrange(-8, 8) # 순환 범위 및 속도(주기)를 randomize 합니다.
        self.last_update = pygame.time.get_ticks()  # 가장 최근에 순환된 시간을 로드합니다. 

    def rotate(self):
        time_now = pygame.time.get_ticks() # 가장 최근에 순환된 기점부터
        if time_now - self.last_update > 50: # 단위는 ms입니다.
            self.last_update = time_now # 현재 시간으로 업데이트 합니다.
            self.rotation = (self.rotation + self.rotation_speed) % 360 
            new_image = pygame.transform.rotate(self.image_orig, self.rotation) # 새 운석 이미지로 업데이트 하여 다시 순환시킵니다.
            old_center = self.rect.center # 이전에 있던 위치를 로드합니다.
            self.image = new_image              ## 새 운석 이미지 
            self.rect = self.image.get_rect()   ## 및
            self.rect.center = old_center       ## 위치 재로드
 
    def update(self):
        self.rotate()
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        ## now what if the mob element goes out of the screen
 
        ## 운석이 화면 바깥으로 나간 경우
        if (self.rect.top > HEIGHT + 10) or (self.rect.left < -25) or (self.rect.right > WIDTH + 20):
            self.rect.x = random.randrange(0, WIDTH - self.rect.width)
            self.rect.y = random.randrange(-100, -40)
            self.speedy = random.randrange(1, 8)        ## for randomizing the speed of the Mob

        background_rect.top += 1 #배경 움직이기 입니다.
        if (background_rect.top == 600):
            background_rect.top = -600
 
        background1_rect.top += 1 #배경 다음에 오는 배경 움직이기 입니다.
        if (background1_rect.top == 600):
            background1_rect.top = -600


# 파워업 아이템 기능에 대한 클래스.
class Pow(pygame.sprite.Sprite):
    def __init__(self, center):
        pygame.sprite.Sprite.__init__(self) # pygame 내 sprite 초기화 / 추가 합니다.
        self.type = random.choice(['shield', 'gun']) # 미사일 아이템과 쉴드 아이템을 무작위로 선택합니다.
        self.image = powerup_images[self.type] # 해당하는 이미지 업로드
        self.image.set_colorkey(BLACK) # 나머지 부분의 배경색을 설정힙니다.
        self.rect = self.image.get_rect() # 이미지에 대한 위치 및 너비 높이 정보를 로드합니다.

         ## 플레이어의 위치에 따라서 아이템 위치를 알맞게 조정합니다.
        self.rect.center = center
        self.speedy = 2 # 아이템이 떨어지는 속도를 살짝 줄입니다. 몹 속도에 비해서 비교적 느린 편


    def update(self):
        self.rect.y += self.speedy # 플레이어와 같은 수직방향에서 스폰할 수 있도록
        
        # 화면 바깥으로 나간 경우 해당 아이템 소멸
        if self.rect.top > HEIGHT:
            self.kill()

            

# 총알에 대한 클래스.
class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self) # pygame 내 sprite 초기화 / 추가 합니다.
        self.image = bullet_img # 총알 이미지 업로드
        self.image.set_colorkey(BLACK) # 나머지 부분의 배경색을 설정힙니다.
        self.rect = self.image.get_rect() # 이미지에 대한 위치 및 너비 높이 정보를 로드합니다.
        # 현재 플레이어의 위치로부터 총알이 발사될 수 있도록 위치를 지정해줍니다.
        self.rect.bottom = y 
        self.rect.centerx = x
        self.speedy = -10  

    def update(self):
        self.rect.y += self.speedy # 플레이어가 이동된 위치에 따른 업데이트

        # 화면 바깥으로 나간 경우 해당 아이템 소멸
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

#배경화면 2개를 선언해줌
background = pygame.image.load(path.join(img_dir, 'starfield.png')).convert()
background1 = pygame.image.load(path.join(img_dir, 'starfield.png')).convert()
background_rect = background.get_rect()
background1_rect = background1.get_rect()
## ^^ draw this rect first 

## 플레이어 이미지와 총알,미사일 이미지 로드
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

## 운석 폭발 애니메이션 설정. 크기에 따라 다르다
explosion_anim = {} # 저장해 둘 딕셔너리.
explosion_anim['lg'] = [] # lg-> 큰 운석
explosion_anim['sm'] = [] # sm -> 작은 운석
explosion_anim['player'] = [] # 플레이어가 폭발할 경우

for i in range(9): ## 총 여덟 종류의 폭발 이미지에 대해(애니메이션화에 필요한 리소스)
    filename = 'regularExplosion0{}.png'.format(i) # regularExplision*.png를 전부 불러들입니다.
    img = pygame.image.load(path.join(img_dir, filename)).convert() #불러들인 이미지로 설정합니다.
    img.set_colorkey(BLACK) # 나머지 배경색을 설정합니다.

    ## lg-> 큰 운석에 대한 폭발. 변경되는 크기를 더 크게 = 더 큰 폭발 구현
    img_lg = pygame.transform.scale(img, (75, 75))
    explosion_anim['lg'].append(img_lg)
    ## sm-> 작은 운석에 대한 폭발. lg 폭발보다 작은 구현
    img_sm = pygame.transform.scale(img, (32, 32))
    explosion_anim['sm'].append(img_sm)

    ## 플레이어가 폭발 할 경우
    filename = 'sonicExplosion0{}.png'.format(i) # 운석 폭발과는 다른 이미지 sonicExplosion*.png를 전부 불러들입니다.
    img = pygame.image.load(path.join(img_dir, filename)).convert() #불러들인 이미지로 설정합니다.
    img.set_colorkey(BLACK) # 나머지 배경색을 설정합니다.
    explosion_anim['player'].append(img)

## 파워업 이미지 로드
powerup_images = {} # 파워업 이미지를 저장해둘 공간.
powerup_images['shield'] = pygame.image.load(path.join(img_dir, 'shield_gold.png')).convert() # 쉴드 아이템 이미지 로드
powerup_images['gun'] = pygame.image.load(path.join(img_dir, 'bolt_gold.png')).convert() # 총알 아이템 이미지 로드


###################################################


###################################################
## 브금 불러오기
shooting_sound = pygame.mixer.Sound(path.join(sound_folder, 'pew.wav')) # 발사 소리
missile_sound = pygame.mixer.Sound(path.join(sound_folder, 'rocket.ogg')) # 미사일 소리

expl_sounds = []
for sound in ['expl3.wav', 'expl6.wav']:
    expl_sounds.append(pygame.mixer.Sound(path.join(sound_folder, sound)))
## main background music
#pygame.mixer.music.load(path.join(sound_folder, 'tgfcoder-FrozenJam-SeamlessLoop.ogg'))
pygame.mixer.music.set_volume(0.2)      # 음약 음량 조

player_die_sound = pygame.mixer.Sound(path.join(sound_folder, 'rumble1.ogg')) #플레이어가 죽을 때 나는 소
###################################################

#
## TODO: make the game music loop over again and again. play(loops=-1) is not working
# Error : 
# TypeError: play() takes no keyword arguments
#pygame.mixer.music.play()

#############################

#main
running = True #게임을 특정 이벤트가 일어나지 않는한 무한루프로 실행시키기 위해 running이란 변수를 True(참)으로 할당해줌
menu_display = True #게임이 진행되는 동안 display또한 계속 보여져야 하므로 True(참)으로 할당해줌
## Game loop를 조정해주는 while문
while running: #바로 위에서 정의한 running이 참이기 때문에 무한 루프로 실행
    if menu_display: #menu_display가 참이기 때문에 if문을 실행한다.
        main_menu() #위에서 정의한 main_menu()를 호출한다.
        pygame.time.wait(3000) #3초간 기다림

        #Stop menu music
        pygame.mixer.music.stop()  #game music을 멈춰주는 함수
        #Play the gameplay music
        pygame.mixer.music.load(path.join(sound_folder, 'tgfcoder-FrozenJam-SeamlessLoop.ogg')) #gameplay music을 로딩 시켜줌
        pygame.mixer.music.play(-1)     ## makes the gameplay sound in an endless loop 게임 소리를 끝없이 나게 해줌
        
        menu_display = False
        
         ## group all the sprites together for ease of update
        all_sprites = pygame.sprite.Group() #모든 스프라이트들을 pygame.sprite.Group()함수를 통해 그룹핑해준다
        player = Player() #player에 Player()함수를 불러주고
        all_sprites.add(player) #그룹핑 되어있는 모든 스프라이트틀에 player를 넣어줌

        #### Score board variable
        score = 0 #장애물을 격파 시킬 때마다 누적되는 점수

        ## spawn a group of mob if문 써서 뭐가 뭐이면 숫자 조정해주면 될거같은데
        mobs = pygame.sprite.Group() #몬스터 몹을 출현시키기 위해 만들어준거임

        for i in range(8):      ## 8 mobs
            # mob_element = Mob()
            # all_sprites.add(mob_element)
            # mobs.add(mob_element)
            newmob()
        ## group for bullets
        bullets = pygame.sprite.Group() #레이저
        powerups = pygame.sprite.Group() #레이저를 업그레이드 시켜주는 아이템


    #1 Process input/events
    clock.tick(FPS)     ##게임의 속도를 같은 속도로 해줌
    for event in pygame.event.get():        # gets all the events which have occured till now and keeps tab of them.
        ## listening for the the X button at the top
        if event.type == pygame.QUIT:
            running = False

        ## Esc를 눌렀을 때 게임을 종료 시켜줌
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
        # ## event for shooting the bullets
        # elif event.type == pygame.KEYDOWN:
        #     if event.key == pygame.K_SPACE:
        #         player.shoot()      ## we have to define the shoot()  function

    #2 Update
    all_sprites.update()

    #장애물이 끊임없이 재생성 되게하고, 장애물을 격파 시켰을 때 점수를 주는 for문
    hits = pygame.sprite.groupcollide(mobs, bullets, True, True)
    for hit in hits: 
        score += 50 - hit.radius         ##장애물의 크기에 따라 격파 시켰을 때 주는 점수를 다르게 해줌

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
        newmob()        ## 장애물을 계속 만듬

    ## 플레이어가 장애물과 충돌을 하였을때 발생하는 for문
    hits = pygame.sprite.spritecollide(player, mobs, True, pygame.sprite.collide_circle)        ## gives back a list, True makes the mob element disappear
    for hit in hits:
        player.shield -= hit.radius * 2 #hit(장애물)의 반경의 따라 플레이어의 체력바가 다르게 깎임을 나타내는 거임
        expl = Explosion(hit.rect.center, 'sm')
        all_sprites.add(expl)
        newmob()
        if player.shield <= 0: #충돌을 하였을 때 만약 플레이어의 체력바가 0보다 아래가 됐을 경우
            player_die_sound.play()
            death_explosion = Explosion(player.rect.center, 'player')
            all_sprites.add(death_explosion)
            # running = False     ## GAME OVER 3:D
            player.hide()
            player.lives -= 1
            player.shield = 100

    ## 플레이어가 체력을 향상시켜주는 아이템을 먹었거나 레이저의 성능을 향상시켜주는 아이템을 먹었을 때 작동하는 for문
    hits = pygame.sprite.spritecollide(player, powerups, True)
    for hit in hits:
        if hit.type == 'shield':
            player.shield += random.randrange(10, 30)
            if player.shield >= 100:
                player.shield = 100
        if hit.type == 'gun': #플레이어의 레이저의 성능을 한단계 높여줌
            player.powerup()
    ## if player died and the explosion has finished, end game
    if player.lives == 0 and not death_explosion.alive():
        running = False
        # menu_display = True
        # pygame.display.update()


    #3 Draw/render
    screen.fill(BLACK)
    ## draw the stargaze.png image

    #blit함수를 통해 background사진 2개를 번갈아 가면서
    #보이게 함으로써 dynamic한 배경화면을 구현함
    screen.blit(background, background_rect)
    screen.blit(background1, background1_rect)


    #모든 sprites들을 화면에 가져온다
    all_sprites.draw(screen)
    draw_text(screen, str(score), 18, WIDTH / 2, 10)  ## 10px down from the screen
    draw_shield_bar(screen, 5, 5, player.shield)

    #비행기의 목숨
    draw_lives(screen, WIDTH - 100, 5, player.lives, player_mini_img)

    ##화면이 필요한 것들을 가져오고난 후 끝을냄
    pygame.display.flip()

pygame.quit()
