import numpy as np
from . import pso_functions as psof
from . import Particula as Part
#import test_functions as tfun
import matplotlib.pyplot as plt
from matplotlib.animation import ArtistAnimation
from mpl_toolkits import mplot3d
import matplotlib
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

matplotlib.use('TkAgg')

def pso_anim(n_part,w_max,w_min,max_iter,c1,c2,azim,ele,lims,func,title):
    #INICIAR FIGURA
    fig = plt.figure()

    ax = plt.axes(projection='3d')
    ax.view_init(elev=ele, azim=azim)

    # PARAMETROS PSO
    # n_part = 20
    # w_max = 0.9
    # w_min = 0.4
    # max_iter = 20
    # c1 = 0.8
    # c2 = 0.8
    dec_w = (w_max - w_min)/max_iter
    # lims = {'x0':[-4.5,4.5],'x1':[-4.5,4.5]}
    # func = tfun.gold
    #----------------------------------------
    # GRAFICAR FUNCION
    x = np.outer(np.linspace(lims['x0'][0], lims['x1'][1], 30), np.ones(30))
    y = x.copy().T # transpose
    z = np.zeros(shape=x.shape)

    n = len(x)
    for i in range(n):
        for j in range(n):
            z[i,j] = func([x[i,j],y[i,j]])


    ax.plot_surface(x, y, z,cmap='plasma', edgecolor='none', alpha=0.4)
    ax.set_title(title)
    artists = []
    #-------------------------------------------------------------------------
    #INICIALIZAR PSO
    g_pos = [np.inf, np.inf]
    g_fit = np.inf
    enjambre = psof.crearEnjambre(n_part, lims, w_max, func)
    g_pos, g_fit = psof.ordenarEnjambre(enjambre, g_pos, g_fit)
    artists.append(psof.graficarEnjambre(enjambre,ax))
    elite = Part.Particula(enjambre[0].id,
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
            elite = Part.Particula(enjambre[0].id,
                                enjambre[0].pos,
                                enjambre[0].vel,
                                enjambre[0].b_pos,
                                lims, enjambre[0].w)
            elite.updateFitness(func)
        artists.append(psof.graficarEnjambre(enjambre,ax))
    #---------------------------------------------------------------
    #RESULTADO
    ax.text2D(0.05, 0.95, 'El minimo se encuentra en: ({0:0.2f},{1:0.2f})\n{2:0.2f}'.format(g_pos[0],g_pos[1],g_fit), transform=ax.transAxes)

    anim = ArtistAnimation(fig,artists,blit=True,repeat=False)
    plt.show()
