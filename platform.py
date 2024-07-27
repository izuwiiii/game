import play
import math
import pygame
import random

pygame.mixer.init()
h = 600
w = 600
# play.screen.width=w*2
# play.screen.height=h*2
play.set_backdrop('light green')
demons = []
prtals = []
prtals_image = ["images/portal1.png", "images/portal2.png", "images/portal3.png", "images/portal4.png"]
pltforms = []
pltformsl2 = []
pltformsl3 = []
coins = []
coinslv2 = []
coins_image = ["images/coin1.png", "images/coin2.png", "images/coin3.png", "images/coin4.png", "images/coin5.png", "images/coin6.png", "images/coin7.png", "images/coin8.png", ]###load
igli = []
iglilv2 = []

score_txt = play.new_text(words = 'Score:', x = play.screen.right-100, y = play.screen.top-30, size=70)
score = play.new_text(words = '0', x = play.screen.right-30, y = play.screen.top-30, size=70)

#tips
text = play.new_text(words = 'Tap SPACE to jump, A/D to move', x = 0, y = play.screen.bottom+60, size=70)
text1 = play.new_text(words = 'Tap W to ATTACK, S to HEAL', x = 0, y = play.screen.bottom+60, size=70)
text1.hide()
lose_text = play.new_text(words = 'YOU LOSE', x = 0, y = 0, size=200, color='white')
lose_text.hide()
win_text = play.new_text(words = 'YOU WIN!', x = 0, y = 0, size=200, color='BLACK')
win_text.hide()
sprite = play.new_image(image='images/def1.png', x=-280, y=250, size=180)
demon = play.new_image(image='images/ldemon1.png', x=-5000, y = 170, size=80)
demon.hide()
hp = 100
demon_hp = 4
can_attack = False
health = play.new_text(words = str(hp)+' HP', x = play.screen.left+50, y = play.screen.top-20, size=70, color='green')
is_jumping = False
max_jump_height = 120
sea = play.new_box(color='blue', width=play.screen.width, height=50, x=0, y=play.screen.bottom+20)
loseline=play.new_box(color='blue', width=play.screen.width, height=50, x=0, y=play.screen.bottom+20)
portal = play.new_image(image='images/portal.png', x=200, y = 150, size=30)
portal2 = play.new_image(image='images/portal.png', x=-300, y = 180, size=30)
portal2.hide()
portal3 = play.new_image(image='images/portal.png', x=-320, y = -20, size=30)
portal3.hide()
prtals.append(portal)
prtals.append(portal2)
prtals.append(portal3)
last_player_side = True
health_potion = play.new_image(image='images/potion.png', x=200, y = -40, size=10)
health_potion.hide()

key = play.new_image(image='images/key.png', x=-5000, y = 170, size=25)
key.hide()
have_key = False
potion = 0
potions = play.new_text(words=str(potion+1), x = play.screen.top - 80, y = play.screen.top - 30, size=70)
potions.hide()

boss = play.new_image(image='images/boss1.png', x=-5000, y = 10, size=350)
boss.hide()
dead = play.new_image(image='images/dead1.png', x=-5000, y = 10, size=350)
dead.hide()
fire = play.new_image(image='images/fire.png', x=-5000, y = 10, size=350)
fire.hide()
lfire = play.new_image(image='images/lfire.png', x=-5000, y = 10, size=350)
lfire.hide()
bossfight = False
playerx = 0
playery = 0
boss_hp = 1000
boss_health = play.new_text(words=str(boss_hp), x = play.screen.top - 80, y = play.screen.top - 30, size=70)
boss_health.hide()
chest = play.new_image(image='images/chestop.png', x=-5000, y = 10, size=350)
# chest.hide()
chestop = play.new_image(image='images/chestop.png', x=-5000, y = 10, size=350)
# chestop.hide()

def draw_platforms():
    plt1 = play.new_image(image='images/land.png', x=-280, y = 70, size=100)
    pltforms.append(plt1)
    plt2 = play.new_image(image='images/land.png', x=-20, y = 40, size=100)
    pltforms.append(plt2)
    plt3 = play.new_image(image='images/land.png', x=200, y = 50, size=100)
    pltforms.append(plt3)

    for pl in pltforms:
        pl.start_physics(can_move = False, x_speed = 0, y_speed = 0, bounciness = 0.2)
    for coin in coins:
        coin.start_physics(can_move = False, x_speed = 0, y_speed = 0, bounciness = 0.2)

