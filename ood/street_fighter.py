import collections

class TrieNode:
    
    def __init__(self, key, end_value=None):
        self.letter = key
        self.action = end_value 
        self.children = {}
        self.is_end = False

class Trie:
    
    def __init__(self):
        self.root = TrieNode("*", "*")

    def insert(self, word, action):
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode(char)
            curr = curr.children[char]
        curr.is_end = True
        curr.action = action

class StreetFighter:
    
    def __init__(self):
        self.combos = Trie()
        self.inflight = collections.deque()
        
    def register(self, sequence, action):
        self.combos.insert(sequence, action)
        
    def emit(self, input):
        executed = []
        # add new inflight node
        self.inflight.append(self.combos.root)
        # update all nodes
        for node in list(self.inflight):
            self.inflight.pop()
            if input in node.children:
                self.inflight.appendleft(node.children[input])
        # check if any completed
        for node in list(self.inflight):
            if node.is_end:
                executed.append(node.action)
        print(executed)
        return executed

# Test cases

client = StreetFighter()

client.register("UDLR", "Fireball")
client.register("UD", "Punch")
client.register("U", "Jump")
client.register("LR", "Kick")
client.register("UDLRUDLR", "Sit")

client.emit("U")
client.emit("D")
client.emit("L")
client.emit("R")

client.emit("U")
client.emit("D")
client.emit("L")
client.emit("R")

client.emit("U")
client.emit("D")
client.emit("L")
client.emit("L")
client.emit("R")

# O(n*m) where n is the number of inputs and m is the longest registered input
# The inflight list can only be as long as the longest registered input, otherwise 
# they would have expired and left the list already