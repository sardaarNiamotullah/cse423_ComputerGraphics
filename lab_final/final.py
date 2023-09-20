import random
import math
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

id = int(input('give number: '))
iniZone = None


# for circle
def circle_draw_points(x, y):
    glPointSize(2)
    glBegin(GL_POINTS)
    glVertex2f(x, y)
    glEnd()
def midPointCircleDraw(cx, cy, r):
    x = r
    y = 0

    circle_draw_points(x+cx, y+cy)

    if (r > 0):
        P = 1 - r

        while x >= y:
            y += 1
            if P <= 0:
                P = P + 2 * y + 3
            else:
                x -= 1
                P = P + 2 * y - 2 * x + 5

            circle_draw_points(x + cx, y + cy)
            circle_draw_points(-x + cx, y + cy)
            circle_draw_points(x + cx, -y + cy)
            circle_draw_points(-x + cx, -y + cy)

            circle_draw_points(y + cx, x + cy)
            circle_draw_points(-y + cx, x + cy)
            circle_draw_points(y + cx, -x + cy)
            circle_draw_points(-y + cx, -x + cy)
# for squre
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
    glPointSize(2)
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
def ifnot1(xf):
    line = [-xf, xf, xf, xf]
    drawLineSegment(line)
    line = [-xf, -xf, xf, -xf]
    drawLineSegment(line)
    line = [-xf, -xf, -xf, xf]
    drawLineSegment(line)
    line = [xf, -xf, xf, xf]
    drawLineSegment(line)

    newRad = math.sqrt(2 * (xf ** 2))
    midPointCircleDraw(0, 0, newRad)
def drawSquare(numt):
    x = 25
    rad = math.sqrt(2 * (x ** 2))
    # first circle
    glColor3f(random.random(), random.random(), random.random())
    midPointCircleDraw(0, 0, rad)
    #first squre
    line = [-x, x, x, x]
    drawLineSegment(line)
    line = [-x, -x, x, -x]
    drawLineSegment(line)
    line = [-x, -x, -x, x]
    drawLineSegment(line)
    line = [x, -x, x, x]
    drawLineSegment(line)

    if numt > 1 :
        xt = 2
        ine = numt + 1
        while xt < ine:
            ifnot1(rad)
            rad = math.sqrt(2 * (rad ** 2))
            xt += 1

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
    drawSquare(id)
    glutSwapBuffers()

glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(500, 500) #window size
glutInitWindowPosition(0, 0)
wind = glutCreateWindow(b"Task_1") #window name
glutDisplayFunc(showScreen)

glutMainLoop()