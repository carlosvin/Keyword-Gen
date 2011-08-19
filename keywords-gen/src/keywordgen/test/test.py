'''
Created on 16/08/2011

@author: carlos
'''
import unittest
from keywordgen.keyword_calc import get_keywords

class Test(unittest.TestCase):
    
    def testKeyWordGen(self):
        keywords_expected = ["perro", "San", "Roque", "tiene", "rabo"]
        keywords_observed = get_keywords (
                                          "El perro de San Roque no tiene rabo, perro;San Roque tiene perro. perro perro, San San",
                                          [",", "de", "no", "a", "El"])
        print(keywords_observed)
        self.assertEqual( keywords_expected, keywords_observed ) 
         

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testKeyWordGen']
    unittest.main()