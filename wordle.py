import random
from tkinter import *

f=open(r'./wordle.txt','r')
word=f.readlines()[random.randint(0,5756)][:-1]
f.close()

root=Tk()
root.title('Wordle')
root.config(bg='#121214')

grp=[['A1','A2','A3','A4','A5'],
     ['B1','B2','B3','B4','B5'],
     ['C1','C2','C3','C4','C5'],
     ['D1','D2','D3','D4','D5'],
     ['E1','E2','E3','E4','E5'],
     ['F1','F2','F3','F4','F5']]

blank=PhotoImage(file=r'./blank.png')
green=PhotoImage(file=r'./green.png')
yellow=PhotoImage(file=r'./yellow.png')

for i in range(6):
    for j in range(5):
            grp[i][j]=Label(root,image=blank,borderwidth=0)
            grp[i][j].grid(row=i,column=j)

row=0
col=0
word_list=[]
flag,end=True,False
def game(event):
    global row,col,grp,word_list,flag,end
    key_pressed=event.keysym
    if key_pressed in 'qwertyuiopasdfghjklzxcvbnm' and col<6:
        L=grp[row][col]
        t=str(key_pressed.upper())
        L.configure(text=t,fg='#d2d5d6',image=blank,compound='center',font=('Helvatical bold',40),padx=0,pady=0)
        col+=1
        word_list+=[key_pressed]
    if key_pressed == 'BackSpace' and col>0:
        col-=1
        L=grp[row][col]
        t=str(key_pressed.upper())
        L.configure(text='',fg='#d2d5d6',image=blank)
        word_list.pop(-1)
    if key_pressed=='Return' and col==5:
        row+=1
        col=0
        flag=False
        l1=list(word)
        for j in range(5):
            if word[j]==word_list[j]:
                l1.remove(word_list[j])
                word_list[j]=word_list[j].upper()
                L=grp[row-1][j]
                L.configure(image=green)
        for k in range(5):
           if word_list[k] in l1:
                l1.remove(word_list[k])
                L=grp[row-1][k]
                L.configure(image=yellow)
        s=''
        for h in word_list:
            s+=h
        if s.lower()==word:
            print("You win -",word)
            flag=True
            end=True
        word_list=[]
    if not flag and row==6:
        print("You lose -",word)
        end=True
c=True
while c==True:
    if not end:
        root.bind('<Key>', game)
        root.update()
    if end:
        root.after(2000)
        root.destroy()
        c=False
