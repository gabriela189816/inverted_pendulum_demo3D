# -*- coding: utf-8 -*-
"""
Created on Sun Nov  6 17:43:45 2022

@author: Gabriela Hilario Acuapan
# Fecha de entrega: 11/Noviembre/2022
# Descripción: Animación 3D del péndulo invertido (carrito con péndulo)

"""
from vpython import *
import numpy as np 

# Configuración de la Escena
scene.width = 600
scene.height = 300
scene.background = color.white
scene.title = "\t \t \t Animación 3D del carrito con péndulo \n \t \t \t \t Con f = 1"
# Ejes coordenados y etiquetas
ejex = arrow(pos=vector(0,-1.5,0), size=vector(10,0.1,0.1), shaftwidth=0.05, color=color.black, visible=True)
ejex2 = arrow(pos=vector(0,-1.5,0), size=vector(10,0.1,0.1), shaftwidth=0.05, color=color.black, visible=True)
ejex2.rotate(angle=pi, axis=vec(0,0,1))
o = cylinder(pos=vector(0,-2,0), size=vector(0.5,0.1,0.1),color=color.black)
o.rotate(angle=pi/2, axis=vec(0,0,1))
t0 = label(text='0', pos = vector(0,-2.5,0))
t2 = label(text='x', pos = vector(10,-2.5,0))
t3 = label(text='-x', pos = vector(-10,-2.5,0))

# PARÁMETROS
l = 4           # longitud de la varilla
mc = 5          # masa del carrito
mp = 1          # masa del la bolita
g = 9.81        # gravedad
f = 1           # fuerza aplicada f = 0 o 1
# Condiciones iniciales
x = 0           # x (posición lineal) inicial
th = pi/2       # theta (posición angular) inicial
xdot = 0        # dx/dt (velocidad lineal) inicial
thdot = 0       # dth/dt (velocidad angular) inical
# tiempo y paso de tiempo
t = 0           # tiempo inicial
dt = 0.02       # paso de integración

# Coordenadas y velocidades generalizadas
q = np.array([[x],[th]])
qdot = np.array([[xdot], [thdot]])
print(f'Posiciones iniciales: \n x = {q[0]}, theta = {q[1]} radianes')
print(f'Velocidades iniciales: \n xdot = {qdot[0]}, thetadot = {qdot[1]}')

# ------------------------------------ Animación 3D ------------------------------
# posición inical del carito
car = box(pos=vector(x,0,0), size=vector(4,2,2), color=color.cyan, visible=True)    # carrito
s1 = sphere(pos=vector(-1.5,-1,1), color=color.black, radius=0.5)                   # rueda 1
s2 = sphere(pos=vector(1.5,-1,1), color=color.black, radius=0.5)                    # rueda 2
s3 = sphere(pos=vector(1.5,-1,-1), color=color.black, radius=0.5)                   # rueda 3
s4 = sphere(pos=vector(-1.5,-1,-1), color=color.black, radius=0.5)                  # rueda 4
# posición inicial de la bolita
ball = sphere(pos=vector(x + l*sin(th),-l*cos(th),0), color=color.magenta, radius=0.5, make_trail=True, visible=True)
# orientación inicial de la varilla
rod = cylinder(pos=vector(0,0,0), size=vector(4,0.1,0.1), color=color.black)
rod_ang = rod.rotate(angle=pi-th, axis=vec(0,0,1))

while t<10:
    rate(50) # limit animation rate, render scene
    scene.caption = f'\t Tiempo de simulación \t t = {round(t,2)} segundos'
    # Variables: q[0]=x, q[1]=th,  qdot[0]=xdot, qdot[1]=thdot

    # Matrices H, C, G, Bu -----------------------------------------
    H = np.array([[mc+mp, mp*l*cos(q[1])],[mp*l*cos(q[1]), mp*l**2]])
    C = np.array([[0, -qdot[1]*mp*l*sin(q[1])],[0,0]])
    G = np.array([[0],[mp*l*g*sin(q[1])]])
    Bu = np.array([[f],[0]])
    # Variables temporales ----------------
    HI= np.linalg.inv(H) #Inversa de H
    T = Bu - np.dot(C,qdot) - G

    # Solución de las ecuaciones con el método de euler-------------
    qddot = np.dot(HI, T)
    qdot = qdot + qddot*dt
    q = q + qdot*dt

    # Movimiento del sistema ---------------------------------------
    ball.pos = vector(q[0] + l*sin(q[1]),-l*cos(q[1]),0)
    rod.pos=vector(q[0],0,0)
    rod.axis=ball.pos - vector(q[0],0,0)
    car.pos = vector(q[0],0,0)
    s1.pos = vector(-1.5 + q[0],-1,1)
    s2.pos = vector(1.5 + q[0],-1,1)
    s3.pos = vector(1.5 + q[0],-1,-1)
    s4.pos = vector(-1.5 + q[0],-1,-1)
    t = t + dt