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
        if node not in self.parent:
            return False
        if node == self.parent[node]:
            return node
        self.parent[node] = self.find(self.parent[node])
        return self.parent[node]
    
    def union(self, node1, node2):
        node1 = self.find(node1)
        node2 = self.find(node2)
        if node1 == node2:
            return
        if self.size[node1] >= self.size[node2]:
            self.size[node1] += self.size[node2]
            self.parent[node2] = node1
        else:
            self.size[node2] += self.size[node1]
            self.parent[node1] = node2

class InfiniteHorizontal:
    
    def __init__(self, num_to_win):
        self.red_positions = DisjointSets()
        self.black_positions = DisjointSets()
        self.k = num_to_win
        
    def red_place(self, location):
        self.red_positions.insert(location)
        if self.red_positions.find(location-1):
            self.red_positions.union(location, location-1)
        if self.red_positions.find(location+1):
            self.red_positions.union(location, location+1)
        location_seq = self.red_positions.find(location)
        if self.red_positions.size[location_seq] >= self.k:
            print("RED WINS")
            
    def black_place(self, location):
        self.black_positions.insert(location)
        if self.black_positions.find(location-1):
            self.black_positions.union(location, location-1)
        if self.black_positions.find(location+1):
            self.black_positions.union(location, location+1)
        location_seq = self.black_positions.find(location)
        if self.black_positions.size[location_seq] >= self.k:
            print("BLACK WINS")
        
# Test cases        

# ufds = DisjointSets()
# ufds.insert("Hello")
# ufds.insert("World")

# ufds.union("Hello", "World")
# print(ufds.find("World"))
# ufds.insert("Bruh")
# ufds.union("Bruh", "Hello")
# print(ufds.find("Bruh"))

game = InfiniteHorizontal(8)
game.red_place(1)
game.red_place(2)
game.red_place(3)
game.red_place(5)
game.red_place(4)
game.red_place(7)
game.red_place(8)
game.red_place(9)
game.red_place(11)
game.red_place(10)

game.black_place(1)
game.black_place(2)
game.black_place(3)
game.black_place(7)
game.black_place(8)
game.black_place(9)
game.black_place(5)
game.black_place(6)
game.black_place(4)

# print("RED POSITIONS SIZE DICT")
# for node in game.red_positions.parent.keys():
#     print(game.red_positions.size[node])

# print("BLACK POSITIONS SIZE DICT")
# for node in game.black_positions.parent.keys():
#     print(game.black_positions.size[node])

# O(n) amortized