from matplotlib.pyplot import axis
from basic import showVec
import numpy as np

def showComplex(comList):
    vec = np.concatenate([np.array([[c.real, c.imag]]).transpose() for c in comList], axis=1).transpose()
    showVec(vec)

com_a = 1+1j

deg = 30
# 𝑧 = cos(θ) + 𝑖 sin(θ)
com_r = complex(np.cos(np.deg2rad(deg)), np.sin(np.deg2rad(deg)))

# θ = atan2(𝑏, 𝑎)
deg = np.rad2deg(np.arctan2(com_r.imag, com_r.real))

print("Rotate {} degrees.".format(deg))
print("Scale: {}.".format(abs(com_r)))

c = com_r * com_a

showComplex([com_a, c])