"""
    Generic window to display a grid of information
"""

import PySimpleGUI as sg
from collections import namedtuple

class GridWindow(sg.Window):
    """
        Takes a list of named tuple (where the elements in the list are the same type)

        generates a grid view where each of the columns would be a field and the rows
        are the values of the fields

        can I have a button?
    """
    def _genLayout(self):
        self._layout = []

        if len(self._contents) < 1:
            raise("need atleast one element in the list")

        tmp_row = [sg.Text("\t")]
        for i, field in enumerate(self._contents[0]._fields):
            print(i, field)
            tmp_row.append(sg.Text(field))

        self._layout.append(tmp_row)

        for i, item in enumerate(self._contents):
            tmp_row = [sg.Button("{}\t".format(i), key=i)]
            for i, field in enumerate(item._fields):
                tmp_row.append(sg.Text("{}\t".format(item[i])))


            self._layout.append(tmp_row)
            
        print(self._layout)
        return self._layout

    def __init__(self, list_of_named_tuple):
        self._contents = list_of_named_tuple
        self._title = type(self._contents).__name__
        self._genLayout()
        super(GridWindow, self).__init__(self._title, self._layout)


if __name__ == "__main__":
    GroceryList = namedtuple("Shop", ['name', 'price', 'quantity'])
    myGL =  [ GroceryList("bannana", 12.20, 2),
              GroceryList("egg", 2.20, 2)]

    for item in myGL:
        print(item)
    window = GridWindow(myGL)

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Cancel':
            break
        
        print(event, values)
    
    window.close()