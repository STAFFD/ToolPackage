import matplotlib.pyplot as plt
import numpy as np
from numpy.core.function_base import linspace

def plot2DFormular(func, fRange=[0, 120], precision=0.1, showSave=False):
    # Data for plotting
    x = np.arange(fRange[0], fRange[1], precision)
    y = [func(each) for each in x]

    fig, ax = plt.subplots()
    ax.plot(x, y)

    ax.set(xlabel='x', 
        ylabel=func.__name__,
        title='Plot of {}'.format(func.__name__))
    ax.grid()
    if showSave:
        fig.savefig("{}.png".format(func.__name__))
    plt.show()
