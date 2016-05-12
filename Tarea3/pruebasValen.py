'''
Created on May 12, 2016

@author: valentina
'''
import unittest
from BilleteraVirtual import *

class PruebasVarias(unittest.TestCase):
    
    #Prueba de Malicia
    def testNombresCorrectos(self):
        b = BilleteraElectronica("125", "áéíóä'ëïöüñ", "ÁÉÍÓÚÄ-ËÏÖÜÑ", "12345678", "123456")
        self.assertEqual(b.nombres, "áéíóä'ëïöüñ", 'Nombre con caracteres especiales Correcto')
    
    def testPinNoNumerico(self):
        b = BilleteraElectronica('123', 'Valen','Hernandez', '21534', 'abc')
        self.assertTrue(isinstance(b.PIN, int))
        
        
        