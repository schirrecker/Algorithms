import pygame, time, random, pygbutton, copy
from random import randint

# Define some colors
BLACK     = (   10,   31,   102)
WHITE     = ( 20, 185, 100)
LIGHTBLUE = ( 131,248,255)
RED       = (0, 0, 0)

MAXWIDTH = 400
FONTSIZE = 50
FONTSIZESQUARES = 12
BOARDSIZE   = 5

WIDTH  = int(MAXWIDTH/BOARDSIZE)
HEIGHT = WIDTH
MARGIN = max(1, int(WIDTH/20))
TEXTBOXSIZE = 2
TEXTBOX = TEXTBOXSIZE*FONTSIZE + MARGIN
MAXHEIGHT = MAXWIDTH + TEXTBOX

class Player:
    def __init__(self, color):
        self.color = color
        self.sound  = pygame.mixer.Sound("bounce.wav")  
        
    def play(self, x, y, grid):
        col = x // (grid.square_width + grid.margin)
        row = y // (grid.square_height + grid.margin)
        if row < grid.grid_size and col < grid.grid_size: 
            self.sound.play()
            grid.matrix[row][col] = 1
            print ("row: ", row, "  col: ", col)
            # grid.matrix goes from (0,0) upper left to (BOARDSIZE-1, BOARDSIZE-1) lower right
            return True
        else:
            return False  
'''
class Token:
    def __init__(self):
        self.token_img = pygame.image.load("red_token.jpg")
        self.sound  = pygame.mixer.Sound("bounce.wav")  
        
    def display(self, x, y, grid, screen):
        if x < grid.grid_size and y < grid.grid_size: 
            self.sound.play()
            image = pygame.transform.scale(self.token_img, (grid.square_width, grid.square_height))
            screen.blit(image, (x, y))
'''
class Grid:
    def __init__(self, grid_size, square_width, square_height, margin):
        self.grid_size = grid_size
        self.square_width = square_width
        self.square_height = square_height
        token_img = pygame.image.load("white_token.jpg")
        path_img = pygame.image.load("path.jpg")
        self.token = pygame.transform.scale(token_img, (self.square_width, self.square_height))
        self.path = pygame.transform.scale(path_img, (self.square_width, self.square_height))
        self.margin = margin
        self.matrix = []
        self.clear_matrix()

    def clear_matrix(self):
         for row in range(self.grid_size):
            self.matrix.append([])
            for column in range(self.grid_size):
                self.matrix[row].append(0)

    def draw(self, screen):
        for row in range(self.grid_size):
            for col in range(self.grid_size):
                x = (self.margin+self.square_width)*col+self.margin
                y = (self.margin+self.square_height)*row+self.margin
                pygame.draw.rect(screen, WHITE, [x, y, self.square_width, self.square_height])
                pygame.draw.rect(screen, BLACK, [x, y, self.square_width - 1, self.square_height - 1])
                if self.matrix[row][col] == 1:
                    screen.blit(self.token, (x, y))
                elif self.matrix[row][col] == 2:
                    screen.blit(self.path, (x, y))
                    
#----------------------------------------------------------------
#          Initialization
#----------------------------------------------------------------

