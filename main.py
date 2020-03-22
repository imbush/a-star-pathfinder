from settings import Cell, reconstruct_path, pathfinder, Settings
import time, pygame, sys
import numpy as np


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
        board[starting_point[0]], [starting_point[1]] = 2
        board[end_point[0]], [end_point[1]] = 2
        print(board)

        start_time = time.time()
        path = pathfinder(board, starting_point, end_point)
        end_time = time.time()

        for y_coord, x_coord in path:
            if board[y_coord][x_coord] == 0:
                board[y_coord][x_coord] = 2

        print("Algorithm took ", end_time - start_time, " seconds.")

        for row in board:
            print(row)

        print('The shortest distance is ', path[2], ' units.')

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

def pygame_version():
    board = [[0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 1, 2, 1, 0, 0, 1, 1, 0],
            [0, 0, 1, 1, 1, 0, 1, 1, 0, 0],
            [0, 1, 1, 0, 1, 0, 1, 2, 0, 0],
            [0, 1, 0, 0, 0, 0, 1, 1, 1, 0],
            [0, 1, 0, 1, 1, 0, 0, 0, 1, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 1, 1, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
    
    starting_point = (2,3)
    end_point = (4,7)

    start_time = time.time()
    path = pathfinder(board, starting_point, end_point)
    end_time = time.time()

    if path[0] == False:
        print('No possible paths')

    else: 
        for p in path[1]:
            if board[p[0]][p[1]] == 0:
                board[p[0]][p[1]] = 3
    
    pygame.init()

    while True:
        settings = Settings() #initializes settings

        screen = pygame.display.set_mode((settings.window_width, settings.window_height))
        pygame.display.set_caption("A-Star")

        settings.draw_board(board, screen)
        pygame.display.flip()

        for event in pygame.event.get(): 
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()



if __name__ == "__main__":
    #manual_version()
    pygame_version()
    #terminal_version()