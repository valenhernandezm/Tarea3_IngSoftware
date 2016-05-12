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
        
    def Saldo(self):
        return self.balance
     
    
    