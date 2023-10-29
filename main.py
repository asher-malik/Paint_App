import customtkinter as ctk
import tkinter as tk
from PIL import Image

ctk.set_appearance_mode("light")

window = ctk.CTk()
window.geometry('1000x600')
window.resizable(False, False)
window.title('Paint')

BLACK = '#000101'
DARK_GREY = '#9e9f9f'
LIGHT_GREY = '#bfbebe'
WHITE = '#efefef'

VERY_DARK_RED = '#470000'
DARK_RED = '#910008'
SHADED_RED = '#910008'
RED = '#ee0100'

VERY_DARK_GREEN = '#0a5b09'
DARK_GREEN = '#0ebb00'
SHADED_GREEN = '#0edf0c'
GREEN = '#12ff0c'

VERY_DARK_BLUE = '#000048'
DARK_BLUE = '#010196'
SHADED_BLUE = '#0001b9'
BLUE = '#0801f5'

PINK = '#e901f4'
YELLOW = '#fdff07'
HIGHLIGHT_BLUE = '#0ffffd'
RANDOM_COLOR = '#f05e6d'

PURPLE = '#973fbb'
ORANGE = '#f39c06'
TURQUOISE = '#069f8c'
PEACH = '#f5cdd5'

pen_down = True

class Paint(tk.Canvas):
    def __init__(self, parent):
        super().__init__(master=parent)
        self.pack(expand=True, fill=tk.BOTH)
        self.bind("<B1-Motion>", self.draw_line)
        self.bind("<ButtonRelease-1>", self.release)
        self.prev_x, self.prev_y = None, None
        self.radius = 10
        self.color = 'black'

    def draw_line(self, event):
        if pen_down:
            x, y = event.x, event.y
            if self.prev_x is not None and self.prev_y is not None:
                self.create_oval(x, y, x + self.radius, y + self.radius, fill=self.color, outline=self.color)
                #self.create_line(self.prev_x, self.prev_y, x, y, fill=self.color, width=self.radius * 2)
            self.prev_x, self.prev_y = x, y
        elif not pen_down:
            x, y = event.x, event.y
            if self.prev_x is not None and self.prev_y is not None:
                self.create_line(self.prev_x, self.prev_y, x, y, fill='#f1f1f0', width=self.radius * 2)
            self.prev_x, self.prev_y = x, y

    def release(self, event):
        self.prev_x, self.prev_y = None, None

class PaintOption(ctk.CTkToplevel):
    def __init__(self, parent):
        super(PaintOption, self).__init__(master=parent)
        self.title('Settings')
        self.geometry('250x380')
        self.resizable(False, False)
        self.top_frame = TopFrame(self, paint)
        self.mid_frame = MidFrame(self, paint)
        self.brush_size = BottomFrame(self, paint, self.top_frame)

class TopFrame(ctk.CTkFrame):
    def __init__(self, parent, paint_canvas):
        super(TopFrame, self).__init__(master=parent)
        self.paint_canvas = paint_canvas

        self.columnconfigure((0, 1), uniform='a', weight=2)
        self.rowconfigure((0, 1, 2), uniform='b', weight=1)

        self.mini_canvas = tk.Canvas(self, width=140, height=120)

        self.red_var = ctk.IntVar(value=0)
        self.green_var = ctk.IntVar(value=0)
        self.blue_var = ctk.IntVar(value=0)

        self.red_slider = ctk.CTkSlider(self, from_=0, to=255, button_color='red', button_hover_color='red', command=self.rgb_to_hex_color, variable=self.red_var)
        self.green_slider = ctk.CTkSlider(self, from_=0, to=255, button_color='green', button_hover_color='green', command=self.rgb_to_hex_color, variable=self.green_var)
        self.blue_slider = ctk.CTkSlider(self, from_=0, to=255, button_color='blue', button_hover_color='blue', command=self.rgb_to_hex_color, variable=self.blue_var)

        self.red_slider.grid(row=0, column=0, pady=10)
        self.green_slider.grid(row=1, column=0, pady=10)
        self.blue_slider.grid(row=2, column=0, pady=10)

        self.mini_canvas.grid(row=0, rowspan=3, column=1)

        self.pack(pady=(0, 15))

    def rgb_to_hex_color(self, event):
        r = round(self.red_slider.get())
        g = round(self.green_slider.get())
        b = round(self.blue_slider.get())
        self.paint_canvas.color = f"#{r:02x}{g:02x}{b:02x}"

