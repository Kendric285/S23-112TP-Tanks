
from cmu_graphics import *
import math, copy,decimal
from functions import *

def almostEqual(d1, d2, epsilon=10**-7): #helper-fn
    # note: use math.isclose() outside 15-112 with Python version 3.5 or later
    return (abs(d2 - d1) < epsilon)

def roundHalfUp(d): #helper-fn
    # Round to nearest with ties going away from zero.
    rounding = decimal.ROUND_HALF_UP
    # See other rounding options here:
    # https://docs.python.org/3/library/decimal.html#rounding-modes
    return int(decimal.Decimal(d).to_integral_value(rounding=rounding))

def isBorderish(L):
    outerSum = 0
    innerSum = 0
    rows,cols = len(L), len(L[0])

    for row in range(rows):
        for col in range(cols):
            firstOrLastRow = row == 0 or row == (rows-1)
            firstOrLastCol = col == 0 or col == (cols-1)
            if (firstOrLastRow) or firstOrLastCol:
                outerSum += L[row][col]
            else:
                innerSum += L[row][col]
    if innerSum == outerSum:
        return True
    return False
def swapCols(L,col1,col2):
    rows,cols = len(L), len(L[0])
    M = copy.deepcopy(L)
    for row in range(rows):
        for col in range(cols):
            if col == col1:
                L[row][col] = M[row][col2]
            elif col == col2:
                L[row][col] = M[row][col1]
def makeBorderish(L):
    rows,cols = len(L), len(L[0])
    for i in range(cols):
        for j in range(cols):
            swapCols(L,i,j)
            if isBorderish(L):
                return None
            swapCols(L,j,i)


def testMakeBorderish():
    print('Testing makeBorderish()...', end='')
    L = [ [ 1, 0, 2, 1 ],
          [ 2, 5, 0, 4 ],
          [ 1, 1, 1, 0 ]
        ]
    M = [ [ 1, 0, 1, 2 ],
          [ 2, 5, 4, 0 ],
          [ 1, 1, 0, 1 ]
        ]
    assert(makeBorderish(L) == None)
    assert(L == M)

    L = [ [ 2, 0, 1 ],
          [ 8, 0, 2 ],
          [ 1, 1, 1 ]
        ]
    M = [ [ 0, 2, 1 ],
          [ 0, 8, 2 ],
          [ 1, 1, 1 ]
        ]
    assert(makeBorderish(L) == None)
    assert(L == M)

    L = [ [ 2, 0, 1 ],
          [ 8, 0, 2 ],
          [ 5, 1, 1 ],
          [ 1, 2, 3 ]
        ]
    M = [ [ 0, 2, 1 ],
          [ 0, 8, 2 ],
          [ 1, 5, 1 ],
          [ 2, 1, 3 ]
        ]
    assert(makeBorderish(L) == None)
    assert(L == M)
    print('Passed')

#################################################
# Test animation 
#################################################

def onAppStart(app):
    app.cx = app.width/2
    app.cy = app.height/2
    app.dx = 2
    app.dy = 1
    app.rectWidth = 100
    app.rectHeight = 50
    
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
    drawRect(app.cx, app.cy, app.rectWidth, app.rectHeight, 
             align = 'center', fill = 'green')
    drawLabel(f"{add(1,2)}", app.cx, app.cy, size = 20, fill = 'white')
    drawLabel("cmu_graphics is installed!", app.width/2, 20, size = 20)
    
#################################################
# main
#################################################

def main():
    testMakeBorderish()
    runApp()

if __name__ == '__main__':
    main()
