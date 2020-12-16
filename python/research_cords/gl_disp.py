import sys

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from PIL import Image

widowWidth = 480
windowHeight = 480

def load_texture():
    img = Image.open("icon01.png")
    w, h = img.size
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, w, h, 0, GL_RGBA, GL_UNSIGNED_BYTE, img.tobytes())

def display():

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glColor3f(1.0, 1.0, 1.0)

    glEnable(GL_TEXTURE_2D)

    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)

    glBegin(GL_QUADS)
    glTexCoord2d(0.0, 1.0)
    glVertex3d(-1.0, -1.0,  0.0)
    glTexCoord2d(1.0, 1.0)
    glVertex3d( 1.0, -1.0,  0.0)
    glTexCoord2d(1.0, 0.0)
    glVertex3d( 1.0,  1.0,  0.0)
    glTexCoord2d(0.0, 0.0)
    glVertex3d(-1.0,  1.0,  0.0)
    glEnd()

    glDisable(GL_TEXTURE_2D)


    glFlush()

def reshape(w, h):
    glViewport(0, 0, w, h)
    glLoadIdentity()
    w_margin = (widowWidth - w) // 2
    h_margin = (windowHeight - h) // 2
    print(w, h)
    # glOrtho(-1., 1., -1., 1., -1., 1.)
    #Make the display area proportional to the size of the view
    glOrtho(-w / widowWidth, w / widowWidth, -h / windowHeight, h / windowHeight, -1.0, 1.0)

def keyboard(key, x, y):
    # convert byte to str
    key = key.decode('utf-8')
    # press q to exit
    if key == 'q':
        print('exit')
        sys.exit()

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGBA)
    glutInitWindowSize(widowWidth, windowHeight)
    glutCreateWindow(b"TextureSample1")
    glutDisplayFunc(display)
    glutReshapeFunc(reshape)
    glutKeyboardFunc(keyboard)

    glClearColor(0., 0., 0., 0.)

    load_texture()

    glutMainLoop()

if __name__ == '__main__':
    main()
