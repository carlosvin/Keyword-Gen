'''
Created on 06/08/2011

@author: carlos
'''
import re

def get_keywords (text, exclusion_list):
    
    keywords = []
        
    list_of_words = filter(lambda w: not w in exclusion_list, re.split('\W+', text ))

    counts = {}
    for word in list_of_words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 0
    return list(map(lambda pair: pair[0], sorted(counts.items(), key=lambda kv: kv[1], reverse=True)))

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description='Extract a list of relevant keywords from an input string')
    parser.add_argument('sentence', type=str)
    parser.add_argument('--exclusion_list', default=[], nargs='*')
    args = parser.parse_args()
    for key_word in get_keywords(args.sentence, args.exclusion_list): 
        print(key_word)
