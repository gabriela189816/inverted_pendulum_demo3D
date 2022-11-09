# -*- coding: utf-8 -*-
"""
Created on Sun Nov  6 17:43:45 2022

@author: Gabriela Hilario Acuapan
# Fecha: 05/Noviembre/2022
# Descripción: Animación 3D del péndulo invertido

"""
from vpython import *

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
th = 3*pi/4       # theta (posición angular) inicial
thdot = 0       # dth/dt (velocidad angular) inical
x = 0           # x (posición lineal) inicial

#a = arrow(pos=vector(-1,0,0), axis=vector(+1,+5,+1), shaftwidth=0.5)
# carito
car = box(pos=vector(x,0,0), size=vector(4,2,2), color=color.green, visible=True)
s1 = sphere(pos=vector(-1.5,-1,1), color=color.black, radius=0.5)
s2 = sphere(pos=vector(1.5,-1,1), color=color.black, radius=0.5)
s3 = sphere(pos=vector(1.5,-1,-1), color=color.black, radius=0.5)
s4 = sphere(pos=vector(-1.5,-1,-1), color=color.black, radius=0.5)
#bolita
ball = sphere(pos=vector(x + l*sin(th),-l*cos(th),0), color=color.blue, radius=0.5, make_trail=True, visible=True)
#varilla
rod = cylinder(pos=vector(0,0,0), size=vector(4,0.1,0.1), color=color.black)
rod_ang = rod.rotate(angle=pi-th, axis=vec(0,0,1))

t = 0
dt = 0.005
while t<10:
    rate(5) # limit animation rate, render scene
    ## Animación
    t = t + dt


