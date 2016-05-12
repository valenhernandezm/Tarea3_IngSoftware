'''
Created on May 12, 2016

@author: valentina
'''

import unittest
from BilleteraVirtual import *

class TestBilletera(unittest.TestCase):
    
    '''def testAtributoIDcreado(self):
        b1 = BilleteraElectronica('456')'''
        
    '''def testAtributosDueno(self):
        b2 = BilleteraElectronica('456','Valentina','Hernandez', '21534334')'''
    
    def testMetodoSaldo(self):
        b3 = BilleteraElectronica('456','Valentina','Hernandez', '21534334', 123)
        b3.Saldo()

if __name__ == '__main__':
    unittest.main()
    
     
    
        
    
        
        
        
        
        
        