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
        b4.recargar(21000, "981yHJ32")
        
    def testDebitoyMetodoConsumir(self):
        b5 = BilleteraElectronica("42Sbb90j" , "Luis", "Pacheco", 8374562, 450183)
        b5.recargar(21000, "981yHJ32")
        b5.consumir(2, "HOj234t1", 450183)
        
    def testRecargaCorrecta(self):
        b4 = BilleteraElectronica("01", "Pedro", "Perez", "5617234", 156)
        b4.recargar(3, "11")
        self.assertEquals(3,b4.balance)
        self.assertEquals(1,len(b4.creditos))
        
    def testConsumoCorrecto(self):
        b5 = BilleteraElectronica("123" , "Luis", "Pacheco", 8374562, 450183)
        b5.recargar(250, "02")
        b5.consumir(100, "60", 450183)
        self.assertEquals(150, b5.balance)
        b5.recargar(50, "04")
        b5.consumir(25, "40", 450183)
        self.assertEquals(175, b5.balance)


if __name__ == '__main__':
    unittest.main()
    
    
    
     
    
        
    
        
        
        
        
        
        