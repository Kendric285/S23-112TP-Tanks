
from cmu_graphics import *
import math, copy,decimal
from functions import *
from classes import *

def onAppStart(app): 
    app.playerX = app.width/2
    app.playerY = app.height/2
    app.player = Player(3,10,app.width/2,app.height/2,0,0,0,0)
    app.game = TankGame(app.player,[])

def onMouseMove(app, mouseX, mouseY):
    app.player.mouseX = mouseX
    app.player.mouseY = mouseY

def onKeyPress(app,key):
    return True

def onKeyHold(app,keys):
    angle = app.player.body_direction
    radians = math.radians(angle)
    if 'w' in keys:
        app.player.y -= (10 * math.cos(radians))
        app.player.x += (10 * math.sin(radians))
        print(app.player.y)
    elif 's' in keys:
        app.player.y += (10 * math.cos(radians))
        app.player.x -= (10 * math.sin(radians))
    if 'd' in keys:
        app.player.body_direction += 5
    elif 'a' in keys:
        app.player.body_direction -= 5

def redrawAll(app):
    app.player.drawPlayer()

def main():
    runApp()

if __name__ == '__main__':
    main()
