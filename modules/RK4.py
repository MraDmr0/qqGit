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
    print(t) 
    K0 =  np.zeros(2 , dtype = complex)
    K1 =  np.zeros(2 , dtype = complex)
    K2 =  np.zeros(2 , dtype = complex)
    K3 =  np.zeros(2 , dtype = complex)
    q0 =  np.zeros(2 , dtype = complex)
    qf =  np.zeros(2 , dtype = complex)
    q0 = n.copy()
    
    q_save = open("q_"+str(prefix)+".txt" , "w")
    t_save = open("t_"+str(prefix)+".txt" , "w")
    #np.savetxt(t_save , np.atleast_1d(t0) )
    #q0_save = np.column_stack((q0[0] , q0[1]))
    #np.savetxt(q_save , q0_save )
    a     = int(N/20)
    tff   = np.zeros(a)
    qff0  = np.zeros(a , dtype = complex)
    qff1  = np.zeros(a , dtype = complex)
    
    qff0[0] = q0[0].copy()
    qff1[0] = q0[1].copy()
    tff[0]  = t[0].copy()
    i       = 1


    for j in range(N):
    
        V  = potential_qb(t[j-1] , dt , wrr, w , F )
        
        K0 = np.dot(V[0] , q0)
        K1 = np.dot(V[1] , q0 + 0.5*dt*K0)
        K2 = np.dot(V[1] , q0 + 0.5*dt*K1)
        K3 = np.dot(V[2] , q0 + dt*K2)

        qf = q0 + dt/6*(K0 + 2*K1 + 2*K2 + K3)

        norm = np.sqrt(np.dot(qf.conjugate() , qf))
        qf   = qf/norm

        q0 = qf.copy()
        if j%20 == 0:

            qff0[i] = q0[0].copy()
            qff1[i] = q0[1].copy()
            tff[i]  = t[j].copy()
            i = i + 1

 
    #save
    qff = np.column_stack((qff0 , qff1))
    
    np.savetxt(q_save , qff)
    np.savetxt(t_save , tff)
    q_save.close()
    t_save.close()




