'''
Created on May 12, 2016

@author: valentina
'''

class BilleteraElectronica(object):
    def __init__(self,ID, nombres, apellidos, CI, PIN):
        self.ID = ID 
        self.nombres = nombres
        self.apellidos = apellidos
        self.CI = CI
        self.PIN = PIN 
        self.balance = 0
        self.creditos = []

        
        
    def saldo(self):
        return self.balance
    
    def recargar (self, monto, fecha, identificador):
        if monto <= 0:
            raise Exception ("ERROR : No se pueden recargar montos negativos") 
        else:
            recarga = (monto,fecha,identificador) 
            self.creditos.append(recarga)
            self.balance += monto 
     
    
    