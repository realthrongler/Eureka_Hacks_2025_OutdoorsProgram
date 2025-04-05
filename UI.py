#Modules
import random
import tkinter
import datetime 
from tkinter import filedialog

#random number generators for item selection
first_item = random.randint(1,3)
second_item = random.randint(1,3)
third_item = random.randint(1,3)

#List of outdoor items
items = ["stop sign", "flower", "clouds"]

#drawing window with tkinter, some basic setup
root = tkinter.Tk()
root.title("Real life scavenger hunt")

def upload_image():
    file = filedialog.askopenfile(title="Please select a file.", filetypes=(("png files", "*.png"),("jpg files","*.jpg")))


#UI design
file_upload_button = tkinter.Button(root, text="Upload", padx="5", pady="3", command=upload_image)
file_upload_button.grid(row="1", column="2")

Label_one = tkinter.Label(root, text="Today's items:").grid(row="4", column="1")

#TODO Put 3 random items in the following text labels

LabelRandom1 = tkinter.Label(root, text="item one").grid(row="5", column="1")
LabelRandom2 = tkinter.Label(root, text="item two").grid(row="6",column="1")
LabelRandom3 = tkinter.Label(root, text="item three").grid(row="7", column="1")

#looping window to allow for user interaction
root.mainloop()
