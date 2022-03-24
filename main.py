import PySimpleGUI as sg
from Threads.thread_network_graph_matplotlib import threaded_network_plot

import settings as s
import SystemHelper.system_helper as sh
import GuiSystem.system_network_window as snw

from GuiSystem.system_pid_window import open_pid_window


sg.theme("DarkAmber")

threads = []
system_info = sh.SystemInfo()

def close_threads():
    for t in threads:
        t.close()

def join_threads():
    for t in threads:
        t.join()

"""
window = snw.NetworkGrid(system_info)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel':
        close_threads()
        break
    

    #get the (cu)pid
    #this should be done inside the NetworkGrid class through overrides.
    pid = system_info.connections[event][6]
    if pid:
        t = threaded_network_plot(system_info, pid)
        threads.append(t)
    else:
        print("pid was not selected {}".format(pid))

    #these should be threaded 
    #open_pid_window(system_info, pid)
"""
pid = None
print(system_info.connections)
for i, c in enumerate(system_info.connections):
    if c[6]:
        pid = c[6]
        break
if pid:
    t = threaded_network_plot(system_info, pid)
    t.run()
    threads.append(t)
else:
    print("no suitable pid was found", pid)

join_threads()

#join_threads()
