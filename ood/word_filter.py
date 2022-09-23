from typing import List

class TrieNode:
    
    def __init__(self, letter, index=None):
        self.letter = letter
        self.largest_index = index
        self.children = {}
        
class WordFilter:

    def __init__(self, words: List[str]):
        self.root = TrieNode("*")
        for index, word in enumerate(words):
            word = word + "#"
            for i in range(len(word)):
                curr = self.root
                curr.largest_index = index
                for j in range(i, 2 * len(word) - 1):
                    curr_letter = word[j % len(word)]
                    if curr_letter not in curr.children:
                        curr.children[curr_letter] = TrieNode(curr_letter)
                    curr = curr.children[curr_letter]
                    curr.largest_index = index
                
    def f(self, pref: str, suff: str) -> int:
        curr = self.root
        search_word = suff + "#" + pref
        for char in search_word:
            if char not in curr.children:
                return -1
            curr = curr.children[char]
        return curr.largest_index


# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(pref,suff)