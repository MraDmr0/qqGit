import numpy as np
from numba import njit , complex128

#definition of local variables (meV s)
h_bar = 6.582119569E-13
im = 1j
#
@njit
def potential_qb(t0 , dt , wr , w , F):
    """
    Function that computes the qubit potential at the three times needed for the RK4 algorithm.
    
    wr is intended as the following array:

    wr[0]  = (wr[1] + im*wr[2])*0.5
    wr[1]  = wr[0] + wr[3]
    wr[2]  = wr[0] - wr[3]
    wr[3]  = w - wl
    wr[4]  = w + wl
    
    The Larmor frequency is the difference between the two states
    """
    #Variables assignement
    V    = np.zeros((3,2,2) , dtype = complex128)

    t = np.array([t0 , t0+0.5*dt , t0+dt])
    
    for k in range(3):
      V[k,1,1] = wr[1]*np.cos(w*t[k])
      V[k,1,0] = wr[0].conjugate()*(np.exp(-im*t[k]*wr[3])+np.exp(im*t[k]*wr[4]))
      V[k,0,1] = wr[0]*(np.exp(im*t[k]*wr[3])+np.exp(-im*t[k]*(wr[4])))   
      V[k,0,0] = wr[2]*np.cos(w*t[k])
    V *= -im*F
    
    return V


@njit
def potential_qq(t , dt , wr , wl , w , F):
    """Function that computes the qubit potential at the three times needed for the RK4 algorithm.
        The Rabi frequencies are given in matrix form, while Larmor frequencies are intended as the energy of each level in meV"""

    V     = np.zeros((3,4,4) , dtype = complex128)

    for k in range(3):
        for i in range(4):
            for j in range(4):
                V[k,i,j] = wr[i,j]*np.exp((im/h_bar)*(wl[i] - wl[j])*t)
   
        V[k,:,:] *= -im*F*np.cos(w*t)
        t += dt*0.5

    return V



