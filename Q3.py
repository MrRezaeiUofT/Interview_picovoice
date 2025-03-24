"""
 Q3, Find the n most frequent words in the TensorFlow Shakespeare dataset.
"""
from collections import Counter
from typing import List

def find_frequent_words(path: str, n: int) -> List[str]:
    with open(path, 'r', encoding='utf-8') as f:
        text = f.read()
    
    # spliting
    words = text.lower().split()
    
    # Counter for word frequencies
    word_counts = Counter(words)
    
    most_common = word_counts.most_common(n)
    return [word for word, _ in most_common]
path = "shakespeare.txt"
top_words = find_frequent_words(path, 10)
print("Top 10 frequent words:", top_words)