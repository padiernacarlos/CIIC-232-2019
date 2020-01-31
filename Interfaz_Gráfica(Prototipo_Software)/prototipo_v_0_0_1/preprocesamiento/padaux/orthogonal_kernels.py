"""
Created on Fri Dec 13 14:24:06 2019
@author: Carlos Padierna
"""
import numpy as np, matplotlib.pyplot as plt
from sklearn.metrics.pairwise import check_pairwise_arrays, euclidean_distances
from sklearn.utils.extmath import safe_sparse_dot

#En caso lineal Y = X.T
def K_linear(X, Y=None):       
    
    X, Y = check_pairwise_arrays(X, Y)             
    K = np.zeros((X.shape[0],Y.shape[0]))
    
    if X is Y: #fit-> La gramiana K es simétrica
        for i,x in enumerate(X):
            for j,z in enumerate(Y):                
                K[i][j] = K[j][i] = (x@z)**2
                if j > i:
                    break
    else: #predict-> K NO es simétrica, es K<x,x_i>
        
        return (X@Y.T) **2
        #for i,x in enumerate(X):
         #   for j,z in enumerate(Y):                
          #      K[i][j] = x@z
                         
    return K

# KERNEL S-HERMITE:
# ********************************************
# FALTA OPTIMIZAR EL CICLO PARA APROVECHAR SIMETRÍA DE MATRIZ
# PUEDE OMITIRSE VALIDACIÓN DE VECTORES SPARSE.
def K_sHerm(X, Y=None, degree=2):  
    X, Y = check_pairwise_arrays(X, Y)             
    K = np.zeros((X.shape[0],Y.shape[0]))
    if X is Y: #fit-> La gramiana K es simétrica
        for l,x in enumerate(X):
            for m,z in enumerate(X):
                summ, mult, i, j = 0, 1, 0, 0
                xlen, zlen = x.size, z.size
                while(i < xlen and j < zlen):
                    if i == j : 
                        summ = 1
                        for k in range(1,degree + 1, 1):
                            summ += H(x[i],k)*H(z[j],k) * (2**(-2*k))
                        mult *= summ
                        i = i+1
                        j = j+1
                    elif i > j:
                        j += 1
                    else:
                        i += 1
                X_gram[l][m] = mult
    return np.array(X_gram)


def my_linear(X, Y=None, dense_output=True):    
    X, Y = check_pairwise_arrays(X, Y)
    #print('shape X = ',X.shape)
    #print('shape Y = ',Y.shape)
    #print('X = ',X)
    #print('**************************')
    #print('Y = ',Y)
    return X@Y.T
    #return safe_sparse_dot(X, Y.T, dense_output=dense_output)


# HERMITE POLYNOMIALS
# *******************************************
def H(x_i,n): 
  if(n == 0):
    return 1
  if(n == 1):
    return x_i
  return (x_i * H(x_i,n-1) - (n-1) * H(x_i, n-2))




def test_K_sHerm():
    """MUESTRA POLINOMIOS DE S-HERMITE PARA VALIDAR LA H(x_i,n) ESCALADA"""
    plt.figure()
    t = np.arange(-1,1.1,.1) #Rango de prueba
    for i in range(1,6):
        plt.plot(t, H(t,i)*2**(-i), label = 'Grado '+str(i))
    plt.legend()
    plt.title("Polinomios Ortogonales de s-Hermite")  
    
    
def my_rbf(X, Y=None, gamma=None):
    """
    Compute the rbf (gaussian) kernel between X and Y::

        K(x, y) = exp(-gamma ||x-y||^2)

    for each pair of rows x in X and y in Y.

    Read more in the :ref:`User Guide <rbf_kernel>`.

    Parameters
    ----------
    X : array of shape (n_samples_X, n_features)

    Y : array of shape (n_samples_Y, n_features)

    gamma : float, default None
        If None, defaults to 1.0 / n_features

    Returns
    -------
    kernel_matrix : array of shape (n_samples_X, n_samples_Y)
    """
    print('RBF >>>')
    print('Y es None ->',Y)
    X, Y = check_pairwise_arrays(X, Y)
    print('X = Y ->',np.array_equal(X,Y))
    print('shape X = ',X.shape)
    print('shape Y = ',Y.shape)
    print('X = ',X,"\n++++++++++++++++++++++++++++")
    print('Y = ',Y)
    if gamma is None:
        gamma = 1.0 / X.shape[1]

    K = euclidean_distances(X, Y, squared=True)
    K *= -gamma
    np.exp(K, K)  # exponentiate K in-place
    print('shape K = ',K.shape)
    print('K = ',K)
    return K



def polynomial_kernel(X, Y=None, degree=3, gamma=None, coef0=1):
    """
    Compute the polynomial kernel between X and Y::

        K(X, Y) = (gamma <X, Y> + coef0)^degree

    Read more in the :ref:`User Guide <polynomial_kernel>`.

    Parameters
    ----------
    X : ndarray of shape (n_samples_1, n_features)

    Y : ndarray of shape (n_samples_2, n_features)

    degree : int, default 3

    gamma : float, default None
        if None, defaults to 1.0 / n_features

    coef0 : float, default 1

    Returns
    -------
    Gram matrix : array of shape (n_samples_1, n_samples_2)
    """
    X, Y = check_pairwise_arrays(X, Y)
    if gamma is None:
        gamma = 1.0 / X.shape[1]

    K = safe_sparse_dot(X, Y.T, dense_output=True)
    K *= gamma
    K += coef0
    K **= degree
    return K


def sigmoid_kernel(X, Y=None, gamma=None, coef0=1):
    """
    Compute the sigmoid kernel between X and Y::

        K(X, Y) = tanh(gamma <X, Y> + coef0)

    Read more in the :ref:`User Guide <sigmoid_kernel>`.

    Parameters
    ----------
    X : ndarray of shape (n_samples_1, n_features)

    Y : ndarray of shape (n_samples_2, n_features)

    gamma : float, default None
        If None, defaults to 1.0 / n_features

    coef0 : float, default 1

    Returns
    -------
    Gram matrix : array of shape (n_samples_1, n_samples_2)
    """
    X, Y = check_pairwise_arrays(X, Y)
    if gamma is None:
        gamma = 1.0 / X.shape[1]

    K = safe_sparse_dot(X, Y.T, dense_output=True)
    K *= gamma
    K += coef0
    np.tanh(K, K)  # compute tanh in-place
    return K

def my_kernel(X, Y):
    """
    We create a custom kernel:

                 (2  0)
    k(X, Y) = X  (    ) Y.T
                 (0  1)
    """
    M = np.array([[2, 0], [0, 1.0]])
    
    return X @ M @ Y.T