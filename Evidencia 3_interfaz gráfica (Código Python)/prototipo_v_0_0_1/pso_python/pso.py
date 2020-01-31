import numpy as np
import pso_functions as psof
from Particula import Particula
import test_functions as tfun
import matplotlib.pyplot as plt
from matplotlib.animation import ArtistAnimation
from mpl_toolkits import mplot3d

#INICIAR FIGURA
fig = plt.figure()
ax = plt.axes(projection='3d')

# PARAMETROS PSO
n_part = 20
w_max = 0.9
w_min = 0.4
max_iter = 20
c1 = 0.8
c2 = 0.8
dec_w = (w_max - w_min)/max_iter
lims = {'x0':[-4.5,4.5],'x1':[-4.5,4.5]}
func = tfun.gold
#----------------------------------------
# GRAFICAR FUNCION
x = np.outer(np.linspace(lims['x0'][0], lims['x1'][1], 20), np.ones(20))
y = x.copy().T # transpose
z = np.zeros(shape=x.shape)

n = len(x)
for i in range(n):
    for j in range(n):
        z[i,j] = func([x[i,j],y[i,j]])


ax.plot_surface(x, y, z,cmap='viridis', edgecolor='none', alpha=0.4)
ax.set_title('Surface plot')
artists = []
#-------------------------------------------------------------------------
#INICIALIZAR PSO
g_pos = [np.inf, np.inf]
g_fit = np.inf
enjambre = psof.crearEnjambre(n_part, lims, w_max, func)
g_pos, g_fit = psof.ordenarEnjambre(enjambre, g_pos, g_fit)
artists.append(psof.graficarEnjambre(enjambre,ax))
elite = Particula(enjambre[0].id,
                    enjambre[0].pos,
                    enjambre[0].vel,
                    enjambre[0].b_pos,
                    lims, enjambre[0].w)
elite.updateFitness(func)
#-----------------------------------------
#PSO
for i in range(max_iter):
    psof.moverEnjambre(enjambre,c1,c2,g_pos,dec_w,func)
    #print(enjambre[0].pos)
    g_pos, g_fit = psof.ordenarEnjambre(enjambre, g_pos, g_fit)
    if enjambre[0].fitness > elite.fitness:
        enjambre[0] = elite
        g_pos, g_fit = np.copy(elite.pos), elite.fitness
    else:
        elite = Particula(enjambre[0].id,
                            enjambre[0].pos,
                            enjambre[0].vel,
                            enjambre[0].b_pos,
                            lims, enjambre[0].w)
        elite.updateFitness(func)
    artists.append(psof.graficarEnjambre(enjambre,ax))
#---------------------------------------------------------------
#RESULTADO
print(g_pos,g_fit)

anim = ArtistAnimation(fig,artists,blit=True,repeat=False)
plt.show()
