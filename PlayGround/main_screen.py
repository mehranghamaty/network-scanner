import PySimpleGUI as sg
from network_graph import NetworkGraph
import settings as s

class MainScreen(sg.Window):
    def _make_layout(self):
        return [ [sg.Text('Select network adaptor'), sg.DropDown(values=self._system_info.nics, default_value=self._system_info.nics[0], key=s.NICS)],
                [sg.Text('Select a process'), sg.Drop(values=self._system_info.processes, default_value=self._system_info.processes[0], key=s.PROCS)],
                [sg.Text('Proc Info'), sg.Text('', key=s.INFO)],
                [sg.Text('Network Connections'), sg.Drop(values=self._system_info.connections, default_balue=self._system_info.connections[0], key=s.CON)],
                [self._make_graph()],
                [sg.Button('Ok'), sg.Button('Cancel')] ]

    def __init__(self, title, system_info):
        self._system_info = system_info
        self._network_graph = NetworkGraph(canvas_size=(400, 400), graph_bottom_left=(0,0),
             graph_top_right=(400, 400), background_color='red', 
             enable_events=True, key='graph')
             
        self._layout = self._make_layout()

        super(MainScreen, self).__init__(title, self._layout)
