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
    
    def draw_lin(self, line, fill_color):
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
    line2.draw(win.canvas, "magenta")
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
    

main()