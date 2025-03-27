"""
Q2 [C, Python] A phoneme is a sound unit (similar to a character for text). We have an extensive pronunciation
dictionary (think millions of words). Given a sequence of phonemes as input find all the combinations of the words that
can produce this sequence. You can
preprocess the dictionary into a different data structure if needed.

"""

from typing import Sequence, List, Dict,Tuple
from collections import defaultdict

def preprocess_dictionary(dictionary: Dict):
    """
    Preprocess the pronunciation dictionary
    """
    ph_words = defaultdict(list)
    
    for word in dictionary:
        # Split into word and seq of phonemes
        parts = dictionary[word].split()
        
        # create the map
        ph_words[tuple(parts)].append(word)
    
    return ph_words

def find_word_combos_with_pronunciation(phonemes: Sequence[str], 
                                         dictionary: Dict) -> Sequence[Sequence[str]]:
    """
    Find all combinations of words
    """
    # Preprocess
    ph_words = preprocess_dictionary(dictionary)
    
    # dp[i] all word combinations that can form the phoneme sequence up to index i
    dp = [[] for _ in range(len(phonemes) + 1)]
    dp[0] = [[]] 
    
    for i in range(1, len(phonemes) + 1):
        for j in range(i):
            # check subsequence from j to i can form a word
            c_phonemes = tuple(phonemes[j:i])
            
            if c_phonemes in ph_words:
                
                for word in ph_words[c_phonemes]:
                    # Extend previous combinations
                    for prev_combo in dp[j]:
                        new_comb = prev_combo + [word]
                        dp[i].append(new_comb)
    
    return dp[len(phonemes)]


dictionary = {
        "ABACUS": "AE B AH K AH S",
        "BOOK": "B UH K",
        "THEIR": "DH EH R",
        "THERE": "DH EH R",
        "TOMATO": "T AH M AA T OW",
        "TOMATO": "T AH M EY T OW"
    }
    

result = find_word_combos_with_pronunciation( ["DH", "EH", "R", "DH", "EH", "R"], dictionary)
print(" combinations:")
for combo in result:
        print(combo)