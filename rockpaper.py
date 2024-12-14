from tkinter import *
from PIL import Image , ImageTk
from random import  randint

window = Tk()
window.title("Game Rock Paper and  Scissor")
window.configure(background="black")

image_rocks1= ImageTk.PhotoImage(Image.open("rock1.png"))
image_paper1= ImageTk.PhotoImage(Image.open("paper1.png"))
image_scissor1= ImageTk.PhotoImage(Image.open("scissor1.png"))
image_rocks2= ImageTk.PhotoImage(Image.open("rock2.png"))
image_paper2= ImageTk.PhotoImage(Image.open("paper2.png"))
image_scissor2= ImageTk.PhotoImage(Image.open("scissor2.png"))


label_player = Label(window,image=image_scissor1)
label_computer = Label(window,image=image_scissor2)
label_computer.grid(row=1,column=0)
label_player.grid(row=1 , column=4)



 



button_rock = Button(window,width=16 , height=3 , text="ROCK", font=("arial",20,"bold"),bg='yellow',fg="red",).grid(row=2 , column=1)


button_paper = Button(window,width=16 , height=3 , text="PAPER", font=("arial",20,"bold"),bg='yellow',fg="red",).grid(row=2 , column=2)


button_scissor = Button(window,width=16 , height=3 , text="SCISSOR", font=("arial",20,"bold"),bg='yellow',fg="red",).grid(row=2 , column=3)



window.mainloop()