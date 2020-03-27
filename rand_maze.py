from settings import Settings
import time, pygame, sys, random
import numpy as np

'''Maze generation algorithm which creates random paths. 
Wildly inefficient, but a fun homebrew maze generation algorithm (also creates interesting cave system like paths)
'''

def path_generator(height, width, start:tuple, end:tuple):
    '''Outputs a list of tuples representing a path from start to end within the height and width'''

    adjacent_cells = [(-1,0),(0,-1),(0,1),(1,0)]
    path_not_found = True
    path = 0

    while path_not_found:
        main_path = np.zeros((height, width))
        current_cell = start
        path_list = [start]
        path += 1
        while True:
            #creates list of viable adjacent cells
            viable_adjacent = []
            for neighbor in adjacent_cells:
                neighbor = tuple(map(lambda i, j: i + j, current_cell, neighbor))
                if neighbor[0] < 0 or neighbor[1] < 0 or neighbor[0] > (height-1) or neighbor[1] > (width - 1):
                    continue
                elif main_path[neighbor] != 0:
                    continue
                viable_adjacent.append(neighbor)

            #Breaks if no viable adjacent cells found
            if not viable_adjacent:
                break

            #randomly selects the next step in the main path and ends if the cell is 
            current_cell = random.choice(viable_adjacent)
            main_path[current_cell] = 3
            path_list.append(current_cell)

            for neighbor in viable_adjacent:
                if neighbor != current_cell:
                    main_path[neighbor] = 1

            if current_cell == end:
                path_not_found = False
                break
    return(path_list)


def random_start_end(height: int, width: int):
    '''outputs 2 random points '''
    start = (random.randint(0,height-1),random.randint(0,width -1))
    end = (random.randint(0,height-1),random.randint(0,width -1))
    return start, end

def board_from_tuples(height: int, width: int, tuple_list: list):
    '''returns a board of shape height by width filled with ones except for the members within the tuple list'''
    board = np.ones((height,width))
    
    for coord in tuple_list:
        board[coord] = 0

    return board.tolist()

def maze_generator(n_randpaths: int, height: int,width: int,start: tuple, end: tuple):
    '''returns a maze with height by width shape and start and end nodes. 
    n_randpaths = number of paths created within maze
    '''
    empty_squares = []

    empty_squares.extend(path_generator(height,width, start, end))

    for _ in range(n_randpaths): # creates n_randpaths random paths within the board
        pos_initial, pos_final = random_start_end(height, width)
        empty_squares.extend(path_generator(height,width, pos_initial, pos_final))

    #makes board and marks endpoint
    board = board_from_tuples(height, width, empty_squares)

    return(board)

if __name__ == "__main__":
    height = 50
    width = 50
    start = (0,0)
    end = (height-1, width -1)
    
    board = maze_generator(5, height, width, start, end)

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