
import tkinter as tk
from tkinter.ttk import *
import operacje as op
from functools import partial
from sympy import *

#funkcje
def dodaj_obwod(i:int):
    global linie
    linie.append(tlo.create_line(0, i*100+80, 700, i*100+80, fill="blue"))
    global przyciski
    przyciski[i].config(text='-', command=partial(usun_obwod, i))
    przyciski.append(Button(okno, width=5, text="+", command=partial(dodaj_obwod, i+1)))
    przyciski[i+1].place(x=20, y=(i+1)*100+70)
    if i!=0:
        przyciski[i-1].config(state=tk.DISABLED)
    global paski
    paski.append(tk.Frame(okno, height=70, width=700, bg=""))
    paskowanie(i)
    paski[i].place(x=62, y=i*100+43)

def usun_obwod(i:int):
    global linie
    global tlo
    tlo.delete(linie[i])
    linie.pop(i)
    global przyciski
    przyciski[i+1].destroy()
    przyciski.pop(i+1)
    przyciski[i].config(text='+', command=partial(dodaj_obwod, i))
    if i!=0:
        przyciski[i-1].config(state=tk.NORMAL)
    global paski
    paski[i].destroy()
    paski.pop(i)
    global bramki
    del bramki[i]
    global obwod
    obwod.pop(i)
    global macierz
    macierz=op.skladanie(obwod)
    wypisanie()

def stawianie(opcja:str):
    global bramki
    for i in range(len(bramki)):
        for j in range(10):
            if type(bramki[i][j])==tk.Button:
                bramki[i][j].config(state=tk.NORMAL, command=partial(bramkowanie, opcja, i, j))

def paskowanie(i:int):
    global bramki
    bramki.append([])
    global paski
    for n in range(10):
        bramki[i].append(tk.Button(paski[i], bg='red', activebackground='red', relief=tk.FLAT, state=tk.DISABLED))
        bramki[i][n].place(x=n*70+30, rely=0.52, anchor="center", width=10, height=10)
    global obwod
    obwod.append([op.I for i in range(10)])
    global macierz
    macierz=op.skladanie(obwod)
    wypisanie()
    
def bramkowanie(opcja:str, i:int, n:int):
    global bramki
    bramki[i][n].destroy()
    bramki[i][n]=tk.Label(paski[i], text=opcja)
    bramki[i][n].place(x=n*70+30, rely=0.52, anchor="center", height=50, width=50)
    global obwod
    if opcja=='X':
        obwod[i][n]=op.X
    elif opcja=='Y':
        obwod[i][n]=op.Y
    elif opcja=='Z':
        obwod[i][n]=op.Z
    elif opcja=='H':
        obwod[i][n]=op.H
    elif opcja=='S':
        obwod[i][n]=op.S
    global macierz
    macierz=op.skladanie(obwod)
    wypisanie()

    
def wypisanie():
    global wynik
    global macierz
    wynik.delete("all")
    n=len(macierz)
    wynik.create_line(20, 10, 10, 10, 10, 60*n+10, 20, 60*n+10)
    wynik.create_line(60*n, 10, 60*n+10, 10, 60*n+10, 60*n+10, 60*n, 60*n+10)
    for i in range(len(macierz)):
        for j in range(len(macierz[i])):
            napis=str(macierz[i][j])
            wynik.create_text(60*j+40, 60*i+30, anchor='center', text=napis)
        

#main
if __name__=="__main__":
    okno=tk.Tk()
    okno.geometry("1200x600")
    okno.resizable(False, True)
    okno.title("Qbit")
    tlo=tk.Canvas(okno, width=700, height=700, bg="black")
    tlo.place(x=60, y=0)
    

    #przyciski
    przyciski=[]
    linie=[]
    przyciski.append(Button(okno, width=5, text="+", command=partial(dodaj_obwod, 0)))
    przyciski[0].place(x=20, y=70)

    #obwod
    bramki=[]
    paski=[]
    obwod=[]
    macierz=[[]]
    wynik=tk.Canvas(okno, height=500, width=430, bg='grey')
    wynik.place(x=770, y=30)
    wypisanie()


    #pasek narzedzi
    toolbar = Frame(okno, height=70)
    toolbar.pack(side=tk.BOTTOM)
    bramki=[]
    X=Button(toolbar, text='X', command=partial(stawianie, 'X'))
    Y=Button(toolbar, text='Y', command=partial(stawianie, 'Y'))
    Z=Button(toolbar, text='Z', command=partial(stawianie, 'Z'))
    S=Button(toolbar, text='S', command=partial(stawianie, 'S'))
    H=Button(toolbar, text='H', command=partial(stawianie, 'H'))
    X.pack(side = tk.LEFT, expand = True, fill = tk.BOTH)
    Y.pack(side = tk.LEFT, expand = True, fill = tk.BOTH)
    Z.pack(side = tk.LEFT, expand = True, fill = tk.BOTH)
    S.pack(side = tk.LEFT, expand = True, fill = tk.BOTH)
    H.pack(side = tk.LEFT, expand = True, fill = tk.BOTH)

    #petla glowna
    okno.mainloop()