'''
Created on May 12, 2016

@author: valentina
'''
import unittest
from BilleteraVirtual import *

class PruebasVarias(unittest.TestCase):
    
    #Prueba de Malicia
    def testNombresCorrectos(self):
        b = BilleteraElectronica("125", "áéíóä'ëïöüñ", "ÁÉÍÓÚÄ-ËÏÖÜÑ", 54, 12345)
        self.assertEqual(b.nombres, "áéíóä'ëïöüñ", 'Nombre con caracteres especiales Correcto')
    
    #Prueba de Malicia
    def testPinNoNumerico(self):
        b = BilleteraElectronica('123', 'Valen','Hernandez', 24534, 123)
        self.assertTrue(isinstance(b.PIN, int))
        
    #PruebaMalicia  
    def testCedulaNumerica(self):
        b = BilleteraElectronica('123', 'Valen','Hernandez', 123, 123)
        self.assertTrue(isinstance(b.CI, int))     
        
    #Prueba Malicia
    def testCedulaNegativa(self):
        b = BilleteraElectronica('123', 'Valen','Hernandez', 24534, 123)
        self.assertRaises(Exception, b.CI)
           
    def testCedulaCero(self):
         b = BilleteraElectronica('123', 'Valen','Hernandez', 1, 123)
         self.assertRaises(Exception, b.CI)