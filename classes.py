
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

        tankX = getLineCoorX(self.x,self.y,self.mouseX,self.mouseY)
        tankY = getLineCoorY(self.x,self.y,self.mouseX,self.mouseY)
        #wheels, top square, 
        drawRect(self.x,self.y,65,45,rotateAngle = self.body_direction,fill = "grey", align = "center")
        drawRect(self.x,self.y,50,50,rotateAngle = self.body_direction,fill = "black", align = "center")
        drawLine(frontX1,frontY1,frontX2,frontY2,fill = 'red', lineWidth = 5)
        drawLine(self.x,self.y,self.x + tankX, self.y + tankY, fill = 'orange', lineWidth = 10)
        drawCircle(self.x,self.y,10, fill = 'grey',align= "center")
        
def getLineCoorX(x1,y1,mouseX,mouseY):
    hypotenuse = distance(x1,y1,mouseX,mouseY)
    if mouseY > y1:
        adjacent = mouseY - y1
        theta = math.acos(adjacent/hypotenuse)
        xAdd = 100 * math.sin(theta)

        return xAdd if mouseX > x1 else (-xAdd)

    elif y1 > mouseY:
        opposite = y1 - mouseY
        theta = math.asin(opposite/hypotenuse)
        xAdd = 100 * math.cos(theta)

        return xAdd if mouseX > x1 else (-xAdd)

def getLineCoorY(x1,y1,mouseX,mouseY):
    hypotenuse = distance(x1,y1,mouseX,mouseY)
    if mouseY > y1:
        adjacent = mouseY - y1
        theta = math.acos(adjacent/hypotenuse)
        yAdd = 100 * math.cos(theta)

        return yAdd

    elif y1 > mouseY:
        opposite = y1 - mouseY
        theta = math.asin(opposite/hypotenuse)
        yAdd = 100 * math.sin(theta)

        return (-yAdd)
    