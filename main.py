from DiceRollerV2.dice_roller_functions import DiceRoller as drf

import tkinter as tk
from tkinter.constants import LEFT
import PIL.ImageTk as itk
import PIL.Image as img
from tkinter import messagebox

# Setting window dimension variables
window_height = 500
window_width = 600

# Empty die type string
die_type = ''
# Dice Total 
dice_total = 0

# Die setting functions
def set_d4():
    global die_type
    die_type = 'd4'

def set_d6():
    global die_type
    die_type = 'd6'

def set_d8():
    global die_type
    die_type = 'd8'

def set_d10():
    global die_type
    die_type = 'd10'

def set_d12():
    global die_type
    die_type = 'd12'

def set_d20():
   global die_type
   die_type = 'd20'

window = tk.Tk()
# Set default size of the window displayed.
window.geometry(f'{(window_width)}x{(window_height)}')
# Window Title to Describe the program.
window.title('Random Dice Roller')
# Formatted color of the window background.
window.config(background='dim gray')

# Frame for the heading picture to reside in.
photo_frame = tk.LabelFrame(window, borderwidth=0)
photo_frame.pack()

# Format the picture to a more useable size.
photo1 = img.open('DiceRollerV2/dice/dice-image.png').resize((window_width, int(window_height/4)), img.ANTIALIAS)
# Put the photo into a variable that can be used in the label.
heading_pic = itk.PhotoImage(photo1)
# Added the Photo as a label at the top of the program.
photo_label = tk.Label(photo_frame, image=heading_pic, bg='dim gray')
photo_label.pack()

# Instruction text
dice_selection = tk.Label(text="Please select the die you will be rolling.", bg='dim gray', fg='orange')
dice_selection.pack(pady=20)

# This frame will hold the icon for dice
dice_icon_frame = tk.LabelFrame(window, padx=5, pady=5, borderwidth=0, highlightthickness=2, highlightbackground='black', highlightcolor='black')
dice_icon_frame.pack()

# Dice Start Here
# D4
d4_photo = img.open('DiceRollerV2/dice/d4-image.png').resize((70, 70), img.ANTIALIAS)
d4_photo_edited = itk.PhotoImage(d4_photo)
d4_photo_label = tk.Button(dice_icon_frame, image=d4_photo_edited, bg='dim gray', command=set_d4)
d4_photo_label.pack(side=LEFT)
#D6
d6_photo = img.open('DiceRollerV2/dice/d6-image.png').resize((70, 70), img.ANTIALIAS)
d6_photo_edited = itk.PhotoImage(d6_photo)
d6_photo_label = tk.Button(dice_icon_frame, image=d6_photo_edited, bg='dim gray', command=set_d6)
d6_photo_label.pack(side=LEFT)
#D8 
d8_photo = img.open('DiceRollerV2/dice/d8-image.png').resize((70, 70), img.ANTIALIAS)
d8_photo_edited = itk.PhotoImage(d8_photo)
d8_photo_label = tk.Button(dice_icon_frame, image=d8_photo_edited, bg='dim gray', command=set_d8)
d8_photo_label.pack(side=LEFT)
#D10
d10_photo = img.open('DiceRollerV2/dice/d10-image.png').resize((70, 70), img.ANTIALIAS)
d10_photo_edited = itk.PhotoImage(d10_photo)
d10_photo_label = tk.Button(dice_icon_frame, image=d10_photo_edited, bg='dim gray', command=set_d10)
d10_photo_label.pack(side=LEFT)
#D12
d12_photo = img.open('DiceRollerV2/dice/d12-image.png').resize((70, 70), img.ANTIALIAS)
d12_photo_edited = itk.PhotoImage(d12_photo)
d12_photo_label = tk.Button(dice_icon_frame, image=d12_photo_edited, bg='dim gray', command=set_d12)
d12_photo_label.pack(side=LEFT)
#D20
d20_photo = img.open('DiceRollerV2/dice/d20-image.png').resize((70, 70), img.ANTIALIAS)
d20_photo_edited = itk.PhotoImage(d20_photo)
d20_photo_label = tk.Button(dice_icon_frame, image=d20_photo_edited, bg='dim gray',  command=set_d20)
d20_photo_label.pack(side=LEFT)
#Dice End here

# Dice Input Frame
dice_input_frame = tk.LabelFrame(window, pady=5, bg='dim gray', borderwidth=0, 
    highlightthickness=2, highlightbackground='orange', highlightcolor='orange')
dice_input_frame.pack(pady=50)

# User input window text
user_input_text = tk.Label(dice_input_frame, text="Please Enter Your Dice Quantity Here", bg='dim grey', fg='orange')
user_input_text.pack(pady=5)

# User input window
user_input = tk.Entry(dice_input_frame, bg='snow', width=int(window_width/16))
user_input.pack(padx=10)

def calc_roll():
    global dice_total
    amt_of_dice = int(user_input.get())
    while(amt_of_dice != 0):
        if (die_type == 'd4'):
            dice_total += drf.four_sided_roll()
            amt_of_dice -= 1
        elif(die_type == 'd6'):
            dice_total += drf.six_sided_roll()
            amt_of_dice -= 1
        elif(die_type == 'd8'):
            dice_total += drf.eight_sided_roll()
            amt_of_dice -= 1
        elif(die_type == 'd10'):
            dice_total += drf.ten_sided_roll()
            amt_of_dice -= 1
        elif(die_type == 'd12'):
            dice_total += drf.twelve_sided_roll()
            amt_of_dice -= 1
        elif(die_type == 'd20'):
            dice_total += drf.twenty_sided_roll()
            amt_of_dice -= 1
        else:
            messagebox.showinfo("Error", "Invalid die chosen please start again")
            amt_of_dice = 0
    messagebox.showinfo("Total Roll", f'Your total roll is: {str(dice_total)}')
    dice_total = 0

# User Input btn to submit entry
# TODO Button will capture the input that is entered and use it in the programs logic.
user_input_btn = tk.Button(dice_input_frame, text="          Roll!          ", bg='snow', command=calc_roll)
user_input_btn.pack(pady=5)

# Close out the loop
window.mainloop()