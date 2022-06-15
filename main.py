from tkinter import *
from time import strftime

taillepardefaut = {"taille":200}

def ajournerheure():
    heure = strftime('%H:%M:%S')
    display.config(text=heure)
    display.after(1000, ajournerheure)
    print("update")

def ajournerdate():
    date = strftime('%d du %m en 20%y')
    datedisplay.config(text=date)
    datedisplay.after(1000, ajournerdate)

def fermerfenetre():
    print("fenêtre fermée via le boutton")
    root.destroy()

def themeclair():
    root.configure(background="#CAD0DA")
    display.config(bg="#CAD0DA")
    display.config(fg="#2C323C")
    datedisplay.config(bg="#CAD0DA")
    datedisplay.config(fg="#2C323C")
    quitter.config(bg="#CAD0DA")
    quitter.config(fg="#2C323C")


def themefoncé():
    root.configure(background="#2C323C")
    display.config(bg="#2C323C")
    display.config(fg="#CAD0DA")
    datedisplay.config(fg="#CAD0DA")
    datedisplay.config(bg="#2C323C")
    quitter.config(fg="#CAD0DA")
    quitter.config(bg="#2C323C")

def changertaille():
    if taillepardefaut["taille"] == 200:
        taillepardefaut["taille"] = 300
        display.config(font=("Digital-7", 300))
        return
    else:
        if taillepardefaut["taille"] == 300:
            taillepardefaut["taille"] = 100
            display.config(font=("Digital-7", 100))
            return
        else:
            if taillepardefaut["taille"] == 100:
                taillepardefaut["taille"] = 200
                display.config(font=("Digital-7", 200))
                return




root = Tk()
root.geometry("1920x1080")
root.title("Horloge")
root.attributes('-fullscreen', False)
root.configure(background="#2C323C")
root.iconbitmap()
display = Label(root, text="Chargement...", font=("Digital-7", 250), anchor=CENTER,justify=CENTER,bg="#2C323C",fg="#CAD0DA",pady=200)
display.pack(expand=YES)

quitter = Button(root, text="Quitter", command= fermerfenetre, font=("Umpush",10),relief=SUNKEN,bd=0,bg="#2C323C",width=30,highlightthickness=0,activebackground="#CC0000")
quitter.pack(side=LEFT)

boutclair = Button(root,text="Jedi", command= themeclair, font=("Umpush",10),relief=GROOVE,bd=0,bg="#CAD0DA",fg="#2E3B51",width=10,highlightthickness=0,activebackground="#576376")
boutclair.pack(side=RIGHT)
boutfoncé = Button(root,text="Sith", command= themefoncé, font=("Umpush",10),relief=GROOVE,bd=0,bg="#2C323C",fg="#CAD0DA",width=10,highlightthickness=0,activebackground="#576376")
boutfoncé.pack(side=RIGHT)

boutsize = Button(root,text="Taille", command= changertaille, font=("Umpush",10),relief=GROOVE,bd=0,bg="#2C323C",fg="#CAD0DA",width=10,highlightthickness=0,activebackground="#576376")
boutsize.pack(side=RIGHT)


datedisplay = Label (root, text="Chargement...", font=("Uroob", 20), anchor=CENTER,justify=CENTER,bg="#2C323C",fg="#CAD0DA")
datedisplay.pack(side=TOP)

ajournerheure()
ajournerdate()
root.mainloop()