def draw_platformsl2():
    l2plt1 = play.new_image(image='images/land.png', x=-280, y = 100, size=100)
    pltforms.append(l2plt1)
    l2plt2 = play.new_image(image='images/land.png', x=-50, y = 120, size=100)
    pltforms.append(l2plt2)
    l2plt3 = play.new_image(image='images/land.png', x=200, y = 130, size=100)
    pltforms.append(l2plt3)
    l2plt4 = play.new_image(image='images/land.png', x=-280, y = -100, size=100)
    pltforms.append(l2plt4)
    l2plt5 = play.new_image(image='images/land.png', x=-50, y = -100, size=100)
    pltforms.append(l2plt5)
    l2plt6 = play.new_image(image='images/land.png', x=200, y = -80, size=100)
    pltforms.append(l2plt6)

    for pl in pltformsl2:
        pl.start_physics(can_move = False, x_speed = 0, y_speed = 0, bounciness = 0.2)
    for coin in coins:
        coin.start_physics(can_move = False, x_speed = 0, y_speed = 0, bounciness = 0.2)

def draw_platformsl3():
    l3plt1 = play.new_image(image='images/wood.png', x=-280, y = 100, size=300)
    pltforms.append(l3plt1)
    l3plt2 = play.new_image(image='images/bigwood.png', x=0, y = -100, size=80)
    pltforms.append(l3plt2)

    for pl in pltformsl3:
        pl.start_physics(can_move = False, x_speed = 0, y_speed = 0, bounciness = 0.2)
    for coin in coins:
        coin.start_physics(can_move = False, x_speed = 0, y_speed = 0, bounciness = 0.2)

def draw_coins():
    coinlvl1 = play.new_image(image = 'images/coin1.png', x = -20, y = 90, size = 35)
    coins.append(coinlvl1)

def draw_coinslvl2():
    coinlvl2 = play.new_image(image = 'images/coin1.png', x = -50, y = -50, size = 35)
    coins.append(coinlvl2)

def draw_coinslvl3():
    coinlvl3 = play.new_image(image = 'images/coin1.png', x = 120, y = -40, size = 35)
    coins.append(coinlvl3)
    coin2lvl3 = play.new_image(image = 'images/coin1.png', x = 60, y = -40, size = 35)
    coins.append(coin2lvl3)
    coin3lvl3 = play.new_image(image = 'images/coin1.png', x = 00, y = -40, size = 35)
    coins.append(coin3lvl3)
    coin4lvl3 = play.new_image(image = 'images/coin1.png', x = -60, y = -40, size = 35)
    coins.append(coin4lvl3)
    coin5lvl3 = play.new_image(image = 'images/coin1.png', x = -120, y = -40, size = 35)
    coins.append(coin5lvl3)
    coin6lvl3 = play.new_image(image = 'images/coin1.png', x = -180, y = -40, size = 35)
    coins.append(coin6lvl3)
    # coinlvl3 = play.new_image(image = 'images/coin1.png', x = 120, y = -20, size = 35)
    # coins.append(coinlvl3)
    # coin2lvl3 = play.new_image(image = 'images/coin1.png', x = 80, y = -20, size = 35)
    # coins.append(coin2lvl3)
    # coin3lvl3 = play.new_image(image = 'images/coin1.png', x = 40, y = -20, size = 35)
    # coins.append(coin3lvl3)

@play.repeat_forever
def touch_coin():
    for coin in coins:
        if sprite.is_touching(coin):
            pygame.mixer.music.load("collect.mp3")
            pygame.mixer.music.play()
            coin.hide()
            coins.remove(coin)
            score.words=int(score.words)+1


@play.when_program_starts
def start():
    draw_platforms()
    draw_coins()
    sprite.start_physics(can_move=True, x_speed=0, y_speed=0, bounciness=0.1, obeys_gravity=True, stable=True, mass=10)
    demon.start_physics(can_move=True, x_speed=0, y_speed=0, bounciness=0.1, obeys_gravity=True, stable=True, mass=10)
    boss.start_physics(can_move=True, x_speed=0, y_speed=0, bounciness=0.1, obeys_gravity=True, stable=True, mass=10)

