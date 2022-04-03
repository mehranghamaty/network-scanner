"""
Would like an ecapsulating class
 to plot the different metric per process
"""

from dataclasses import dataclass
import threading
import time
from typing import Dict, List

import psutil

from SystemHelper.system_helper import SystemInfo



@dataclass
class MetricInfo:
    title: str 
    xs: List[float]
    ys: List[float]

class MetricPlot:
    """
        Whould hold multiple line plots. 
    """
    
    import matplotlib.pyplot as plt

    _lines : Dict[str, MetricInfo]

    READ_COUNT = 'read count'
    WRITE_COUNT = 'write count'

    READ_BYTES = 'read bytes'
    WRITE_BYTES = 'write bytes'
    
    READ_CHARS = 'read chars'
    WRITE_CHARS = 'write chars'

    def _plot(self):
        self.plt.clf()
        for key, info in self._lines.items():
            self.plt.plot(info.xs, info.ys, label = key)

        self._fig.canvas.set_window_title(self._user_name)
        self._fig.suptitle(self._app_name)
        self.plt.legend()
        self.plt.draw()
        self.plt.pause(0.00000001)

    def add_point(self, metric_str : str, x : float, y : float):
        if metric_str not in self._lines:
            self._lines[metric_str] = MetricInfo(metric_str, [], [])

        self._lines[metric_str].xs.append(x)
        self._lines[metric_str].ys.append(y)

        self._plot()

    def close(self):
        self.plt.close()

    def __init__(self, app_name = "", user_name=""):
        print("appname ", app_name, " user name ", user_name)
        self._app_name = app_name
        self._user_name = user_name
        self.plt.ion()
        self._fig = self.plt.gcf()
        self.plt.show()
        self._lines = {}

if __name__ == "__main__":
    mp = MetricPlot()

    x, y = 1, 1

    while True:
        mp.add_point("test", x, y)
        x += 1
        print(x, y)
