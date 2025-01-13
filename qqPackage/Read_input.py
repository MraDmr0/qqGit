#functions for input reading
#
import numpy as np
#
#
def read_run(filein):
    """
    Reads the parameters of the run from input

    """
    #open the input file
    input_file = open(filein , 'r')
    line_list  = input_file.readlines()    
    prefix     = str(line_list[5].split('=')[1])
    prefix     = prefix.strip() 
    # 
    D  = int(line_list[7].split('=')[1])
    ti = float(line_list[9].split('=')[1])
    tf = float(line_list[11].split('=')[1])
    N  = int(line_list[13].split('=')[1])
    S  = int(line_list[15].split('=')[1])
    #
    psi0      = float(line_list[19].split('=')[1])
    psi1      = float(line_list[20].split('=')[1])
    psi2      = float(line_list[21].split('=')[1])
    psi3      = float(line_list[22].split('=')[1])
    #
    wr00    = float(line_list[24].split('=')[1])
    wr01    = float(line_list[25].split('=')[1])
    wr02    = float(line_list[26].split('=')[1])
    wr03    = float(line_list[27].split('=')[1])
    wr10    = float(line_list[28].split('=')[1])
    wr11    = float(line_list[29].split('=')[1])
    wr12    = float(line_list[30].split('=')[1])
    wr13    = float(line_list[31].split('=')[1])
    wr20    = float(line_list[32].split('=')[1])
    wr21    = float(line_list[33].split('=')[1])
    wr22    = float(line_list[34].split('=')[1])
    wr23    = float(line_list[35].split('=')[1])
    wr30    = float(line_list[36].split('=')[1])
    wr31    = float(line_list[37].split('=')[1])
    wr32    = float(line_list[38].split('=')[1])
    wr33    = float(line_list[39].split('=')[1])
    #
    wl0     = float(line_list[41].split('=')[1])
    wl1     = float(line_list[42].split('=')[1])
    wl2     = float(line_list[43].split('=')[1])
    wl3     = float(line_list[44].split('=')[1])
    #
    w       = float(line_list[46].split('=')[1])
    F       = int(line_list[48].split('=')[1])
    ##
    psi    = np.array([psi0,psi1] , dtype = complex)
    nomr   = np.sqrt(np.linalg.norm(psi))
    psi    = psi/nomr
    #
    if D == 2:
      wr     = np.array([wr00 , wr01 , wr02 , wr03] , dtype = complex)
      wl     = np.array([wl0])
      psi    = np.array([psi0,psi1] , dtype = complex)
      nomr   = np.sqrt(np.linalg.norm(psi))
      psi    = psi/nomr
    else:
      psi    = np.array([psi0,psi1,psi2,psi3] , dtype = complex)
      nomr   = np.sqrt(np.linalg.norm(psi))
      psi    = psi/nomr
      wr   = np.array([[wr00 , wr01 , wr02 , wr03],
                       [wr10 , wr11 , wr12 , wr13],
                       [wr20 , wr21 , wr22 , wr23],
                       [wr30 , wr31 , wr32 , wr33]] , dtype = complex)
      wl   = np.array([wl0 , wl1 , wl2 , wl3])

    return  prefix , D , ti , tf , N , S , psi , wr , wl , w , F

