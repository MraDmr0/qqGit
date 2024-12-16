from Potential import potential_qb
import numpy as np

im = 1j


def rk4_qb(prefix , n , t0 , tf , N , wr , wl , w , F ):

    wrr = np.zeros(5 , dtype = complex)
    wrr[0]  = (wr[1] + im*wr[2])*0.5
    wrr[1]  = wr[0] + wr[3]
    wrr[2]  = wr[0] - wr[3]
    wrr[3]  = w - wl
    wrr[4]  = w + wl

    dt = (tf-t0)/N
    t = np.linspace(t0 , tf , N)
    #
    t_save = open("t_"+str(prefix)+".txt" , "ab")
    np.savetxt(t_save , t )
    
    for j in range(N):
        
        V = potential_qb(t[j] , dt , wrr, w , F )
