from itertools import count
from tkinter import*
from tkinter import messagebox
Logs=Tk()
Logs.title("TIC-TAC-TOE")
Logs.configure(bg="turquoise")

speletajsX=True
speletajsO=False
count=0

def btnClick(button):
    global speletajsX,count,speletajsO
    if button["text"]==""and speletajsX==True:
        button["text"]="X"
        speletajsX=False
        speletajsO=True
        count+=1
        Winner()
        
    elif button["text"]==""and speletajsX==False:
        button["text"]="O"
        speletajsX=True
        speletajsO=False
        count+=1
        Winner()

    else:
        messagebox.showerror("TIC-TAC-TOE","Lauciņš jau aizņemts!")

def disableButtons(): #spēle beidzas, pogas izslēgtas​
    btn1.config(state=DISABLED) #pogas stāvoklis izslēgts
    btn2.config(state=DISABLED)
    btn3.config(state=DISABLED)
    btn4.config(state=DISABLED)
    btn5.config(state=DISABLED)
    btn6.config(state=DISABLED)
    btn7.config(state=DISABLED)
    btn8.config(state=DISABLED)
    btn9.config(state=DISABLED)

def infoLogs():
        jaunsLogs=Toplevel()
        jaunsLogs.title('Info par programmu')
        jaunsLogs.geometry("500x300")
        apraksts=Label(jaunsLogs,text='Spēles noteikumi The game is played on a grid thats 3 squares by 3 squares.\n You are X, your friend (or the computer in this case) is O.\n The first player to get 3 of her marks in a row (up, down, across, or diagonally) is the winner.\n When all 9 squares are full, the game is over.')
        apraksts.grid(row=0,column=0)
        return 0

def reset():
    btn1.config(state=NORMAL)
    btn2.config(state=NORMAL)
    btn3.config(state=NORMAL)
    btn4.config(state=NORMAL)
    btn5.config(state=NORMAL)
    btn6.config(state=NORMAL)
    btn7.config(state=NORMAL)
    btn8.config(state=NORMAL)
    btn9.config(state=NORMAL)

    btn1["text"]=""
    btn2["text"]=""
    btn3["text"]=""
    btn4["text"]=""
    btn5["text"]=""
    btn6["text"]=""
    btn7["text"]=""
    btn8["text"]=""
    btn9["text"]=""

    global winner,count,speletajsX
    winner=False
    count=0
    speletajsX=True
    return 0

def Winner():
    global winner
    if (btn1["text"]=="X"and btn2["text"]=="X" and btn3["text"]=="X"
    or btn4["text"]=="X"and btn5["text"]=="X" and btn6["text"]=="X"
    or btn7["text"]=="X"and btn8["text"]=="X" and btn9["text"]=="X"
    or btn1["text"]=="X"and btn5["text"]=="X" and btn9["text"]=="X"
    or btn3["text"]=="X"and btn5["text"]=="X" and btn7["text"]=="X"
    or btn1["text"]=="X"and btn4["text"]=="X" and btn7["text"]=="X"
    or btn2["text"]=="X"and btn5["text"]=="X" and btn8["text"]=="X"
    or btn3["text"]=="X"and btn6["text"]=="X" and btn9["text"]=="X"):
        winner=True
        disableButtons()
        messagebox.showinfo("TIC-TAC-TOE","Uzvar X spēlētajs")
    elif (btn1["text"]=="O"and btn2["text"]=="O" and btn3["text"]=="O"
    or btn4["text"]=="O"and btn5["text"]=="O" and btn6["text"]=="O"
    or btn7["text"]=="O"and btn8["text"]=="O" and btn9["text"]=="O"
    or btn1["text"]=="O"and btn5["text"]=="O" and btn9["text"]=="O"
    or btn3["text"]=="O"and btn5["text"]=="O" and btn7["text"]=="O"
    or btn1["text"]=="O"and btn4["text"]=="O" and btn7["text"]=="O"
    or btn2["text"]=="O"and btn5["text"]=="O" and btn8["text"]=="O"
    or btn3["text"]=="O"and btn6["text"]=="O" and btn9["text"]=="O"):
        winner=True
        disableButtons()
        messagebox.showinfo("TIC-TAC-TOE","Uzvar O Spēlētājs")
    elif (count==9):
        messagebox.showinfo("TIC-TAC-TOE","Neizšķirts")
        disableButtons()


btn1=Button(Logs,text="",width=5,height=2,font=("Arial",24),fg="White",bg="turquoise",command=lambda:btnClick(btn1))
btn2=Button(Logs,text="",width=5,height=2,font=("Arial",24),fg="White",bg="turquoise",command=lambda:btnClick(btn2))
btn3=Button(Logs,text="",width=5,height=2,font=("Arial",24),fg="White",bg="turquoise",command=lambda:btnClick(btn3))
btn4=Button(Logs,text="",width=5,height=2,font=("Arial",24),fg="White",bg="turquoise",command=lambda:btnClick(btn4))
btn5=Button(Logs,text="",width=5,height=2,font=("Arial",24),fg="White",bg="turquoise",command=lambda:btnClick(btn5))
btn6=Button(Logs,text="",width=5,height=2,font=("Arial",24),fg="White",bg="turquoise",command=lambda:btnClick(btn6))
btn7=Button(Logs,text="",width=5,height=2,font=("Arial",24),fg="White",bg="turquoise",command=lambda:btnClick(btn7))
btn8=Button(Logs,text="",width=5,height=2,font=("Arial",24),fg="White",bg="turquoise",command=lambda:btnClick(btn8))
btn9=Button(Logs,text="",width=5,height=2,font=("Arial",24),fg="White",bg="turquoise",command=lambda:btnClick(btn9))

btn1.grid(row=0,column=0)
btn2.grid(row=0,column=1)
btn3.grid(row=0,column=2)

btn4.grid(row=1,column=0)
btn5.grid(row=1,column=1)
btn6.grid(row=1,column=2)

btn7.grid(row=2,column=0)
btn8.grid(row=2,column=1)
btn9.grid(row=2,column=2)

galvenaIzvelne=Menu(Logs)
Logs.config(menu=galvenaIzvelne)

opcijas=Menu(galvenaIzvelne,tearoff=False)
galvenaIzvelne.add_cascade(label="Opcijas", menu=opcijas)

opcijas.add_command(label="Jauna spēle",command=reset)
opcijas.add_command(label="Iziet",command=Logs.quit)

galvenaIzvelne.add_command(label="Par programmu",command=infoLogs)

Logs.mainloop()