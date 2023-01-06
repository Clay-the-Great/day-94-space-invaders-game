from turtle import Screen
import time
from invader import Invader
from spaceship import Spaceship
from bullet import Bullet
from enemy_bullet import EnemyBullet
from scoreboard import Scoreboard

MOVE_DISTANCE = 10
x_move_distance = MOVE_DISTANCE
y_move_distance = MOVE_DISTANCE
delay_time = 0.01
ready_to_fire = True
game_on = True
bullet = Bullet()
bullet.goto(0, 400)

invaders = []
invader_direction = "right"
enemy_bullets = []
ship = Spaceship()
scoreboard = Scoreboard()


def fire():
    global bullet
    if ready_to_fire:
        bullet = Bullet()
        bullet.goto(ship.xcor(), -250)
        bullet.move()


def reset():
    global invaders, invader_direction, enemy_bullets, game_on
    game_on = True
    for invader in invaders:
        invader.disappear()
    invaders = []
    invader_positions = []
    for i in range(2):
        for j in range(5):
            invader_positions.append([-140 + 70 * j, 260 - 50 * i])
    invaders = [Invader(position[0], position[1]) for position in invader_positions]
    scoreboard.score = 0
    scoreboard.life_number = 2
    for enemy_bullet in enemy_bullets:
        enemy_bullet.hideturtle()
    enemy_bullets = []
    invader_direction = "right"
    scoreboard.display()
    game()


screen = Screen()
screen.setup(width=800, height=600)
screen.bgpic("static/space.gif")
screen.title("Space Invaders")
screen.register_shape("static/invader.gif")
screen.listen()
screen.onkey(fire, "space")
screen.onkey(ship.move_left, "Left")
screen.onkey(ship.move_right, "Right")
screen.onkey(reset, "r")


def game():
    global ready_to_fire, game_on, invader_direction, enemy_bullets, invaders
    while game_on:
        # time.sleep(delay_time)
        screen.update()

        if bullet.ycor() < 310:
            ready_to_fire = False
            bullet.move()
        else:
            ready_to_fire = True
        # loop through the invaders
        for invader in invaders:
            # enemy hit by our missile
            if bullet.ycor() > 200 and invader.visible and bullet.distance(invader) < 15:
                invader.disappear()
                bullet.disappear()
                bullet.forward(200)
                scoreboard.increase_score()
                # victory
                if scoreboard.score == 10:
                    game_on = False
                    scoreboard.victory()

            # enemy shoots
            if invader.visible and invader.fire():
                enemy_bullet = EnemyBullet()
                enemy_bullet.goto(invader.xcor(), invader.ycor())
                enemy_bullets.append(enemy_bullet)

        # iterate through the enemy bullets
        for em_bullet in enemy_bullets:
            if em_bullet.ycor() < -300:
                enemy_bullets.remove(em_bullet)
            em_bullet.move()
            # bullets cancel out
            if em_bullet.xcor() == bullet.xcor() and em_bullet.distance(bullet) < 15:
                em_bullet.hideturtle()
                enemy_bullets.remove(em_bullet)
                bullet.disappear()
                bullet.forward(600)
            # ship hit by enemy bullet
            if ship.distance(em_bullet) < 20:
                time.sleep(0.5)
                scoreboard.decrease_life()
                # defeat
                if scoreboard.life_number == 0:
                    game_on = False
                    scoreboard.defeat()

                for current_bullet in enemy_bullets:
                    current_bullet.hideturtle()
                ship.goto(0, -250)
                enemy_bullets = []

        if invader_direction == "right":
            for invader in invaders:
                invader.move_right()
        else:
            for invader in invaders:
                invader.move_left()

        if invaders[0].xcor() < -350:
            invader_direction = "right"

        if invaders[4].xcor() > 350:
            invader_direction = "left"


reset()
game()

screen.exitonclick()
