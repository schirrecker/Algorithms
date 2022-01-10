from guizero import App, Text
from time import sleep

DELAY = 0.5

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
        self.app = App(layout="grid")
        self.grid = []
        print(self.grid)
        self.display_maze((0,3))

    def display_maze(self, token_pos):
        for row in range(0, self.size):
            for col in range (0, self.size):
                if self.data[col][row] == "W":
                    # self.empty_cell = Picture(self.app, image="blocked_cell.gif", grid=[row,col])
                    self.grid.append(Text(self.app, text="W", grid=[row,col]))
                if self.data[col][row] == ".":
                    # self.empty_cell = Picture(self.app, image="blocked_cell.gif", grid=[row,col])
                    self.grid.append(Text(self.app, text=".", grid=[row,col]))
                if row == token_pos[0] and col == token_pos[1]:
                    # self.empty_cell = Picture(self.app, image="token.gif", grid=[row,col])
                    self.grid.append(Text(self.app, text="o", grid=[row,col]))


    def path_finder(self):
        pos = (0, 0)                                    # initial position
        self.path = [pos]                               # stack
        tried = [pos]                                   # tried cells
        moves = [(1, 0), (0, 1), (-1, 0), (0, -1)]      
      
        while (pos[0] != self.size-1 or pos[1] != self.size-1):
            tried.append(pos)
            moved = False
            for move in moves:
                if pos[0] + move[0] >= 0 and pos[0] + move[0] < self.size and pos[1] + move[1] >= 0 and pos[1] + move[1] < self.size:          
                    x, y = pos[0] + move[0], pos[1] + move[1]
                    if (x, y) not in tried:                 # have not tried that cell yet
                        if self.data[x][y] == '.':                  # it's open
                            new_pos = (x, y)                # new pos into that new position
                            self.path.append(new_pos)       # add it to path
                            print (new_pos)
                            Text(self.app, text="o", grid=[y, x])
                            sleep(DELAY)
                            pos = new_pos                   # move to new_pos and continue the loop
                            moved = True                    # one position worked
            if not moved:                                   # none of the moves worked
                self.path.pop()                             # remove last cell tried
                if len(self.path) == 0: return False        # if we are back to the initial position, the False    
                                                            # if not, we continue on the while loop
        return True     

maze = Maze()
maze.path_finder()
maze.app.display()