async def jump():
    global is_jumping
    global sprite_return
    is_jumping = True
    sprite_return = sprite.y

    while play.key_is_pressed('space') and sprite.y < sprite_return + max_jump_height:
        sprite.y += 7
        if play.key_is_pressed('a'):
            sprite.x -= 2
        if play.key_is_pressed('d'):
            sprite.x += 2
        move_horizontal()
        await play.timer(seconds=0.001)

    while sprite.y > sprite_return :  
        sprite.y -= 7
        move_horizontal()
        await play.timer(seconds=0.001)
    
    is_jumping = False

def move_horizontal():
    if play.key_is_pressed('a'):
        sprite.x -= 3
    if play.key_is_pressed('d'):
        sprite.x += 3

@play.repeat_forever
async def regen_hp(): 
    global hp
    global health
    await play.timer(seconds=1)
    if hp <= 100:
        hp = hp + 1
    if hp >= 100:
        hp = 100
    health.words = str(hp)+' HP'

async def lose_hp():
    global hp
    global health
    global back
    hp = int(hp) - 35
    health.words = str(hp)+' HP'
    health.color = 'red'
    await play.timer(seconds=0.5)
    health.color = 'green'
    await play.timer(seconds=0.5)
    health.color = 'red'
    await play.timer(seconds=0.5)
    health.color = 'green'

def hide_all1():
    for pl in pltforms:
        pl.x = -5000
    # for cn in coins:
    #     cn.hide()
    portal.x = -5000
    health.hide()
    score.hide()
    score_txt.hide()
    sea.hide()
    loseline.hide()
    text.hide()
    demon.hide()
    portal2.hide()
    key.hide()
    health_potion.hide()
    boss_health.hide()

# @play.repeat_forever
# async def demon_move():
    # while demon.x != 200:
    #     demon.x += 1

@play.repeat_forever
async def demon_damage():
    global hp
    if sprite.is_touching(demon):
        await lose_hp()
# pygame.mixer.music.load("spooky.mp3")
# pygame.mixer.music.set_volume(0.5)
# pygame.mixer.music.play()
@play.repeat_forever
async def sprite_damage():
    global can_attack
    global demon_hp
    if sprite.is_touching(demon) and can_attack == True:
        pygame.mixer.music.load("hit.mp3")
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.play()
        demon.y += 10
        demon.x += 10
        await play.timer(seconds=0.01)
        demon.y -= 10
        demon_hp = demon_hp - 1
    if demon_hp == 0:
        demon.x = -5000

@play.repeat_forever
async def get_key():
    global have_key
    if sprite.is_touching(key):
        await play.timer(seconds=0.5)
        have_key = True
        key.hide()

@play.repeat_forever
async def lose():
    global hp
    global health

    if hp <= 35:
        health.color = 'red'

    if hp <= 0:
        play.set_backdrop('black')
        lose_text.show()   
        sprite.hide()
        boss.hide()
        boss_health.hide()
        fire.hide()
        hide_all1()
        await play.timer(seconds=5)
        quit()

@play.repeat_forever
async def game():
    global bossfight
    global is_jumping
    global potion
    global playerx
    global playery
    # print(sprite.x)
    # print(playerx)
    playerx = sprite.x
    playery = sprite.y

    if (play.key_is_pressed('space')) and not is_jumping:
        await jump()
    else:
        move_horizontal()

    if not (sprite.is_touching(sea) or any(sprite.is_touching(plt) for plt in pltforms)):
        sprite.y -= 7 

    if sprite.is_touching(sea):
        sprite.y = 150
        sprite.x = -280
        await lose_hp()

    for plt in pltforms:
        if sprite.is_touching(plt) and sprite.y > plt.y:
            sprite.y = plt.y + plt.height / 2 + sprite.height / 2
# LVL 2
    if sprite.is_touching(portal):
        hide_all1()
        health.show()
        score.show()
        score_txt.show()
        sprite.x = -250
        sprite.y = 200
        portal2.show()
        draw_platformsl2()
        demon.show()
        demon.x = -10
        key.show()
        key.x = 200
        draw_coinslvl2()
        health_potion.show()
        portal3.show()
        sea.show()
        loseline.show()
        text1.show()

