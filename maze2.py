def path_finder(maze):
    a = maze.split("\n")
    size = len(a)
    pos = (0, 0)                                    # initial position
    path = [pos]                                    # stack
    tried = [pos]                                   # tried cells
    moves = [(1, 0), (0, 1), (-1, 0), (0, -1)]      
  
    def try_move(pos):
        if pos[0] == size-1 and pos[1] == size-1:
            # print (path)
            return True
        tried.append(pos)
        for move in moves:
            if pos[0] + move[0] >= 0 and pos[0] + move[0] < size and pos[1] + move[1] >= 0 and pos[1] + move[1] < size:          
                x, y = pos[0] + move[0], pos[1] + move[1]
                if (x, y) not in tried:                 # have not tried that cell yet
                    if a[x][y] == '.':                  # open
                        new_pos = (x, y)
                        path.append(new_pos)
                        return try_move(new_pos)
        # none of the moves worked
        path.pop()           # remove last cell tried
        if len(path) == 0:
            return False
        else:
            return try_move(path[-1])    # retry last cell for another move

    return (try_move(pos))


# main
a = "\n".join([
          ".W...",
          ".W...",
          ".W.W.",
          "...W.",
          "...W."])

print(path_finder(a))


