class DisjointSets:
    
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1]*n # size allows for O(logn) time find
        
    def find(self, node):
        if node == self.parent[node]: # always have at least one parent node that maintains its parent status
            return node
        self.parent[node] = self.find(self.parent[node]) # path compression of O(log*n) find amortized
        return self.parent[node]
    
    def union(self, node1, node2):
        node1 = self.find(node1)
        node2 = self.find(node2)
        if node1 == node2: # check if this connection removes a disconnected graph component (if it doesn't, return False)
            return False
        if self.size[node1] >= self.size[node2]: # otherwise optimize the tree grafting to union two sets, and return True
            self.size[node1] += self.size[node2]
            self.parent[node2] = node1
        else:
            self.size[node2] += self.size[node1]
            self.parent[node1] = node2
        return True

    def largest_group_size(self):
        largest = 0
        for i, x in enumerate(self.parent):
            if i != x:
                continue
            largest = max(largest, self.size[x])
        return largest
