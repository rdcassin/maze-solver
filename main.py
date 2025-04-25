from graphics import Window, Point, Line
from cell import Cell
from maze import Maze

def main():
    win_x = 800
    win_y = 800
    win = Window(win_x, win_y)
    margin = 20
    rows = 16
    cols = 16
    cell_size_x = (win_x - 2 * margin) / cols
    cell_size_y = (win_y - 2 * margin) / rows

    maze = Maze(margin, margin, rows, cols, cell_size_x, cell_size_y, win)
    win.wait_for_close()

main()