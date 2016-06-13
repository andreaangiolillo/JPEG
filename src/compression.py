'''
Created on 11 giu 2016

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


import numpy
from PIL import Image
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from scipy import misc

class Compress:
    
    #attributi privati
    quality = 1 #qualita immagine
    qf = 1  #costante  che moltiplica la matrice di quantizzazione standard per le immagini 
    Q = [] #matrice di quantizzazione
    N = 1 # n definito dall'utente
    
    def __init__(self, quality):#costruttore
        
        N = 1
        if (quality > 100):
            print "Warning: quality > 100 is not possible, quality initialize to 100"
            self.quality = 100
        elif(quality < 1):
            print "Warning: quality < 1 is not possible, quality initialize to 1"
            self.quality = 1
            
        #definizione qf
        elif (quality > 50):
            
            self.qf = (100.0 - float(quality))/50.0
            print self.qf
        else:
            self.qf = 50.0/float(quality)   
        
        
        self.quality = quality
           
        if quality != 100:
            self.Q = numpy.dot(self.qf, [[16.0000, 11.0000, 10.0000, 16.0000, 24.0000, 40.0000, 51.0000, 61.0000],
                           [12.0000, 12.0000, 14.0000, 19.0000, 26.0000, 58.0000, 60.0000, 55.0000],
                           [14.0000, 13.0000, 16.0000, 24.0000, 40.0000, 57.0000, 69.0000, 56.00000],
                           [14.0000, 17.0000, 22.0000, 29.0000, 51.0000, 87.0000, 80.0000, 62.0000],
                           [18.0000, 22.0000, 37.0000, 56.0000, 68.0000, 109.0000, 103.0000, 77.0000],
                           [24.0000, 35.0000, 55.0000, 64.0000, 81.0000, 104.0000, 113.0000,92.0000],
                           [49.0000, 64.0000, 78.0000, 87.0000, 103.0000, 121.0000, 120.0000, 101.0000],
                           [72.0000, 92.0000, 95.0000, 98.0000, 112.0000, 100.0000, 103.0000, 99.0000]
                           ])
            print self.qf
            print self.Q
            self.Q = numpy.matrix.round(self.Q)
            print self.Q
        else:
            self.Q = numpy.ones(8,8)#se la quality = 100 allora Q = una matrice di soli 1
            
    def getquality(self):
        return self.quality;
    def getqf(self):
        return self.qf
    def getQ(self):
        return self.Q
    def getN(self):
        return self.N
      
      
    def setquality(self,q):
        if (q > 100):
            print "Warning: quality > 100 is not possible, quality initialize to 100"
            self.quality = 100
        elif(q < 1):
            print "Warning: quality < 1 is not possible, quality initialize to 1"
            self.quality = 1
        else: self.quality = q
        
        if (self.quality > 50):
            self.qf = (100 - self.quality)/ 50
        else:
            qf = 50/self.quality  
    
        
    
    def setN(self,N):
        self.N = N
    
    def sefQ(self,Q): #la tabella Q passata ha tutte le proprieta per iniziare la compressione
        self.Q = Q
        
    def get_2D_dct(self,img):
        """ Get 2D Cosine Transform of Image"""
        return fftpack.dct(fftpack.dct(img.T, norm='ortho').T, norm='ortho')
    
    def get_2d_idct(self,coefficients):
        """ Get 2D Inverse Cosine Transform of Image"""
        return fftpack.idct(fftpack.idct(coefficients.T, norm='ortho').T, norm='ortho')
    
    def compress(self,filename):
        
       img = Image.open(filename)
       A = numpy.array(img)
       print A
       print A.shape
     
        