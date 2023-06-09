from cmu_graphics import *
import math, copy, decimal
from functions import *

class GameBoard:
    def __init__(self,board):
        self.board = board
    def drawBoard(self):
        cols = len(self.board[0])
        rows = len(self.board)
        for row in range(rows):
            for col in range(cols):
                if self.board[row][col] == 1:
                    drawRect((150 + (col * 38)),(120 + (row * 38)), 38,38,fill = 'green', align = 'center', border = 'green')
                else:
                    drawRect((150 + (col * 38)),(120 + (row * 38)), 38,38,fill = 'black', align = 'center')
class TankGame:
    def __init__(self,player,enemies, balls):
        self.player = player
        self.enemies = enemies

class Ball:
    def __init__(self,x,y,contacts,angle,plusX,plusY,type):
        self.x = x
        self.y = y
        self.contacts = contacts
        self.angle = angle
        self.plusX = plusX
        self.plusY = plusY
        self.type = type
    def updateXY(self):

        self.x += 8
        self.y += 8

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
     
        drawRect(self.x,self.y,55,35,rotateAngle = self.body_direction,fill = "grey", align = "center")
        self.base = drawRect(self.x,self.y,40,40,rotateAngle = self.body_direction,fill = "black", align = "center")
        drawLine(frontX1,frontY1,frontX2,frontY2,fill = 'red', lineWidth = 5)
        drawLine(self.x,self.y,self.x + self.tankAddX, self.y + self.tankAddY, fill = 'orange', lineWidth = 10)
        drawCircle(self.x,self.y,10, fill = 'grey',align= "center")
    def endOfBarrel(self):
        tankX = self.x + self.tankAddX
        tankY = self.y + self.tankAddY
        return (tankX,tankY)
    
    
class Enemy:
    def __init__(self,x,y,bullet_direction,body_direction,movement):
        self.x = x
        self.y = y
        self.body_direction = body_direction
        self.tankAddX, self.tankAddY = (0,0)
        self.movement = movement
        if self.movement == 'updown':
            self.moving = 'down'
        if self.movement == 'leftright':
            self.moving = 'left'
    def rotate(self,final_angle):
        self.body_direction = final_angle
    def move(self):
        if self.movement == 'updown':
            if self.moving == 'down' and self.y < 652:
                self.y += 9.5
                if self.y >= 652:
                    self.moving = 'up'
            elif self.moving == 'up' and self.y > 158:
                self.y -= 9.5
                if self.y <= 158:
                    self.moving = 'down'
        elif self.movement == 'leftright':
            if self.moving == 'left' and self.x > 188:
                self.x -= 9.5
                if self.x <= 188:
                    self.moving = 'right'
            elif self.moving == 'right' and self.x < 682:
                self.x += 9.5
                if self.x >= 682:
                    self.moving = 'left'

    def drawEnemy(self,playerX,playerY):
        theta = math.radians(self.body_direction - 45)
        self.bullet_direction = theta
        frontX1 = (self.x + (50/2) * math.sin(theta))
        frontY1 = (self.y - (50/2) * math.cos(theta))
        frontX2 = (self.x + (50/2) * math.cos(theta))
        frontY2 = (self.y + (50/2) * math.sin(theta))
        self.body_direction = self.bullet_direction
        self.tankAddX, self.tankAddY = lcoor(self.x, self.y, playerX, playerY)

        drawRect(self.x,self.y,65,45,rotateAngle = self.body_direction,fill = "grey", align = "center")
        self.base = drawRect(self.x,self.y,50,50,rotateAngle = self.body_direction,fill = "blue", align = "center")
        drawLine(frontX1,frontY1,frontX2,frontY2,fill = 'orange', lineWidth = 5)
        drawLine(self.x,self.y,self.x + self.tankAddX, self.y + self.tankAddY, fill = 'orange', lineWidth = 10)
        drawCircle(self.x,self.y,10, fill = 'yellow',align= "center")
    def endOfBarrel(self):
        tankX = self.x + self.tankAddX
        tankY = self.y + self.tankAddY
        return (tankX,tankY)
    
def lcoor(x1,y1,mouseX,mouseY):
    r = distance(x1,y1,mouseX,mouseY)
    dx = mouseX - x1
    dy = mouseY - y1
    return (((dx / r) * 30), ((dy / r) * 30))

