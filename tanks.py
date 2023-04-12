
from cmu_graphics import *
import math, copy,decimal
import random
from random import randint
from functions import *
from classes import *


def reset(app):
    app.gameOver = False
    app.playerX = app.width/2
    app.playerY = app.height/2
    app.player = Player(3,10,app.width/2,app.height/2,0,0,0,0)
    app.game = TankGame(app.player,[],[])
    app.balls = []
    app.step = 0
    app.enemies = []

def onAppStart(app): 
    reset(app)

def onMouseMove(app, mouseX, mouseY):
    app.player.mouseX = mouseX
    app.player.mouseY = mouseY

def onMousePress(app, mouseX, mouseY):
    ballX,ballY = app.player.endOfBarrel()
    app.balls.append(Ball(ballX,ballY,0,app.player.body_direction,app.player.tankAddX, app.player.tankAddY))
    
def onStep(app):
    app.step += 1
    if app.balls != []:
        checkBallWallCollision(app, app.balls)
        updateBallPosition(app.balls)
        isTouching(app,app.balls)
    if app.step % 50 == 0:
        enemyShoot(app,app.enemies)
def updateBallPosition(balls):
    for ball in balls:
        ball.x += ball.plusX
        ball.y += ball.plusY

def checkBallWallCollision(app,balls):
    for ball in balls:
        if (ball.x < 5 ) or (ball.x > app.width - 5):
            ball.contacts += 1
            if ball.contacts > 1:
                app.balls.remove(ball)
            else:
                ball.plusX = ball.plusX * (-1)
        if (ball.y > app.height - 5) or (ball.y < 5):
            ball.contacts += 1
            if ball.contacts > 1:
                app.balls.remove(ball)
            else:
                ball.plusY = ball.plusY * (-1)

def onKeyPress(app,key):
    randx = randint(200,app.width)
    randy = randint(200,app.height)

    if key == 'r':
        app.enemies.append(Enemy((randx),(randy), 0,0))
    if key == 'c':
        app.enemies = []
    if key == 'l':
        reset(app)
def onKeyHold(app,keys):
    angle = app.player.body_direction
    radians = math.radians(angle)
    if 'w' in keys:
        app.player.y -= (20 * math.cos(radians))
        app.player.x += (20 * math.sin(radians))
    elif 's' in keys:
        app.player.y += (20 * math.cos(radians))
        app.player.x -= (20 * math.sin(radians))
    if 'd' in keys:
        app.player.body_direction += 10
    elif 'a' in keys:
        app.player.body_direction -= 10
def enemyShoot(app,enemies):
    for enemy in enemies:
        ballX,ballY = enemy.endOfBarrel()
        app.balls.append(Ball(ballX,ballY,0,app.player.body_direction,enemy.tankAddX,enemy.tankAddY))

def drawBalls(app,balls):
    for ball in balls:
        circle = drawCircle(ball.x, ball.y, 5, fill = "red")
       
def drawEnemies(app,enemies):
    for enemy in enemies:
        enemy.drawEnemy(app.player.x, app.player.y)

def redrawAll(app):
    if not app.gameOver:
        app.player.drawPlayer()
        drawEnemies(app,app.enemies)
        drawBalls(app,app.balls)

def isTouching(app,balls):
    for ball in balls:
        if distance(ball.x, ball.y, app.player.x, app.player.y) <= (13 * math.sqrt(2)):
            app.gameOver = True

def main():
    runApp()

if __name__ == '__main__':
    main()
