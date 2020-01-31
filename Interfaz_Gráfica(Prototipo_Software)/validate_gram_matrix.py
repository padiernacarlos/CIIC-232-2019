# -*- coding: utf-8 -*-
"""
Created on Thu Dec 19 20:39:25 2019
@author: TUF-PC8
"""

import numpy as np, pandas as pd, config as cf
import padaux.orthogonal_kernels_v2 as ks

path = 'C:/Users/TUF-PC8/Google Drive/2018.12 work/datasets/Gram Matrices/cryotherapy/'
gt = pd.read_excel(path+'.gramMatrixHERMITE(n=4).xlsx',header=None)

# Parameters
dataset   = 'cryotherapy'
df        = pd.read_csv(cf.datapath+dataset+'.csv',header=None)
X,y       = (df.iloc[:,0:-1]) , df.iloc[:,-1]
dfk       = pd.DataFrame.from_dict(cf.dicsHerm) # para futura extensión
my_C      = dfk[dataset]['C']       = 32.0
my_gamma  = dfk[dataset]['gamma']   = 0.01
my_degree = dfk[dataset]['degree']  = 4
my_alpha  = dfk[dataset]['alpha']   = 0.1
#my_kernel = ks.build_K_gegen(my_degree,my_alpha)
my_kernel = ks.build_K_sHerm(my_degree)
print('\n****VERIFICANDO MATRIZ GRAM*****')


K = my_kernel(X)
K = pd.DataFrame(K)
D = K-gt
#D = np.round(K-gt,2)
E = K.eq(gt)
#X_gram = my_rbf(X, gamma=my_gamma)
print(type(K))
print('Gram Max =',K.max().max(),'Gram min =',K.min().min())
print('Dif max =',D.max().max(),'Dif min =',D.min().min())
#NANs = np.argwhere(np.isnan(K))
#print('Valores tipo NAN: ',NANs)