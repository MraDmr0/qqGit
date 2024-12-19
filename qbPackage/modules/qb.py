"Main executable file of qbPackage Ver. 1.0"

#import needed packages
import numpy as np
import time
from Read_input import read_run
from Write_output import write_out_qb , write_outt
from RK4 import rk4_qb 
from Plot import plot_qb
import sys
#imaginary unit
im = 1j
#Staring message
print("Execution of qq.py started\n")
#input file reading
filein = str(sys.argv[1])
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
    #time evolution    
    rk4_qb(prefix , n , ti , tf , N,S , wr , wl , w , F)
    #
    time2 = time.time()
    #output
    write_outt(prefix, time1 , time2)
    plot_qb(prefix)

else:
    raise TypeError("Wrong number of states")





