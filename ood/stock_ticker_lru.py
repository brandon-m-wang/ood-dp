# StockTicker class
# addOrUpdate(stock, price) -> none: add or update the price of a stock to the data structure. O(1)
# top(k) -> list(tuples): return the top k most recently modified stocks and their prices. O(k)
# removeStock(stock) -> none: remove the stock from the data structure. O(1)
# Assume k <= number of stocks at any given point. Assume no bad removals.

class DoublyLinkedNode:

    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class DoublyLinkedList:

    def __init__(self):
        self.sentinel = DoublyLinkedNode()
        self.sentinel.prev = self.sentinel.next = self.sentinel
    
    def append(self, node):
        nextNode = self.sentinel.next
        nextNode.prev = node
        node.next = nextNode
        node.prev = self.sentinel
        self.sentinel.next = node

    def remove(self, node):
        nextNode = node.next
        prevNode = node.prev
        nextNode.prev = prevNode
        prevNode.next = nextNode

    def pop(self): # Not used in this specific problem.
        self.remove(self.sentinel.prev)

    def moveToFront(self, node):
        self.remove(node)
        self.append(node)

class StockTicker:

    def __init__(self):
        self.stocks = {}
        self.dll = DoublyLinkedList()

    def addOrUpdate(self, stock, price):
        if stock in self.stocks:
            node = self.stocks[stock]
            node.value = price
            self.dll.moveToFront(node)
        else:
            node = DoublyLinkedNode(stock, price)
            self.dll.append(node)
            self.stocks[stock] = node
    
    def top(self, k):
        pointer = self.dll.sentinel
        topK = []
        for _ in range(k):
            pointer = pointer.next
            topK.append((pointer.key, pointer.value))
        return topK

    def remove(self, stock):
        node = self.stocks[stock]
        self.dll.remove(node)
        del self.stocks[stock]

# Test case

ticker = StockTicker()
ticker.addOrUpdate("AAPL", 50)
ticker.addOrUpdate("GOOGL", 75)
ticker.addOrUpdate("TSLA", 165)
ticker.addOrUpdate("FB", 97)
ticker.addOrUpdate("DOGE", 420)
ticker.addOrUpdate("GME", 1337)

print(ticker.top(5)) # GME, DOGE, FB, TSLA, GOOGL
ticker.addOrUpdate("AAPL", 60)
print(ticker.top(5)) # AAPL, GME, DOGE, FB, TSLA
ticker.remove("TSLA")
print(ticker.top(5)) # AAPL, GME, DOGE, FB, GOOGL
ticker.addOrUpdate("GOOGL", 30)
print(ticker.top(5)) # GOOGL, APPL, GME, DOGE, FB
ticker.addOrUpdate("SONY", 45)
print(ticker.top(5)) # SONY, GOOGL, APPL, GME, DOGE
