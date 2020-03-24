import numpy as np
import pygame
class Cell:
    def __init__(self, parent = None, position = None, g = 0):
        self.parent = parent
        self.position = position
        self.g = g #the cost of the cheapest known path from the start to a cell 
        self.h = 0 #the cost of the cheapest known path from the start to a cell 
        self.f = 0 #the sum of g and h
    def __eq__(self, other):
        return self.position == other.position

def reconstruct_path(final_cell):
    '''returns a list of tuples identifying the path squares'''
    path = []
    current = final_cell
    while current is not None: #Follows the parents of each cell and adds to 
        path.append(current.position)
        current = current.parent
    return path

def pathfinder(table, start: tuple, end: tuple):
    """returns an array with """
    start = Cell(None, start)
    end = Cell(None, end)
    
    #open and closed lists
    open_cells =[start]
    closed_cells = []


    while len(open_cells) > 0: #Runs while open_cells is not empty

        #Sets current_cell to the minimum f-cost cell in open_cells
        current_cell = open_cells[0]
        current_index = 0
        for index, cell in enumerate(open_cells):
            if cell.f < current_cell.f:
                current_cell = cell
                current_index = index

        if current_cell == end:
            return [True, reconstruct_path(current_cell), current_cell.g]

        #removes current from open_cells
        del(open_cells[current_index])


        neighbors = []
        for neighbor_change in [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]:
            neighbor_position =  tuple(map(lambda i, j: i + j, current_cell.position, neighbor_change))
            
            #skips if neighbor is outside bounds or is an obstacle
            if neighbor_position[0] < 0 or neighbor_position[1] < 0 or neighbor_position[0] > (len(table) - 1) or neighbor_position[1] > (len(table[0]) - 1):
                continue
            if table[neighbor_position[0]][neighbor_position[1]] == 1:
                continue

            #Creates new cell from neighbor info
            neighbor_cell = Cell(current_cell, neighbor_position)

            #Finds tentative g = to the current g-score plus the distance to the current
            neighbor_cell.g = current_cell.g + ((neighbor_change[0]**2) + (neighbor_change[1]**2))**0.5

            neighbors.append(neighbor_cell)

        #loops through neighbors and resets g-scores
        for neighbor in neighbors:
            
            continue_bool = True
            #does not add to open cell list if it is in closed cell list
            for closed_item in closed_cells:
                if neighbor == closed_item:
                    continue_bool = False 

            #Sets neighbor h-cost to distance from end; sets f to g+h
            neighbor.h = (((neighbor.position[0]- end.position[0])**2)+(neighbor.position[1] - end.position[1])**2)**0.5
            neighbor.f = neighbor.h + neighbor.g

            #does not add to open if it is in open cell list already
            for open_cell in open_cells:
                if neighbor == open_cell:
                    if neighbor.g > open_cell.g: 
                        continue_bool = False
                    else:
                        open_cells.remove(open_cell)

            if continue_bool:
                open_cells.append(neighbor)

        closed_cells.append(current_cell)

    return (False, [])