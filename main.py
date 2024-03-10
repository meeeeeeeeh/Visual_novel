import tkinter as tk
from PIL import Image, ImageTk

window = tk.Tk()
window.title("Visual novel")
window.geometry("500x500")

def act1():
  label1.pack_forget()
  but1.pack_forget()
  but2.pack_forget()
  canvas.itemconfig(container, image=image2)
  label2.pack()
  but5.pack()
  but6.pack()

def act2():
  label1.pack_forget()
  but1.pack_forget()
  but2.pack_forget()
  canvas.itemconfig(container, image=image3)
  label3.pack()
  but3.pack()
  but4.pack()

def badEnd():
  label2.pack_forget()
  label3.pack_forget()
  but3.pack_forget()
  but4.pack_forget()
  but5.pack_forget()
  but6.pack_forget()
  canvas.itemconfig(container, image=image4)
  label4.pack()
  but7.pack()

def goodEnd():
  label2.pack_forget()
  label3.pack_forget()
  but3.pack_forget()
  but4.pack_forget()
  but5.pack_forget()
  but6.pack_forget()
  canvas.itemconfig(container, image=image5)
  label5.pack()
  but7.pack()

def restart():
  label5.pack_forget()
  label4.pack_forget()
  but7.pack_forget()
  canvas.itemconfig(container, image=image)
  label1.pack()
  but1.pack()
  but2.pack()
  
canvas = tk.Canvas(window, width = 500, height = 400)
canvas.pack()

image = ImageTk.PhotoImage(Image.open("pictures/sticker1.webp"))
image2 = ImageTk.PhotoImage(Image.open("pictures/sticker4.webp"))
image3 = ImageTk.PhotoImage(Image.open("pictures/sticker5.webp"))
image4 = ImageTk.PhotoImage(Image.open("pictures/sticker3.webp"))
image5 = ImageTk.PhotoImage(Image.open("pictures/sticker2.webp"))

container = canvas.create_image(250,200,image=image)

label1 = tk.Label(text="You feel lost and lonely. What would you do? ")
label1.pack()
label2 = tk.Label(text="You see a pretty woman in this bar. What will you say?")
label3 = tk.Label(text="You decided to stay at home but you still feel really lonely.\nWill you ask a friend to join you?")
label4 = tk.Label(text="You're crying alone in bed.")
label5 = tk.Label(text="It was a good evening.\nYou've watched a comedy and gossiped about your exes")


but1 = tk.Button(text="Go to a bar.", command = act1)
but1.pack()
but2 = tk.Button(text="Stay at home and watch a film.", command = act2)
but2.pack()
but3 = tk.Button(text="No. I don't have friends and noone loves me.", command = badEnd)
but4 = tk.Button(text="Yea it will be fun.", command = goodEnd)
but5 = tk.Button(text="Hi. Let's get married?", command = badEnd)
but6 = tk.Button(text="Hi. Let's drink together and then get married?", command = badEnd)
but7 = tk.Button(text="Restart", command = restart)

tk.mainloop()