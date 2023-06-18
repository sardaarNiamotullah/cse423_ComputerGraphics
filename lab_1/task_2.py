import random
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *


def draw_house():
    glPointSize(5)
    glColor3f(random.random(), random.random(), random.random())

    glBegin(GL_LINES) #skeleton lines
    #top line
    glVertex2f(200, 220)
    glVertex2f(300, 220)
    #bottom line
    glVertex2f(200, 150)
    glVertex2f(300, 150)
    #left line
    glVertex2f(200, 150)
    glVertex2f(200, 220)
    #right line
    glVertex2f(300, 150)
    glVertex2f(300, 220)
    glEnd()

    glColor3f(random.random(), random.random(), random.random())

    glBegin(GL_TRIANGLES) #rooftop
    glVertex2f(250, 250)
    glVertex2f(200, 220)
    glVertex2f(300, 220)
    glEnd()

    glBegin(GL_QUADS) #left window
    glVertex2f(215, 190)
    glVertex2f(215, 180)

    glVertex2f(225, 180)
    glVertex2f(225, 190)
    glEnd()

    glBegin(GL_QUADS) #right window
    glVertex2f(275, 190)
    glVertex2f(275, 180)

    glVertex2f(285, 180)
    glVertex2f(285, 190)
    glEnd()

    glColor3f(random.random(), random.random(), random.random())

    glBegin(GL_LINES) #door lines
    #top line
    glVertex2f(240, 200)
    glVertex2f(260, 200)
    #bottom line
    glVertex2f(240, 150)
    glVertex2f(260, 150)
    #left line
    glVertex2f(240, 150)
    glVertex2f(240, 200)
    #right line
    glVertex2f(260, 150)
    glVertex2f(260, 200)
    glEnd()


    glPointSize(3)
    glBegin(GL_POINTS) #door knob
    glVertex2f(253, 170)
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
    draw_house()
    glutSwapBuffers()



glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(500, 500) #window size
glutInitWindowPosition(0, 0)
wind = glutCreateWindow(b"Task_2") #window name
glutDisplayFunc(showScreen)

glutMainLoop()