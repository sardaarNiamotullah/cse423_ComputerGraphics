from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *


def draw_number():
    glPointSize(5)

    glBegin(GL_QUADS)
    glVertex2f(20, 500)
    glVertex2f(20, 20)
    glVertex2f(5, 20)
    glVertex2f(5, 500)
    glEnd()

    glColor3f(1.0, 0.0, 0.0)

    glBegin(GL_QUADS)
    glVertex2f(35, 500)
    glVertex2f(35, 485)
    glVertex2f(120, 485)
    glVertex2f(120, 500)
    glEnd()

    glBegin(GL_QUADS)
    glVertex2f(35, 300)
    glVertex2f(35, 285)
    glVertex2f(120, 285)
    glVertex2f(120, 300)
    glEnd()

    glBegin(GL_QUADS)
    glVertex2f(35, 500)
    glVertex2f(35, 285)
    glVertex2f(50, 285)
    glVertex2f(50, 500)
    glEnd()

    glBegin(GL_QUADS)
    glVertex2f(120, 500)
    glVertex2f(120, 20)
    glVertex2f(105, 20)
    glVertex2f(105, 500)
    glEnd()

    glColor3f(0.0, 1.0, 0.0)

    glBegin(GL_QUADS)
    glVertex2f(220, 500)
    glVertex2f(220, 480)
    glVertex2f(135, 480)
    glVertex2f(135, 500)
    glEnd()

    glBegin(GL_QUADS)
    glVertex2f(220, 500)
    glVertex2f(220, 20)
    glVertex2f(205, 20)
    glVertex2f(205, 500)
    glEnd()

    glBegin(GL_QUADS)
    glVertex2f(220, 300)
    glVertex2f(220, 280)
    glVertex2f(135, 280)
    glVertex2f(135, 300)
    glEnd()

    glBegin(GL_QUADS)
    glVertex2f(220, 40)
    glVertex2f(220, 20)
    glVertex2f(135, 20)
    glVertex2f(135, 40)
    glEnd()

    glColor3f(0.0, 0.0, 1.0)

    glBegin(GL_QUADS)
    glVertex2f(315, 500)
    glVertex2f(315, 20)
    glVertex2f(330, 20)
    glVertex2f(330, 500)
    glEnd()

    glBegin(GL_QUADS)
    glVertex2f(235, 500)
    glVertex2f(235, 20)
    glVertex2f(250, 20)
    glVertex2f(250, 500)
    glEnd()

    glBegin(GL_QUADS)
    glVertex2f(235, 30)
    glVertex2f(235, 20)
    glVertex2f(315, 20)
    glVertex2f(315, 30)
    glEnd()

    glBegin(GL_QUADS)
    glVertex2f(235, 500)
    glVertex2f(235, 490)
    glVertex2f(315, 490)
    glVertex2f(315, 500)
    glEnd()

    glColor3f(1.0, 1.0, 1.0)

    glBegin(GL_QUADS)
    glVertex2f(360, 500)
    glVertex2f(360, 20)
    glVertex2f(345, 20)
    glVertex2f(345, 500)
    glEnd()

    glColor3f(1.0, 0.0, 1.0)

    glBegin(GL_QUADS)
    glVertex2f(390, 500)
    glVertex2f(390, 20)
    glVertex2f(375, 20)
    glVertex2f(375, 500)
    glEnd()

    glColor3f(0.0, 1.0, 1.0)

    glBegin(GL_QUADS)
    glVertex2f(480, 500)
    glVertex2f(480, 480)
    glVertex2f(405, 480)
    glVertex2f(405, 500)
    glEnd()

    glBegin(GL_QUADS)
    glVertex2f(415, 500)
    glVertex2f(415, 290)
    glVertex2f(405, 290)
    glVertex2f(405, 500)
    glEnd()

    glBegin(GL_QUADS)
    glVertex2f(480, 290)
    glVertex2f(480, 275)
    glVertex2f(405, 275)
    glVertex2f(405, 290)
    glEnd()

    glBegin(GL_QUADS)
    glVertex2f(480, 40)
    glVertex2f(480, 20)
    glVertex2f(405, 20)
    glVertex2f(405, 40)
    glEnd()

    glBegin(GL_QUADS)
    glVertex2f(480, 290)
    glVertex2f(480, 20)
    glVertex2f(470, 20)
    glVertex2f(470, 290)
    glEnd()

    glColor3f(1.0, 0.5, 0.5)

    glBegin(GL_QUADS)
    glVertex2f(500, 500)
    glVertex2f(500, 20)
    glVertex2f(490, 20)
    glVertex2f(490, 500)
    glEnd()


def iterate():
    glViewport(0, 0, 500, 500)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 500, 0.0, 500, 0.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()

def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    glColor3f(1.0, 1.0, 0.0)
    draw_number()
    glutSwapBuffers()



glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(500, 500) #window size
glutInitWindowPosition(0, 0)
wind = glutCreateWindow(b"Task_3") #window name
glutDisplayFunc(showScreen)

glutMainLoop()