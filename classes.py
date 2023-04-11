
from cmu_graphics import *
import math, copy, decimal
from functions import *
#4 hours on 4/10

class TankGame:
    def __init__(self,player,enemies, balls):
        self.player = player
        self.enemies = enemies

class Ball:
    def __init__(self,x,y,contacts,angle,plusX,plusY):
        self.x = x
        self.y = y
        self.contacts = contacts
        self.angle = angle
        self.plusX = plusX
        self.plusY = plusY
    def updateXY(self):

        self.x += 4
        self.y += 4

    def __repr__(self):
        return f'Ball x:{self.x}, y:{self.y}, angle:{self.angle}'
    

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
        self.tankAddX, self.tankAddY = lcoor(self.x, self.y, self.mouseX, self.mouseY)
    def drawPlayer(self):
        theta = math.radians(self.body_direction - 45)
        self.bullet_direction = theta
        frontX1 = (self.x + (50/2) * math.sin(theta))
        frontY1 = (self.y - (50/2) * math.cos(theta))
        frontX2 = (self.x + (50/2) * math.cos(theta))
        frontY2 = (self.y + (50/2) * math.sin(theta))


        self.tankAddX, self.tankAddY = lcoor(self.x, self.y, self.mouseX, self.mouseY)

        # tankX = getLineCoorX(self.x,self.y,self.mouseX,self.mouseY)
        # tankY = getLineCoorY(self.x,self.y,self.mouseX,self.mouseY)
        #wheels, top square, 
        drawRect(self.x,self.y,65,45,rotateAngle = self.body_direction,fill = "grey", align = "center")
        drawRect(self.x,self.y,50,50,rotateAngle = self.body_direction,fill = "black", align = "center")
        drawLine(frontX1,frontY1,frontX2,frontY2,fill = 'red', lineWidth = 5)
        drawLine(self.x,self.y,self.x + self.tankAddX, self.y + self.tankAddY, fill = 'orange', lineWidth = 10)
        drawCircle(self.x,self.y,10, fill = 'grey',align= "center")
    def endOfBarrel(self):
        tankX = self.x + self.tankAddX
        tankY = self.y + self.tankAddY
        return (tankX,tankY)
    
# class Enemy:
#     def __init__(self,x,y,bullet_direction,body_direction,mouseX, mouseY):
#         self.lives = 

def lcoor(x1,y1,mouseX,mouseY):
    r = distance(x1,y1,mouseX,mouseY)
    dx = mouseX - x1
    dy = mouseY - y1
    return (((dx / r) * 30), ((dy / r) * 30))


