'''
Created on 06/08/2011

@author: carlos
'''
import re

def element_cmp (a, b):
    return a(0) < b(0)


def get_keywords (text, exclusion_list):
    
    keywords = []
        
    list_of_words = re.split('\W+', text )
    
    for exclusion_word in exclusion_list:
        try:
            list_of_words.remove (exclusion_word)
        except ValueError:
            pass
        
    words_count = []
    for word in list_of_words:
        words_count.append( (list_of_words.count( word ), word) )
        salir = False
        while (not salir):
            try:
                list_of_words.remove( word )
            except ValueError:
                salir = True
        print(list_of_words)
        
    words_count.sort( key=lambda word_count : word_count[0], reverse = True )
    
    for word in words_count:
        keywords.append( word[1] )
    
    return keywords