class MidFrame(ctk.CTkFrame):
    def __init__(self, parent, paint_canvas):
        super(MidFrame, self).__init__(master=parent)
        self.paint_canvas = paint_canvas
        self.columnconfigure((0, 1, 2, 3), uniform='a', weight=1)
        self.rowconfigure((0, 1, 2, 3, 4, 5), uniform='a', weight=1)

        black_button = ctk.CTkButton(master=self, corner_radius=0, fg_color=BLACK, text='', hover_color=BLACK, command=lambda :self.change_pen_color(BLACK))
        dark_grey_button = ctk.CTkButton(master=self, corner_radius=0, fg_color=DARK_GREY, text='', hover_color=DARK_GREY, command=lambda :self.change_pen_color(DARK_GREY))
        light_grey_button = ctk.CTkButton(master=self, corner_radius=0, fg_color=LIGHT_GREY, text='', hover_color=LIGHT_GREY, command=lambda :self.change_pen_color(LIGHT_GREY))
        white_button = ctk.CTkButton(master=self, corner_radius=0, fg_color=WHITE, text='', hover_color=WHITE, command=lambda :self.change_pen_color(WHITE))

        very_dark_red_button = ctk.CTkButton(master=self, corner_radius=0, fg_color=VERY_DARK_RED, text='', hover_color=VERY_DARK_RED, command=lambda :self.change_pen_color(VERY_DARK_RED))
        dark_red_button = ctk.CTkButton(master=self, corner_radius=0, fg_color=DARK_RED, text='', hover_color=DARK_RED, command=lambda :self.change_pen_color(DARK_RED))
        shade_red_button = ctk.CTkButton(master=self, corner_radius=0, fg_color=SHADED_RED, text='', hover_color=SHADED_RED, command=lambda :self.change_pen_color(SHADED_RED))
        red_button = ctk.CTkButton(master=self, corner_radius=0, fg_color=RED, text='', hover_color=RED, command=lambda :self.change_pen_color(RANDOM_COLOR))

        very_dark_green_button = ctk.CTkButton(master=self, corner_radius=0, fg_color=VERY_DARK_GREEN, text='',
                                             hover_color=VERY_DARK_GREEN, command=lambda :self.change_pen_color(VERY_DARK_GREEN))
        dark_green_button = ctk.CTkButton(master=self, corner_radius=0, fg_color=DARK_GREEN, text='', hover_color=DARK_GREEN, command=lambda :self.change_pen_color(DARK_GREEN))
        shade_green_button = ctk.CTkButton(master=self, corner_radius=0, fg_color=SHADED_GREEN, text='',
                                         hover_color=SHADED_GREEN, command=lambda :self.change_pen_color(SHADED_GREEN))
        green_button = ctk.CTkButton(master=self, corner_radius=0, fg_color=GREEN, text='', hover_color=GREEN, command=lambda :self.change_pen_color(GREEN))

        very_dark_blue_button = ctk.CTkButton(master=self, corner_radius=0, fg_color=VERY_DARK_BLUE, text='',
                                               hover_color=VERY_DARK_BLUE, command=lambda :self.change_pen_color(VERY_DARK_BLUE))
        dark_blue_button = ctk.CTkButton(master=self, corner_radius=0, fg_color=DARK_BLUE, text='',
                                          hover_color=DARK_BLUE, command=lambda :self.change_pen_color(DARK_BLUE))
        shade_blue_button = ctk.CTkButton(master=self, corner_radius=0, fg_color=SHADED_BLUE, text='',
                                           hover_color=SHADED_BLUE, command=lambda :self.change_pen_color(SHADED_BLUE))
        blue_button = ctk.CTkButton(master=self, corner_radius=0, fg_color=BLUE, text='', hover_color=BLUE, command=lambda :self.change_pen_color(BLUE))

        pink_button = ctk.CTkButton(master=self, corner_radius=0, fg_color=PINK, text='',
                                              hover_color=PINK, command=lambda :self.change_pen_color(PINK))
        yellow_button = ctk.CTkButton(master=self, corner_radius=0, fg_color=YELLOW, text='',
                                         hover_color=YELLOW, command=lambda :self.change_pen_color(YELLOW))
        high_light_blue_button = ctk.CTkButton(master=self, corner_radius=0, fg_color=HIGHLIGHT_BLUE, text='',
                                          hover_color=HIGHLIGHT_BLUE, command=lambda :self.change_pen_color(HIGHLIGHT_BLUE))
        random_color_button = ctk.CTkButton(master=self, corner_radius=0, fg_color=RANDOM_COLOR, text='', hover_color=RANDOM_COLOR, command=lambda :self.change_pen_color(RANDOM_COLOR))

        purple_button = ctk.CTkButton(master=self, corner_radius=0, fg_color=PURPLE, text='',
                                    hover_color=PURPLE, command=lambda :self.change_pen_color(PURPLE))
        orange_button = ctk.CTkButton(master=self, corner_radius=0, fg_color=ORANGE, text='',
                                      hover_color=ORANGE, command=lambda :self.change_pen_color(ORANGE))
        turquoise_button = ctk.CTkButton(master=self, corner_radius=0, fg_color=TURQUOISE, text='',
                                               hover_color=TURQUOISE, command=lambda :self.change_pen_color(TURQUOISE))
        peach_button = ctk.CTkButton(master=self, corner_radius=0, fg_color=PEACH, text='',
                                            hover_color=PEACH, command=lambda :self.change_pen_color(PEACH))

        black_button.grid(row=0, column=0)
        dark_grey_button.grid(row=0, column=1)
        light_grey_button.grid(row=0, column=2)
        white_button.grid(row=0, column=3)

        very_dark_red_button.grid(row=1, column=0)
        dark_red_button.grid(row=1, column=1)
        shade_red_button.grid(row=1, column=2)
        red_button.grid(row=1, column=3)

        very_dark_green_button.grid(row=2, column=0)
        dark_green_button.grid(row=2, column=1)
        shade_green_button.grid(row=2, column=2)
        green_button.grid(row=2, column=3)

        very_dark_blue_button.grid(row=3, column=0)
        dark_blue_button.grid(row=3, column=1)
        shade_blue_button.grid(row=3, column=2)
        blue_button.grid(row=3, column=3)

        pink_button.grid(row=4, column=0)
        yellow_button.grid(row=4, column=1)
        high_light_blue_button.grid(row=4, column=2)
        random_color_button.grid(row=4, column=3)

        purple_button.grid(row=5, column=0)
        orange_button.grid(row=5, column=1)
        turquoise_button.grid(row=5, column=2)
        peach_button.grid(row=5, column=3)

        self.pack(padx=10)

    def change_pen_color(self, color):
        self.paint_canvas.color = color


