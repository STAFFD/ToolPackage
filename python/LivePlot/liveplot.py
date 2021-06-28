import random
from itertools import count
import time
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


x_values = []
y_values = []
z_values = []
q_values = []

counter = 0

index = count()

def animate(i):
    
    #print(counter)
    

    x = next(index) # counter or x variable -> index
    counter = next(index)
    print(counter)
    x_values.append(x)
    '''
    Three random value series ->
    Y : 0-5
    Z : 3-8
    Q : 0-10
    '''
    y = random.randint(0, 5)
    z = random.randint(3, 8)
    q = random.randint(0, 10)
    # append values to keep graph dynamic
    # this can be replaced with reading values from a csv files also
    # or reading values from a pandas dataframe
    y_values.append(y)
    z_values.append(z)
    q_values.append(q)
    
    
    if counter >40:
        '''
        This helps in keeping the graph fresh and refreshes values after every 40 timesteps
        '''
        x_values.pop(0)
        y_values.pop(0)
        z_values.pop(0)
        q_values.pop(0)
        #counter = 0
        plt.cla() # clears the values of the graph
        
    plt.plot(x_values, y_values,linestyle='--')
    plt.plot(x_values, z_values,linestyle='--')
    plt.plot(x_values, q_values,linestyle='--')
    
    ax.legend(["Value 1 ","Value 2","Value 3"])
    ax.set_xlabel("X values")
    ax.set_ylabel("Values for Three different variable")
    plt.title('Dynamic line graphs')



class LivePlot:

    def __init__(self, dataSize=1, intervel=50) -> None:
        self.interval = intervel

        plt.style.use('fivethirtyeight')
        self.fig, self.ax = plt.subplots(dpi=120)
        self.index = count()

        x_values = []

    def animate(self):
        x = next(self.index) # counter or x variable -> index
        x_values.append(x)


    def display(self):
        ani = FuncAnimation(plt.gcf(), self.animate, self.interval)
        plt.tight_layout()
        plt.show()