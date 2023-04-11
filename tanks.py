
from cmu_graphics import *
import math, copy,decimal
from functions import *
from classes import *

def onAppStart(app): 
    app.playerX = app.width/2
    app.playerY = app.height/2
    app.player = Player(3,10,app.width/2,app.height/2,0,0,0,0)
    app.game = TankGame(app.player,[],[])
    app.balls = []
    app.step = 0

def onMouseMove(app, mouseX, mouseY):
    app.player.mouseX = mouseX
    app.player.mouseY = mouseY

def onMousePress(app, mouseX, mouseY):
    ballX,ballY = app.player.endOfBarrel()
    app.balls.append(Ball(ballX,ballY,0,app.player.body_direction,app.player.tankAddX, app.player.tankAddY))
    
def onStep(app):
    if app.balls != []:
        checkBallCollision(app, app.balls)
        updateBallPosition(app.balls)
    
def updateBallPosition(balls):
    for ball in balls:
        ball.x += ball.plusX
        ball.y += ball.plusY
def checkBallCollision(app,balls):
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
    return True

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

def drawBalls(balls):
    for ball in balls:
        drawCircle(ball.x, ball.y, 5, fill = "red")

def redrawAll(app):
    app.player.drawPlayer()
    drawBalls(app.balls)


def main():
    runApp()

if __name__ == '__main__':
    main()
