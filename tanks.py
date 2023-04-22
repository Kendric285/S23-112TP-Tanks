from cmu_graphics import *
import math, copy,decimal
import random
import pprint
from random import randint
from functions import *
from classes import *

def reset(app):
    app.pause = False
    app.gameState = 'game'
    app.gameOver = False
    app.playerX = app.width/2
    app.playerY = app.height/2
    x,y = translator(0.5,12.5)
    app.player = Player(3,10,x,y,0,0,0,0)
    app.game = TankGame(app.player,[],[])
    app.balls = []
    app.step = 0
    randx = randint(169,701)
    randy = randint(139,671)
    app.enemies = [Enemy((randx),(randy), 0,0)]
    app.drag = False
    app.pause = True
    app.bullets = 10
    app.lives = 3
    app.wave = 1
    app.money = 10
    app.barriers = [(8,3),(9,3),(10,3),(11,3),(12,3),(12,4),(12,5),(12,6),(12,7),
                    (9,6),(8,7),(7,8),(6,9),
                    (3,7),(3,8),(3,9),(3,10),(3,11),(3,12),(4,12),(5,12),(6,12),(7,12),(8,12)]
    app.board = [[1 if row == 0 or col == 0 or row == 15 or col == 15 else 0 for col in range(16)] for row in range(16)]
    makeBarriers(app,app.barriers)
    pprint.pprint(app.board)
    app.gameBoard = GameBoard(app.board)

def importantData(app):
    drawLabel(f'Lives: {app.lives}', 50,50,size = 15)
    drawLabel(f'Bullets: {app.bullets}', 50,75, size = 15)
    drawLabel(f'Wave: {app.wave}', 50,100, size = 15)
    drawLabel(f'Money: ${app.money}', 50,125, size = 15)
    x,y = XYtoRowCol(app.player.x,app.player.y)
    app.board[x][y] == 5
    drawLabel(f'X: {x}, Y: {y}', 50,150, size = 15)

def onAppStart(app): 
    app.width = 800
    app.height = 800
    app.gameState = 'home'

def onMouseMove(app, mouseX, mouseY):
    if app.gameState == 'game':
        app.player.mouseX = mouseX
        app.player.mouseY = mouseY

def onMousePress(app, mouseX, mouseY):
    if app.gameState == 'home':
        reset(app)

def onMouseRelease(app, mouseX, mouseY):
    if app.gameState == 'game':
        ballX,ballY = app.player.endOfBarrel()
        if app.bullets != 0:
            app.balls.append(Ball(ballX,ballY,0,app.player.body_direction,(1/2)*(app.player.tankAddX), (1/2) * app.player.tankAddY))
            app.bullets -= 1
            app.drag = False
    
def onStep(app):
    if app.gameState == 'game' and app.pause:
        app.step += 1
        if app.enemies == []:
            app.wave += 1
            for i in range(0,app.wave):
                randx = randint(169,701)
                randy = randint(139,671)
                app.enemies.append(Enemy((randx),(randy), 0,0))
        if app.balls != []:
            isTouching(app,app.balls)
            checkBallWallCollision(app, app.balls)
            updateBallPosition(app, app.balls)
            hitEnemy(app,app.balls,app.enemies)
        if app.step % 50 == 0:
            enemyShoot(app,app.enemies)

def updateBallPosition(app,balls):
    if app.gameState == 'game':
        for ball in balls:
            ball.x += ball.plusX
            ball.y += ball.plusY

def checkBallWallCollision(app,balls):
    if app.gameState == 'game':
        for ball in balls:
            if (ball.x < 179 ) or (ball.x > 701 - 5):
                ball.contacts += 1
                if ball.contacts > 2:
                    app.balls.remove(ball)
                else:
                    ball.plusX = ball.plusX * (-1)
            if (ball.y > 671 - 5) or (ball.y < 139 + 5):
                ball.contacts += 1
                if ball.contacts > 2:
                    if ball in app.balls:
                        app.balls.remove(ball)
                else:
                    ball.plusY = ball.plusY * (-1)
            hitBarriers(app,ball)
               
    
def store(app):
    drawLabel('Store Bois', app.width/2, 100, size = 16)
    drawRect(app.width/2, 300, 150,50,align= 'center', fill = 'green')
    drawLabel('Buy ammo', app.width/2, 300, size = 16)
    drawRect(app.width/2, 375, 150,50,align= 'center', fill = 'blue')
    drawLabel('Buy Lives', app.width/2, 375, size = 16)
    drawRect(app.width/2, 450, 150,50,align= 'center', fill = 'yellow')
    drawLabel('Buy Speed', app.width/2, 450, size = 16)

    importantData(app)

