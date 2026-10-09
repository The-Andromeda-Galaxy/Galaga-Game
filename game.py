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
    global score,speed,lives

    #move ship left/right
    if keyboard.left:
        ship.x -= speed
        if ship.x <= 0:
            ship.x = 0
    elif keyboard.right:
        ship.x += speed
        if ship.x>= WIDTH:
            ship.x = WIDTH

    #bullet movement
    for bullet in bullets:
        if bullet.y<=0:
            bullets.remove(bullet)
        else:
            bullet.y -= 10

    #enemies movement
    for enemy in enemies:
        enemy.y += 5
        if enemy.y > HEIGHT:
            enemy.x = random.randint(0,1000)
            enemy.y = random.randint(-30,0)

        #collision with bullet
        for bullet in bullets:
            if enemy.colliderect(bullet):
                score +=100
                sounds.eep.play()
                if bullet in bullets:
                    bullets.remove(bullet)
                if enemy in enemies:
                    enemies.remove(enemy)
                break

        #collision with ship
        if enemy.colliderect(ship):
            lives -=1
            if enemy in enemies:
                enemies.remove(enemy)
            if lives == 0:
                game_over()

    #recreating enemies
    if len(enemies) < 8:
        enemy = Actor("enemy")
        enemy.x = random.randint(0,1000)
        enemy.y = random.randint(-30,0)
        enemies.append(enemy)

def game_over():
    global is_game_over
    is_game_over = True

def game_over_screen():
    screen.clear()
    screen.fill("#2C5554")
    screen.draw.text("GAME OVER!!",(CENTER_X,CENTER_Y),fontsize = 50,color = "white")
    screen.draw.text(f"Your score is {score}", (CENTER_X,CENTER_Y+50),fontsize = 40, color ="white")
    screen.draw.text("Press the SPACE key to play again!",(CENTER_X,CENTER_Y+80),fontsize = 40, color ="white") 
           














pgzrun.go()