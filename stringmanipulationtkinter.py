#Left to do:
#make grids ie: organise buttons and input fields
#extra: add MEMES LEL
from tkinter import *
from PIL import Image, ImageTk
import tkinter
from functools import partial  ##our saviour @nan
window = tkinter.Tk()

window.geometry('300x450')  #here
load = Image.open("cat.gif")
render = ImageTk.PhotoImage(load)

img = Label(image=render)
img.image = render
img.place(x=20, y=288)
#YYAAAAASSSSSSS HAHAHAHHAHA

inputstring = tkinter.StringVar(
)  ##this is why it kept screwing up, use StringVar no matter what kind of variable
inputlen = tkinter.StringVar()
inputstart = tkinter.StringVar()


##functions
def LEFT(inputstring, inputlen):
    updatetext(inputstring.get()[0:int(inputlen.get())])
    return None


def RIGHT(inputstring, inputlen):
    # Returns the right most characters of a string
    updatetext(inputstring.get()[int(inputlen.get()):len(inputstring.get())])
    return None


def MID(inputstring, inputstart, inputlen):
    updatetext(inputstring.get()[int(inputstart.get()):int(inputstart.get()) +
                                 int(inputlen.get())])


def LENGTH(inputstring):
    updatetext(len(inputstring.get()))


def LCASE(inputstring):
    updatetext(inputstring.get().lower())


def UCASE(inputstring):
    updatetext(inputstring.get().upper())


def NUMTOSTRING(inputstring):
    updatetext(str(inputstring.get()))


def STRINGTONUM(inputstring):
    try:
        updatetext(int(inputstring.get()))
    except:
        updatetext("invalid")


def CONVTOINT(inputstring):
    try:
        updatetext(int(inputstring.get()))
    except:
        updatetext("invalid")


def CONVTOASC(inputstring):
    inputstr = inputstring.get()
    x = ""
    for i in inputstr:
        x = x + str(ord(i)) + " "
    updatetext(x)


def updatetext(x):
    print(x)
    outputlabel.config(text=x)
#tkinter.Label(window, #text=displaytext,font="Helvetica 16 bold").pack()


##GUI
##string entry and input length
tkinter.Label(
    window, text="string:", font="Helvetica 16 bold").grid(
        row=0, column=0)
strentry = tkinter.Entry(
    window, textvariable=inputstring, font='calibre 10').grid(
        row=0, column=1)

tkinter.Label(
    window, text="length:", font="Helvetica 16 bold").grid(
        row=1, column=0)
lenentry = tkinter.Entry(
    window, textvariable=inputlen, font='calibre 10').grid(
        row=1, column=1)

tkinter.Label(
    window, text="from start:", font="Helvetica 16 bold").grid(
        row=2, column=0)
startentry = tkinter.Entry(
    window, textvariable=inputstart, font='calibre 10').grid(
        row=2, column=1)

##used to call the variables, put variable names inside too
callleft = partial(LEFT, inputstring,
                   inputlen)  ##partial function to get inputs
callright = partial(RIGHT, inputstring, inputlen)
callmid = partial(MID, inputstring, inputlen, inputstart)
calllen = partial(LENGTH, inputstring)
calllcase = partial(LCASE, inputstring)
callucase = partial(UCASE, inputstring)
callnum_to_string = partial(NUMTOSTRING, inputstring)
callstring_to_num = partial(STRINGTONUM, inputstring)
callint = partial(CONVTOINT, inputstring)
callasc = partial(CONVTOASC, inputstring)

##buttons
#left
leftbutt = tkinter.Button(
    window, text="LEFT", bg='#ff0000', command=callleft).grid(
        row=3, column=0)  ##uses call ^^
#right
rightbutt = tkinter.Button(
    window, text="RIGHT", bg='#ffa500', command=callright).grid(
        row=4, column=0)
#mid
midbutt = tkinter.Button(
    window, text="MID", bg='#ffff00', command=callmid).grid(
        row=5, column=0)
#length
lenbutt = tkinter.Button(
    window, text="LEN", bg='#008000', command=calllen).grid(
        row=6, column=0)
#lcase
lcasebutt = tkinter.Button(
    window, text="LCASE", bg='#0000ff', command=calllcase).grid(
        row=7, column=0)
#UCASE
ucasebutt = tkinter.Button(
    window, text="UCASE", bg='#800080', command=callucase).grid(
        row=3, column=1)
#num to string
num_to_stringbutt = tkinter.Button(
    window, text="NUM_TO_STRING", bg='#da70d6',
    command=callnum_to_string).grid(
        row=4, column=1)
#STRING_TO_NUM
string_to_numbutt = tkinter.Button(
    window, text="STRING_TO_NUM", bg='#ff69b4',
    command=callstring_to_num).grid(
        row=5, column=1)
#int
intbutt = tkinter.Button(
    window, text="INT", bg='#a52a2a', command=callint).grid(
        row=6, column=1)
#ascii
ascbutt = tkinter.Button(
    window, text="ASC", bg='#fffff0', command=callasc).grid(
        row=7, column=1)
#yo you need to make the partial funcitons (line 57) yea after i do these buttons
#display text code here
tkinter.Label(
    window, text="Answer:", font="Helvetica 16 bold").grid(row=9, column=0)
displaytext = tkinter.StringVar()
outputlabel = tkinter.Label(window, text=displaytext, font="Helvetica 16 bold")
outputlabel.config(text="")
outputlabel.grid(row=9, column=1)

window.mainloop()
