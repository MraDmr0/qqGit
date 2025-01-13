"Main executable file of qbPackage Ver. 1.5"

#import needed packages
import numpy as np
import time
from Read_input import read_run
from Write_output import write_out_qb , write_outt , save_out , write_out_qq
from RK4 import rk4_qb , rk4_qq
from Plot import plot_qb , plot_qq
import sys
#imaginary unit
im = 1j
#Staring message
print("Execution of qq.py started\n")
#input file reading
filein = str(sys.argv[1])
print("Reading input file "+str(filein)+"...\n")
prefix , D , ti , tf , N, S , psi , wr , wl , w , F = read_run(filein)
#
#qubit run
if D == 2:
    print("Begin of calculation...")
    #output
    write_out_qb(D , ti , tf , N,S , psi , wr , wl , w , F)
    #
    time1 = time.time()
    #
    #time evolution    
    psiff , tff = rk4_qb( psi , ti , tf , N, S , wr , wl , w , F)
    save_out(prefix , psiff , tff)
    #
    time2 = time.time()
    #output
    write_outt(prefix, time1 , time2)
    plot_qb(prefix)
elif D == 4:
    print("Begin of calculation...")
    #output
    write_out_qq(D , ti , tf , N , S , psi , wr , wl , w , F)
    #
    time1 = time.time()
    #
    #time evolution    
    psiff , tff = rk4_qq( psi , ti , tf , N, S , wr , wl , w , F)
    save_out(prefix , psiff , tff)
    #
    time2 = time.time()
    #output
    write_outt(prefix, time1 , time2)
    plot_qq(prefix)



else:
    raise TypeError("Wrong number of states")





