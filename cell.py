from graphics import Line, Point

class Cell:
    def __init__(self, win=None, x1=None, y1=None, x2=None, y2=None, has_left_wall=True, has_top_wall=True, has_right_wall=True, has_bottom_wall=True):
        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2
        self.has_left_wall = has_left_wall
        self.has_top_wall = has_top_wall
        self.has_right_wall = has_right_wall
        self.has_bottom_wall = has_bottom_wall
        self._win = win
        self.visited = False

    def draw(self):
        if self._win is None:
            return
        if self.has_left_wall:
            line = Line(Point(self._x1, self._y1), Point(self._x1, self._y2))
            self._win.draw_line(line)
        else:
            line = Line(Point(self._x1, self._y1), Point(self._x1, self._y2))
            self._win.draw_line(line, "white")
        if self.has_top_wall:
            line = Line(Point(self._x1, self._y1), Point(self._x2, self._y1))
            self._win.draw_line(line)
        else:
            line = Line(Point(self._x1, self._y1), Point(self._x2, self._y1))
            self._win.draw_line(line, "white")
        if self.has_right_wall:
            line = Line(Point(self._x2, self._y1), Point(self._x2, self._y2))
            self._win.draw_line(line)
        else:   
            line = Line(Point(self._x2, self._y1), Point(self._x2, self._y2))
            self._win.draw_line(line, "white")
        if self.has_bottom_wall:
            line = Line(Point(self._x1, self._y2), Point(self._x2, self._y2))
            self._win.draw_line(line)
        else:
            line = Line(Point(self._x1, self._y2), Point(self._x2, self._y2))
            self._win.draw_line(line, "white")

    def draw_move(self, to_cell, undo=False):
        line = Line(Point((self._x1 + self._x2) / 2, (self._y1 + self._y2) / 2), Point((to_cell.x1 + to_cell.x2) / 2, (to_cell.y1 + to_cell.y2) / 2))
        if undo:
            color = "red"
        else:
            color = "grey"
            
        if self._x1 > to_cell.x1 and self._y1 == to_cell.y1:
            if self.has_left_wall or to_cell.has_right_wall:
                return
        elif self._x1 == to_cell.x1 and self._y1 > to_cell.y1:
            if self.has_left_wall or to_cell.has_right_wall:
                return
        elif self._x1 < to_cell.x1 and self._y1 == to_cell.y1:
            if self.has_left_wall or to_cell.has_right_wall:
                return
        elif self._x1 == to_cell.x1 and self._y1 < to_cell.y1:
            if self.has_left_wall or to_cell.has_right_wall:
                return
        else:
            return
        self._win.draw_line(line, color)
        
            