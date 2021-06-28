import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

import numpy as np
# from loadobj import loadObjModel
import socket

verticies = (
    (1, -1, -1),
    (1, 1, -1),
    (-1, 1, -1),
    (-1, -1, -1),
    (1, -1, 1),
    (1, 1, 1),
    (-1, -1, 1),
    (-1, 1, 1)
    )

edges = (
    (0,1),
    (0,3),
    (0,4),
    (2,1),
    (2,3),
    (2,7),
    (6,3),
    (6,4),
    (6,7),
    (5,1),
    (5,4),
    (5,7)
    )

colors = (
    (1,1,1),
    (0,1,0),
    (0,0,1),
    (0,1,0),
    (1,1,1),
    (0,1,1),
    (1,0,0),
    (0,1,0),
    (0,0,1),
    (1,0,0),
    (1,1,1),
    (0,1,1),
    )

def Cube():
    glBegin(GL_LINES)
    for edge in edges:
        x = 0
        for vertex in edge:
            x += 1
            glColor3fv(colors[x])
            glVertex3fv(verticies[vertex])
    glEnd()

def rot_mat_3D_x(pitch):
    angel = pitch
    return np.array([[1, 0, 0, 0], 
                    [0, np.cos(angel), -np.sin(angel), 0], 
                    [0, np.sin(angel), np.cos(angel), 0], 
                    [0, 0, 0, 1]], dtype=np.float64)


def rot_mat_3D_y(roll):
    angel = roll
    return np.array([[np.cos(angel), 0, np.sin(angel), 0], 
                    [0, 1, 0, 0], 
                    [-np.sin(angel), 0, np.cos(angel), 0], 
                    [0, 0, 0, 1]], dtype=np.float64)

def rot_mat_3D_z(yaw):
    angel = yaw
    return np.array([[np.cos(angel), -np.sin(angel), 0, 0], 
                    [np.sin(angel), np.cos(angel), 0, 0], 
                    [0, 0, 1, 0], 
                    [0, 0, 0, 1]], dtype=np.float64)


def rotate(pitch, roll, yaw):
    glPushMatrix()
    glMatrixMode(GL_MODELVIEW)
    glMultMatrixf(rot_mat_3D_x(-pitch))
    glMultMatrixf(rot_mat_3D_y(-yaw))
    glMultMatrixf(rot_mat_3D_z(roll))
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    Cube()
    glPopMatrix()

def main():

    angel = 0

    HOST = '10.53.14.103'  # Standard loopback interface address (localhost)
    PORT = 9000        # Port to listen on (non-privileged ports are > 1023)

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind((HOST, PORT))
        s.listen()
        print("\nWaiting for client to connect...")
        conn, addr = s.accept()
        with conn:
            print('Connected by', addr)

            pygame.init()
            pygame.display.set_caption('3D rotation')
            display = (1600, 1080)
            pygame.display.set_mode(display, DOUBLEBUF|OPENGL)

            gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)

            glTranslatef(0.0,0.0, -5)

            while True:
                data = conn.recv(1024)
                if not data:
                    break

                
                data = data.decode("utf-8").split("\n")[-2]
                pitch, roll, yaw = data.split(" ")
                pitch = float(pitch)
                roll = float(roll)
                yaw = float(yaw)
                print("pitch: {}".format(np.rad2deg(pitch)))
                print("roll: {}".format(np.rad2deg(roll)))
                print("yaw: {}".format(np.rad2deg(yaw)))
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        print("Close connection.")
                        conn.sendall(b"c")
                        conn.close()
                        s.close()
                        
                        pygame.quit()
                        quit()

                # glRotatef(1, 1, 1, 1)
                rotate(pitch, roll, yaw)



                pygame.display.flip()
                pygame.time.wait(10)


main()