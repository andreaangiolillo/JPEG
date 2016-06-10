
import numpy



class Compress:
    self.quality #qualità immagine
    self.qf #costante  che moltiplica la matrice di quantizzazione standard per le immagini 
    self.Q #matrice di quantizzazione
    self.N # n definito dall'utente
    
    def __init__(self, quality):#costruttore
        
        N = 1
        if (quality > 100):
            print "Warning: quality > 100 is not possible, quality initialize to 100"
            self.quality = 100
        elif(quality < 1):
            print "Warning: quality < 1 is not possible, quality initialize to 1"
            self.quality = 1
            
        #definizione qf
        if (quality > 50):
            self.qf = (100 - quality)/ 50
        else:
            qf = 50/quality    
            
        if quality != 100:
            Q = round(qf* [[16, 11, 10, 16, 24, 40, 51, 61],
                           [12, 12, 14, 19, 26, 58, 60, 55],
                           [14, 13, 16, 24, 40, 57, 69, 56],
                           [14, 17, 22, 29, 51, 87, 80, 62],
                           [18, 22, 37, 56, 68, 109, 103, 77],
                           [24, 35, 55, 64, 81, 104, 113,92],
                           [49, 64, 78, 87, 103, 121, 120, 101],
                           [72, 92, 95, 98, 112, 100, 103, 99]
                           ])
        else:
            Q = np.ones(8,8)#se la quality è 100 allora Q è una matrice di soli 1
            
    def getquality(self):
        return self.quality;
    def getqf(self):
        return self.qf
    def getQ(self):
        return self.Q
    def getN(self):
        return N
      
      
    def setquality(self,q):
        if (q > 100):
            print "Warning: quality > 100 is not possible, quality initialize to 100"
            self.quality = 100
        elif(q < 1):
            print "Warning: quality < 1 is not possible, quality initialize to 1"
            self.quality = 1
        else: self.quality = q
        if (quality > 50):
            self.qf = (100 - quality)/ 50
        else:
            qf = 50/quality  
    
        
    
    def setN(self):
        self.N = N
    
    def sefQ(self,Q):
        self.Q = Q
        

                