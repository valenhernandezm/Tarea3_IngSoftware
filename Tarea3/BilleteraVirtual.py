'''
Created on May 12, 2016

@author: valentina
'''
from datetime import *
import calendar
import sys
import time



class movimientos:
    def __init__(self, monto, fecha, ident):
        self.monto = monto
        self.fecha = fecha
        self.ident = ident

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
    
    def recargar (self, monto, identificador):
        if monto <= 0:
            raise Exception ("ERROR : No se pueden recargar montos negativos") 
        else:
            fecha = time.strftime("%c")
            recarga = movimientos(monto, fecha, identificador) 
            self.creditos.append(recarga)
            self.balance += monto 
     
    
