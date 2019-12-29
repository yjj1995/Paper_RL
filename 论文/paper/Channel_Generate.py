import numpy as np
def Channel_Generate(N,M,dis):
     dis1 = dis
     H = 2**0.5/2*(np.random.randn(N,M))+1j*(np.random.randn(N,M))*dis1**-2 
     return H