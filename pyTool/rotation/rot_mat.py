import numpy as np
from basic import showVec

def r_mat(degrees):
    deg = np.deg2rad(degrees)
    return np.array([[np.cos(deg), -np.sin(deg)],
                    [np.sin(deg), np.cos(deg)]])

# V = np.array([[1, 0], [1, 1], [2, 3]])
vector_a = np.array([[1, 1]]).transpose()
print(vector_a)
vector_b = r_mat(30).dot(vector_a)*1.2

proj_a2b = np.dot(vector_b.transpose(), vector_a)/np.square(np.linalg.norm(vector_b))*vector_b

V = np.concatenate([vector_a, vector_b, proj_a2b], axis=1).transpose()
print(V)
showVec(V)