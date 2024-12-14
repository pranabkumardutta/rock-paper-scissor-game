
from tkinter import *
from PIL import Image , ImageTk
from random import  randint

window = Tk()
window.title("Game Rock Paper and  Scissor")
window.configure(background="black")
#images
image_rocks1 = ImageTk.PhotoImage(Image.open("rock1.png").resize((200, 196)))
image_paper1 = ImageTk.PhotoImage(Image.open("paper1.png").resize((200, 196)))
image_scissor1 = ImageTk.PhotoImage(Image.open("scissor1.png").resize((200, 196)))
image_rocks2 = ImageTk.PhotoImage(Image.open("rock2.png").resize((200, 196)))
image_paper2 = ImageTk.PhotoImage(Image.open("paper2.png").resize((200, 196)))
image_scissor2 = ImageTk.PhotoImage(Image.open("scissor2.png").resize((200, 196)))

#lable for the computer and player
label_player = Label(window,image=image_scissor2)
label_computer = Label(window,image=image_scissor1)
label_computer.grid(row=2,column=0)
label_player.grid(row=2, column=4)

#score card for computer and player
computer_score= Label(window,font=('arial',60,"bold"),
                      text="0",fg="red")
player_score = Label(window,font=('arial',60,"bold"),
                     text="0",fg="red")
computer_score.grid(row=2 , column=1)
player_score.grid(row=2 , column=3)

#indicator for comp and player
player_indicator = Label(window,font=("arial",40,"bold"),
                         text="PLAYER", bg="orange",fg="blue")

computer_indicator = Label(window,font=("arial",40,"bold"),
                         text="COMPUTER", bg="orange",fg="blue")
computer_indicator.grid(row=0 , column=1)
player_indicator.grid(row=0 , column=3)

#message for who win or who loss
final_message = Label(window,font=("arial",40,"bold"),bg="red",fg="white")
final_message.grid(row=3 ,column=2)

def msg_updation(a):
    final_message['text'] = a

def Computer_Update():
    final = int(score_computer['text'])
    final += 1
    score_computer["text"] = str(final)

def Player_Update():
    final = int(score_player['text'])
    final += 1
    score_player["text"] = str(final)

def winner_check(p,c):
    if p ==c:
        updateMessage("It's a tie ")
    elif p == "rock":
        if c == "paper":
            updateMessage("Computer Wins.")
            Computer_Update()
        else:
            updateMessage("player Wins.")
            Player_Update()

    elif p == "paper":
       if c == "scissor":
           updateMessage("Computer Wins")
           Computer_Update()
       else:
             updateMessage("player Wins.")
             Player_Update()
    elif p == "scissor":
        if  c == "rock":
            updateMessage("Computer Wins")
            Computer_Update()
        else:
            updateMessage("player Wins.")
            Player_Update()

    else:
        pass

#button
button_rock = Button(window,width=16 , height=3 , text="ROCK", font=("arial",20,"bold"),bg='yellow',fg="red",).grid(row=4 , column=1)
button_paper = Button(window,width=16 , height=3 , text="PAPER", font=("arial",20,"bold"),bg='yellow',fg="red",).grid(row=4 , column=2)
button_scissor = Button(window,width=16 , height=3 , text="SCISSOR", font=("arial",20,"bold"),bg='yellow',fg="red",).grid(row=4 , column=3)



window.mainloop()