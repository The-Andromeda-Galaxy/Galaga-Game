import pgzrun,random

WIDTH =1200
HEIGHT = 600
TITLE = "GALAGA GAME"
CENTER_X = 600
CENTER_Y = 300
CENTER = (CENTER_X,CENTER_Y)

#game variables
score = 0
lives = 3
speed = 5
is_game_over = False
enemies = []
bullets = []

#ship
ship = Actor("ship.png")
ship.pos = (CENTER_X,HEIGHT-60)

#enemies
for i in range(8):
    enemy = Actor("enemy")
    enemy.x = random.randint(0,1000)
    enemy.y = random.randint(-30,0)
    enemies.append(enemy)

#score and lives display
def score_and_lives_display():
    screen.draw.text(f"Score:{score}",(50,30),fontsize= 50)
    screen.draw.text(f"Lives:{lives}",(50,60),fontsize= 50)

#create bullets
def on_key_down(key):
    if key == keys.SPACE:
        bullet = Actor("bullet")
        bullet.x = ship.x
        bullet.y = ship.y-50
        bullets.append(bullet)

#draw
def draw():
    if lives > 0:
        screen.clear()
        screen.fill("#053D4A")
        ship.draw()
        for enemy in enemies:
            enemy.draw()
        for bullet in bullets:
            bullet.draw()
        score_and_lives_display()
    else:
        game_over_screen()

def update():
    pass














pgzrun.go()