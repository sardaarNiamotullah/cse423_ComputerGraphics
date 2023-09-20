import random
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def draw_points(x, y):
    glPointSize(3)
    glBegin(GL_POINTS)
    glVertex2f(x, y)
    glEnd()


def midPointCircleDraw(cx, cy, r):
    x = r
    y = 0

    draw_points(x+cx, y+cy)

    if (r > 0):
        P = 1 - r

        while x >= y:
            y += 1
            if P <= 0:
                P = P + 2 * y + 3
            else:
                x -= 1
                P = P + 2 * y - 2 * x + 5

            draw_points(x + cx, y + cy)
            draw_points(-x + cx, y + cy)
            draw_points(x + cx, -y + cy)
            draw_points(-x + cx, -y + cy)

            draw_points(y + cx, x + cy)
            draw_points(-y + cx, x + cy)
            draw_points(y + cx, -x + cy)
            draw_points(-y + cx, -x + cy)


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
    midPointCircleDraw(0, 0, 450)

    glColor3f(random.random(), random.random(), random.random())
    midPointCircleDraw(225, 0, 225)
    midPointCircleDraw(-225, 0, 225)
    midPointCircleDraw(0, 225, 225)
    midPointCircleDraw(0, -225, 225)

    glColor3f(random.random(), random.random(), random.random())
    midPointCircleDraw(160, 160, 225)
    midPointCircleDraw(-160, 160, 225)
    midPointCircleDraw(-160, -160, 225)
    midPointCircleDraw(160, -160, 225)

    glutSwapBuffers()



glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(500, 500) #window size
glutInitWindowPosition(0, 0)
wind = glutCreateWindow(b"Lab3task") #window name
glutDisplayFunc(showScreen)

glutMainLoop()