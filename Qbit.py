
import tkinter as tk
from tkinter.ttk import *
import operacje as op
from functools import partial
# from sympy import *
from cmath import sqrt
from math import log2

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
    if len(paski)>1:
        global paski_splatujace
        paski_splatujace.append(tk.Frame(okno, height=70, width=700, bg=""))
        paskowanie_splatujace(i-1)
        paski_splatujace[i-1].place(x=62, y=i*100-10)

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
    if i>0:
        global paski_splatujace
        paski_splatujace[i-1].destroy()
        paski_splatujace.pop(i-1)
        global bramki_splatujace
        del bramki_splatujace[i-1]
    global obwod
    obwod.pop(i)
    if i!=0:
        for n in range(len(obwod[i-1])):
            if len(obwod[i-1][n])==4:
                obwod[i-1][n]=op.I
    global macierz
    macierz=op.skladanie(obwod)
    wypisanie()
    
def stawianie(opcja:str):
    global bramki
    global obwod
    for i in range(len(bramki)):
        for j in range(10):
            if type(bramki[i][j])==tk.Button:
                bramki[i][j].config(state=tk.NORMAL, command=partial(bramkowanie, opcja, i, j))

def stawianie_splatujace(opcja:str):
    global obwod
    global bramki_splatujace
    for i in range(len(bramki_splatujace)):
        for j in range(5):
            if type(bramki_splatujace[i][j])==tk.Button:
                if obwod[i][2*j]==op.I and obwod[i+1][2*j]==op.I and obwod[i][2*j+1]==op.I and obwod[i+1][2*j+1]==op.I:
                    bramki_splatujace[i][j].config(state=tk.NORMAL, command=partial(bramkowanie_splatujace, opcja, i, j))

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
    
def paskowanie_splatujace(i:int):
    global bramki_splatujace
    bramki_splatujace.append([])
    global paski_splatujace
    for n in range(5):
        bramki_splatujace[i].append(tk.Button(paski_splatujace[i], bg='orange', activebackground='orange', relief=tk.FLAT, state=tk.DISABLED))
        bramki_splatujace[i][n].place(x=n*140+30, rely=0.52, anchor="center", width=10, height=10)

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
    elif opcja=='SX':
        obwod[i][n]=op.SX
    elif opcja=='Rx':
        obwod[i][n]=op.Rx
    elif opcja=='Ry':
        obwod[i][n]=op.Ry
    elif opcja=='Rz':
        obwod[i][n]=op.Rz
    global macierz
    macierz=op.skladanie(obwod)
    wypisanie()

def bramkowanie_splatujace(opcja:str, i:int, n:int):
    global bramki_splatujace
    bramki_splatujace[i][n].destroy()
    bramki_splatujace[i][n]=tk.Label(paski_splatujace[i], text=opcja)
    bramki_splatujace[i][n].place(x=n*140+68, rely=0.52, anchor="center", height=40, width=100)
    global obwod
    if opcja=='pSWAP':
        obwod[i][2*n]=op.pSWAP
    elif opcja=='SWAP':
        obwod[i][2*n]=op.SWAP
    elif opcja=='iSWAP':
        obwod[i][2*n]=op.iSWAP
    elif opcja=='CNOT':
        obwod[i][2*n]=op.CNOT
    elif opcja=='rCNOT':
        obwod[i][2*n]=op.rCNOT
    elif opcja=='Rxx':
        obwod[i][2*n]=op.Rxx
    elif opcja=='Ryy':
        obwod[i][2*n]=op.Ryy
    elif opcja=='Rzz':
        obwod[i][2*n]=op.Rzz
    obwod[i][2*n+1]=op.pSWAP2
    obwod[i+1][2*n]=op.pSWAP2
    obwod[i+1][2*n+1]=op.pSWAP2
    global macierz
    macierz=op.skladanie(obwod)
    wypisanie()
    
