from tkinter import *
from tkinter.colorchooser import askcolor
import tkinter.font as font
from PIL import Image
from PIL import ImageTk
trace = 0


class Paint(object):

    DEFAULT_PEN_SIZE = 5.0
    DEFAULT_COLOR = 'black'

    def __init__(self):
        self.root = Tk()

        self.myFont = font.Font(family='Helvetica', size=15)

        self.pen_button = Button(self.root, text='  Pen  ', command=self.use_pen)
        self.pen_button.grid(row=0, column=0, columnspan=2)
        self.pen_button['font'] = self.myFont

        self.color_button = Button(self.root, text='  Color  ', command=self.choose_color)
        self.color_button.grid(row=0, column=2, columnspan=2)
        self.color_button['font'] = self.myFont

        self.eraser_button = Button(self.root, text='  Eraser  ', command=self.use_eraser)
        self.eraser_button.grid(row=0, column=4, columnspan=2)
        self.eraser_button['font'] = self.myFont

        self.choose_size_button = Scale(self.root, from_=1, to=10, orient=HORIZONTAL)
        self.choose_size_button.grid(row=0, column=6, columnspan=3)
        self.choose_size_button['font'] = self.myFont

        image = Image.open('circle.jpg')
        image = image.resize((20, 20)) 
        self.photo_image_circle = ImageTk.PhotoImage(image)

        self.circle_button = Button(self.root, image=self.photo_image_circle, command=self.draw_circle)
        self.circle_button.grid(row=1, column=0)
        
        image = Image.open('filled_circle.png')
        image = image.resize((20, 20))
        
        self.photo_image_circle_filled = ImageTk.PhotoImage(image)


        self.circle_filled_button = Button(self.root, image=self.photo_image_circle_filled, command=self.draw_circle_filled)
        self.circle_filled_button.grid(row=1, column=1)

        image = Image.open("rectangle.png")
        image = image.resize((20,20))
        self.photo_image_rectangle = ImageTk.PhotoImage(image)

        self.rectangle_button = Button(self.root, image=self.photo_image_rectangle, command=self.draw_rect)
        self.rectangle_button.grid(row=1, column=2)

        image = Image.open("rectangle.png")
        image = image.resize((20, 20))
        
        self.photo_image_rectangle_filled = ImageTk.PhotoImage(image)

        self.rectangle_filled_button = Button(self.root, image=self.photo_image_rectangle_filled, command=self.draw_rect_filled)
        self.rectangle_filled_button.grid(row=1, column=3)

        image = Image.open("arc.png")
        image = image.resize((20, 20))
        self.photo_image_arc = ImageTk.PhotoImage(image)

        self.arc_button = Button(self.root, image=self.photo_image_arc, command=self.draw_arc)
        self.arc_button.grid(row=1, column=4)

        image = Image.open("filled_arc.png")
        image = image.resize((20, 20))
        self.photo_arc_circle_filled = ImageTk.PhotoImage(image)

        self.arc_filled_button = Button(self.root, image=self.photo_arc_circle_filled, command=self.draw_arc_filled)
        self.arc_filled_button.grid(row=1, column=5)

        image = Image.open("line.png")
        image = image.resize((20, 20))
        self.photo_image_line = ImageTk.PhotoImage(image)

        self.line_button = Button(self.root, image=self.photo_image_line, command=self.draw_line)
        self.line_button.grid(row=1, column=6)

        image = Image.open("arrow.png")
        image = image.resize((20, 20))
        self.photo_image_arrow = ImageTk.PhotoImage(image)

        self.arrow_button = Button(self.root, image=self.photo_image_arrow, command=self.draw_arrow)
        self.arrow_button.grid(row=1, column=7)

        image = Image.open("dashed_line.png")
        image = image.resize((20, 20))
        self.photo_image_dashed_line = ImageTk.PhotoImage(image)

        self.dashed_line_button = Button(self.root, image=self.photo_image_dashed_line, command=self.draw_dashed_line)
        self.dashed_line_button.grid(row=1, column=8)

        self.c = Canvas(self.root, bg='white', width=700, height=700)
        self.c.grid(row=2, columnspan=9)

        self.drawn = None
        self.kinds = [self.c.create_oval, self.c.create_rectangle, self.c.create_arc, self.c.create_line]
        self.setup()
        self.root.mainloop()

    def setup(self):
        self.old_x = None
        self.old_y = None
        self.line_width = self.choose_size_button.get()
        self.color = self.DEFAULT_COLOR
        self.eraser_on = False
        self.active_button = self.pen_button

    def use_pen(self):
        self.activate_button(self.pen_button)
        self.c.bind('<B1-Motion>', self.paint)
        self.c.bind('<ButtonRelease-1>', self.reset)

    def choose_color(self):
        self.eraser_on = False
        self.color = askcolor(color=self.color)[1]

    def use_eraser(self):
        self.activate_button(self.eraser_button, eraser_mode=True)
        self.c.bind('<B1-Motion>', self.paint)
        self.c.bind('<ButtonRelease-1>', self.reset)

    def activate_button(self, some_button, eraser_mode=False):
        #self.active_button.config(relief=RAISED)
        #some_button.config(relief=SUNKEN)
        self.active_button = some_button
        self.eraser_on = eraser_mode

    def draw_circle(self):
        self.activate_button(self.circle_button)
        self.c.bind('<ButtonPress-1>', self.on_start_circle)
        self.c.bind('<B1-Motion>', self.on_grow_shapes)

    def on_start_circle(self, event):
        self.shape = self.kinds[0]
        self.start = event
        self.drawn = None

    def draw_circle_filled(self):
        self.activate_button(self.circle_filled_button)
        self.c.bind('<ButtonPress-1>', self.on_start_circle_filled)
        self.c.bind('<B1-Motion>', self.on_grow_shapes_filled)

    def on_start_circle_filled(self, event):
        self.shape = self.kinds[0]
        self.start = event
        self.drawn = None

    def draw_rect(self):
        self.activate_button(self.rectangle_button)
        self.c.bind('<ButtonPress-1>', self.on_start_rect)
        self.c.bind('<B1-Motion>', self.on_grow_shapes)

    def on_start_rect(self, event):
        self.shape = self.kinds[1]
        self.start = event
        self.drawn = None

    def draw_rect_filled(self):
        self.activate_button(self.rectangle_filled_button)
        self.c.bind('<ButtonPress-1>', self.on_start_rect_filled)
        self.c.bind('<B1-Motion>', self.on_grow_shapes_filled)

    def on_start_rect_filled(self, event):
        self.shape = self.kinds[1]
        self.start = event
        self.drawn = None

    def draw_arc(self):
        self.activate_button(self.arc_button)
        self.c.bind('<ButtonPress-1>', self.on_start_arc)
        self.c.bind('<B1-Motion>', self.on_grow_shapes)

    def on_start_arc(self, event):
        self.shape = self.kinds[2]
        self.start = event
        self.drawn = None

    def draw_arc_filled(self):
        self.activate_button(self.arc_filled_button)
        self.c.bind('<ButtonPress-1>', self.on_start_arc_filled)
        self.c.bind('<B1-Motion>', self.on_grow_shapes_filled)

    def on_start_arc_filled(self, event):
        self.shape = self.kinds[2]
        self.start = event
        self.drawn = None

    def on_grow_shapes(self, event):
        self.line_width = self.choose_size_button.get()
        c = event.widget
        if self.drawn:
            c.delete(self.drawn)
        objectId = self.shape(self.start.x, self.start.y, event.x, event.y, outline=self.color, width=self.line_width)
        if trace:
            print(objectId)
        self.drawn = objectId

    def on_grow_shapes_filled(self, event):
        c = event.widget
        if self.drawn:
            c.delete(self.drawn)
        objectId = self.shape(self.start.x, self.start.y, event.x, event.y, outline=self.color, fill=self.color)
        if trace:
            print(objectId)
        self.drawn = objectId

    def draw_line(self):
        self.activate_button(self.line_button)
        self.c.bind('<ButtonPress-1>', self.on_start_line)
        self.c.bind('<B1-Motion>', self.on_grow_line)

    def on_start_line(self, event):
        self.shape = self.kinds[3]
        self.start = event
        self.drawn = None

    def on_grow_line(self, event):
        self.line_width = self.choose_size_button.get()
        c = event.widget
        if self.drawn:
            c.delete(self.drawn)
        objectId = self.shape(self.start.x, self.start.y, event.x, event.y, fill=self.color, width=self.line_width)
        if trace:
            print(objectId)
        self.drawn = objectId

    def draw_arrow(self):
        self.activate_button(self.arrow_button)
        self.c.bind('<ButtonPress-1>', self.on_start_arrow)
        self.c.bind('<B1-Motion>', self.on_grow_arrow)

    def on_start_arrow(self, event):
        self.shape = self.kinds[3]
        self.start = event
        self.drawn = None

    def on_grow_arrow(self, event):
        self.line_width = self.choose_size_button.get()
        c = event.widget
        if self.drawn:
            c.delete(self.drawn)
        objectId = self.shape(self.start.x, self.start.y, event.x, event.y, fill=self.color, arrow=BOTH, width=self.line_width)
        if trace:
            print(objectId)
        self.drawn = objectId

    def draw_dashed_line(self):
        self.activate_button(self.dashed_line_button)
        self.c.bind('<ButtonPress-1>', self.on_start_dashed_line)
        self.c.bind('<B1-Motion>', self.on_grow_dashed_line)

    def on_start_dashed_line(self, event):
        self.shape = self.kinds[3]
        self.start = event
        self.drawn = None

    def on_grow_dashed_line(self, event):
        self.line_width = self.choose_size_button.get()
        c = event.widget
        if self.drawn:
            c.delete(self.drawn)
        objectId = self.shape(self.start.x, self.start.y, event.x, event.y, fill=self.color, dash=(4, 2), width=self.line_width)
        if trace:
            print(objectId)
        self.drawn = objectId

    def paint(self, event):
        self.line_width = self.choose_size_button.get()
        paint_color = 'white' if self.eraser_on else self.color
        if self.old_x and self.old_y:
            self.c.create_line(self.old_x, self.old_y, event.x, event.y, width=self.line_width, fill=paint_color,
                               capstyle=ROUND, smooth=TRUE, splinesteps=36)
        self.old_x = event.x
        self.old_y = event.y

    def reset(self, event):
        self.old_x, self.old_y = None, None


if __name__ == '__main__':
    Paint()
