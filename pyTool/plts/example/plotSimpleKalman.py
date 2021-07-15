from numpy.lib.type_check import real
from plts.func.plot2D import plotMultiCurve
import numpy as np

init_est = 74
init_est_err = 2
mea_err = 5

realTemperature = np.array([75]*100)
measureTemperature = realTemperature + (np.random.rand(100)-0.5)*10

def kf_sim(mea, est, est_err):
    K_G = est_err / (est_err+mea_err)
    est = est + K_G*(mea-est)
    est_err = (1-K_G)*est_err
    return est, est_err

est_list = []
est = init_est
est_err = init_est_err
for i in measureTemperature:
    est, est_err = kf_sim(i, est, est_err)
    est_list.append(est)

data = np.array([realTemperature, measureTemperature, est_list])

plotMultiCurve(data)