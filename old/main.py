import numpy as np
from Evoluzione import evoluzione
import time
w0 = 7.7E+11
w1 = 3.1E+7
w2 = 3.8E-5
w3 = 4.2E+7
wr = np.array([w0,w1,w2,w3])

n = np.array([1,0])
wl = 1.2*10**(11)
w  = wl

t0 = 1
tf = 1
N  = 10000

dt = tf/N

t1 = time.time()

g = evoluzione(t0 , N , dt , w , wl , wr, n , F = 1 )



V = g.potenziale()



print(V)


t2 = time.time()
print(t2-t1)
