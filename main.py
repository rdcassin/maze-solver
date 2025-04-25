from graphics import Window, Point, Line
from cell import Cell

def main():
    win = Window(800, 600)
    p1 = Point(100, 100)
    p2 = Point(200, 200)
    line = Line(p1, p2)
    win.draw_line(line, "blue")
    cell1 = Cell(50, 50, 150, 150, win)
    cell2 = Cell(150, 50, 250, 150, win, has_left_wall=False)
    cell3 = Cell(50, 150, 150, 250, win, has_top_wall=False)
    cell4 = Cell(150, 150, 250, 250, win, has_right_wall=False)
    cell5 = Cell(50, 250, 150, 350, win, has_bottom_wall=False)
    cell6 = Cell(150, 250, 250, 350, win, has_left_wall=False, has_top_wall=False)
    cell7 = Cell(50, 350, 150, 450, win, has_top_wall=False)
    cell8 = Cell(150, 350, 250, 450, win, has_left_wall=False, has_top_wall=False)
    cell1.draw()
    cell2.draw()
    cell3.draw()
    cell4.draw()
    cell5.draw()
    cell6.draw()
    cell7.draw()
    cell8.draw()
    win.wait_for_close()


main()