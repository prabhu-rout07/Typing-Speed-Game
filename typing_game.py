import tkinter
import random

words=["alphabet", "orange","zippest","zoonomia","abettors","wrainstaff","xerodermia","woundingly","villanelle","python","acids","blog","belt","body","agian","trigonmetry",
       "hello","zero","agent","after","arial","alone","among","angle","apple","beach","grant","begin","basic","lexible","flexible","cleint","flask","monster"]
score = 0
timeleft = 30

def startGame(event):
    if timeleft == 30:
        countdown()
    nextColor()

def nextColor():
    global score
    global timeleft
    color =['red','orange','blue','green',"pink","maroon","lightblue","green","purple","black","yellow"]

    if timeleft > 0:
        
        e.focus_set()
        if e.get().lower() == words[0].lower():
            score = score+1

        e.delete(0,tkinter.END)
        random.shuffle(words)
        random.shuffle(color)
        label.config(text= str(words[0]), fg = str(color[1]))
        score_label.config(text="score: "+ str(score))

    if timeleft == 0:
        e.focus_set()
        label1.config(text="Time Over \n Your Score is "+ str(score))

    else:
        e.focus_set()
        label1.config(text="Hurry The Clock is Ticking")

def countdown():
    global timeleft
    color =['red','orange','blue','green',"pink","maroon","lightblue","green","purple","black","yellow"]
    random.shuffle(color)
    if timeleft > 0:
        timeleft -= 1
        time_label.config(text = "TimeLeft : "+ str(timeleft),font=('arial',17), fg=str(color[1]))
        time_label.after(1000 , countdown)
        

root = tkinter.Tk()
root.title("TYPING GAME")
root.geometry("700x500")
instructions= tkinter.Label(root, text ="<TYPING TEST GAME>" , font=('impact',25), fg="blue")
instructions.pack()

score_label = tkinter.Label(root,text="Press Enter to start", font=('impact',20), fg="red")
score_label.pack()

time_label = tkinter.Label(root, text="TimeLeft : " + str(timeleft), font=('arial',17), fg= "orange")
time_label.pack()

label = tkinter.Label(root, font=('Gill Sans',60))
label.pack()

e = tkinter.Entry(root, width=50,font=('algerian',17), fg="red", bg="pink")
root.bind('<Return>', startGame)
e.place(x= 200, y=230 ,width=300, height= 50)
e.focus_set()

label1 = tkinter.Label(root, font=('impact',20), fg="purple")
label1.place(x=210,y=300)
root.mainloop()
root
             




                     
        
