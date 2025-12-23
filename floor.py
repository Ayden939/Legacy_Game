import tkinter as tk
from PIL import Image, ImageTk


root = tk.Tk()

root.title("Testing timeeeee")

root.geometry("500x300")

canvas = tk.Canvas(root, bg = "black")
canvas.pack(fill = "both", expand = True)

bg_id = canvas.create_image(0, 0, anchor="nw")

original = Image.open("images/dungeon.png")



def size(event):
    resized = original.resize((event.width, event.height))
    photo = ImageTk.PhotoImage(resized)
    canvas.itemconfig(bg_id, image=photo)
    canvas.bg_ref = photo


root.bind("<Configure>", size)





root.mainloop()