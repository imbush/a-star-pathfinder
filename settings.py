import pygame

'''Contains settings and functions for pygame representations'''

class Settings:
    def __init__(self, x_num_rect, y_num_rect):#initialize settings

        self.window_width = 1200 
        self.window_height = 650 
        self.top_margin_height = 10 
        self.bottom_margin_height = 5 
        self.margin_width = 5 #Size of x margin
        self.gap_size = 1 #Space between rectangles
        self.game_running = True

        self.default_font_size = self.top_margin_height * 3/5

        self.x_num_rect = x_num_rect #x and y number of squares in board
        self.y_num_rect = y_num_rect

        self.board_width = self.window_width - 2 * self.margin_width #pixel width of board
        self.board_height = self.window_height - (self.top_margin_height + self.bottom_margin_height)#pixel height of board

        self.box_width = (self.board_width - self.gap_size * (self.x_num_rect - 1))/self.x_num_rect #box height
        self.box_height = (self.board_height - self.gap_size * (self.y_num_rect - 1))/self.y_num_rect #box width

        self.white = (40, 40, 40) #colors used
        self.gray = (199, 199, 199) #May need to change
        self.blue = (64, 133, 198)
        self.red = (240, 79, 69)
        self.dark_blue = (20, 54, 86)
        self.green = (41, 148, 20)
        self.black = (0,0,0)

        #game colors
        self.bg_color = self.white
        self.empty_color = self.gray
        self.obstacle_color = self.black
        self.endpoint_color = self.red
        self.path_color = self.green

    def left_top_coords_of_box(self, boxx,boxy):
        '''converts board coordinates to pixel coordinates'''
        left = (boxx - 1) * (self.box_width + self.gap_size) + self.margin_width #formula for finding left of box
        top = (boxy - 1) * (self.box_height + self.gap_size) + self.top_margin_height #formula for finding top of box
        return left, top

    def draw_board(self, board, screen): 
        '''resets screen with new board'''

        screen.fill(self.bg_color)
        for boxx in range (self.x_num_rect):
            for boxy in range (self.y_num_rect):
                left, top = self.left_top_coords_of_box(boxx + 1, boxy + 1) #I don't know why this works but it works
                if isinstance(board[boxy][boxx], int) or isinstance(board[boxy][boxx], float):
                    if board[boxy][boxx] == 0:
                        pygame.draw.rect(screen, self.empty_color,(left, top, self.box_width, self.box_height)) #draws empty boxes
                    elif board[boxy][boxx] == 1:
                        pygame.draw.rect(screen, self.obstacle_color,(left, top, self.box_width, self.box_height)) #draws infected boxes
                    elif board[boxy][boxx] == 2:
                        pygame.draw.rect(screen, self.endpoint_color,(left, top, self.box_width, self.box_height)) 
                    elif board[boxy][boxx] == 3:
                        pygame.draw.rect(screen, self.path_color,(left, top, self.box_width, self.box_height)) 
                else:
                    pygame.draw.rect(screen, board[boxy][boxx][1],(left, top, self.box_width, self.box_height))