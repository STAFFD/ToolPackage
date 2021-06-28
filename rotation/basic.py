import numpy as np
import matplotlib.pyplot as plt

color = ['b', 'g', 'r', 'c', 'm', 'y', 'k', 'w']

def showVec(vec):
    # show in figure
    fig, ax = plt.subplots()

    vecNum = vec.shape[0]
    origin = np.array([[0 for _ in range(vecNum)], [0 for _ in range(vecNum)]]) # origin point
    
    ax.quiver(*origin, vec[:,0], vec[:,1], color=np.random.choice(color, vecNum), scale=5)
    
    ax.set_aspect('equal')
    ax.grid(True, which='both')

    # set the x-spine (see below for more info on `set_position`)
    ax.spines['left'].set_position('zero')

    # turn off the right spine/ticks
    ax.spines['right'].set_color('none')
    ax.yaxis.tick_left()

    # set the y-spine
    ax.spines['bottom'].set_position('zero')

    # turn off the top spine/ticks
    ax.spines['top'].set_color('none')
    ax.xaxis.tick_bottom()

    plt.show()