# -*- coding: utf-8 -*-
"""
Created on Sun Nov  6 17:43:45 2022

@author: Gabriela Hilario Acuapan
# Fecha: 05/Noviembre/2022
# Descripción: Animación 3D del péndulo invertido

"""
from vpython import *
import numpy as np 

## Configuración de la Escena
scene.width = 800
scene.height = 500
scene.background = color.white
scene.range = 6
# Ejes coordenados
ejex = arrow(pos=vector(-2,-1.5,0), size=vector(7,0.1,0.1), shaftwidth=0.05, color=color.black, visible=True)
ejey = arrow(pos=vector(-2,-1.5,0), size=vector(7,0.1,0.1), shaftwidth=0.05, color=color.black, visible=True)
ejey.rotate(angle=pi/2, axis=vec(0,0,1))

# PARÁMETROS
l = 4           # longitud de la varilla
mc = 1          # masa del carrito
mp = 1          # masa del la bolita
g = 9.81        # gravedad
f = 1           # fuerza aplicada f = 0 o 1
# Condiciones iniciales
x = 0           # x (posición lineal) inicial
th = 3*pi/4     # theta (posición angular) inicial
xdot = 0        # dx/dt (velocidad lineal) inicial
thdot = 0       # dth/dt (velocidad angular) inical
# tiempo y paso de tiempo
t = 0           # tiempo inicial
dt = 0.005      # paso de tiempo

# Coordenadas y velocidades generalizadas
q = np.array([x, th])
qdot = np.array([xdot, thdot])
print(f'Posiciones iniciales: \n x = {q[0]}, theta = {q[1]} radianes')
print(f'Velocidades iniciales: \n xdot = {qdot[0]}, thetadot = {qdot[1]}')

# Matriz de Incercia H(q)
H_list = [[mc+mp, mp*l*cos(th)],[mp*l*cos(th), mp*l^2]]
H = np.array(H_list)
print(f'Matriz de Inercia H(q) = {H}')
HI= np.linalg.inv(H) #Inversa de H
# Matriz de Coriolis
C_list = [[0, -thdot*mp*l*sin(th)],[0,0]]
C = np.array(C_list)
print(f'Matriz de Corilis C(q,qdot) = {C}')
# Vector de Gravedad
G = np.array([[0],[mp*l*g*sin(th)]])
print(f'Vector de Gravedad G(q) = {G}')
# Vector Bu
B = np.array([[1],[0]])
Bu = np.dot(B,f)
print(f'Vector de Bu = {Bu}')

# ------------------------------------ Animación 3D ------------------------------
# posición inical del carito
car = box(pos=vector(x,0,0), size=vector(4,2,2), color=color.cyan, visible=True)
s1 = sphere(pos=vector(-1.5,-1,1), color=color.black, radius=0.5)
s2 = sphere(pos=vector(1.5,-1,1), color=color.black, radius=0.5)
s3 = sphere(pos=vector(1.5,-1,-1), color=color.black, radius=0.5)
s4 = sphere(pos=vector(-1.5,-1,-1), color=color.black, radius=0.5)
# posición inicial de la bolita
ball = sphere(pos=vector(x + l*sin(th),-l*cos(th),0), color=color.magenta, radius=0.5, make_trail=True, visible=True)
# orientación inicial de la varilla
rod = cylinder(pos=vector(0,0,0), size=vector(4,0.1,0.1), color=color.black)
rod_ang = rod.rotate(angle=pi-th, axis=vec(0,0,1))


while t<5:
    rate(10) # limit animation rate, render scene
    ## Animación
    t = t + dt

