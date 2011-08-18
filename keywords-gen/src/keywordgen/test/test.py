'''
Created on 16/08/2011

@author: carlos
'''
import unittest
from keywordgen.keyword_calc import get_keywords
import string

class Test(unittest.TestCase):
    
    def testKeyWordGen(self):
        keywords = get_keywords ("El perro de San Roque no tiene rabo, perro perro perro, San", [",", "de", "no", "a", "El"])
        print (keywords)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testKeyWordGen']
    unittest.main()