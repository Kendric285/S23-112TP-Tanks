
from cmu_graphics import *
import math, copy,decimal
from functions import *

class TankGame:
    def __init__(self,player,enemies):
        self.player = player
        self.enemies = enemies
    def drawPlayer(self):
        #wheels, top square, 
        drawRect(200,200,65,45,rotateAngle = self.player.bodyDirection,fill = "grey", align = "center")
        drawRect(200,200,50,50,rotateAngle = self.player.bodyDirection,fill = "black", align = "center")
        #drawLine(200,200,50,50, fill = 'orange', lineWidth = 10)
        drawCircle(200,200,10, fill = 'grey',align= "center")

class Player:
    def __init__(self,lives,bullets,x,y,bullet_direction,body_direction):
        self.lives = lives
        self.bullets = bullets
        self.x = x
        self.y = y
        self.bullet_direction = bullet_direction
        self.body_direction = body_direction
    
        
    