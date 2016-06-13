'''
Created on 13 giu 2016

@author: Work
'''
import io
import os
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from scipy import fftpack
import urllib2
import IPython
from Tkinter import Tk
from tkFileDialog import askopenfilename

image_url='http://i.imgur.com/8vuLtqi.png'

def get_image_from_url(image_url, size=(128, 128)):
    
    image = Image.open(image_url)
    img_color = image.resize(size, 1) #modifico la dimensione dell'inmmagine
    img_grey = img_color.convert('L') # converte l'immagine monocromatico
    img = np.array(img_grey, dtype=np.float)
    return img
 
def get_2D_dct(img):
    """ Get 2D Cosine Transform of Image
    """
    print fftpack.dct(fftpack.dct(img.T, norm='ortho').T, norm='ortho')
    return fftpack.dct(fftpack.dct(img.T, norm='ortho').T, norm='ortho')

def get_2d_idct(coefficients):
    """ Get 2D Inverse Cosine Transform of Image
    """
    print fftpack.idct(fftpack.idct(coefficients.T, norm='ortho').T, norm='ortho')
    return fftpack.idct(fftpack.idct(coefficients.T, norm='ortho').T, norm='ortho')

def get_reconstructed_image(raw):
    img = raw.clip(0, 255)
    img = img.astype('uint8')
    img = Image.fromarray(img)
    return img



if __name__ == '__main__':
    Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
    filename = askopenfilename() # show an "Open" dialog box and return the path to the selected file
    print(filename)
    print get_image_from_url(filename)
