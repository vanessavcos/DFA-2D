#thanks to Alexey Abramov. Code adaptade from https://salzis.wordpress.com/2012/10/01/robust-least-squares-for-fitting-data/

import numpy as np

def fit2D(k, s, e):
    # coefficients of the model
    a1, a2, a3 = 0.8, 0.14, 0.42
    # ground truth
    A_gt = [a1, a2, a3]
    # create a coordinate matrix
    nx = np.arange(1,s+1)
    ny = np.arange(1,s+1)
    x, y = np.meshgrid(nx, ny)

    # make the estimation
    if e == 1:
        z = a1 * x + a2 * y + a3
    if e == 2:
        z = a1 * x * x + a2 * y * y + a3
        x = np.power(x, 2)
        y = np.power(y, 2)

    # non-robust least squares estimation
    # X*A = Z
    x_fl = x.flatten()
    y_fl = y.flatten()
    z_ones = np.ones([x.size, 1])
    X = np.hstack((np.reshape(x_fl, ([len(x_fl), 1])), np.reshape(y_fl, ([len(y_fl), 1])), z_ones))
    Z_fl = k.flatten()
    Z = np.reshape(Z_fl, ([len(Z_fl), 1]))
    A_lsq = np.linalg.lstsq(X, Z)[0]

    # robust least sqaures (starting with the least squares solution)
    A_robust = A_lsq
    
    #Compute the residuo
    resid = np.dot(X, A_robust) - Z
    resid = np.power(resid,2)
    t = np.sum(resid)/np.power(s,2)
    return t