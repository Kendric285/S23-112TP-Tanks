
from cmu_graphics import *
import math, copy, decimal
from functions import *

class TankGame:
    def __init__(self,player,enemies):
        self.player = player
        self.enemies = enemies
    

class Player:
    def __init__(self,lives,bullets,x,y,bullet_direction,body_direction,mouseX, mouseY):
        self.lives = lives
        self.bullets = bullets
        self.x = x
        self.y = y
        self.bullet_direction = bullet_direction
        self.body_direction = body_direction
        self.mouseX = mouseX
        self.mouseY = mouseY
    def drawPlayer(self):
        theta = math.radians(self.body_direction - 45)

        frontX1 = (self.x + (50/2) * math.sin(theta))
        frontY1 = (self.y - (50/2) * math.cos(theta))
        frontX2 = (self.x + (50/2) * math.cos(theta))
        frontY2 = (self.y + (50/2) * math.sin(theta))
        #wheels, top square, 
        r = drawRect(self.x,self.y,65,45,rotateAngle = self.body_direction,fill = "grey", align = "center")
        drawRect(self.x,self.y,50,50,rotateAngle = self.body_direction,fill = "black", align = "center")
        drawLine(frontX1,frontY1,frontX2,frontY2,fill = 'red', lineWidth = 5)
        drawLine(self.x,self.y,self.mouseX, self.mouseY,fill = 'green', lineWidth = 5, fill = 'orange', lineWidth = 10)
        drawCircle(self.x,self.y,10, fill = 'grey',align= "center")
        
def getLineCoorX(x1,y1,mouseX,mouseY):
    adjacent = mouseY - y1
    hypotenuse = distance(x1,y1,mouseX,mouseY)
    r = math.radians(adjacent/hypotenuse)
    theta = math.acos(r)
    x = math.sqrt((hypotenuse**2) - (adjacent**2))
    print(f'poopo{x}')
    print(0)
    return 10 * math.sin(theta)

def getLineCoorY(x1,y1,mouseX,mouseY):
    adjacent = mouseY - y1
    hypotenuse = distance(x1,y1,mouseX,mouseY)
    r = math.radians(adjacent/hypotenuse)
    theta = math.acos(r)
    return 10 * math.cos(theta)
