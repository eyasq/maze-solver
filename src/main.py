from tkinter import Tk, BOTH, Canvas
import time
class Window:
    def __init__(self,width, height ):
        self.width = width
        self.height = height
        self.__root = Tk()
        self.__root.title = "title"
        self.canvas = Canvas(self.__root, width=self.width, height=self.height)
        self.canvas.pack()
        self.running = False

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()
    
    def wait_for_close(self):
        self.running = True
        while(self.running == True):
            self.redraw()
    
    def draw_line(self, line, fill_color):
        line.draw(self.canvas, fill_color)
        

    def close(self):
        self.running = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close )


def main():
    win = Window(1280, 960)
    point1 = Point(0, 0)
    point2 = Point(40,40)
    point3 = Point(100, 0)
    point4 = Point(50, 50)
    line = Line(point1, point2)
    line2 = Line(point3, point4)
    # line.draw(win.canvas, "black")

    cell = Cell(win)
    # cell.draw(10,10,100,100)
    cell2 = Cell(win)
    # cell2.draw(50,50,200,200)
    cell.draw_move(cell2, True)
    maze = Maze(
        x1=50,
        y1=50,
        num_rows=20,
        num_cols=30,
        cell_size_x=40,
        cell_size_y=40,
        win=win
    )
    win.wait_for_close()



class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        #x=0 is left, y=0 is top

class Line:
    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2

    def draw(self, Canvas, fill_color):
        Canvas.create_line(
            self.point1.x, self.point1.y, self.point2.x, self.point2.y, fill=fill_color, width=2
        )
    
class Cell:
    def __init__(self, window=None):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.__x1 = -1
        self.__x2 = -1
        self.__y1 = -1
        self.__y2 = -1
        self.__win = window
    def draw(self,x1,y1,x2,y2):
        self.__x1 = x1
        self.__x2 = x2
        self.__y1 = y1
        self.__y2 = y2
        if self.has_left_wall:
            point1 = Point(x1,y1)
            point2 = Point(x1, y2)
            line = Line(point1, point2)
            if self.__win:
                line.draw(self.__win.canvas, "black")
        else:
            if self.win:
                line.draw(self.__win.canvas, "white")
        if self.has_right_wall:
            point1 = Point(x2,y1)
            point2 = Point(x2,y2)
            line  = Line(point1,point2)
            if self.__win:
                line.draw(self.__win.canvas, "black")
        else:
            if self.win:
                line.draw(self.__win.canvas, "white")
        if self.has_top_wall:
            point1 = Point(x1,y1)
            point2 = Point(x2,y1)
            line  = Line(point1,point2)
            if self.__win:
                line.draw(self.__win.canvas, "black")
        else:
            if self.win:
                line.draw(self.__win.canvas, "white")
        if self.has_bottom_wall:
            point1 = Point(x1,y2)
            point2 = Point(x2,y2)
            line  = Line(point1,point2)
            if self.__win:
                line.draw(self.__win.canvas, "black")
        else:
            if self.win:
                line.draw(self.__win.canvas, "white")
        
    def draw_move(self, to_cell, undo=False):
        self.center_x = (self.__x1 + self.__x2)/2
        self.center_y = (self.__y1+self.__y2)/2
        to_cell.center_x = (to_cell.__x1+to_cell.__x2)/2
        to_cell.center_y = (to_cell.__y1+to_cell.__y2)/2
        center_self = Point(self.center_x, self.center_y)
        center_to = Point(to_cell.center_x, to_cell.center_y)
        line = Line(center_self, center_to)
        if undo==False:
            if self.__win:
                line.draw(self.__win.canvas, "red")
        else:
            if self.__win:
                line.draw(self.__win.canvas, "gray")


class Maze:
    def __init__(self, x1 ,y1, num_rows, num_cols, cell_size_x, cell_size_y, win=None):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        self.__cells = []
        self.__create_cells()
        self.__break_entrance_and_exit()
    def __create_cells(self):
        for i in range(self.num_cols):
            self.__cells.append([])
            for j in range(self.num_rows):
                self.__cells[i].append(Cell(self.win))
                if self.win:
                    self.__draw_cell(i,j)
        
    def __draw_cell(self,i,j):
        x1 = self.x1 + (i * self.cell_size_x)  
        y1 = self.y1 + (j * self.cell_size_y)  
        x2 = x1 + self.cell_size_x
        y2 = y1 + self.cell_size_y
        if self.win:
            self.__cells[i][j].draw(x1, y1, x2, y2)
        self._animate()
    
    def _animate(self):
        if self.win:
            self.win.redraw()

    def __break_entrance_and_exit(self):
        self.__cells[0][0].has_top_wall = False
        self.__draw_cell(0,0)
        self.__cells[-1][-1].has_bottom_wall = False
        self.__draw_cell(-1,-1)

