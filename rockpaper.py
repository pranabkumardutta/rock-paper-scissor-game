from tkinter import *
from PIL import Image , ImageTk
from random import  randint

window = Tk()
window.title("Game Rock Paper and  Scissor")
window.configure(background="black")

button_rock = Button(window,width=16 , height=3 , text="ROCK", font=("arial",20,"bold"),bg='yellow',fg="red",).grid(row=2 , column=1)


button_paper = Button(window,width=16 , height=3 , text="PAPER", font=("arial",20,"bold"),bg='yellow',fg="red",).grid(row=2 , column=2)


button_scissor = Button(window,width=16 , height=3 , text="SCISSOR", font=("arial",20,"bold"),bg='yellow',fg="red",).grid(row=2 , column=3)



window.mainloop()