def onKeyPress(app,key):
    randx = randint(200,app.width)
    randy = randint(200,app.height)

    if app.gameState == 'game':
        if key == 'r':
            app.enemies.append(Enemy((randx),(randy), 0,0))
        if key == 'c':
            app.enemies = []
        if key == 'l':
            reset(app)
        if key == 'q' :
            app.gameState = 'store'
        if key == 'p':
            app.pause = not app.pause
    elif app.gameState == 'store': 
        if key == 'q':
            app.gameState = 'game'

def onKeyHold(app,keys):
    if app.gameState == 'game':
        angle = app.player.body_direction
        radians = math.radians(angle)
        if 'w' in keys:
            # potentialX = app.player.x + (20 * math.cos(radians))
            # potentialY = app.player.y - (20 * math.sin(radians))
            # if  (potentialX < 0 or potentialX > app.width or potentialY < 0 or potentialY > app.height):
            #     app.player.y -= (20 * math.cos(radians))
            #     app.player.x += (20 * math.sin(radians))
            #app.player.y -= (20 * math.cos(radians))
            #app.player.x += (20 * math.sin(radians))


            potentialX = app.player.x + (50 * math.sin(radians))
            potentialY = app.player.y - (50 * math.cos(radians))
            row,col = XYtoRowCol(potentialX,potentialY)
            print()
            if app.board[row][col] == 0:    
            # if not (potentialX < 0 or potentialX > app.width or potentialY < 0 or potentialY > app.height):
                app.player.y -= (20 * math.cos(radians))
                app.player.x += (20 * math.sin(radians))

        elif 's' in keys:
            potentialX = app.player.x - (50 * math.cos(radians))
            potentialY = app.player.y + (50 * math.sin(radians))
            row,col = XYtoRowCol(potentialX,potentialY)
            if app.board[row][col] == 0:
            #if not (potentialX < 0 or potentialX > app.width or potentialY < 0 or potentialY > app.height):
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
        enemy.body_direction += 0.5
        #enemy.rotate(app.player.body_direction)
        enemy.move()
        if (enemy.x < 0 or enemy.x > app.width or enemy.y < 0 or enemy.y > app.height):
            app.enemies.remove(enemy)

def redrawAll(app):
    print(app.gameState)
    print(app.width)
    print(app.height)
    if app.gameState == 'home':
        drawLabel('Welcome To Tanks', app.width/2,100,size = 20)
        drawLabel('Click Anywhere to Start', app.width/2,125,size = 20)

    elif app.gameState == 'game':
        importantData(app)
        app.gameBoard.drawBoard()
        drawLine(app.player.mouseX - 5, app.player.mouseY - 5, app.player.mouseX + 5, app.player.mouseY + 5, fill = 'white')
        drawLine(app.player.mouseX - 5, app.player.mouseY + 5, app.player.mouseX + 5, app.player.mouseY - 5, fill = 'white')
        drawLine(app.player.mouseX, app.player.mouseY, app.player.x,app.player.y, dashes = True, fill = 'white' )
        drawBalls(app,app.balls)
        app.player.drawPlayer()
        drawEnemies(app,app.enemies)
        
    elif app.gameState == 'store':
        store(app)

def isTouching(app,balls):
    for ball in balls:
        if distance(ball.x, ball.y, app.player.x, app.player.y) <= (21 * math.sqrt(2)):
            app.balls = []
            app.player.x, app.player.y = translator(0.5,12.5)
            app.lives -= 1
            if app.lives == 0:
                app.gameState = 'home'
                #reset(app)

def hitEnemy(app,balls,enemies):
    for ball in balls:
        for enemy in enemies:
            if distance(ball.x, ball.y, enemy.x, enemy.y) <= (21 * math.sqrt(2)):
                enemies.remove(enemy)
                balls.remove(ball)
                app.money += 1

def makeBarriers(app,list):
    for x,y in list:
        app.board[x][y] = 1

def hitBarriers(app, ball):
    for row,col in app.barriers:
        barrierx,barriery = wholeBoardTranslator(row,col)
        if distance(ball.x,ball.y,barrierx,barriery) <= 30:
            ball.contacts += 1
            dx = abs(ball.x - barrierx)
            dy = abs(ball.y - barriery)
            if dx > dy:
                ball.plusX = ball.plusX * (-1)
            else:
                ball.plusY = ball.plusY * (-1)

def main():
    runApp()

if __name__ == '__main__':
    main()
