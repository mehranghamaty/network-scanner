"""
    Provides a detailed view of the network usage of a specific process
"""

import PySimpleGUI as sg
import psutil

class PidWindow(sg.Window):
    """
        Provides more information for a specific pid
    """
    _READ_COUNT = 'readcount'
    _WRITE_COUNT = 'writecount'

    _READ_BYTES = 'readbytes'
    _WRITE_BYTES = 'writebytes'
    
    _READ_CHARS = 'readchars'
    _WRITE_CHARS = 'writechars'

    _UPLOAD = 'upload'
    _DOWNLOAD = 'download'
    
    _process = None


    def update(self):
        #pio(read_count=454556, write_count=3456, read_bytes=110592, write_bytes=0, read_chars=769931, write_chars=203)
        info = self._process.io_counters()
        self.__getitem__(self._READ_COUNT).update(info[0])
        self.__getitem__(self._WRITE_COUNT).update(info[1])
        self.__getitem__(self._READ_BYTES).update(info[2])
        self.__getitem__(self._WRITE_BYTES).update(info[3])
        self.__getitem__(self._READ_CHARS).update(info[4])
        self.__getitem__(self._WRITE_CHARS).update(info[5])


    def __init__(self, system_info, pid):
        self._si = system_info
        self._process = psutil.Process(pid)

        self._info = self._si.process_lookup(pid)
        self._layout = [[sg.Text(pid), sg.Text(self._info["name"]), sg.Text(self._info["username"])],
                        [sg.Text('read count'), sg.Text("", key=self._READ_COUNT)],
                        [sg.Text('write count'), sg.Text("", key=self._WRITE_COUNT)],
                        [sg.Text('read bytes'), sg.Text("", key=self._READ_BYTES)],
                        [sg.Text('write bytes'), sg.Text("", key=self._WRITE_BYTES)],
                        [sg.Text('read chars'), sg.Text("", key=self._READ_CHARS)],
                        [sg.Text('write chars'), sg.Text("", key=self._WRITE_CHARS)],
                        [sg.Button('Ok'), sg.Button('Cancel')]]

        super(PidWindow, self).__init__("title", self._layout)

def open_pid_window(system_info, pid):
    #print(psutil.Process(pid).as_dict())
    window = PidWindow(system_info, pid)

    while True:
        event, value = window.read()
        if event == sg.WIN_CLOSED:
            break
        window.update()

    window.close()

if __name__ == "__main__":
    import SystemHelper.system_helper as sh

    system_info = sh.SystemInfo()
    window = PidWindow(system_info, system_info.processes[0].pid)

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Cancel':
            break

        window.update()
        print(event)

    window.close()