import tkinter as tk
from tkinter.constants import LEFT
import PIL.ImageTk as itk
import PIL.Image as img

# Setting window dimension variables
window_height = 500
window_width = 600

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
d4_photo_label = tk.Button(dice_icon_frame, image=d4_photo_edited, bg='dim gray')
d4_photo_label.pack(side=LEFT)
#D6
d6_photo = img.open('DiceRollerV2/dice/d6-image.png').resize((70, 70), img.ANTIALIAS)
d6_photo_edited = itk.PhotoImage(d6_photo)
d6_photo_label = tk.Button(dice_icon_frame, image=d6_photo_edited, bg='dim gray')
d6_photo_label.pack(side=LEFT)
#D8 
d8_photo = img.open('DiceRollerV2/dice/d8-image.png').resize((70, 70), img.ANTIALIAS)
d8_photo_edited = itk.PhotoImage(d8_photo)
d8_photo_label = tk.Button(dice_icon_frame, image=d8_photo_edited, bg='dim gray')
d8_photo_label.pack(side=LEFT)
#D10
d10_photo = img.open('DiceRollerV2/dice/d10-image.png').resize((70, 70), img.ANTIALIAS)
d10_photo_edited = itk.PhotoImage(d10_photo)
d10_photo_label = tk.Button(dice_icon_frame, image=d10_photo_edited, bg='dim gray')
d10_photo_label.pack(side=LEFT)
#D12
d12_photo = img.open('DiceRollerV2/dice/d12-image.png').resize((70, 70), img.ANTIALIAS)
d12_photo_edited = itk.PhotoImage(d12_photo)
d12_photo_label = tk.Button(dice_icon_frame, image=d12_photo_edited, bg='dim gray')
d12_photo_label.pack(side=LEFT)
#D20
d20_photo = img.open('DiceRollerV2/dice/d20-image.png').resize((70, 70), img.ANTIALIAS)
d20_photo_edited = itk.PhotoImage(d20_photo)
d20_photo_label = tk.Button(dice_icon_frame, image=d20_photo_edited, bg='dim gray')
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

# User Input btn to submit entry
# TODO Button will capture the input that is entered and use it in the programs logic.
user_input_btn = tk.Button(dice_input_frame, text="          Roll!          ", bg='snow')
user_input_btn.pack(pady=5)

window.mainloop()