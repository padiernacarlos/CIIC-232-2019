import numpy as np
from numpy.random import rand
from . import Particula as Part

np.random.seed()

def crearEnjambre(n_part, lims, w, func):
    Poblacion = []
    for i in range(n_part):
        pos = [0]*len(lims)
        for i, limites in enumerate(lims.values()):
            pos[i] = limites[0] + (limites[1]-limites[0])*rand()
        p = Part.Particula(i+1, pos, pos, pos, lims, w)
        p.updateFitness(func)
        Poblacion.append(p)

    return Poblacion

def moverEnjambre(poblacion,c1,c2,g_pos,dec_w,func):
    for particula in poblacion:
        particula.updateVelocidad(c1, c2, g_pos, dec_w)
        particula.updatePosicion(func)

def ordenarEnjambre(poblacion, g_pos, g_fit):
    poblacion.sort(key=lambda x: x.fitness)
    if g_fit > poblacion[0].fitness:
        return np.copy(poblacion[0].pos), poblacion[0].fitness

    return g_pos, g_fit

def graficarEnjambre(poblacion, ax,thrdim=True):
    frame = []
    if thrdim:
        for particula in poblacion:
            x = particula.pos[0]
            y = particula.pos[1]
            frame.append(ax.scatter(x,y,particula.fitness,c='k'))
    else:
        for particula in poblacion:
            x = particula.pos[0]
            y = particula.pos[1]
            frame.append(ax.scatter(x,y,c='k'))
    return frame
