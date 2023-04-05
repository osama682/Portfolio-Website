from tkinter import *

from PIL import ImageTk, Image
root = Tk()
root.geometry("350x200")
img = ImageTk.PhotoImage(Image.open("black car.jpg"))  
l=Label(image=img)
l.pack()

mainloop()
