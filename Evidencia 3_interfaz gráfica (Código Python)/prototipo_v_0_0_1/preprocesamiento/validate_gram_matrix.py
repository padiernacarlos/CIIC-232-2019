# -*- coding: utf-8 -*-
"""
Created on Thu Dec 19 20:39:25 2019
@author: TUF-PC8
"""

import numpy as np, pandas as pd
from . import config as cf
from . import orthogonal_kernels_v2 as ks
import os
import tkinter as tk

def validate(dir, kernel,ds,win):

    if kernel == 'Hermite':
        k_path = '_gramMatrixHERMITE(n=4).xlsx'
    elif kernel == 'Gegenbauer':
        k_path = '_gramMatrixGEGENBAUER(n=4).xlsx'
    elif kernel == 'Linear':
        k_path = '_gramMatrixLINEAR(n=4).xlsx'
    elif kernel == 'RBF':
        k_path = '_gramMatrixRBF(n=4).xlsx'


    path = dir
    gt = pd.read_excel(os.path.join(path,k_path),header=None)

    # Parameters
    dataset   = ds
    c_path = os.path.join(os.getcwd(),'preprocesamiento')
    c_path = os.path.join(c_path,'data')
    df        = pd.read_csv(os.path.join(c_path,dataset)+'.csv',header=None)
    X,y       = (df.iloc[:,0:-1]) , df.iloc[:,-1]
    dfk       = pd.DataFrame.from_dict(cf.dicsHerm) # para futura extensión
    my_C      = dfk[dataset]['C']       = 32.0
    my_gamma  = dfk[dataset]['gamma']   = 0.01
    my_degree = dfk[dataset]['degree']  = 4
    my_alpha  = dfk[dataset]['alpha']   = 0.1

    my_kernel = ks.build_K_sHerm(my_degree)
    m_str = '\n****VERIFICANDO MATRIZ GRAM*****'

    K = my_kernel(X)
    K = pd.DataFrame(K)
    D = K-gt

    E = K.eq(gt)

    m_str += '\n{}'.format(type(K))
    m_str += '\n\nGram Max = {}\tGram min = {}'.format(K.max().max(),K.min().min())
    m_str += '\n\nDif max = {}\tDif min = {}'.format(D.max().max(),D.min().min())
    m_str += '\n\n'
    display = tk.Label(win, text=m_str)
    display.pack()