class BottomFrame(ctk.CTkFrame):
    def __init__(self, parent, paint_canvas, top_frame):
        super(BottomFrame, self).__init__(master=parent)
        self.paint_canvas = paint_canvas
        self.top_frame = top_frame
        self.radius_var = ctk.IntVar(value=self.paint_canvas.radius)
        self.radius_slider = ctk.CTkSlider(master=self, from_=1, to=40, width=230, command=self.increase_pen_size, variable=self.radius_var)
        self.rowconfigure((0, 1), uniform='a', weight=1)
        self.columnconfigure((0, 1, 2), uniform='a', weight=1)

        self.brush_image = ctk.CTkImage(light_image=Image.open('images/brush.png'), size=(20, 20))
        self.eraser_image = ctk.CTkImage(light_image=Image.open('images/eraser.png'), size=(20, 20))
        self.clear_image = ctk.CTkImage(light_image=Image.open('images/clear.png'), size=(20, 20))

        self.draw_button = ctk.CTkButton(corner_radius=5, master=self, text='', image=self.brush_image, fg_color='white', hover_color=WHITE, command=self.set_pen)
        self.erase_button = ctk.CTkButton(corner_radius=5, master=self, text='', fg_color='white', hover_color=WHITE, image=self.eraser_image, command=self.set_eraser)
        self.clear_button = ctk.CTkButton(corner_radius=5, master=self, text='', fg_color='white', hover_color=WHITE, image=self.clear_image, command=lambda: paint.delete('all'))

        self.radius_slider.grid(row=0, column=0, columnspan=3)
        self.draw_button.grid(row=1, column=0, padx=10, pady=(0, 5))
        self.erase_button.grid(row=1, column=1, padx=10, pady=(0, 5))
        self.clear_button.grid(row=1, column=2, padx=10, pady=(0, 5))
        self.pack(pady=10, fill='x')

    def increase_pen_size(self, event):
        pen_size = round(self.radius_slider.get())
        self.paint_canvas.radius = pen_size
        self.top_frame.mini_canvas.delete('all')
        self.top_frame.mini_canvas.create_oval(70 - self.radius_var.get(), 60 - self.radius_var.get(),
                                               70 + self.radius_var.get(), 60 + self.radius_var.get(), fill=self.paint_canvas.color, outline=self.paint_canvas.color)

    def set_eraser(self):
        global pen_down
        pen_down = False

    def set_pen(self):
        global pen_down
        pen_down = True


paint = Paint(window)

paint_option = PaintOption(window)

window.mainloop()
