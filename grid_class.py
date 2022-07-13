from settings import *
import pygame
from cell_class import *

class Grid:
    def __init__(self, game):
        self.game = game
        self.pos = (GRID_POS[0], GRID_POS[1])
        self.cells = []
        self.make_grid()

    def make_grid(self):
        for x in range(3):
            for y in range(3):
                self.cells.append(Cell(x, y, self))
        print(self.cells)

    def update(self):
        for cell in self.cells:
            cell.update()

    def draw(self):
        for cell in self.cells:
            cell.draw()