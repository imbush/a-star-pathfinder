import numpy as np
import random
from settings import *

'''File containing the functions for the recursive_backtracker maze generation algorithm.
Recursive backtracking is a depth first random tree generation algorithm with
'''

class Node:
    def __init__(self, position, parent = None, dist = 0):
        '''dist is distance from start'''
        self.parent = parent
        self.position = position
        self.dist = dist

def rec_backtracker(height: int, width: int, start_coord: tuple):
    '''Returns an array and an end-point as a tuple.
    Height and width should be odd
    '''
    #initializes board, start node and current
    board = np.ones((height,width))
    board[start_coord] = 0
    start = Node(start_coord)
    current = start
    end = start
    first_node = True

    while current != start or first_node:

        #Creates a list of viable neighbor steps to jump to
        neighbors = [(current.position[0]-2,current.position[1]),(current.position[0]+2,current.position[1]),(current.position[0],current.position[1]-2),(current.position[0],current.position[1]+2)]
        viable_neighbors = []
        
        for neighbor in neighbors:
            if neighbor[0] < 0 or neighbor[1] < 0 or neighbor[0] > (height-1) or neighbor[1] > (width-1):
                continue
            elif board[neighbor] == 0:
                continue
            else:
                viable_neighbors.append(neighbor)

        #Backtracks if no viable neighbors, sets current to end if it has the largest distance
        if not viable_neighbors:
            if current.dist > end.dist:
                end = current
            current = current.parent
            continue
        
        # Picks next node, sets new node and node between as 0 on board
        new_coord = random.choice(viable_neighbors)
        board[new_coord] = 0
        board[int((new_coord[0]+current.position[0])/2)][int((new_coord[1]+current.position[1])/2)] = 0
        current = Node(new_coord, current, current.dist + 1)
        first_node = False

    board = board.tolist()
    return board, end.position

if __name__ == "__main__":
    height = 51
    width = 51
    start = (0,0)
    
    board, end = rec_backtracker(height, width, start)

    pygame.init()
    
    settings = Settings(width, height) #initializes settings

    screen = pygame.display.set_mode((settings.window_width, settings.window_height))
    pygame.display.set_caption("Maze")

    settings.draw_board(board, screen)
    pygame.display.flip()
    running = True
    while running:
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                running = False