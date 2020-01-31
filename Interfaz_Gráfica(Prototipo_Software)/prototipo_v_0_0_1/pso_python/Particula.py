import numpy as np
from numpy.random import rand

np.random.seed()

class Particula ():
    def __init__(self, id, pos, vel, b_pos, lims, w):
        n = len(lims)
        self.id = id
        self.pos = np.array(pos,dtype=float)
        self.pos.resize(n,)
        self.vel = np.array(vel,dtype=float)
        self.vel.resize(n,)
        self.b_pos = np.array(b_pos,dtype=float)
        self.b_pos.resize(n,)
        self.lims = lims
        self.w = w
        self.fitness = np.inf

    def updatePosicion(self, func):
        for i, lims in enumerate(self.lims.values()):
            n_comp = self.pos[i] + self.vel[i]
            if n_comp > lims[0] and n_comp < lims[1]:
                self.pos[i] = n_comp
        new_fitness = func(self.pos)
        if self.fitness > new_fitness:
            self.b_pos = np.copy(self.pos)

        self.fitness = new_fitness


    def updateVelocidad(self, c1, c2, g_pos, dec_w):
        for i in range(len(self.vel)):
            self.vel[i] = self.vel[i]*self.w + \
                            rand()*c1*(self.b_pos[i]-self.pos[i]) + \
                            rand()*c2*(g_pos[i]-self.pos[i])
        self.w -= dec_w

    def updateFitness(self, func):
        self.fitness = func(self.pos)
