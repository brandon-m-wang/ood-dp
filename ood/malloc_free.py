import sortedcontainers

class Heap:
    
    def __init__(self, heap_size):
        self.memory = [0]*heap_size
        self.free_memory_by_size = sortedcontainers.SortedSet([(0, heap_size)], key = lambda x: x[1] - x[0])
        self.free_memory_by_index = sortedcontainers.SortedSet([(0, heap_size)], key = lambda x: x[0])
        self.allocated_memory = {}
        self.heap_size = heap_size
        
    def _binary_search_by_size(self, size):
        # O(log^2(n)), logn indexing for each. In the case of a fully implemented BST, O(logn)
        left = 0
        right = len(self.free_memory_by_size)
        mid = None
        while left < right:
            mid = (left + right)//2
            start, end = self.free_memory_by_size[mid]
            curr_size = end - start
            if curr_size < size:
                left = mid + 1
            elif curr_size > size:
                right = mid - 1
            else:
                return mid
        if mid == None:
            return mid
        start, end = self.free_memory_by_size[mid]
        return mid if end - start > size else None
    
    def _binary_search_by_index(self, index):
        # O(log^2(n)), logn indexing for each. In the case of a fully implemented BST, O(logn)
        left = 0
        right = len(self.free_memory_by_index)
        mid = None
        while left < right:
            mid = (left + right)//2
            start, end = self.free_memory_by_index[mid]
            curr_index = start
            if curr_index < index:
                left = mid
            elif curr_index > index:
                right = mid
            else:
                return mid
        if mid == None:
            return mid
        return mid
    
    def _coalesce(self, index):
        # O(n)
        # Coalesce right
        idx = index
        curr_chunk = self.free_memory_by_index[idx]
        coalesced_chunk = list(curr_chunk)
        next_chunk = None
        to_delete = set()
        while idx < len(self.free_memory_by_index) - 1:
            curr_chunk = self.free_memory_by_index[idx]
            cs, ce = curr_chunk
            next_chunk = self.free_memory_by_index[idx + 1]
            ns, ne = next_chunk
            if ce + 1 == ns:
                to_delete.add(curr_chunk)
                to_delete.add(next_chunk)
                coalesced_chunk[1] = next_chunk[1]
            idx += 1
            
        # Coalesce left
        idx = index
        prev_chunk = None
        while idx > 0:
            curr_chunk = self.free_memory_by_index[idx]
            cs, ce = curr_chunk
            prev_chunk = self.free_memory_by_index[idx - 1]
            ps, pe = prev_chunk
            if cs - 1 == pe:
                to_delete.add(curr_chunk)
                to_delete.add(prev_chunk)
                coalesced_chunk[0] = prev_chunk[0]
            idx -= 1
            
        for chunk in to_delete:
            self.free_memory_by_index.remove(chunk)
            self.free_memory_by_size.remove(chunk)

        self.free_memory_by_size.add(tuple(coalesced_chunk))
        self.free_memory_by_index.add(tuple(coalesced_chunk))
                
    def malloc(self, size):
        free_chunk_index = self._binary_search_by_size(size)
        free_chunk = self.free_memory_by_size[free_chunk_index]
        self.free_memory_by_size.remove(free_chunk) # O(logn) if C++ ordered_set
        self.free_memory_by_index.remove(free_chunk)
        
        start, end = free_chunk
        allocated_chunk = (start, start + size - 1)
        self.allocated_memory[start] = allocated_chunk
        
        remnant_chunk = (start + size, end)
        self.free_memory_by_size.add(remnant_chunk) # O(logn) if C++ ordered_set
        self.free_memory_by_index.add(remnant_chunk)
        return start
        
    def free(self, index):
        allocated_chunk = self.allocated_memory[index]
        self.free_memory_by_size.add(allocated_chunk) # O(logn)
        self.free_memory_by_index.add(allocated_chunk)
        
        del self.allocated_memory[index]
        
        start, end = allocated_chunk
        allocated_chunk_index = self._binary_search_by_index(start) # O(logn)
        self._coalesce(allocated_chunk_index)
    
# Test cases
    # For n calls:
        # O(logn) malloc
        # O(logn) free
        # O(n) free with coalesce

heap = Heap(100)

print("\nTesting basic malloc/free...", "\n")

heap.malloc(10)
print("Expecting: ", "[(10, 100)]", heap.free_memory_by_index)
heap.free(0)
print("Expecting: ", "[(0, 100)]", heap.free_memory_by_index)

print("\nTesting advanced malloc/free with coalesce...", "\n")

ptr1 = heap.malloc(20)
print("Expecting: ", "[(20, 100)]", heap.free_memory_by_index)
ptr2 = heap.malloc(5)
print("Expecting: ", "[(25, 100)]", heap.free_memory_by_index)
ptr3 = heap.malloc(10)
print("Expecting: ", "[(35, 100)]", heap.free_memory_by_index)

heap.free(ptr2)
print("Expecting: ", "[(20, 24), (35, 100)]", heap.free_memory_by_index)

heap.free(ptr3)
print("Expecting: ", "[(20, 100)]", heap.free_memory_by_index)

heap.free(ptr1)
print("Expecting: ", "[(0, 100)]", heap.free_memory_by_index)

print("\nTesting multiple malloc/free/coalesce...", "\n")

ptr1 = heap.malloc(10)
ptr2 = heap.malloc(10)
ptr3 = heap.malloc(10)
ptr4 = heap.malloc(10)
ptr5 = heap.malloc(10)
print("Expecting: ", "[(50, 100)]", heap.free_memory_by_index)

heap.free(ptr2)
heap.free(ptr4)
print("Expecting: ", "[(10, 19), (30, 39), (50, 100)]", heap.free_memory_by_index)

heap.free(ptr3)
print("Expecting: ", "[(10, 39), (50, 100)]", heap.free_memory_by_index)

heap.free(ptr1)
print("Expecting: ", "[(0, 39), (50, 100)]", heap.free_memory_by_index)

heap.free(ptr5)
print("Expecting: ", "[(0, 100)]", heap.free_memory_by_index)
