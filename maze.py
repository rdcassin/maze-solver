import random
import time
from cell import Cell

class Maze:
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win=None, seed=None):
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        if seed is not None:
            self._seed = random.seed(seed)
        self._cells = []

        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0, 0)
        self._reset_cells_visited()

    def _create_cells(self):
        for i in range(0, self._num_cols):
            cols = []
            for j in range(0, self._num_rows):
                cols.append(Cell(self._win))
            self._cells.append(cols)
        for i in range(0, self._num_cols):
            for j in range(0, self._num_rows):
                self._draw_cell(i, j)

    def _draw_cell(self, i, j):
        self._cells[i][j]._x1 = self._x1 + i * self._cell_size_x
        self._cells[i][j]._y1 = self._y1 + j * self._cell_size_y
        self._cells[i][j]._x2 = self._x1 + (i + 1) * self._cell_size_x
        self._cells[i][j]._y2 = self._y1 + (j + 1) * self._cell_size_y
        self._cells[i][j].draw()
        self._animate()

    def _animate(self):
        if self._win is None:
            return
        self._win.redraw()
        time.sleep(0.005)

    def _break_entrance_and_exit(self):
        entrance = self._cells[0][0]
        entrance.has_top_wall = False
        entrance.draw()

        exit = self._cells[self._num_cols - 1][self._num_rows - 1]
        exit.has_bottom_wall = False
        exit.draw()
        self._animate()

    def _break_walls_r(self, i, j):
        self._cells[i][j].visited = True
        while True:
            neighbors = []
            if i > 0 and not self._cells[i - 1][j].visited:
                neighbors.append(self._cells[i - 1][j])
            if j > 0 and not self._cells[i][j - 1].visited:
                neighbors.append(self._cells[i][j - 1])
            if i < self._num_cols - 1 and not self._cells[i + 1][j].visited:
                neighbors.append(self._cells[i + 1][j])
            if j < self._num_rows - 1 and not self._cells[i][j + 1].visited:
                neighbors.append(self._cells[i][j + 1])

            if len(neighbors) == 0:
                self._draw_cell(i, j)
                return

            next_index = random.randint(0, len(neighbors) - 1)
            next_cell = neighbors[next_index]

            if next_cell._x1 < self._cells[i][j]._x1:
                self._cells[i][j].has_left_wall = False
                next_cell.has_right_wall = False
                next_i = i - 1
                next_j = j
            elif next_cell._y1 < self._cells[i][j]._y1:
                self._cells[i][j].has_top_wall = False
                next_cell.has_bottom_wall = False
                next_i = i
                next_j = j - 1
            elif next_cell._x1 > self._cells[i][j]._x1:
                self._cells[i][j].has_right_wall = False
                next_cell.has_left_wall = False
                next_i = i + 1
                next_j = j
            elif next_cell._y1 > self._cells[i][j]._y1:
                self._cells[i][j].has_bottom_wall = False
                next_cell.has_top_wall = False
                next_i = i
                next_j = j + 1

            self._break_walls_r(next_i, next_j)

    def _reset_cells_visited(self):
        for i in range(0, self._num_cols):
            for j in range(0, self._num_rows):
                self._cells[i][j].visited = False