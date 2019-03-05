import tkinter
import random
yourmove = ''
move = ["rock","paper","scissors"]
window = tkinter.Tk()
MyTitle = tkinter.Label(window, text="rockpaperscissors",font="Helvetica 16 bold")
MyTitle.pack()

def rock():
    AI = random.choice(move)
    print(AI)

    if AI == "rock":
        whowon = tkinter.Label(window, text="Draw",font="Helvetica 16 bold")
        AI = tkinter.Label(window, text=AI,font="Helvetica 16 bold")
        AI.pack()
        whowon.pack()
    if AI == "paper":
        whowon = tkinter.Label(window, text="You Lose!",font="Helvetica 16 bold")
        AI = tkinter.Label(window, text=AI,font="Helvetica 16 bold")
        AI.pack()
        whowon.pack()
    if AI == "scissors":
        AI = tkinter.Label(window, text=AI,font="Helvetica 16 bold")
        AI.pack()
        whowon = tkinter.Label(window, text="You Win!",font="Helvetica 16 bold")
        whowon.pack()

def paper():
    AI = random.choice(move)
    print(AI)

    if AI == "rock":
        whowon = tkinter.Label(window, text="You Win!",font="Helvetica 16 bold")
        AI = tkinter.Label(window, text=AI,font="Helvetica 16 bold")
        AI.pack()
        whowon.pack()
    if AI == "paper":
        whowon = tkinter.Label(window, text="Draw!",font="Helvetica 16 bold")
        AI = tkinter.Label(window, text=AI,font="Helvetica 16 bold")
        AI.pack()
        whowon.pack()
    if AI == "scissors":
        AI = tkinter.Label(window, text=AI,font="Helvetica 16 bold")
        AI.pack()
        whowon = tkinter.Label(window, text="You Lose!",font="Helvetica 16 bold")
        whowon.pack()


def scissors():
    AI = random.choice(move)
    print(AI)
    if AI == "rock":
        whowon = tkinter.Label(window, text="You Lose!",font="Helvetica 16 bold")
        AI = tkinter.Label(window, text=AI,font="Helvetica 16 bold")
        AI.pack()
        whowon.pack()
    if AI == "paper":
        whowon = tkinter.Label(window, text="You Win!",font="Helvetica 16 bold")
        AI = tkinter.Label(window, text=AI,font="Helvetica 16 bold")
        AI.pack()
        whowon.pack()
    if AI == "scissors":
        whowon = tkinter.Label(window, text="Draw!",font="Helvetica 16 bold")
        AI = tkinter.Label(window, text=AI,font="Helvetica 16 bold")
        AI.pack()
        whowon.pack()

rock = tkinter.Button(window, text="rock", command=rock)
rock.pack()

paper = tkinter.Button(window, text="paper", command=paper)
paper.pack()

scissors= tkinter.Button(window, text="scissors", command=scissors)
scissors.pack()

window.mainloop()

