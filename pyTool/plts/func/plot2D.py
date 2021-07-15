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


def simplePlot(y, 
                x=None,
                style=None, 
                save=False,
                x_label="x",
                y_label="y",
                title=None,
                name="simplePlot.png",
                fitPlot=None):
    fig, ax = plt.subplots()
    if x is None:
        x = np.arange(0, y.shape[1], 1)
    for each in y:
        if type(each)==list:
            ax.plot(x, each)
        else:  
            if type(fitPlot)==FitPlot:
                fitPlot.setup(x, y, ax)
                ax.scatter(x, y)
                fitPlot.plot()
            else:
                ax.plot(x, y)
            break

    ax.set(xlabel=x_label, 
            ylabel=y_label,
            title="Plot of {} vs {}".format(x_label, y_label) if title is None else title)
    ax.grid()
    if save:
        fig.savefig("{}.png".format(name))
    plt.show()


class FitPlot:

    def __init__(self, 
                fitMethod, 
                equation=True, 
                forceZero=False, 
                position=[1, -2]) -> None:
        self.x = None
        self.y = None
        self.ax = None
        self.forceZero = forceZero
        self.equation = equation
        self.position = position
        methods = {
            "linear": self.linear
        }
        self.method = methods[fitMethod]
    
    def setup(self, x, y, ax):
        self.x = np.array(x)
        self.y = np.array(y)
        self.ax = ax

    def linear(self):
        assert self.x is not None or self.y is not None 
        a, b =  np.polyfit(self.x, self.y, 1)
        y = a*self.x+b
        self.ax.plot(self.x, y,  color='orange')
        if self.equation:
            equationText = "y={}x".format(round(a, 2))
            if not self.forceZero:
                equationText += "+{}".format(round(b, 2))
            self.ax.text(self.x[self.position[0]], 
                            self.y[self.position[1]], 
                            equationText)

    def plot(self):
        self.method()
