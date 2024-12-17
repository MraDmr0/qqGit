#Module for output writing
import datetime

width = 40

def write_out_qb(P , ti , tf , N , n , wr , wl , w , F):
    print("Simulation of qubit system")
    print("*" * width+"\n")
    print("Calculation started at : " + str(datetime.datetime.now()))
    print("*" * width+"\n")
    print("Input parameters : \n")
    print("P   = "  + str(P))
    print("t_i = "  + str(ti))
    print("t_f = "  + str(tf))
    print("N   = "  + str(N))
    print("n   = (" + str(n[0])+","+str(n[1])+")")
    print("w_r = "  + str(wr[0])+" , " + str(wr[1])+ " , " + str(wr[2]) + " , " + str(wr[3]))
    print("w_l = "  + str(wl[0]))
    print("w   = "  + str(w))
    print("F   = "  + str(F))
    print("*" * width+"\n")

def write_outt(fileout, time1 , time2):
    print("Calculation compleated successfully at : "+ str(datetime.datetime.now())+"\n")
    print("Elapsed time for main process : " + str(time2-time1) + " s \n" )
    print("Reults written on 'q_"+fileout+".txt'")
    
