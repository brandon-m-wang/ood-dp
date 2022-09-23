import collections
from typing import List

class SnakeGame:

    def __init__(self, width: int, height: int, food: List[List[int]]):
        self.snake = collections.deque([[0, 0]])
        self.snake_hashed = set([(0, 0)])
        self.width = width
        self.height = height
        self.food = list(reversed(food))
        self.score = 0
        
    def _outbounds(self, y: int, x:int) -> bool:
        return x >= self.width or x < 0 or y >= self.height or y < 0
    
    def _collision(self, y: int, x: int) -> bool:
        return (y, x) in self.snake_hashed
    
    def _onfood(self, y: int, x: int) -> bool:
        return self.food and [y, x] == self.food[-1]
        
    def move(self, direction: str) -> int:
        moves = {"U": [-1, 0], "R": [0, 1], "D": [1, 0], "L": [0, -1]}
        curr_y, curr_x = self.snake[0]
        delta_y, delta_x = moves[direction]
        # moved into wall
        if self._outbounds(curr_y + delta_y, curr_x + delta_x):
            return -1
        if not self._onfood(curr_y + delta_y, curr_x + delta_x):
            popped_y, popped_x = self.snake.pop()
            self.snake_hashed.remove((popped_y, popped_x))
        else:
            self.food.pop()
            self.score += 1
        # moved into self
        if self._collision(curr_y + delta_y, curr_x + delta_x):
            return -1
        self.snake.appendleft([curr_y + delta_y, curr_x + delta_x])
        self.snake_hashed.add((curr_y + delta_y, curr_x + delta_x))
        return self.score

# Your SnakeGame object will be instantiated and called as such:
# obj = SnakeGame(width, height, food)
# param_1 = obj.move(direction)