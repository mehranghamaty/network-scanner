from xml.dom.minidom import Element
import PySimpleGUI as sg
from typing import Tuple
from dataclasses import dataclass



class NetworkGraph(sg.Graph):
    """
        simple class which allows adding points to a line chart.

        ideally looking to have a legend, scrolling and more than one line

        auto scalling would be a nice to have as well.

        lots of hard coding until things are normalized
        
        resizing makes things distorted.

        probably have to get a seperate function for resizing

        theres so much not implemented....
        
    """
    _POINTCOLOR = 'green'
    _POINTSIZE = 10
    _legend = None

    def _redraw_points(self):
        """
            check to see if the points are on the canvas
        """
        self.erase()
        for j, (i, (x, y)) in enumerate(self._points):
            self.draw_point((x,y), self._POINTSIZE, color=self._POINTCOLOR)
            if j > 0:
                print(j)
                print(self._points[j-1])
                self.draw_line(self._points[j-1][1], (x,y))
        
    def _draw_legend(self):
        """
            should check to see if it has moved

            not sure if this is worth it, would be able to implement something with
            matplotlib so much quicker
        """
        print("drawing legend")
        if self._legend:
            self.delete_figure(self._legend)
        buffer = 20
        width, height = 100, 50
        #legend size 
        tl = (self.TopRight[0]-width-buffer, self.TopRight[1]-buffer)
        br = (self.TopRight[0]-buffer, self.TopRight[1]-height-buffer)
        self._legend = self.draw_rectangle(top_left=tl, bottom_right=br, fill_color='blue')

    def _check_scroll(self):
        if len(self._points) <=0:
            return
        x, y = self.get_size()
        rx, ry = self._points[-1][1]
        dx, dy = 0, 0

        print(rx, ry, self.TopRight[0])
        if rx > self.TopRight[0]:
            dx = self.TopRight[0] - rx 
        
        print(ry, self.TopRight[1])
        if ry > self.TopRight[1]:
            dy = self.TopRight[1] - ry

        self.move(dx, dy)
        #Why does this not happen in the move function!
        self.BottomLeft = (self.BottomLeft[0] - dx, self.BottomLeft[1] - dy)
        self.TopRight = (self.TopRight[0] - dx, self.TopRight[1] - dy)
        #self._redraw_points()
        #self.set_size((x, y))

    def __init__(self, *args, **kwargs):
        """
            should provide defaults and have it autoscale
        """

        super(NetworkGraph, self).__init__(*args, **kwargs)
        self._points = []
        self._lines = []


    def add_point(self, coord):

        self._draw_legend()
        self._check_scroll()
        if len(self._points) != 0:
            line = self.draw_line(self._points[-1][1], coord)
            self._lines.append(line)


        point = self.draw_point(coord, self._POINTSIZE, color=self._POINTCOLOR)
        self._points.append((point,coord))
        print(self._points)
        
if __name__ == "__main__":
    ng = NetworkGraph(canvas_size=(400, 400), graph_bottom_left=(0,0),
             graph_top_right=(400, 400), background_color='red', 
             enable_events=True, key='graph')
    layout = [[ng]]

    window = sg.Window('Graph Test', layout, finalize=True)
    
    x, y = 10, 10
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Cancel':
            break

        ng.add_point((x, y))
        x += 19
        y += 5

    window.close()