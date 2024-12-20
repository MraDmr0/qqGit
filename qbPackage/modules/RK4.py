from Potential import potential_qb
import numpy as np

im = 1j

def rk4_qb(prefix , psi0 , t0 , tf , N , S , wr , wl , w , F ):

    wrr = np.zeros(5 , dtype = complex)
    wrr[0]  = (wr[1] + im*wr[2])*0.5
    wrr[1]  = wr[0] + wr[3]
    wrr[2]  = wr[0] - wr[3]
    wrr[3]  = w - wl
    wrr[4]  = w + wl

    dt = (tf-t0)/N
    t = np.linspace(t0 , tf , N+1)
    
    K0 =  np.zeros(2 , dtype = complex)
    K1 =  np.zeros(2 , dtype = complex)
    K2 =  np.zeros(2 , dtype = complex)
    K3 =  np.zeros(2 , dtype = complex)
    q0 =  np.zeros(2 , dtype = complex)
    qf =  np.zeros(2 , dtype = complex)
    #psi0 = psi.copy()
    
    if N%S != 0 :
        a     = int(N/S)+2
    else:
        a     = int(N/S)+1
    tff    = np.zeros(a)
    psif0  = np.zeros(a , dtype = complex)
    psif1  = np.zeros(a , dtype = complex)
    
    psif0[0] = psi0[0].copy()
    psif1[0] = psi0[1].copy()
    tff[0]   = t[0].copy()
    i        = 1


    for j in range(1 , N+1):
    
        V  = potential_qb(t[j-1] , dt , wrr, w , F )
        
        K0 = np.dot(V[0] , psi0)
        K1 = np.dot(V[1] , psi0 + 0.5*dt*K0)
        K2 = np.dot(V[1] , psi0 + 0.5*dt*K1)
        K3 = np.dot(V[2] , psi0 + dt*K2)

        psif = psi0 + dt/6*(K0 + 2*K1 + 2*K2 + K3)

        norm = np.sqrt(np.dot(psif.conjugate() , psif))
        psif   = psif/norm

        psi0  = psif.copy()
        if j%S == 0 or j == N:

            psif0[i] = psi0[0].copy()
            psif1[i] = psi0[1].copy()
            tff[i]   = t[j].copy()
            i = i + 1

 
    #save
    psiff = np.column_stack((psif0 , psif1))
    
    q_save = open("psi_"+str(prefix)+".txt" , "w")
    t_save = open("t_"+str(prefix)+".txt" , "w")
    np.savetxt(q_save , psiff)
    np.savetxt(t_save , tff)
    q_save.close()
    t_save.close()