class Game:
    def __init__(self):
        pygame.init()
        self.size = [BOARDSIZE*(WIDTH+MARGIN)+MARGIN, BOARDSIZE*(HEIGHT+MARGIN)+MARGIN+TEXTBOX]
        self.screen = pygame.display.set_mode(self.size)
        self.font = pygame.font.Font(None, FONTSIZE)
        self.clock = pygame.time.Clock()
        self.player = Player(WHITE) # the walls
        self.quit = False
        self.mouse_pos = [None, None]
        self.textbox = []
        self.init_textbox()
        self.init_buttons()
        self.reset()

    def init_buttons(self):
        self.StartButton = pygbutton.PygButton(pygame.Rect(MARGIN, self.screen.get_height()-MARGIN-30, 50, 20),'Start')
        self.EntranceButton = pygbutton.PygButton(pygame.Rect(MARGIN + 70, self.screen.get_height()-MARGIN-30, 100, 20),'Entrance')
        self.ExitButton = pygbutton.PygButton(pygame.Rect(MARGIN + 190, self.screen.get_height()-MARGIN-30, 50, 20),'Exit')

    def display_buttons(self):
        self.StartButton.draw(self.screen)
        self.EntranceButton.draw(self.screen)
        self.ExitButton.draw(self.screen)

    def reset(self):
        pygame.display.set_caption("Maze Solver")
        self.grid = Grid(grid_size = BOARDSIZE, square_width = WIDTH, square_height = HEIGHT, margin = MARGIN)
        self.gameover = False
        self.refresh_screen()

    def run(self):

        while not self.quit:
            self.refresh_screen()   

            for event in pygame.event.get():
                if 'click' in self.EntranceButton.handleEvent(event):
                    pass
                if 'click' in self.ExitButton.handleEvent(event):
                    pass
                if 'click' in self.StartButton.handleEvent(event):
                    self.solve_maze()
                elif event.type == pygame.QUIT: 
                    self.quit = True 
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    self.mouse_pos = pygame.mouse.get_pos()           
                    self.player.play(self.mouse_pos[0], self.mouse_pos[1], self.grid)

            if self.gameover: 
                self.reset()
        pygame.quit() # Be IDLE friendly. If you forget this line, the program will hang on exit

    def refresh_screen(self):
        self.screen.fill(BLACK)           # Set the screen background
        self.grid.draw(self.screen)       # Draw the grid
        self.display_buttons()
        self.display_textbox()            # Display the status text box at the bottom of the screen
        self.clock.tick(60)               # Limit to 60 frames per second      
        pygame.display.flip()             # Go ahead and update the screen with what we've drawn

    def init_textbox(self):
        self.textbox.clear()
        for i in range(0, TEXTBOXSIZE):
            self.textbox.append("")

    def post_to_textbox(self, *args):
        self.textbox.clear()
        line_count = 0
        for txt in args:
            if line_count < TEXTBOXSIZE:
                self.textbox.append(txt)            
            line_count += 1

    def display_textbox(self):
        line_count = 0
        for txt in self.textbox:
            if line_count < TEXTBOXSIZE:
                text = self.font.render(txt, True, WHITE)
                self.screen.blit(text, [MARGIN, self.screen.get_height() - (TEXTBOXSIZE-line_count)*FONTSIZE])               
            line_count += 1           

    def solve_maze(self):
        start = (0, 0)
        finish = (BOARDSIZE-1, BOARDSIZE-1)

        '''
            create graph
            graph will be {(x, y): [list of adjacent open coordinates]}
            will start with "entrance" coordinates
            then traverse graph and search for "exit" coordinates
            use depth-first search algorithm
            self.grid.matrix[row][col] = 0 if empty and 1 if occupied
        '''

        graph = {}
        for row in range (0, BOARDSIZE):
            for col in range (0, BOARDSIZE):
                if self.grid.matrix[row][col] == 0:
                    graph[(row, col)] = []  # assume this cell has no neighbors 
                    # check cells S, W, E, N of (row, col) cell, add them to cell's neighbors list if empty 
                    if row+1 < BOARDSIZE and self.grid.matrix[row+1][col] == 0:
                        graph[(row, col)].append((row+1, col))
                        
                    if row-1 >= 0 and self.grid.matrix[row-1][col] == 0:
                        graph[(row, col)].append((row-1, col))
                        
                    if col+1 < BOARDSIZE and self.grid.matrix[row][col+1] == 0:
                        graph[(row, col)].append((row, col+1))
                        
                    if col-1 >= 0 and self.grid.matrix[row][col-1] == 0:
                        graph[(row, col)].append((row, col-1))
        print(graph)
    
        path = []
        stack = [start]

        while stack:
            cell = stack.pop()
            if cell in path:
                continue
            path.append(cell)
            for neighbor in graph[cell]:
                if neighbor == finish:  # end search
                    stack = []
                    break
                elif len(graph[neighbor]) == 0:  # dead end
                    break
                else:
                    stack.append(neighbor)
        path.append(finish)
        print (path)

        for x in range(0, BOARDSIZE):
            for y in range(0, BOARDSIZE):
                if (x, y) in path:
                    self.grid.matrix[x][y] = 2

             
#----------------------------------------------------------------
#          Main loop
#----------------------------------------------------------------

def main():
    game = Game()
    game.run()    

if __name__ == '__main__':
    
    main()
