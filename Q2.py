"""
Q2 [C, Python] A phoneme is a sound unit (similar to a character for text). We have an extensive pronunciation
dictionary (think millions of words). Below is a snippet:

"""

from typing import List, Sequence, Dict, Tuple

# The keys are tuples representing the sequence of phonemes.
P_dic: Dict[Tuple[str, ...], List[str]] = {
    ("AE", "B", "AH", "K", "AH", "S"): ["ABACUS"],
    ("B", "UH", "K"): ["BOOK"],
    ("DH", "EH", "R"): ["THEIR", "THERE"],
    ("T", "AH", "M", "AA", "T", "OW"): ["TOMATO"],
    ("T", "AH", "M", "EY", "T", "OW"): ["TOMATO"],
}

def find_word_combos_with_pronunciation(phonemes: Sequence[str]) -> Sequence[Sequence[str]]:
    n=len(phonemes)
    memo: Dict[int, List[List[str]]] ={}
    
    def dfs(i):
        # return an empty combinatio at the end.
        if i==n:
            return [[]]
        if i in memo:
            return memo[i]
        
        combs=[]
        # Try every possibilities at i
        for j in range(i + 1, n + 1):
            seg = tuple(phonemes[i:j])
            if seg in P_dic:
                words = P_dic[seg]
                # recursively solve for the remaining phonemes.
                for w in words:
                    for tail in dfs(j):
                        combs.append([w] + tail)
        memo[i]=combs
        return combs

    return dfs(0)


    
input_phonemes = ["DH", "EH", "R", "DH", "EH", "R"]
results = find_word_combos_with_pronunciation(input_phonemes)
print(results)

