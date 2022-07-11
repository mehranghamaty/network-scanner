# Network Tool

Would like a gui application to monitor network traffer for each process id. 



# TODO

The way that psysimple works would like a widget for 

1. graphs
    a. Should have a legend
    b. display 2 lines

Okay seems like the app is somewhat alright. graphing


would like the application name on the main screen, the when you push the button you should get a matplot lib graph I think
preferably would like to have them on several different threads. 

Current State:
    The main screen seems to be okay

    the next would be network_graph_matplotlib.py which plots things appropriately


the problem seems to be related to event returning none, it should be the item row, maybe override the read method in the network window


Seems as though conda doesn't launch python as the same pid so sudo conda ... doesn't seem to generate the expected behavior

Should find a proper structure

Generics/
SystemInfo/
PlotTools/
main.py

?

# Running

python3 main.py


# Install

General

"""
pip install -r requirements.txt
"""

OSX

"""
brew install python-tk
"""

# Docker 
Make sure enough memory has been assigned (this would be with the desktop app)
Dam, you cannot run it in a container for hopefully obvious reasons


Seems as though osx blocks asking for the network traffic information. 

brew 

so sudo python netcontest.py works 

but 

sudo python3 netcontest does not

(no conda)

but conda doesn't seem to have pysimplegui

darwin doesn't give access to io_counters....

maybe just checking .connections and .open_files would be enough...

macs probably lock those for a reason
