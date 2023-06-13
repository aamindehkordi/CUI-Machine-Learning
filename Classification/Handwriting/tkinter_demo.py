import tkinter as tk
import numpy as np
from PIL import Image, ImageTk


# Websites with info about Tkinter:
#  https://tkdocs.com/tutorial/widgets.html
#  https://tkdocs.com/tutorial/grid.html
#  https://www.askpython.com/python-modules/tkinter/python-tkinter-grid-example


################################################################################
#                         INITIALIZE DRAWING CONSTANTS                         #
################################################################################

# The user will be drawing on canvas but we can't just dump the pixels.
# Instead, we must either use platform-dependent code to take a screenshot or
# come up with some alternative. Our alternative is that we will generate an
# internal 2D array of pixels at the same time as we are drawing them.
black_pixel = np.full((1, 3), 0, dtype=np.uint8)
white_pixel = np.full((1, 3), 255, dtype=np.uint8)
test_sample = np.full((140, 140, 3), black_pixel, dtype=np.uint8)


################################################################################
#                           BUTTON HANDLERS FOR GUI                            #
################################################################################

def clear_drawing():
    ''' Clears the drawing canvas and internal array. '''

    cvs_drawspace.delete('all')  # drawing canvas
    test_sample[:] = black_pixel # internal representation of drawing
    lbl_joke1.config(text=joke1_q, background=default_background_color)
    lbl_joke2.config(text=joke2_q, background=default_background_color)


def joke1_handler():
    ''' Shows the punchline for joke #1. '''

    lbl_joke1.config(text=joke1_a, background='lightcoral')


def joke2_handler():
    ''' Shows the punchline for joke #2. '''

    lbl_joke2.config(text=joke2_a, background='lightcoral')


def draw_handwriting(event):
    ''' Draws on the canvas and internal array based on mouse coordinates. '''

    # xy-coordinates and radius of the circle being drawn
    x = event.col
    y = event.y
    r = 2
    cvs_drawspace.create_oval(x - r, y - r, x + r+1, y + r+1, fill='black')
    test_sample[y-2:y+3,x-2:x+3] = white_pixel


################################################################################
#                                 DRAW THE GUI                                 #
################################################################################

# Create a GUI window with a certain size and title
window = tk.Tk()
window.geometry("900x700")
window.wm_title('CSC432 Demo')

# We'll use these variables to tell some jokes
joke1_q = 'Why was 6 afraid of 7?'
joke1_a = "Because 7 ate 9!"
joke2_q = 'Why did 7 eat 9?'
joke2_a = "Because 7 knew that\nhe needed 3 squared\nmeals each day"

# This will be an image that shows in the GUI
elizabeth = Image.open('elizabeth.bmp')
elizabeth.thumbnail((300, 300))
tk_elizabeth = ImageTk.PhotoImage(elizabeth)

# Create all the buttons and stuff. Each column will be as wide as it's
# widest widget. So we make some artifically wide widgets.
lbl_hello_tkinter = tk.Label(text=f'This is my TkInter Demo')
lbl_col0 = tk.Label(text='|             Column 0             |')
lbl_col1 = tk.Label(text='|             Column 1             |')
lbl_col2 = tk.Label(text='|             Column 2             |')
lbl_col3 = tk.Label(text='|             Column 3             |')
lbl_col4 = tk.Label(text='|             Column 4             |')

# The labels will change from jokes to punchlines when the button clicks
lbl_joke1 = tk.Label(text=joke1_q)
btn_joke1 = tk.Button(text='1st Joke', command=joke1_handler)
lbl_joke2 = tk.Label(text=joke2_q)
btn_joke2 = tk.Button(text='2nd Joke', command=joke2_handler)

# This drawing canvas will be very important for our ML model
cvs_drawspace = tk.Canvas(width=140, height=140, bg='white', cursor='tcross',
                          highlightthickness=1, highlightbackground='steelblue')
btn_clear = tk.Button(window, text='Reset Everything', command=clear_drawing)

# There are two steps to placing an image on the screen
lbl_image = tk.Label(text='', image=tk_elizabeth)
lbl_image.image = tk_elizabeth

# The grid layout makes sense but is a bit tedious
lbl_hello_tkinter.grid(row=0, column=0, columnspan=5, pady=5, padx=25)
lbl_col0.grid(row=1, column=0, pady=5)
lbl_col1.grid(row=1, column=1, pady=5)
lbl_col2.grid(row=1, column=2, pady=5)
lbl_col3.grid(row=1, column=3, pady=5)
lbl_col4.grid(row=1, column=4, pady=5)
lbl_joke1.grid(row=3, column=1, pady=5)
lbl_joke2.grid(row=3, column=3, pady=35)
btn_joke1.grid(row=4, column=1, pady=5)
btn_joke2.grid(row=4, column=3, pady=5)
cvs_drawspace.grid(row=5, column=2, pady=5)
btn_clear.grid(row=6, column=2, pady=5)
lbl_image.grid(row=7, column=0, columnspan=5, pady=5)

cvs_drawspace.bind('<B1-Motion>', draw_handwriting)
cvs_drawspace.bind('<Button-1>', draw_handwriting)

default_background_color = lbl_hello_tkinter.cget('background')

window.resizable(False, False)
window.mainloop()
