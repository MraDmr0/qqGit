import numpy as np

#unita immaginaria
im = 1j
#costante di plank ridotta (meV*s)
h_bar = 6.582119569*10**(-13)

class evoluzione:
    """
    Classe per calcolare l'evoluzione di un sistema a due (o quattro) stati  
    quando soggetto ad un potenziale V oscillante; l'indice di python corrisponde con l'indice dello stato.
    
    Input: 
    ti  = tempo iniziale
    N   = numero di passi
    tau = time step
    wp  = frquenza di oscillazione del campo
    wl  = vettore delle frequenze di Larmor (scalare se D = 2)
    wr  = vettore delle frequenze di Raby   (matrice 4x4 se  D = 4 )
    n   = vettore delle condizioni iniziali 
    F   = funzione inviluppo (= 1)
    
    """
    
    def __init__(self,ti,N,tau,wp,wl,wr,psi0,F = 1):
        """
        Creazione della struttura dati
        """
        self.ti  = ti
        self.N   = N
        self.tau = tau
        
	#asse temporale
        self.t = np.zeros(int(N+1))
        for i in range(N+1):
            self.t[i] = self.ti + i*self.tau
        
        #dimensioni del sistema
        self.D  = int(len(psi0))
        #frequenza potenziale
        self.wp = wp
        #frequenze di Rabi
        self.wr = wr
        #frequenze di Larmor
        self.wl = wl
        #condizione iniziale
        self.psi0  = psi0
        #funzione inviluppo        
        self.F  = F
        
        #tempo corrente che viene aggiornato
        self.t0   = self.ti 
        
        #vettore di stato corrente
        self.q1t1 = np.zeros((self.D),dtype = complex)
        #vettore di stato corrente che viene aggiornato
        self.q1t  = np.zeros((self.D),dtype = complex)
        #vettore stato precedente
        self.q1n  = np.zeros((self.D),dtype = complex)
        #vettore derivate
        self.q1d  = np.zeros((self.D),dtype = complex)
        
    def potenziale(self):
        """
        Funzione che restituisce la mtrice del potenziale
        """

        if self.D == 2:
            #variabili temporanee a cui assegnare le frequenze di Rabi
            wrr = self.wr[1]+im*self.wr[2]
            
            V = np.zeros((self.D,self.D) , dtype = complex)
            V[1,1] = (self.wr[0]+self.wr[3])*np.cos(self.wp*self.t0)
            V[1,0] = wrr.conjugate()*0.5*(np.exp(-im*self.t0*(self.wp-self.wl))+np.exp(im*self.t0*(self.wp+self.wl)))
            V[0,1] = wrr*0.5*(np.exp(im*self.t0*(self.wp-self.wl))+np.exp(-im*self.t0*(self.wp+self.wl)))   
            V[0,0] = (self.wr[0]-self.wr[3])*np.cos(self.wp*self.t0)

        elif self.D == 4:
            V = np.zeros((self.D,self.D) , dtype = complex)
            for i in range(self.D):
                for j in range(self.D):
                    V[i,j] = self.wr[i,j]*np.exp((im/h_bar)*(self.wl[i] - self.wl[j])*self.t0) 
            V = V*np.cos(self.wp*self.t0)
        
        return V
        
    def derivata(self):
        """
        Funzione che restituisce il valore della derivata temporale della soluzione
        """
        #calcolo del potenziale
        V = self.potenziale()
        self.q1d = -self.F*(im)*np.dot(V,self.q1t)
                
    def cond_ini(self):
        """
        Funzione che assegna la condizione iniziale al vettore di stato corrente, 
        imponendo anche la normalizzazione
        """
        self.q1t1[:] = self.psi0[:].copy()
        #normalizzazione
        norm = np.sqrt(np.dot(self.q1t1[:].conjugate(),self.q1t1[:]))
        self.q1t1[:] = self.q1t1[:]/norm
        
    def RK4(self):
        """
        Funzione che calcola l'evoluzione temporale del vettore di stato con il metodo RK4
        """
        #coefficienti del metodo
        k0 = np.zeros(len(self.q1t) , dtype = complex)
        k1 = np.zeros(len(self.q1t) , dtype = complex)
        k2 = np.zeros(len(self.q1t) , dtype = complex)
        k3 = np.zeros(len(self.q1t) , dtype = complex)
        
        #condizione iniziale
        self.cond_ini()
       
        #salvataggio condizione iniziale
        q = np.column_stack((self.q1t1[:]))
        f = open("coeff.txt", "ab") 
        g = open("t.txt","ab")
        g.write(b"\n")
        f.write(b"\n")
        
        np.savetxt(g, np.array([self.t[0]]
            self.q1n[:] = self.q1t1[:].copy()
            se))
        np.savetxt(f, q)
        
        #calcolo evoluzione temporale
        for j in range(self.N): 
            #assegnazione stato corrente
            self.q1t[:] = self.q1t1[:].copy()
            self.q1n[:] = self.q1t1[:].copy()
            self.t0     = self.t[j]
   
            # iterazione K0
            self.derivata()
            k0[:] = self.q1d[:].copy()
            
            # iterazione K1
            self.q1t[:] = self.q1n[:] + 0.5*self.tau*k0[:]
            self.t0     = self.t[j]   + self.tau*0.5
            self.derivata()
            k1[:]       = self.q1d[:].copy()
            
            # iterazione K2
            self.q1t[:] = self.q1n[:] + 0.5*self.tau*k1[:] 
            self.t0     = self.t[j]   + self.tau*0.5
            self.derivata()
            k2[:]       = self.q1d[:].copy()
            
            # iterazione K3
            self.q1t[:] = self.q1n[:] + self.tau*k2[:]
            self.t0     = self.t[j]   + self.tau
            self.derivata()
            k3[:]       = self.q1d[:].copy()
            
            #calcolo soluzione step successivo
            self.q1t1[:] = self.q1n[:] + self.tau/6.*(k0[:] + 2.*k1[:] + 2.*k2[:] + k3[:])
            
            #rinormalizzazione soluzione
            norm = np.sqrt(np.dot(self.q1t1.conjugate(),self.q1t1))
            self.q1t1 = self.q1t1/norm

            #salvataggio in memoria della soluzione ogni 20 passi
            q = np.zeros((self.D) , dtype = complex)
            q = np.column_stack((self.q1t1[:]))
            if j % 20 == 0:
                f.write(b"\n")
                g.write(b"\n")
                np.savetxt(g, np.array([self.t0]))
                np.savetxt(f, q)
        #chiusura del file di salvataggio
        f.close()
        g.close()
