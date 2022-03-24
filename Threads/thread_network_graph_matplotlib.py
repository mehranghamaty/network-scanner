
import threading
import time

import psutil

"""
if __name__ == "__main__":
    import sys
    import os

    current_dir = os.path.dirname(os.path.realpath(__file__))
    parent = os.path.dirname(current_dir)
    sys.path.insert(1, parent)
"""

from GuiSystem.network_graph_matplotlib import MetricPlot


class threaded_network_plot(threading.Thread):
    """
        Thread to manage the graph
    """
    def __init__(self, system_info, pid):
        threading.Thread.__init__(self)
        self._pid = pid

        self._system_info = system_info
        self._info = self._system_info.process_lookup(pid)
        self._app_name = self._info["name"]
        self._user_name = self._info["username"]

        self._mp = MetricPlot(self._app_name, self._user_name)
        self._process = psutil.Process(pid)
        self._running = True
    
    def run(self):
        try:
            while self._running:
                t = time.time()
                info = self._process.io_counters()

                self._mp.add_point(self._mp.READ_COUNT, t, info[0])
                self._mp.add_point(self._mp.WRITE_COUNT, t, info[1])

                self._mp.add_point(self._mp.READ_BYTES, t, info[2])
                self._mp.add_point(self._mp.WRITE_BYTES, t, info[3])

                self._mp.add_point(self._mp.READ_CHARS, t, info[4])
                self._mp.add_point(self._mp.WRITE_CHARS, t, info[5])

        finally:
            print('ended')

    def close(self):
        self._mp.close()
        self._running = False


if __name__ == "__main__":

    import SystemHelper.system_helper as sh

    system_info = sh.SystemInfo()
    pid = None

    for i, c in enumerate(system_info.connections):
        if c[i][6]:
            pid = c[i][6]
            break
    if pid:
        t = threaded_network_plot(system_info, pid)
        t.join()
    else:
        print("no suitable pid was found", pid)