class SnakeGame:

    def __init__(self, width: int, height: int, food: List[List[int]]):
        """
        Initialize your data structure here.
        @param width - screen width
        @param height - screen height 
        @param food - A list of food positions
        E.g food = [[1,1], [1,0]] means the first food is positioned at [1,1], the second is at [1,0].
        """
        self.W = width
        self.H = height
        self.food = food
        self.next_food = 0
        self.dirs = {'U': [-1,0],
                     'L': [0,-1],
                     'R': [0,1],
                     'D': [1,0]}
        self.snake = deque()
        self.snake.append((0,0))
        self.body = set()
        self.body.add((0,0))
        self.score = 0
        print(self.body)
    def move(self, direction: str) -> int:
        """
        Moves the snake.
        @param direction - 'U' = Up, 'L' = Left, 'R' = Right, 'D' = Down 
        @return The game's score after the move. Return -1 if game over. 
        Game over when snake crosses the screen boundary or bites its body.
        """
        #3 states for a move - hit an invalid spot, or hit an empty space, or hit food
        next_dir = self.dirs[direction]
        head = self.snake[-1]
        next_pos = (next_dir[0] + head[0], next_dir[1] + head[1])
        if not self.valid_pos(next_pos):
            # print('wattt')
            return -1
        food_pos = self.food[self.next_food] if self.next_food < len(self.food) else []
        if next_pos != tuple(food_pos):
            popped_body = self.snake.popleft()
            self.body.remove(popped_body)
        elif food_pos:
            self.score += 1
            self.next_food += 1
        self.snake.append(next_pos)
        self.body.add(next_pos)
        return self.score
        
    def valid_pos(self, next_pos):
        if -1 < next_pos[0] < self.H and -1 < next_pos[1] < self.W \
            and (next_pos not in self.body or next_pos == self.snake[0]):\
                return True
        return False
        
        
        


# Your SnakeGame object will be instantiated and called as such:
# obj = SnakeGame(width, height, food)
# param_1 = obj.move(direction)