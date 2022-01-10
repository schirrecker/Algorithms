class Maze:
    def __init__(self):
        self.data_pretty = "\n".join([
                  ".W...",
                  ".W...",
                  ".W.W.",
                  "...W.",
                  "...W."])
        self.data = self.data_pretty.split("\n")
        print (self.data)
        self.path = []
        self.size = len(self.data)

    def display_maze(self, token_pos):
        print ("")
        print (token_pos)
        print  ("_" * self.size)
        for row in range(0, self.size):
            str = ""
            for col in range (0, self.size):
                if row == token_pos[0] and col == token_pos[1]:
                    str += "o"
                else:
                    str += self.data[row][col]
            print (str)
        print  ("_" * self.size)

    def path_finder(self):
        self.path = []          
        visited = []                       
        totry = [(0,0)]
        moves = [(1, 0), (0, 1), (-1, 0), (0, -1)]      
      
        while totry:
            pos = totry.pop()
            if pos[0] == self.size-1 and pos[1] == self.size-1:
                print (self.path)
                return True
            for move in moves:
                x, y = pos[0] + move[0], pos[1] + move[1]
                if x >= 0 and x < self.size and y >= 0 and y < self.size and (x, y) not in visited:
                    if self.data[x][y] == '.':                         
                        totry.append((x, y))
                        self.path.append(pos)
                        self.display_maze(pos)
            visited.append(pos)
        return False     

maze = Maze()
maze.path_finder()


