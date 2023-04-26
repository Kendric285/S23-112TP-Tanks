from cmu_graphics import *
import math

def distance(x1, y1, x2, y2):
    x = x2 - x1 
    x_two = x*x
    y = y2 - y1
    y_two = y*y
    d = math.sqrt(x_two + y_two)
    return d

#rows cols within the border
def translator(row,col):
    x = 188 + (38 * row)
    y = 158 + (38 * col)
    return (x,y)

#just the whole board
def wholeBoardTranslator(row,col):
    x = 150 + (38 * row)
    y = 120 + (38 * col)
    return (x,y)

def XYtoRowCol(x,y):
    row = (x - 150) // 38
    col = (y - 120) // 38
    return (int(row),int(col))

def isClicked(centerx,centery,mousex,mousey,height,width):
    xmin = centerx - (width / 2)
    xmax = centerx + (width / 2)
    ymin = centery - (height / 2)
    ymax = centery + (height / 2)
    if (mousex > xmin and mousex < xmax) and (mousey > ymin and mousey < ymax):
        return True
    return False
