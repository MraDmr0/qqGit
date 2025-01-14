import numpy as np
from numba import njit , complex128
#
im = 1j
#
@njit
def potential_qb(t , dt , wr , w , F):
    """
    wr is intended as the following array:

    wr[0]  = (wr[1] + im*wr[2])*0.5
    wr[1]  = wr[0] + wr[3]
    wr[2]  = wr[0] - wr[3]
    wr[3]  = w - wl
    wr[4]  = w + wl
    """
    V0    = np.zeros((2,2) , dtype = complex128)
    V1    = np.zeros((2,2) , dtype = complex128)
    V2    = np.zeros((2,2) , dtype = complex128)
    #
    V0[1,1] = wr[1]*np.cos(w*t)
    V0[1,0] = wr[0].conjugate()*(np.exp(-im*t*wr[3])+np.exp(im*t*wr[4]))
    V0[0,1] = wr[0]*(np.exp(im*t*wr[3])+np.exp(-im*t*(wr[4])))   
    V0[0,0] = wr[2]*np.cos(w*t)
    V0 *= -im*F
    #
    t += dt/2 
    V1[1,1] = wr[1]*np.cos(w*t)
    V1[1,0] = wr[0].conjugate()*(np.exp(-im*t*(wr[3]))+np.exp(im*t*(wr[4])))
    V1[0,1] = wr[0]*(np.exp(im*t*(wr[3]))+np.exp(-im*t*(wr[4])))   
    V1[0,0] = wr[2]*np.cos(w*t)
    V1 *= -im*F
    #
    t += dt/2 
    V2[1,1] = wr[1]*np.cos(w*t)
    V2[1,0] = wr[0].conjugate()*(np.exp(-im*t*(wr[3]))+np.exp(im*t*(wr[4])))
    V2[0,1] = wr[0]*(np.exp(im*t*(wr[3]))+np.exp(-im*t*(wr[4])))   
    V2[0,0] = wr[2]*np.cos(w*t)
    V2 *= -im*F
    #
    return V0 , V1 , V2


