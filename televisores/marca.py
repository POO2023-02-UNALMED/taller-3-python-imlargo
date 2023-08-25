class TV:
    numTV = 0

    def __init__(self, marca, estado):
        self._marca = marca
        self._canal = 1
        self._precio = 500
        self._estado = estado
        self._volumen = 1
     
        #self._control = control


    def setMarca(self, marca):
        self._marca = marca
    

    def setCanal(self, canal):
        self._canal = canal
    

    def setPrecio(self, precio):
        self._precio = precio
    

    def setVolumen(self, volumen):
        self._volumen = volumen
    
    def setControl(self, control):
        self._control = control
    

    def getMarca(self):
        return self._marca
    

    def getCanal(self):
        return self._canal
    

    def getPrecio(self):
        return self._precio
    

    def getVolumen(self):
        return self._volumen
    
    def getControl(self):
        return self._control
    

    #------------------------------
    def setNumTv(self, num):
        TV.numTV = num

    def getNumTv(self):
        return TV.numTV
    
    #------------------------------

    #------------------------------
    def turnOn(self):
        self._estado = true
    

    def turnOff(self):
        self._estado = false
    
    def getEstado(self):
        return self._estado
    
    #------------------------------

    #------------------------------
    #Canal
    def canalUp(self):
        if (self._canal < 120 and self._estado):
            self._canal += 1
        
    def canalDown(self):
        if (self._canal > 1 and self._estado):
            self._canal -= 1
    

    #Volumen
    def volumeUp(self):
        if (self._volumen < 7 and self._estado):
            self._volumen += 1
            

    def volumeDown(self):
        if (self._volumen > 0 and self._estado):
            self._volumen -= 1
    #------------------------------

