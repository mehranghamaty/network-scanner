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


Should find a proper structure

Generics/
SystemInfo/
PlotTools/
main.py

?



# Running

python3 main.py