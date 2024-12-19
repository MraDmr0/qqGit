"Main executable file"

import numpy as np
import time
from Read_input import read_run
from Write_output import write_out_qb , write_outt
from RK4 import rk4_qb 
from Plot import plot_qb
import sys
#
im = 1j
#
print("Execution of qq.py started\n")
#input
filein = str(sys.argv[1])
#read parameters from input
print("Reading input file "+str(filein)+"...\n")
prefix , P , ti , tf , N, S , n , wr , wl , w , F = read_run(filein)
#
#qubit run
if P == 2:
    print("Begin of calculation...")
    #output
    write_out_qb(P , ti , tf , N,S , n , wr , wl , w , F)
    #
    time1 = time.time()
    #
    #main process    
    rk4_qb(prefix , n , ti , tf , N,S , wr , wl , w , F)
    #
    time2 = time.time()
    #output
    write_outt(prefix, time1 , time2)
    plot_qb(prefix)
    
#ququart run
elif P == 4:
    print(ciao)


else:
    raise TypeError("Wrong numer of states")





