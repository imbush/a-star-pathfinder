from settings import Settings
from a_star import *
from rand_maze import *
from recursive_backtracker import rec_backtracker
import time, pygame, random, math
import numpy as np
'''This is a basic implementation of the A* shortest path finding algorithm.
    For all versions, within the arrays:
    0 represents a passable node
    1 represents an obstacle node
    2 represents the start and end nodes
    3 represents a path node
    '''

def terminal_version():
    running = True
    while running:
        #user inputs the board dimensions and board is created
        field_hei = int(input("\nPlease input the height of your field: ").strip())
        field_wid = int(input("Please input the width of your field: ").strip())
        board = np.zeros((field_wid,field_hei))

        #User inputs number of obstacles and position of obstacles
        for num in range(int(input("\nHow many obstacles would you like to input: ").strip())):
            print("\nObstacle", num + 1)
            obst_y = int(input("What is the y position of this obstacle?: ").strip())
            obst_x = int(input("What is the x position of this obstacle?: ").strip())
            board[obst_y][obst_x] = 1

        #User inputs 
        starting_point = (int(input("\nWhat is the y position of the starting point?: ").strip()), int(input("What is the x position of the starting point?: ").strip()))
        end_point = (int(input("\nWhat is the y position of the end point?: ").strip()), int(input("What is the x position of the end point?: ").strip()))
        board[starting_point[0]][starting_point[1]] = 2
        board[end_point[0]][end_point[1]] = 2
        print(board)

        start_time = time.time()
        path = pathfinder(board, starting_point, end_point)
        end_time = time.time()

        if path[0] == False:
            print('No possible paths')
    
        for y_coord, x_coord in path[1]:
            if board[y_coord][x_coord] == 0:
                board[y_coord][x_coord] = 2

        print("Algorithm took ", end_time - start_time, " seconds.")

        for row in board:
            print(row)

        print('The shortest distance is ', path[2], ' units.')

        if input("Type 'yes' if you would like to find another path: ").lower().strip() != "yes":
            running = False

def manual_version():

    board = [[0,0,0,2,1],
            [0,1,1,1,1],
            [0,0,0,0,0],
            [1,1,1,0,0],
            [1,2,0,0,0]]
    
    starting_point = (0,3)
    end_point = (4,1)

    start_time = time.time()
    path = pathfinder(board, starting_point, end_point)
    end_time = time.time()

    if path[0] == False:
        print('No possible paths')

    else: 
        for p in path[1]:
            if board[p[0]][p[1]] == 0:
                board[p[0]][p[1]] = 3

        print("Algorithm took ", end_time - start_time, " seconds.")

        for row in board:
            print(row)

        print('The shortest distance is ', path[2], ' units.')

def rand_maze_pygame():
    height = 40
    width = 40
    starting_point = (random.randint(0, height-1),0)
    end_point = (random.randint(0, height-1), width-1)
    board = maze_generator(10, height, width, starting_point, end_point)

    #Times A-star pathfinder
    start_time = time.time()
    path = pathfinder(board, starting_point, end_point)
    end_time = time.time()

    print("Algorithm took ", end_time - start_time, " seconds.")

    if path[0] == False:
        print('No possible paths')

    else: 
        #Recolors path rainbow
        frequency = 0.3 #Adjusts frequency of transitions
        shade = 0
        for p in path[1]:
            if board[p[0]][p[1]] == 0:
                r = int(math.sin(frequency*shade) * 127 + 128)
                g = int(math.sin(frequency*shade + 2) * 127 + 128)
                b = int(math.sin(frequency*shade + 4) * 127 + 128)
                board[p[0]][p[1]] = [3, (r,g,b)]
                shade += 1

    board[starting_point[0]][starting_point[1]] = 2
    board[end_point[0]][end_point[1]] = 2
    
    #Initializes pygame, creates screen and draws board
    pygame.init()
    settings = Settings(width, height) #initializes settings
    screen = pygame.display.set_mode((settings.window_width, settings.window_height))
    pygame.display.set_caption("A-Star")
    settings.draw_board(board, screen)
    pygame.display.flip()

def recursive_backtracker():
    height = 100
    width = 100
    starting_point = (random.randint(0, height-1),0)
    board, end_point = rec_backtracker(height, width, starting_point)

    #Times A-star pathfinder
    start_time = time.perf_counter()
    path = pathfinder(board, starting_point, end_point)
    end_time = time.perf_counter()

    print("Algorithm took ", end_time - start_time, " seconds to find a ", len(path[1])," unit long path.")

    if path[0] == False:
        print('No possible paths')

    
    else:
        
        #Recolors path rainbow
        frequency = 0.3 #Adjusts frequency of transitions
        shade = 0
        for p in path[1]:
            if board[p[0]][p[1]] == 0:
                r = int(math.sin(frequency*shade) * 127 + 128)
                g = int(math.sin(frequency*shade + 2) * 127 + 128)
                b = int(math.sin(frequency*shade + 4) * 127 + 128)
                board[p[0]][p[1]] = [3, (r, g, b)]
                shade = shade + 1

    board[starting_point[0]][starting_point[1]] = 2
    board[end_point[0]][end_point[1]] = 2

    #Initializes pygame, creates screen and draws board
    pygame.init()
    settings = Settings(width, height) #initializes settings
    screen = pygame.display.set_mode((settings.window_width, settings.window_height))
    pygame.display.set_caption("Maze")
    settings.draw_board(board, screen)
    pygame.display.flip()


if __name__ == "__main__":
    #manual_version()

    for _ in range(10):
        rand_maze_pygame()
        time.sleep(3)

    # for _ in range(5):
    #     recursive_backtracker()
        

    #terminal_version()