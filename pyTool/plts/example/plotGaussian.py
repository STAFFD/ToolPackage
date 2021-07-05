from plts.basic.plot2D import plot2DFormular
import numpy as np

def gaussian(x, sig=0.5, mu=0.5):
    return 1/np.sqrt(2*np.pi*np.square(sig))*np.exp(-(np.square(x-mu)/(2*np.square(sig))))

plot2DFormular(gaussian, fRange=[-10, 10])