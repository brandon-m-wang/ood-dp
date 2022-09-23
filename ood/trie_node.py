class TrieNode:
    
    def __init__(self, letter):
        self.letter = letter
        self.children = {}
        self.is_end = False
        
class Trie:
    
    def __init__(self):
        self.root = TrieNode("*")
    
    def insert(self, word):
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode(char)
            curr = curr.children[char]
        curr.is_end = True
    
    def search(self, word):
        curr = self.root
        for char in word:
            if char not in curr.children:
                return False
            curr = curr.children[char]
        return curr.is_end

# Test cases

words = Trie()

words.insert("Hello")
words.insert("Hel")

print(words.search("Hello"))
print(words.search("Hell"))
print(words.search(""))

words.insert("")

print(words.search(""))
