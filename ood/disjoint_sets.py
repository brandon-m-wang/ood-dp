class DisjointSets:
    
    def __init__(self):
        self.parent = {}
        self.size = {}
        
    def insert(self, node):
        if node in self.parent:
            return
        self.parent[node] = node
        self.size[node] = 1
    
    def find(self, node):
        if self.parent[node] == node:
            return node
        self.parent[node] = self.find(self.parent[node])
        return self.parent[node]
    
    def union(self, node1, node2):
        node1 = self.find(node1)
        node2 = self.find(node2)
        if node1 == node2:
            return
        if self.size[node1] >= self.size[node2]:
            self.parent[node2] = node1
            self.size[node1] += self.size[node2]
        else:
            self.parent[node1] = node2
            self.size[node2] += self.size[node1]
            
# Test cases

ufds = DisjointSets()
ufds.insert("Hello")
ufds.insert("World")

ufds.union("Hello", "World")
print(ufds.find("World"))
ufds.insert("Bruh")
ufds.union("Bruh", "Hello")
print(ufds.find("Bruh"))

for node in ufds.parent.keys():
    print(ufds.size[node])

for node in ufds.parent.keys():
    print(ufds.size[node])