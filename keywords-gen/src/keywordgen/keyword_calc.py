'''
Created on 06/08/2011

@author: carlos
'''
def element_cmp (a, b):
    return a(0) < b(0)

def apply_separators (text, separators, return_list):
    if separators == None or separators == []:
        return_list.append( text )
    else:
        separators_cp = separators
        for separator in separators:
            splitted_text = text.split ( separator )
            separators_cp.remove ( separator )
            for splitted_word in splitted_text:
                apply_separators (splitted_word, separators_cp, return_list )
            

def get_keywords (text, num, separators):
    list_of_words = []
    keywords = []
    
    for splitted_text in text.split():
        apply_separators(splitted_text, separators, list_of_words)
    
    print(list_of_words)
    
    words_count = []
    for word in list_of_words:
        words_count.append( (list_of_words.count( word ), word) )
    words_count.sort( key=lambda word_count : word_count[0], reverse = True )
    
    for word in words_count:
        if keywords.count(word[1]):
            keywords.append( word[1] )
    
    return keywords

#if __name__ == '__main__':
#    print (get_keywords ("El perro de San Roque no tiene rabo, perro perro perro, San", 10, [","," ", "de"]))
    