# LVL 3
    if sprite.is_touching(portal3):
        hide_all1()
        text1.hide()
        health.show()
        score.show()
        score_txt.show()
        sprite.x = -250
        sprite.y = 200
        for c in coins:
            c.x = -5000
        if potion >= 1:
            health_potion.show()
        else:
            health_potion.hide()
            potions.hide()
        portal3.hide()
        portal3.x = -5000
        sea.show()
        loseline.show()
        play.set_backdrop('black')
        sea.color='red'
        loseline.color='red'
        text.color = 'white'
        score_txt.color = 'white'
        score.color = 'white'
        draw_platformsl3()
        demon.x = -5000
        boss.show()
        boss.x = 120
        boss.y = 40
        dead.x = 120
        dead.y = 40
        fire.x = 120
        fire.y = 40
        fire.show()
        bossfight = True

lastx = 0
lasty = 0
win = False

async def lose_hp_fire():
    global hp
    global health
    global back
    hp = int(hp) - 35
    health.words = str(hp)+' HP'
    fire.x = 500
    fire.y = 5000
    await play.timer(seconds=1)

@play.repeat_forever
async def boss_attack():
    global lastx
    global lasty
    global playerx
    global playery
    global can_attack
    global boss_hp
    global win
    global hp
    # print(math.floor(math.floor(sprite.y)))

    if bossfight == True:
        # pygame.mixer.music.load("boss.mp3")
        # pygame.mixer.music.play()
        boss_health.color = 'white'
        boss_health.show()
        if fire.x <= -600:
            fire.x = 120
            fire.y = 00
        if fire.x >= -800:
            lfire.x += 10
            fire.x-=3
        if sprite.is_touching(fire) and can_attack == True:
            lastx = fire.x
            lasty = fire.y
            fire.x=-168
            fire.y=5000
            lfire.x = (lastx)
            lfire.y = lasty
            lfire.show()
        if (sprite.x-20 <= fire.x <= sprite.x-20) and 50 >= math.floor(sprite.y) >= -50:
        # if sprite.is_touching(fire):
            print(fire.x)
            print(sprite.x)
            print(fire.y)
            print(sprite.y)
            await lose_hp_fire()
            print("DAMAGE")
        if lfire.is_touching(boss):
            boss_hp -= 250
            boss_health.words = str(boss_hp)
            lfire.x = 5000
        if sprite.is_touching(boss):
            hp = 0
            boss_health.hide()
            fire.hide()
        if boss_hp == 0 and win != True:
            await play.timer(seconds=2)
            fire.hide()
            fire.x = 50000000
            boss.hide()
            boss.x = 5000
            dead.y = -20
            dead.show()
            await anim_dead() 
            dead.hide()
            win = True
            draw_coinslvl3()
            chest.show()
            play.set_backdrop('white')
            win_text.show()   
            loseline.color = 'blue'
            sea.color = 'blue'

            # sprite.hide()
            # hide_all1()
            # await play.timer(seconds=5)
            # quit()
        

@play.repeat_forever
async def health_potion_add():
    global potion
    global potions
    if sprite.is_touching(health_potion):
        potion += 1
        health_potion.x = play.screen.top-100
        health_potion.y = play.screen.top-30
        potions.show()

