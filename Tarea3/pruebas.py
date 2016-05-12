'''
Created on May 12, 2016

@author: valentina
'''

import unittest
from BilleteraVirtual import *
from datetime import datetime



class TestBilletera(unittest.TestCase):
    
    '''def testAtributoIDcreado(self):
        b1 = BilleteraElectronica('456')'''
        
    '''def testAtributosDueno(self):
        b2 = BilleteraElectronica('456','Valentina','Hernandez', '21534334')'''
    
    def testMetodoSaldo(self):
        b3 = BilleteraElectronica('456','Valentina','Hernandez', '21534334', 123)
        b3.saldo()
        
    def testCreditoyMetodoRecargar(self):
        b4 = BilleteraElectronica("759TgHJ1", "Pedro", "Perez", "5617234", 156)
        Fecha = datetime(2016, 5, 28, 7, 5)
        b4.recargar(21000, Fecha, "981yHJ32")

if __name__ == '__main__':
    unittest.main()
    
     
    
        
    
        
        
        
        
        
        