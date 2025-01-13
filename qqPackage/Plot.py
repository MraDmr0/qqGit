import numpy as np
import matplotlib.pyplot as plt


def plot_qb(prefix):
    """Function that plots the computed square moduli of the two components of the wavefunction, 
   stored in psi_preix.txt  and t_prefix, as a function of time"""
   
    #load wfc and time axis
    psi = np.loadtxt("psi_" +prefix+".txt" , dtype = complex)
    t   = np.loadtxt("t_"   +prefix+".txt" , dtype = float)
    #conversion to us
    t   = t*10**(6)
    #creation of the figure
    fig , ax = plt.subplots(1 , 1 , figsize = (8,8) ,  dpi = 300)
    #append data to the figure
    ax.plot(t , abs(psi)[:,0]**2 , label = r"State $|0\rangle$")
    ax.plot(t , abs(psi)[:,1]**2 , label = r"State $|1\rangle$")
    #personalization
    ax.set_xlabel(r"Time $(\mu s)$")
    ax.set_ylabel("$|\Psi|^2$")
    plt.legend()
    #save fiugre
    plt.savefig(prefix+".png")

def plot_qq(prefix):
    """Function that plots the computed square moduli of the four components of the wavefunction, 
   stored in psi_preix.txt  and t_prefix, as a function of time"""
    
    #load wfc and time axis
    psi      = np.loadtxt("psi_" +prefix+".txt" , dtype = complex)
    t        = np.loadtxt("t_"   +prefix+".txt" , dtype = float)
    #conversion to ms
    t        = t*10**(6)
    #creation of the figure
    fig , ax = plt.subplots(1, 1 , figsize = (8,8) ,  dpi = 300)
    #append data to the figure
    ax.plot(t , abs(psi)[:,0]**2 , label = r"State $|0\rangle$")
    ax.plot(t , abs(psi)[:,1]**2 , label = r"State $|1\rangle$")
    ax.plot(t , abs(psi)[:,2]**2 , label = r"State $|2\rangle$")
    ax.plot(t , abs(psi)[:,3]**2 , label = r"State $|3\rangle$")
    #personalization
    ax.set_xlabel(r"Time $(\mu s)$")
    ax.set_ylabel("Occupations")
    plt.legend()
    #save figure
    plt.savefig(prefix+".png")
