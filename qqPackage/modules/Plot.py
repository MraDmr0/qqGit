import numpy as np
import matplotlib.pyplot as plt


def plot_qb(prefix):
    fig , ax = plt.subplots(1,1,figsize = (8,8) ,  dpi = 300)
    q = np.loadtxt("q_"+prefix+".txt" , dtype = complex)
    t = np.loadtxt("t_"+prefix+".txt" , dtype = float)
    t = t*10**(6)
    
    ax.plot(t , abs(q)[:,0] , label = r"State $|0\rangle$")
    ax.plot(t , abs(q)[:,1] , label = r"State $|1\rangle$")
    ax.set_xlabel("time (ns)")
    plt.legend()
    plt.savefig(prefix+".png")
