from tkinter import *
def click(event):
    global scvalue
    text=event.widget.cget('text') # cget func-Return the resource value for a KEY given as string.
    if screen.get() == 'Error':
        scvalue.set('')
        screen.update()
    elif text=='=':
        if scvalue.get().isdigit():
            value=int(scvalue.get())
        else:
            try:
                value=eval(screen.get())  # eval function- returns the string value as operator
            except Exception as e:
                value='Error'
        scvalue.set(value)
        screen.update()  # updates the screen each time you change it
    elif text=='C':
        screen.delete(0,END)
    elif text=='AC':
        root.destroy()
    elif text=='<-':
        scvalue.set(scvalue.get()[:-1])
        screen.update()
    else:
        scvalue.set(scvalue.get()+text)
        screen.update()

root=Tk()
root.title('Calculator by Anuj')
root.geometry('500x480')
root.configure(background='black')
root.wm_iconbitmap('calc.ico')

scvalue = StringVar()
scvalue.set('')
screen=Entry(root,textvar=scvalue,font='timesnewroman 40 bold',bg='black',fg='white',borderwidth=0)
screen.pack(fill=X,ipadx=8,pady=10,padx=10)

buttons=[['C','<-','%','/'],
         ['7','8','9','*'],
         ['4','5','6','-'],
         ['1','2','3','+'],
         ['AC','0','.','=']]
for i in buttons:
    f = Frame(root,bg='black')
    f.pack()
    for j in i:
        b = Button(f, text=j, padx=24, pady=10, font='timesnewroman 15 bold', fg='white', bg='black',borderwidth=0)
        b.pack(side=LEFT, padx=20, pady=5)
        b.bind('<Button-1>',click)

root.mainloop()