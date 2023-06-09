# -*- coding: utf-8 -*-
"""Taller escala de grises.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/15ozyAMiydvZE3lAYpXciqTujBjXGgSPP

#Taller escala de grises, blanco y negro
"""

import matplotlib.pyplot as plt
import numpy as np

size=(20,30)

#Matriz blanca y gris
imagen_blanca = np.ones(size)
plt.imshow(imagen_blanca,vmin=0,vmax=1)

plt.figure()

imagen_gris = np.ones(size)*0.5
plt.imshow(imagen_gris,vmin=0,vmax=1)

#Matriz gris oscuro e imagen aleatoria
imagen_gris_oscuro = np.ones(size)*0.2
plt.imshow(imagen_gris_oscuro,vmin=0,vmax=1)

plt. figure()

imagen_aleatoria = np.random.rand(size[0],size[1])
plt.imshow(imagen_aleatoria,vmin=0,vmax=1)