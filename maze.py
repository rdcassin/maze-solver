from cell import Cell
import time

class Maze:
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win):
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        self._cells = []

        self._create_cells()

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
        self._cells[i][j].x1 = self._x1 + i * self._cell_size_x
        self._cells[i][j].y1 = self._y1 + j * self._cell_size_y
        self._cells[i][j].x2 = self._x1 + (i + 1) * self._cell_size_x
        self._cells[i][j].y2 = self._y1 + (j + 1) * self._cell_size_y
        self._cells[i][j].draw()
        self._animate()

    def _animate(self):
        self._win.redraw()
        time.sleep(0.005)
