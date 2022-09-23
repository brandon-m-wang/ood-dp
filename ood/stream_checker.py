import collections

class TrieNode:
    
    def __init__(self, letter):
        self.letter = letter
        self.children = {}
        self.is_end = False

class StreamChecker:
    
    def __init__(self, words):
        self.root = TrieNode("*")
        for word in words:
            curr = self.root
            for i in range(len(word)):
                if word[i] not in curr.children:
                    curr.children[word[i]] = TrieNode(word[i])
                curr = curr.children[word[i]]
            curr.is_end = True
        self.inflight = collections.deque()
    
    def query(self, letter):
        curr = self.root
        self.inflight.append(curr)
        for node in list(self.inflight):
            # update inflights
            self.inflight.pop()
            if letter in node.children:
                self.inflight.appendleft(node.children[letter])
        # check if criteria is met
        for node in self.inflight:
            if node.is_end:
                return True
        return False
