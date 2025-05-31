from tkinter import Tk, BOTH, Canvas

class Window:
    def __init__(self,width, height ):
        self.width = width
        self.height = height
        self.__root = Tk()
        self.__root.title = "title"
        self.canvas = Canvas()
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
    win = Window(800, 600)
    point1 = Point(0, 0)
    point2 = Point(40,40)
    point3 = Point(100, 0)
    point4 = Point(50, 50)
    line = Line(point1, point2)
    line2 = Line(point3, point4)
    line.draw(win.canvas, "black")

    cell = Cell(win)
    cell.draw(10,10,100,100)
    cell2 = Cell(win)
    cell2.draw(50,50,200,200)
    cell.draw_move(cell2, True)
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
    def __init__(self, window):
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
            line.draw(self.__win.canvas, "black")
        if self.has_right_wall:
            point1 = Point(x2,y1)
            point2 = Point(x2,y2)
            line  = Line(point1,point2)
            line.draw(self.__win.canvas, "black")
        if self.has_top_wall:
            point1 = Point(x1,y1)
            point2 = Point(x2,y1)
            line  = Line(point1,point2)
            line.draw(self.__win.canvas, "black")
        if self.has_bottom_wall:
            point1 = Point(x1,y2)
            point2 = Point(x2,y2)
            line  = Line(point1,point2)
            line.draw(self.__win.canvas, "black")
        
    def draw_move(self, to_cell, undo=False):
        self.center_x = (self.__x1 + self.__x2)/2
        self.center_y = (self.__y1+self.__y2)/2
        to_cell.center_x = (to_cell.__x1+to_cell.__x2)/2
        to_cell.center_y = (to_cell.__y1+to_cell.__y2)/2
        center_self = Point(self.center_x, self.center_y)
        center_to = Point(to_cell.center_x, to_cell.center_y)
        line = Line(center_self, center_to)
        if undo==False:
            line.draw(self.__win.canvas, "red")
        else:
            line.draw(self.__win.canvas, "gray")



main()