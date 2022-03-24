#from dataclasses import dataclass
from typing import Optional
import psutil


class Proc:
    """ class for holding info related to the """
    def __init__(self, proc):
        self._proc = proc

    @property
    def name(self):
        return self._proc.name()

    @property
    def pid(self):
        return self._proc.pid

    def __repr__(self):
        return "{} ::: {}".format(self._proc.name(), self._proc.pid)




class SystemInfo:
    """
        Holds system information.
    """
    _processes : Optional[list[Proc]]
    _nics : Optional[list[str]]
    _connections = None
    _process_lookup = None

    def _getNics(self):
        self._nics = list(psutil.net_if_addrs().keys())

    def _getProcesses(self):
        self._processes = []
        for proc in psutil.process_iter(attrs=None, ad_value=None):
            try:
                self._processes.append(Proc(proc))
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                pass
        print("processes are ", self._processes)

    def _getConnections(self):
        self._connections = psutil.net_connections()
        #for conn in self._connections:
        #    print(conn)

    def _makeLookupTable(self):
        #should be namedtuples
        self._process_lookup = {p.pid :  p.info for p in psutil.process_iter(['name', 'username'])}


    @property
    def nics(self):
        if self._nics == None:
            self._getNics()
        return self._nics

    @property
    def processes(self):
        if self._processes == None:
            self._getProcesses()
        return self._processes

    @property
    def connections(self):
        if self._connections == None:
            self._getConnections()
        return self._connections


    def process_lookup(self, pid):
        if self._process_lookup == None:
            self._makeLookupTable()
        print(pid)
        print(self._process_lookup)
        print(pid)
        return self._process_lookup[pid]

    def __init__(self):
        self._processes = None
        self._nics = None
        self._connections = None
        self._process_lookup = None

if __name__ == "__main__":
    si = SystemInfo()
    si.processes
    #si._getConnections()

