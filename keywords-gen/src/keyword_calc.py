'''
Created on 06/08/2011

@author: carlos
'''
def element_cmp (a, b):
    return a(0) < b(0)

def get_keywords (text, num, separators):
    list_of_words = []
    keywords = []
    for separator in separators:
        list_of_words.extend( text.rsplit( separator ) )
    words_count = []
    for word in list_of_words:
        words_count.append( (list_of_words.count( word ), word) )
    words_count.sort( element_cmp )
    
    for word in words_count:
        keywords.append( word(0) )
         
    
    return keywords

if __name__ == '__main__':
    print (get_keywords ("El perro de San Roque no tiene rabo, perro perro perro, San", 10, [","," ", "de"]))
    