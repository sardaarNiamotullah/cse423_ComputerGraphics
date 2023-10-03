import random
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

id = list(map(int, str(input('Please enter your id: '))))
digit_1 = id[-2]
digit_2 = id[-1]
iniZone = None

def backTo_iniZone(x, y, iniZone):
    if (iniZone == 1):
        x, y = y, x
    elif (iniZone == 2):
        x, y = -y, x
    elif (iniZone == 3):
        x, y = -x, y
    elif (iniZone == 4):
        x, y = -x, -y
    elif (iniZone == 5):
        x, y = -y, -x
    elif (iniZone == 6):
        x, y = -y, x
    else:
        x, y = x, -y

    return [x, y]
def draw_points(x, y):
    global iniZone
    glPointSize(1)
    if (iniZone == 0):
        glBegin(GL_POINTS)
        glVertex2f(x, y)
        glEnd()
    else:
        points = backTo_iniZone(x, y, iniZone)
        x, y = points[0], points[1]
        glBegin(GL_POINTS)
        glVertex2f(x, y)
        glEnd()
def drawLine(x1, y1, x2, y2):
    draw_points(x1, y1)

    dx = x2 - x1
    dy = y2 - y1

    d = 2 * dy - dx
    x = x1
    y = y1

    while (x <= x2):
        x += 1
        if (d < 0):
            d += 2 * dy
        else:
            d += (2 * dy) - (2 * dx)
            y += 1
        draw_points(x, y)
def findZone(x1, y1, x2, y2):
    global iniZone
    delx = (x2 - x1)
    dely = (y2 - y1)
    delxabs = abs(x2 - x1)
    delyabs = abs(y2 - y1)

    if (delxabs > delyabs):  # it's fall under Zone 0, 3, 4, 7
        if (delx > 0 and dely > 0):
            iniZone = 0
        elif (delx < 0 and dely < 0):
            iniZone = 4
        elif (delx < 0 and dely > 0):
            iniZone = 3
        else:
            iniZone = 7
    else:  # it's fall under Zone 1, 2, 5, 6
        if (delx > 0 and dely > 0):
            iniZone = 1
        elif (delx < 0 and dely < 0):
            iniZone = 5
        elif (delx < 0 and dely > 0):
            iniZone = 2
        else:
            iniZone = 6
def convertToZone_0(x1, y1, x2, y2, iniZone):
    if (iniZone == 1):
        x1, y1 = y1, x1
        x2, y2 = y2, x2
    elif (iniZone == 2):
        x1, y1 = y1, -x1
        x2, y2 = y2, -x2
    elif (iniZone == 3):
        x1, y1 = -x1, y1
        x2, y2 = -x2, y2
    elif (iniZone == 4):
        x1, y1 = -x1, -y1
        x2, y2 = -x2, -y2
    elif (iniZone == 5):
        x1, y1 = -y1, -x1
        x2, y2 = -y2, -x2
    elif (iniZone == 6):
        x1, y1 = y1, -x1
        x2, y2 = y2, -x2
    else:
        x1, y1 = x1, -y1
        x2, y2 = x2, -y2

    return [x1, y1, x2, y2]
def drawLineSegment(line):
    findZone(*line)
    if (iniZone == 0):
        drawLine(*line)
    else:
        convertedPoints = convertToZone_0(*line, iniZone)
        drawLine(*convertedPoints)
    return
def drawDigit_1(digit):
    if (digit == 0):
        line = [-51, 150, -201, 151]
        drawLineSegment(line)
        line = [-199, -149, -200, 1]
        drawLineSegment(line)
        line = [-50, 0, -51, 150]
        drawLineSegment(line)
        line = [-199, -149, -49, -150]
        drawLineSegment(line)
        line = [-49, -150, -50, 0]
        drawLineSegment(line)
        line = [-200, 1, -201, 151]
        drawLineSegment(line)
    elif (digit == 1):
        line = [-50, 0, -51, 150]
        drawLineSegment(line)
        line = [-49, -150, -50, 0]
        drawLineSegment(line)
    elif (digit == 2):
        line = [-51, 150, -201, 151]
        drawLineSegment(line)
        line = [-199, -149, -200, 1]
        drawLineSegment(line)
        line = [-50, 0, -51, 150]
        drawLineSegment(line)
        line = [-199, -149, -49, -150]
        drawLineSegment(line)
        line = [-200, 1, -50, 0]
        drawLineSegment(line)
    elif (digit == 3):
        line = [-51, 150, -201, 151]
        drawLineSegment(line)
        line = [-49, -150, -50, 0]
        drawLineSegment(line)
        line = [-50, 0, -51, 150]
        drawLineSegment(line)
        line = [-199, -149, -49, -150]
        drawLineSegment(line)
        line = [-200, 1, -50, 0]
        drawLineSegment(line)
    elif (digit == 4):
        line = [-50, 0, -51, 150]
        drawLineSegment(line)
        line = [-49, -150, -50, 0]
        drawLineSegment(line)
        line = [-200, 1, -201, 151]
        drawLineSegment(line)
        line = [-200, 1, -50, 0]
        drawLineSegment(line)
    elif (digit == 5):
        line = [-51, 150, -201, 151]
        drawLineSegment(line)
        line = [-199, -149, -49, -150]
        drawLineSegment(line)
        line = [-49, -150, -50, 0]
        drawLineSegment(line)
        line = [-200, 1, -201, 151]
        drawLineSegment(line)
        line = [-200, 1, -50, 0]
        drawLineSegment(line)
    elif (digit == 6):
        line = [-51, 150, -201, 151]
        drawLineSegment(line)
        line = [-199, -149, -200, 1]
        drawLineSegment(line)
        line = [-199, -149, -49, -150]
        drawLineSegment(line)
        line = [-49, -150, -50, 0]
        drawLineSegment(line)
        line = [-200, 1, -201, 151]
        drawLineSegment(line)
        line = [-200, 1, -50, 0]
        drawLineSegment(line)
    elif (digit == 7):
        line = [-51, 150, -201, 151]
        drawLineSegment(line)
        line = [-50, 0, -51, 150]
        drawLineSegment(line)
        line = [-49, -150, -50, 0]
        drawLineSegment(line)
    elif (digit == 8):
        line = [-51, 150, -201, 151]
        drawLineSegment(line)
        line = [-199, -149, -200, 1]
        drawLineSegment(line)
        line = [-50, 0, -51, 150]
        drawLineSegment(line)
        line = [-199, -149, -49, -150]
        drawLineSegment(line)
        line = [-49, -150, -50, 0]
        drawLineSegment(line)
        line = [-200, 1, -201, 151]
        drawLineSegment(line)
        line = [-200, 1, -50, 0]
        drawLineSegment(line)
    elif (digit == 9):
        line = [-51, 150, -201, 151]
        drawLineSegment(line)
        line = [-50, 0, -51, 150]
        drawLineSegment(line)
        line = [-49, -150, -50, 0]
        drawLineSegment(line)
        line = [-200, 1, -201, 151]
        drawLineSegment(line)
        line = [-200, 1, -50, 0]
        drawLineSegment(line)
