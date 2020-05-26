from tkinter import *
from tkinter.colorchooser import askcolor
from tkinter import filedialog, messagebox
import tkinter.font as font
from tkinter.ttk import Scale
from PIL import Image
from PIL import ImageTk
import pyscreenshot as ImageGrab
trace = 0
class Paint():
    DEFAULT_PEN_SIZE = 5.0
    DEFAULT_COLOR = 'black'

    def __init__(self):
        self.root = Tk()
        self.root.geometry('1000x800')
        

        #adding widgets
        self.color_frame = LabelFrame(self.root, text='Color', font=('arial', 15), bd=5, relief=RIDGE, bg="white")
        #bd is borderwidth
        self.color_frame.place(x = 0, y =0, width=82, height= 185)
        colors = ["white", "black", "red", "green", "blue", "cyan",
                  "yellow", "magenta", 'pale violet red', 'maroon', 'turquoise1', 'purple2']

        i = 0
        j = 0
        #i for row and j for column
        for color in colors:
            Button(self.color_frame, bg = color, bd=2, relief=RIDGE, width=1, command=lambda col=color:self.select_color(col)).grid(row = i, column = j)
            i = i + 1
            if(i == 6):
                i = 0
                j = 1

        #eraser button
        image = Image.open("eraser.png")
        image = image.resize((40, 40))
        self.photo_image_eraser = ImageTk.PhotoImage(image)
        self.eraser_button = Button(self.root, image = self.photo_image_eraser, command = self.use_eraser, relief= RIDGE)
        self.eraser_button.place(x = 0, y = 187)

        #pen button
        image = Image.open("pen.jpeg")
        image = image.resize((40, 40))
        self.photo_image_pen = ImageTk.PhotoImage(image)
        self.pen_button = Button(
            self.root, image=self.photo_image_pen, command=self.use_pen, relief=RIDGE)
        self.pen_button.place(x = 43, y = 187)

        #clear button
        self.clear_button = Button(self.root, text="CLEAR", bd = 4, bg='white', command = lambda:self.c.delete("all"), width = 8, relief=RIDGE)
        self.clear_button.place(x = 0, y = 225)
        

        #save button
        self.save_button = Button(
            self.root, text="SAVE", bd=4, bg='white', command = self.save, width=8, relief=RIDGE)
        self.save_button.place(x=0, y= 255)

        self.canvas_color_button = Button(
            self.root, text="Canvas", bd=4, bg='white', command=self.canvas_color, width=8, relief=RIDGE)
        self.canvas_color_button.place(x=0, y=285)

        #creating a scale for pen and eraser size
        self.pen_size_scale_frame = LabelFrame(self.root, text="SIZE",bd = 5, bg="white", font=('arial', 15, 'bold'), relief=RIDGE)
        self.pen_size_scale_frame.place(x = 0, y = 318, height = 200, width = 85)
        self.pen_size = Scale(self.pen_size_scale_frame, orient=VERTICAL, from_=50, to=0, length = 170)
        #setting the default value 
        self.pen_size.set(1)
        self.pen_size.grid(row = 0 , column = 1, padx = 15)

        #Circle button
        image = Image.open('circle.jpg')
        image = image.resize((40, 40))
        self.photo_image_circle = ImageTk.PhotoImage(image)
        self.circle_button = Button(
            self.root, image=self.photo_image_circle, command=self.draw_circle, relief=RIDGE)
        self.circle_button.place(x = 0, y = 518)

        #FILLED_CIRCLE 
        image = Image.open('filled_circle.png')
        image = image.resize((40, 40))
        self.photo_image_circle_filled = ImageTk.PhotoImage(image)
        self.circle_filled_button = Button(
            self.root, image=self.photo_image_circle_filled, command=self.draw_circle_filled, relief=RIDGE)
        self.circle_filled_button.place(x = 43, y = 518)

        #Rectangle
        image = Image.open("rectangle.png")
        image = image.resize((40, 40))
        self.photo_image_rectangle = ImageTk.PhotoImage(image)
        self.rectangle_button = Button(
            self.root, image=self.photo_image_rectangle, command=self.draw_rect, relief=RIDGE)
        self.rectangle_button.place(x = 0, y = 564)

        #Filled Rectangle
        image = Image.open("filled_rectangle.png")
        image = image.resize((40, 40))
        self.photo_image_rectangle_filled = ImageTk.PhotoImage(image)
        self.rectangle_filled_button = Button(
            self.root, image=self.photo_image_rectangle_filled, command=self.draw_rect_filled, relief=RIDGE)
        self.rectangle_filled_button.place(x = 43, y = 564)

        #Arc
        image = Image.open("arc.png")
        image = image.resize((40, 40))
        self.photo_image_arc = ImageTk.PhotoImage(image)
        self.arc_button = Button(
            self.root, image=self.photo_image_arc, command=self.draw_arc, relief=RIDGE)
        self.arc_button.place(x = 0 , y = 610)

        #Filled arc
        image = Image.open("filled_arc.png")
        image = image.resize((40, 40))
        self.photo_arc_circle_filled = ImageTk.PhotoImage(image)
        self.arc_filled_button = Button(
            self.root, image=self.photo_arc_circle_filled, command=self.draw_arc_filled, relief=RIDGE)
        self.arc_filled_button.place(x = 43, y = 610)

        #line
        image = Image.open("line.png")
        image = image.resize((40, 40))
        self.photo_image_line = ImageTk.PhotoImage(image)
        self.line_button = Button(
            self.root, image=self.photo_image_line, command=self.draw_line, relief=RIDGE)
        self.line_button.place(x = 0, y = 656)

        #dashed_line
        image = Image.open("dashed_line.png")
        image = image.resize((40, 40))
        self.photo_image_dashed_line = ImageTk.PhotoImage(image)
        self.dashed_line_button = Button(
            self.root, image=self.photo_image_dashed_line, command=self.draw_dashed_line, relief=RIDGE)
        self.dashed_line_button.place(x = 43, y = 656)


        #creating canvas
        self.c = Canvas(self.root, bg = "white", bd = 5, height=500, width = 700)
        self.c.place(x = 90, y = 0)
        self.drawn = None
        self.kinds = [self.c.create_oval, self.c.create_rectangle,
                      self.c.create_arc, self.c.create_line]
        self.setup()
        self.eraser_color = 'white'
        self.root.mainloop()
    
    def setup(self):
        self.old_x = None
        self.old_y = None
        self.line_width = self.pen_size.get()
        self.color = self.DEFAULT_COLOR
        self.eraser_on = False
        #self.active_button = self.pen_button

    def use_pen(self):
        self.activate_button(self.pen_button)
        self.c.bind('<B1-Motion>', self.paint)
        self.c.bind('<ButtonRelease-1>', self.reset)


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
        self.line_width = self.pen_size.get()
        c = event.widget
        if self.drawn:
            c.delete(self.drawn)
        objectId = self.shape(self.start.x, self.start.y, event.x,
                              event.y, outline=self.color, width=self.line_width)
        if trace:
            print(objectId)
        self.drawn = objectId

    def on_grow_shapes_filled(self, event):
        c = event.widget
        if self.drawn:
            c.delete(self.drawn)
        objectId = self.shape(self.start.x, self.start.y, event.x,
                              event.y, outline=self.color, fill=self.color)
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
        self.line_width = self.pen_size.get()
        c = event.widget
        if self.drawn:
            c.delete(self.drawn)
        objectId = self.shape(self.start.x, self.start.y, event.x,
                              event.y, fill=self.color, width=self.line_width)
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
        self.line_width = self.pen_size.get()
        c = event.widget
        if self.drawn:
            c.delete(self.drawn)
        objectId = self.shape(self.start.x, self.start.y, event.x,
                              event.y, fill=self.color, dash=(4, 2), width=self.line_width)
        if trace:
            print(objectId)
        self.drawn = objectId

    def paint(self, event):
        self.line_width = self.pen_size.get()
        paint_color = self.eraser_color if self.eraser_on else self.color
        if self.old_x and self.old_y:
            self.c.create_line(self.old_x, self.old_y, event.x, event.y, width=self.line_width, fill=paint_color,
                               capstyle=ROUND, smooth=TRUE, splinesteps=36)
        self.old_x = event.x
        self.old_y = event.y

    def reset(self, event):
        self.old_x, self.old_y = None, None

    def select_color(self, col):
        self.color = col

    def canvas_color(self):
        color  = askcolor()
        #returns a tuple (rgbvalue, hexadecimal value)
        #we are using hexadecimal value
        self.c.configure(background = color[1])
        self.eraser_color = color[1]

    def save(self):
        try:
            filename = filedialog.asksaveasfilename(defaultextension=".jpg")
            x = self.root.winfo_rootx() + self.c.winfo_x()
            y = self.root.winfo_rooty() + self.c.winfo_y()
            x1 = x + self.c.winfo_width()
            y1 = y + self.c.winfo_height()
            im = ImageGrab.grab(bbox = (x, y, x1, y1))
            #print(str(filename))
            im.save(str(filename))
            #messagebox.showinfo("Image is saved as", str(filename))

        except:
            pass




if __name__ == "__main__":
    p = Paint()
