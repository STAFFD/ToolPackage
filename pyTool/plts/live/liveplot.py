from matplotlib.animation import FuncAnimation
import matplotlib._color_data as mcd
import matplotlib.pyplot as plt
# from celluloid import Camera
import numpy as np
import random
import time

"""Easy matplotlib animation."""
# from typing import Dict, List
from collections import defaultdict

from matplotlib.figure import Figure
from matplotlib.artist import Artist
from matplotlib.animation import ArtistAnimation


class Camera:
    """Make animations easier."""

    def __init__(self, figure):
        """Create camera from matplotlib figure."""
        self._figure = figure
        # need to keep track off artists for each axis
        self._offsets = {
            k: defaultdict(int) for k in [
                'collections', 'patches', 'lines', 'texts', 'artists', 'images'
            ]
        }
        self._photos = []

    def snap(self):
        """Capture current state of the figure."""
        frame_artists = []
        for i, axis in enumerate(self._figure.axes):
            if axis.legend_ is not None:
                axis.add_artist(axis.legend_)
            for name in self._offsets:
                new_artists = getattr(axis, name)[self._offsets[name][i]:]
                frame_artists += new_artists
                self._offsets[name][i] += len(new_artists)
        self._photos.append(frame_artists)
        return frame_artists

    def animate(self, *args, **kwargs):
        """Animate the snapshots taken.

        Uses matplotlib.animation.ArtistAnimation

        Returns
        -------
        ArtistAnimation

        """
        return ArtistAnimation(self._figure, self._photos, *args, **kwargs)


class LivePlot:

    def __init__(self, dataSize, legends, ylim=[], title="", intervel=50, dtype=np.float64, xMax=50):
        assert len(legends) == dataSize, "Titles number does not match"
        assert type(ylim) == list and (len(ylim) == 2 or len(ylim) == 0)
        self.legends = legends
        self.title = title
        self.interval = intervel
        self.ylim = ylim
        plt.style.use('fivethirtyeight')
        self.fig, self.ax = plt.subplots(dpi=200)
        self.cam = Camera(self.fig)

        self.x_values = np.empty([0], dtype=np.int64)
        self.y_values = np.empty([dataSize, 0], dtype=np.float64)
        self.index = 0
        self.counter = 0
        self.xMax = xMax
        self.colors = np.random.choice(list(mcd.CSS4_COLORS.values()), dataSize)

    def append(self, data):
        self.y_values = np.append(self.y_values, data, axis=1)
        idx = self.index + data.shape[1]
        self.x_values = np.append(self.x_values, np.arange(self.index, idx))
        self.index = idx

        if self.counter > self.xMax:
            '''
            This helps in keeping the graph fresh
            '''
            self.x_values = np.delete(self.x_values, 0, axis=0)
            self.y_values = np.delete(self.y_values, 0, axis=1)
            plt.cla() # clears the values of the graph
        else:
            self.counter += 1

        for color, each in enumerate(self.y_values):
            plt.plot(self.x_values, each, linestyle='-', linewidth=1.0, color=self.colors[color])
        
        self.ax.legend(self.legends, loc = "upper right", fontsize=10)
        if self.title:
            plt.title(self.title, fontsize=10)
        self.ax.tick_params(axis='both', which='major', labelsize=10)
        if len(self.ylim) == 2:
            plt.ylim(self.ylim)
        self.cam.snap()
        

    def display(self):
        ani = FuncAnimation(plt.gcf(), self.cam.animate, self.interval)
        plt.tight_layout()
        plt.show()


if __name__ == '__main__':
    lp = LivePlot(dataSize=3, ylim=[0, 50], legends=["random1", "random2", "random3"], intervel=1)

    import threading
    import time
    def thread_function(name):
        print(name)
        time.sleep(0.5)
        while True:
            lp.append(np.array([[random.randint(0, 5)], [random.randint(3, 8)], [random.randint(0, 10)]]))
            time.sleep(0.05)

    x = threading.Thread(target=thread_function, args=(1,))
    x.start()


    lp.display()