def drawDigit_2(digit):
    if (digit == 0):
        line = [51, 150, 201, 151]
        drawLineSegment(line)
        line = [199, -149, 200, 1]
        drawLineSegment(line)
        line = [51, 150, 50, 0]
        drawLineSegment(line)
        line = [199, -149, 49, -150]
        drawLineSegment(line)
        line = [50, 0, 49, -150]
        drawLineSegment(line)
        line = [201, 151, 200, 1]
        drawLineSegment(line)
    elif (digit == 1):
        line = [200, 1, 201, 151]
        drawLineSegment(line)
        line = [200, 1, 199, -149]
        drawLineSegment(line)
    elif (digit == 2):
        line = [51, 150, 201, 151]
        drawLineSegment(line)
        line = [201, 151, 200, 1]
        drawLineSegment(line)
        line = [200, 1, 50, 0]
        drawLineSegment(line)
        line = [50, 0, 49, -150]
        drawLineSegment(line)
        line = [199, -149, 49, -150]
        drawLineSegment(line)
    elif (digit == 3):
        line = [51, 150, 201, 151]
        drawLineSegment(line)
        line = [201, 151, 200, 1]
        drawLineSegment(line)
        line = [200, 1, 50, 0]
        drawLineSegment(line)
        line = [199, -149, 200, 1]
        drawLineSegment(line)
        line = [199, -149, 49, -150]
        drawLineSegment(line)
    elif (digit == 4):
        line = [201, 151, 200, 1]
        drawLineSegment(line)
        line = [200, 1, 50, 0]
        drawLineSegment(line)
        line = [199, -149, 200, 1]
        drawLineSegment(line)
        line = [51, 150, 50, 0]
        drawLineSegment(line)
    elif (digit == 5):
        line = [51, 150, 201, 151]
        drawLineSegment(line)
        line = [200, 1, 50, 0]
        drawLineSegment(line)
        line = [199, -149, 200, 1]
        drawLineSegment(line)
        line = [51, 150, 50, 0]
        drawLineSegment(line)
        line = [199, -149, 49, -150]
        drawLineSegment(line)
    elif (digit == 6):
        line = [51, 150, 201, 151]
        drawLineSegment(line)
        line = [199, -149, 200, 1]
        drawLineSegment(line)
        line = [51, 150, 50, 0]
        drawLineSegment(line)
        line = [199, -149, 49, -150]
        drawLineSegment(line)
        line = [50, 0, 49, -150]
        drawLineSegment(line)
        line = [50, 0, 200, 1]
        drawLineSegment(line)
    elif (digit == 7):
        line = [51, 150, 201, 151]
        drawLineSegment(line)
        line = [200, 1, 201, 151]
        drawLineSegment(line)
        line = [200, 1, 199, -149]
        drawLineSegment(line)
    elif (digit == 8):
        line = [51, 150, 201, 151]
        drawLineSegment(line)
        line = [199, -149, 200, 1]
        drawLineSegment(line)
        line = [51, 150, 50, 0]
        drawLineSegment(line)
        line = [199, -149, 49, -150]
        drawLineSegment(line)
        line = [50, 0, 49, -150]
        drawLineSegment(line)
        line = [201, 151, 200, 1]
        drawLineSegment(line)
        line = [50, 0, 200, 1]
        drawLineSegment(line)
    elif (digit == 9):
        line = [51, 150, 201, 151]
        drawLineSegment(line)
        line = [199, -149, 200, 1]
        drawLineSegment(line)
        line = [51, 150, 50, 0]
        drawLineSegment(line)
        line = [201, 151, 200, 1]
        drawLineSegment(line)
        line = [50, 0, 200, 1]
        drawLineSegment(line)

def iterate():
    glViewport(0, 0, 500, 500)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-500, 500, -500, 500, 0.0, 1.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    glColor3f(random.random(), random.random(), random.random())
    drawDigit_1(digit_1)
    drawDigit_2(digit_2)
    glutSwapBuffers()

glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(500, 500) #window size
glutInitWindowPosition(0, 0)
wind = glutCreateWindow(b"Task_1") #window name
glutDisplayFunc(showScreen)

glutMainLoop()