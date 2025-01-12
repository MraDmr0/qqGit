import numpy as np
import matplotlib.pyplot as plt


def plot_qb(prefix):
    fig , ax = plt.subplots(1,1,figsize = (8,8) ,  dpi = 300)
    psi = np.loadtxt("psi_"+prefix+".txt" , dtype = complex)
    t = np.loadtxt("t_"+prefix+".txt" , dtype = float)
    t = t*10**(6)
    
    ax.plot(t , abs(psi)[:,0]**2 , label = r"State $|0\rangle$")
    ax.plot(t , abs(psi)[:,1]**2 , label = r"State $|1\rangle$")
    ax.set_xlabel("Time (ns)")
    ax.set_ylabel("Occupations")
    plt.legend()
    plt.savefig(prefix+".png")

def plot_qq(prefix):
    fig , ax = plt.subplots(1,1,figsize = (8,8) ,  dpi = 300)
    psi      = np.loadtxt("psi_"+prefix+".txt" , dtype = complex)
    t        = np.loadtxt("t_"+prefix+".txt" , dtype = float)
    t        = t*10**(6)
    
    ax.plot(t , abs(psi)[:,0]**2 , label = r"State $|0\rangle$")
    ax.plot(t , abs(psi)[:,1]**2 , label = r"State $|1\rangle$")
    ax.plot(t , abs(psi)[:,2]**2 , label = r"State $|2\rangle$")
    ax.plot(t , abs(psi)[:,3]**2 , label = r"State $|3\rangle$")
    ax.set_xlabel("Time (ns)")
    ax.set_ylabel("Occupations")
    plt.legend()
    plt.savefig(prefix+".png")
