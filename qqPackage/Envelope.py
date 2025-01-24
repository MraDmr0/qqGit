import numpy as np

def off(ti , tf  , N , *args , **kwargs):
  E = np.zeros(N+1)
  return E

def singimp(ti , tf , N , F , t0 , t1  , *args):
  if t0 < ti or t1 > tf:
    raise TypeError("The impulse must be within the simulation time")
  
  else:
    E = np.zeros(N+1)
    t = np.linspace(ti , tf , N+1)
    dt = t[1]
    i = int((t0-ti)/(dt))
    f = int((t1-ti)/(dt))
    E[i:f] = F
  return E

def gauss(ti , tf , N , F , t0 , t1 , sigma):
  if t0 < ti:
    raise TypeError("The impulse must be within the simulation time")
  
  else:
    E  = np.zeros(N+1)
    t  = np.linspace(ti , tf , N+1)
    dt = t[1]

    E  = F / (np.sqrt(2.0 * np.pi) * sigma) * np.exp(-np.power((t - t0)*10**(6) / sigma, 2.0) / 2)

  return E/np.max(E)
  
def twoimp(ti , tf , N , F , t0 , t1 , sigma , t00 , t11 , *args):
  if t0  < ti or t1  > tf or t00 < ti or t11 > tf:
    raise TypeError("The impulse must be within the simulation time")
  
  else:
    E = np.zeros(N+1)
    t = np.linspace(ti , tf , N+1)
    dt = t[1]
    i = int((t0-ti)/(dt))
    f = int((t1-ti)/(dt))
    i1= int((t00-ti)/(dt))
    f1 = int((t11-ti)/(dt))
    
  E[i:f] = F

  E[i1:f1] = F

  return E

def twogauss(ti , tf , N , F , t0 , t1 , sigma , t00 , t11 , *args):
  if t0 < ti or t00 > tf:
     raise TypeError("The impulse must be within the simulation time")
  
  else:

    E1  = np.zeros(N+1)
    E2  = np.zeros(N+1)
    t  = np.linspace(ti , tf , N+1)
    dt = t[1]

    E1  = F / (np.sqrt(2.0 * np.pi) * sigma) * np.exp(-np.power((t - t0)*10**(6) / sigma, 2.0) / 2)
    E2  = F / (np.sqrt(2.0 * np.pi) * sigma) * np.exp(-np.power((t - t00)*10**(6) / sigma, 2.0) / 2)
    
  return E1+E2



modes = {"off":off , 'singimp': singimp , "gauss":gauss , "2imp":twoimp , "2gauss":twogauss}

def envelope(ti , tf , N , mode , F , t0 , t1 , sigma , t00 , t11):
  print(mode)
  print(str(mode))
  if mode in modes:
    E = modes[mode](ti , tf , N , F , t0 , t1 , sigma , t00 , t11)
    return E

  else:
    raise TypeError("Envelope mode not supported")
