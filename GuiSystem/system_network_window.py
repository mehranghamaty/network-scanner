"""
    Shows the pid and the network usage for the process
"""
import PySimpleGUI as sg
from GuiGeneric.grid_window import GridWindow

class NetworkGrid(GridWindow):
    """
        Static view 
    """

    def __init__(self, system_info):
        self._si = system_info
        super(NetworkGrid, self).__init__(self._si.connections)

    def read(self):

        event, values = super(NetworkGrid, self).read()

        print("from network monitor", event)
        print(self._si.connections[event])

        return event, values


if __name__ == "__main__":
    import SystemHelper.system_helper as sh

    system_info = sh.SystemInfo()
    window = NetworkGrid(system_info)

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Cancel':
            break

        print(event, values)

    window.close()