@play.repeat_forever
async def anim_player():
    global sprite_return
    global last_player_side
    global can_attack
    global potion
    global hp

    if play.key_is_pressed('s') and potion >= 1:
        potions.hide()
        potion = 0
        health_potion.x = -5000
        hp = hp + 50

    if play.key_is_pressed('w') and last_player_side == True:

        sprite.image = 'images/adventurer-attack2-00.png'
        await play.timer(seconds=0.05)
        sprite.image = 'images/adventurer-attack2-01.png'
        await play.timer(seconds=0.05)
        sprite.image = 'images/adventurer-attack2-02.png'
        await play.timer(seconds=0.05)
        can_attack = True
        pygame.mixer.music.load("sword.wav")
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.play()
        sprite.image = 'images/adventurer-attack2-03.png'
        await play.timer(seconds=0.05)
        can_attack = False
        sprite.image = 'images/adventurer-attack2-04.png'
        await play.timer(seconds=0.05)
        sprite.image = 'images/adventurer-attack2-05.png'
        await play.timer(seconds=0.05)

    if play.key_is_pressed('w') and last_player_side == False:
        sprite.image = 'images/ladventurer-attack2-00.png'
        await play.timer(seconds=0.05)
        sprite.image = 'images/ladventurer-attack2-01.png'
        await play.timer(seconds=0.05)
        sprite.image = 'images/ladventurer-attack2-02.png'
        await play.timer(seconds=0.05)
        can_attack = True
        pygame.mixer.music.load("sword.wav")
        pygame.mixer.music.play()
        sprite.image = 'images/ladventurer-attack2-03.png'
        await play.timer(seconds=0.05)
        can_attack = False
        sprite.image = 'images/ladventurer-attack2-04.png'
        await play.timer(seconds=0.05)
        sprite.image = 'images/ladventurer-attack2-05.png'
        await play.timer(seconds=0.05)

    if play.key_is_pressed('d') and not is_jumping:
        sprite.image = 'images/run1.png'
        await play.timer(seconds=0.05)
        sprite.image = 'images/run2.png'
        await play.timer(seconds=0.05)
        sprite.image = 'images/run3.png'
        await play.timer(seconds=0.05)
        sprite.image = 'images/run4.png'
        await play.timer(seconds=0.05)
        sprite.image = 'images/run5.png'
        last_player_side = True
    if last_player_side == True:
        sprite.image = 'images/def1.png'
    if play.key_is_pressed('a') and not is_jumping:
        sprite.image = 'images/lrun1.png'
        await play.timer(seconds=0.05)
        sprite.image = 'images/lrun2.png'
        await play.timer(seconds=0.05)
        sprite.image = 'images/lrun3.png'
        await play.timer(seconds=0.05)
        sprite.image = 'images/lrun4.png'
        await play.timer(seconds=0.05)
        sprite.image = 'images/lrun5.png'
        last_player_side = False
    if last_player_side == False:
        sprite.image = 'images/ldef1.png'

    if is_jumping == True and last_player_side == True:
        sprite.image = 'images/adventurer-fall-00.png'
        await play.timer(seconds=0.05)
        sprite.image = 'images/adventurer-fall-01.png'
        await play.timer(seconds=0.05)

    if is_jumping == True and last_player_side == False:
        sprite.image = 'images/adventurer-lfall-00.png'
        await play.timer(seconds=0.05)
        sprite.image = 'images/adventurer-lfall-01.png'
        await play.timer(seconds=0.05)

@play.repeat_forever
async def anim_coins():
    for c in coins:
        for i in range(7):
            c.image=coins_image[i]
            await play.timer(seconds=0.1)

@play.repeat_forever
async def anim_portals():
    for p in prtals:
        for i in range(len(prtals_image)):
            p.image=prtals_image[i]
            await play.timer(seconds=0.2)

@play.repeat_forever
async def anim_demon():
    demon.image = 'images/ldemon1.png'
    await play.timer(seconds=0.1)
    demon.image = 'images/ldemon2.png'
    await play.timer(seconds=0.1)
    demon.image = 'images/ldemon3.png'
    await play.timer(seconds=0.1)
    demon.image = 'images/ldemon4.png'
    await play.timer(seconds=0.1)

@play.repeat_forever
async def anim_boss():
    boss.image = 'images/boss1.png'
    await play.timer(seconds=0.1)
    boss.image = 'images/boss2.png'
    await play.timer(seconds=0.1)
    boss.image = 'images/boss3.png'
    await play.timer(seconds=0.1)
    boss.image = 'images/boss4.png'
    await play.timer(seconds=0.1)
    boss.image = 'images/boss5.png'
    await play.timer(seconds=0.1)
    boss.image = 'images/boss6.png'
    await play.timer(seconds=0.1)

async def anim_dead():
    dead.image = 'images/dead1.png'
    await play.timer(seconds=0.2)
    dead.image = 'images/dead2.png'
    await play.timer(seconds=0.2)
    dead.image = 'images/dead3.png'
    await play.timer(seconds=0.2)
    dead.image = 'images/dead4.png'
    await play.timer(seconds=0.2)
    dead.image = 'images/dead5.png'
    await play.timer(seconds=0.2)
    dead.image = 'images/dead6.png'
    await play.timer(seconds=0.2)
    dead.image = 'images/dead7.png'
    await play.timer(seconds=0.2)
    dead.image = 'images/dead8.png'
    await play.timer(seconds=0.2)

@play.repeat_forever
async def anim_key():
    key.y += 6
    await play.timer(seconds=0.4)
    key.y -= 6
    await play.timer(seconds=0.4)

@play.repeat_forever
async def anim_potion():
    global potion
    if potion != 1:
        health_potion.y += 3
        await play.timer(seconds=0.6)
        health_potion.y -= 3
        await play.timer(seconds=0.6)

play.start_program()