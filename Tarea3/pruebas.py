'''
Created on May 12, 2016

@author: valentina
'''

import unittest
from BilleteraVirtual import *

class TestBilletera(unittest.TestCase):
    
    def testAtributoIDcreado(self):
        billetera = BilleteraElectronica('456')
        
        
        