def wypisanie():
    global wynik
    global macierz
    wynik.delete("all")
    n=len(macierz)
    wynik.create_line(20, 10, 10, 10, 10, 40*n+10, 20, 40*n+10)
    wynik.create_line(40*n, 10, 40*n+10, 10, 40*n+10, 40*n+10, 40*n, 40*n+10)
    for i in range(len(macierz)):
        for j in range(len(macierz[i])):
            # napis=str(macierz[i][j])
            #
            if abs(macierz[i][j])==0:
                napis="-"
            else:
                # napis="".join(['0' for n in range(len(macierz)-i)])
                # napis=napis[:-1]
                # napis='{0:b}'.format(i)
                napis=str(macierz[i][j])
            #
            wynik.create_text(40*j+40, 40*i+30, anchor='center', text=napis)
        wektor='|'
        # a=['0' for n in range(int(log2(len(macierz))))]
        # if i%2==1:
        #     a[i]='1'
        a=str('{0:b}'.format(i))
        b=int(log2(len(macierz)))-len(a)
        if b!=0:
            c=['0' for n in range(b)]
            wektor+=''.join(c)
        wektor+=a
        wektor+='>'
        wynik.create_text(40*len(macierz)+40, 40*i+30, anchor='center', text=wektor)
        

#main
if __name__=="__main__":
    okno=tk.Tk()
    okno.geometry("1500x600")
    okno.resizable(True, True)
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
    bramki_splatujace=[]
    paski=[]
    paski_splatujace=[]
    obwod=[]
    macierz=[[]]
    wynik=tk.Canvas(okno, height=1000, width=1000, bg='grey')
    wynik.place(x=770, y=0)
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
    SX=Button(toolbar, text='SX', command=partial(stawianie, 'SX'))
    Rx=Button(toolbar, text='Rx', command=partial(stawianie, 'Rx'))
    Ry=Button(toolbar, text='Ry', command=partial(stawianie, 'Ry'))
    Rz=Button(toolbar, text='Rz', command=partial(stawianie, 'Rz'))
    X.pack(side = tk.LEFT, expand = True, fill = tk.BOTH)
    Y.pack(side = tk.LEFT, expand = True, fill = tk.BOTH)
    Z.pack(side = tk.LEFT, expand = True, fill = tk.BOTH)
    S.pack(side = tk.LEFT, expand = True, fill = tk.BOTH)
    H.pack(side = tk.LEFT, expand = True, fill = tk.BOTH)
    SX.pack(side = tk.LEFT, expand = True, fill = tk.BOTH)
    Rx.pack(side = tk.LEFT, expand = True, fill = tk.BOTH)
    Ry.pack(side = tk.LEFT, expand = True, fill = tk.BOTH)
    Rz.pack(side = tk.LEFT, expand = True, fill = tk.BOTH)
    pSWAP=Button(toolbar, text='sqrt(SWAP)', command=partial(stawianie_splatujace, 'pSWAP'))
    pSWAP.pack(side = tk.LEFT, expand = True, fill = tk.BOTH)
    SWAP=Button(toolbar, text='SWAP', command=partial(stawianie_splatujace, 'SWAP'))
    SWAP.pack(side = tk.LEFT, expand = True, fill = tk.BOTH)
    iSWAP=Button(toolbar, text='iSWAP', command=partial(stawianie_splatujace, 'iSWAP'))
    iSWAP.pack(side = tk.LEFT, expand = True, fill = tk.BOTH)
    CNOT=Button(toolbar, text='CNOT', command=partial(stawianie_splatujace, 'CNOT'))
    CNOT.pack(side = tk.LEFT, expand = True, fill = tk.BOTH)
    rCNOT=Button(toolbar, text='rCNOT', command=partial(stawianie_splatujace, 'rCNOT'))
    rCNOT.pack(side = tk.LEFT, expand = True, fill = tk.BOTH)
    # Rxx=Button(toolbar, text='Rxx', command=partial(stawianie_splatujace, 'Rxx'))
    # Rxx.pack(side = tk.LEFT, expand = True, fill = tk.BOTH)
    # Ryy=Button(toolbar, text='Ryy', command=partial(stawianie_splatujace, 'Ryy'))
    # Ryy.pack(side = tk.LEFT, expand = True, fill = tk.BOTH)
    # Rzz=Button(toolbar, text='Rzz', command=partial(stawianie_splatujace, 'Rzz'))
    # Rzz.pack(side = tk.LEFT, expand = True, fill = tk.BOTH)

    #petla glowna
    okno.mainloop()