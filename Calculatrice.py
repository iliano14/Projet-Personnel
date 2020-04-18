# Projet personnel ;
# Import des module :
from tkinter import *
from functools import partial

# Fenêtre :
window = Tk()

# Réglages de la fenetre :
window.title("Calculatrice (PP)")
window.geometry("400x460")
window.iconbitmap("calculator.ico")
window.minsize(400,460)
window.maxsize(400,460)
window.config(background = "black")

# Centrer la fenêtre :
w = 400
h = 460
ws = window.winfo_screenwidth()
hs = window.winfo_screenheight()
x = (ws/2) - (w/2)
y = (hs/2) - (h/2)
window.geometry('%dx%d+%d+%d' % (w, h, x, y))
#-----------------------------------------------------------------------------------------------------------------------
# Définir les fonctions:
# Ajouter un nombre
def ins(x) :
    box.insert("end",x)
# Point
def point():
    box.insert("end",".")
# Opérations
def opp(x):
    global o
    global num
    num = float(box.get())
    box.delete(0,"end")
    o = x
# Égal
def equ():
    nume = float(box.get())
    if o == "a":
        rep = num + nume
    elif o == "s":
        rep = num - nume
    elif o == "m":
        rep = num * nume
    else:
        rep = num / nume
    box.delete(0,"end")
    box.insert("end",rep)
#-----------------------------------------------------------------------------------------------------------------------
# Input
box = Entry(window, font = ("Arial", 25))
box.pack(pady = 10)

# Bouton 7
button7 = Button(window, text=" 7 ", font=("Arial", 30), bg="black", fg="white",activebackground ="white",activeforeground = "black", command=partial(ins,7))
button7.place(x = 7, y = 70)

# Bouton 8
button8 = Button(window, text=" 8 ", font=("Arial", 30), bg="black", fg="white",activebackground ="white",activeforeground = "black", command=partial(ins,8))
button8.place(x = 107, y = 70)

# Bouton 9
button9 = Button(window, text=" 9 ", font=("Arial", 30), bg="black", fg="white",activebackground ="white",activeforeground = "black", command=partial(ins,9))
button9.place(x = 207, y = 70)

# Bouton /
buttond = Button(window, text="  /  ", font=("Arial", 30), bg="black", fg="white",activebackground ="white",activeforeground = "black", command=partial(opp,"d"))
buttond.place(x = 307, y = 70)

# Bouton 4
button4 = Button(window, text=" 4 ", font=("Arial", 30), bg="black", fg="white",activebackground ="white",activeforeground = "black", command=partial(ins,4))
button4.place(x = 7, y = 170)

# Bouton 5
button5 = Button(window, text=" 5 ", font=("Arial", 30), bg="black", fg="white",activebackground ="white",activeforeground = "black", command=partial(ins,5))
button5.place(x = 107, y = 170)

# Bouton 6
button6 = Button(window, text=" 6 ", font=("Arial", 30), bg="black", fg="white",activebackground ="white",activeforeground = "black", command=partial(ins,6))
button6.place(x = 207, y = 170)

# Bouton X
buttonm = Button(window, text=" X ", font=("Arial", 30), bg="black", fg="white",activebackground ="white",activeforeground = "black", command=partial(opp,"m"))
buttonm.place(x = 307, y = 170)

# Bouton 1
button1 = Button(window, text=" 1 ", font=("Arial", 30), bg="black", fg="white",activebackground ="white",activeforeground = "black", command=partial(ins,1))
button1.place(x = 7, y = 270)

# Bouton 2
button2 = Button(window, text=" 2 ", font=("Arial", 30), bg="black", fg="white",activebackground ="white",activeforeground = "black", command=partial(ins,2))
button2.place(x = 107, y = 270)

# Bouton 3
button3 = Button(window, text=" 3 ", font=("Arial", 30), bg="black", fg="white",activebackground ="white",activeforeground = "black", command=partial(ins,3))
button3.place(x = 207, y = 270)

# Bouton -
buttons = Button(window, text="  -  ", font=("Arial", 30), bg="black", fg="white",activebackground ="white",activeforeground = "black", command=partial(opp,"s"))
buttons.place(x = 307, y = 270)

# Bouton .
buttonp = Button(window, text="  .  ", font=("Arial", 30), bg="black", fg="white",activebackground ="white",activeforeground = "black", command=point)
buttonp.place(x = 7, y = 370)

# Bouton 0
button0 = Button(window, text=" 0 ", font=("Arial", 30), bg="black", fg="white",activebackground ="white",activeforeground = "black", command=partial(ins,0))
button0.place(x = 107, y = 370)

# Bouton +
buttona = Button(window, text=" + ", font=("Arial", 30), bg="black", fg="white",activebackground ="white",activeforeground = "black", command=partial(opp,"a"))
buttona.place(x = 307, y = 370)

# Bouton =
buttone = Button(window, text=" = ", font=("Arial", 30), bg="black", fg="white",activebackground ="white",activeforeground = "black", command=equ)
buttone.place(x = 207, y = 370)
#-----------------------------------------------------------------------------------------------------------------------
# Fin
window.mainloop()