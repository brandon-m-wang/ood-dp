class TrieNode:
    
    def __init__(self, key, value=None):
        self.key = key
        self.value = value
        self.children = {}
        self.is_end = False
        
class Trie:
    
    def __init__(self):
        self.root = TrieNode("*", "*")
        
    def insert(self, key, value):
        curr = self.root
        for char in key:
            if char not in curr.children:
                curr.children[char] = TrieNode(key)
            curr = curr.children[char]
        curr.value = value
        curr.is_end = True
        
    def search(self, key):
        curr = self.root
        for char in key:
            if char not in curr.children:
                return False
            curr = curr.children[char]
        if curr.is_end:
            return curr.value
        return False

class PiecewiseStore:
    
    def __init__(self):
        self.db = Trie()
        self.inflight = set()
    
    def store(self, key, value):
        self.db.insert(key, value)  
    
    def key_in(self, key):
        db_hits = []
        self.inflight.add(self.db.root)
        for node in list(self.inflight):
            self.inflight.remove(node)
            if key in node.children:
                self.inflight.add(node.children[key])
        for node in list(self.inflight):
            if node.is_end:
                db_hits.append(node.value)
        print(db_hits)
        
# Test cases

ps = PiecewiseStore()

ps.store("He", 0)
ps.store("Hel", 1)
ps.store("Hello", 2)
ps.store("llo", 3)
ps.store("o", 4)

ps.key_in("H")
ps.key_in("e")
ps.key_in("l")
ps.key_in("l")
ps.key_in("o")
