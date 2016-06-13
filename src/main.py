'''
Created on 11 giu 2016

@author: Work
'''
from Tkinter import Tk
from tkFileDialog import askopenfilename
import compression

if __name__ == '__main__':

    Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
    filename = askopenfilename() # show an "Open" dialog box and return the path to the selected file
    print(filename)
    
    dct2 = compression.Compress(75)
    dct2.compress(filename)