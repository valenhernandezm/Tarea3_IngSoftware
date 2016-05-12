'''
Created on 12 de may. de 2016

@author: giuli
'''
import unittest
from BilleteraVirtual import *
from datetime import datetime

class TestPrograma(unittest.TestCase):
    
        def testRecargaNegative(self):
            Billetera = BilleteraElectronica("42Sbb90j" , "Luis", "Pacheco", "8542847", "450183")
            self.assertRaises(Exception, Billetera.recargar, -5000, "HOk234t1" )
            
        def testConsumoInvalid(self):
            Billetera = BilleteraElectronica("42Sbb90j" , "Luis", "Pacheco", "8542847", "450183")
            Billetera.recargar(100, "HOj234t1")
            self.assertRaises(Exception, Billetera.consumir, 500, "HOj234t1", 450183)
            
        def testPINInvalid(self):
            Billetera = BilleteraElectronica("42Sbb90j" , "Luis", "Pacheco", "8542847", "450183")
            Billetera.recargar(100, "HOj234t1")
            self.assertRaises(Exception, Billetera.consumir, 500, "HOj234t1", 450183)
        
        