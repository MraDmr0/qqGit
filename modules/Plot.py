import numpy as np
import matplotlib.pyplot as plt


def plot_qb(prefix):
    q1 = np.loadtxt("q_"+prefix+".txt" , dtype = complex)
    t = np.loadtxt("t_"+prefix+".txt" , dtype = float)

    plt.plot(t , abs(q1)[:-1,0])
    plt.savefig(prefix+".img")
