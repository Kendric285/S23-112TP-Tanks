
from cmu_graphics import *
import math, copy,decimal
from classes import *
from functions import *



def onAppStart(app): 
    app.cx = app.width/2
    app.cy = app.height/2
    app.dx = 2
    app.dy = 1
    app.rectWidth = 100
    app.rectHeight = 50
    app.playerX = app.width/2
    app.playerY = app.height/2
    app.player = Player(3,10,app.width/2,app.height/2,0,0)
    app.game = TankGame(app.player,[])

def onMousePress(app, mouseX, mouseY):
    app.cx = mouseX
    app.cy = mouseY

def onStep(app):
    left = app.cx - app.rectWidth/2
    right = app.cx + app.rectWidth/2
    top = app.cy - app.rectHeight/2
    bottom = app.cy + app.rectHeight/2
    if left < 0: app.dx = abs(app.dx)
    elif right > app.width: app.dx = -abs(app.dx)

    if top < 0: app.dy = abs(app.dy)
    elif bottom > app.height: app.dy = -abs(app.dy)

    app.cx += app.dx
    app.cy += app.dy

def redrawAll(app):
    app.game.drawPlayer()
    
    


def main():
    runApp()

if __name__ == '__main__':
    main()
