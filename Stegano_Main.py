from tkinter import * # appel à tous les composants du module Tkinter
from tkinter import filedialog #appel à filedialog
import tkinter as tk #au lieu d'utiliser le mot tkinter on le remplace par tk
from PIL import Image, ImageTk #appel à Image et ImageTk
import os #appel à  os (fctions systeme)
from stegano import lsb #lsb du module stegano

root = Tk() ## création de la fenêtre principale
root.title("Steganographie Mini Projet Traitement d'image") # donner un titre à la fenetre
root.geometry("700x500+150+180")
#Modifie la taille de la fenêtre. s est une chaîne de caractères de type "wxh±x±y".
# w et h sont la largeur et la hauteur. x et y sont la position du coin supérieur haut à l’écran.
root.resizable(False, False) #Spécifie si la fenêtre peut changer de taille. w et h sont des booléens.
root.configure(bg="#2f4155") #couleur de l'arrière plan

def Aff_Image():
    global filename #variable globale sera utilisée dans d'autres fonctions
    filename = filedialog.askopenfilename(initialdir=os.getcwd(),
                                          title= 'selectionner une image',
                                          filetype=(("PNG","*.png"),
                                                    ("JPG","*.jpg"),
                                                    ("Tous","*.txt"))) # l'ecran qui s'affiche pour choisir une image
    IMG =Image.open(filename) # ouverture de l'image
    IMG =ImageTk.PhotoImage(IMG) #creation et affichage de l'image
    lbl.configure(image=IMG,width=250,height=250) # redimensionnement de l'image
    lbl.image =IMG #LSB = Least significant bit : remplace le dernier bit avec un bit du message secret

def cacher_Image():
    global secret # variable globale sera utilisée après dans d'autres fonction
    message = text1.get(1.0, END) # prendre ce que l'utilisateur a saisie
    secret = lsb.hide(str(filename), message) # cacher le message via la méthode LSB



def sauv():
    secret.save("hidden.png") # sauvegarder l'image sous le nom hidden.png


def Aff_Img():
    message_clair = lsb.reveal(filename) # trouver le message caché
    text1.delete(1.0,END)
    text1.insert(END,message_clair) #afficher le texte




#icone en haut
image_icon =PhotoImage(file="logo.png")
root.iconphoto(False,image_icon) ##icone de l'interface ( dans ce cas j'ai choisi celle de supmti

#logo :
logo = PhotoImage(file='logo2.png')
Label(root,image=logo,bg='#2f4155').place(x=10,y=0)
Label(root,text="SupMTI Traitement d'image", bg='#2d4155',fg='white',font='arial 25 bold').place(x=100, y=20)

# Frame N° 1
f = Frame(root,bd=3,bg='black', width=340,height=280,relief=GROOVE)
f.place(x=10,y=80)
lbl = Label(f,bg='black')
lbl.place(x=40,y=10)

#Frame N°2
f2 = Frame(root,bd=3,bg='white', width=340,height=280, relief=GROOVE)
f2.place(x = 350, y=80)
text1 =Text(f2, font="Rebote 20", bg='white',fg='black', relief=GROOVE, wrap=WORD)
text1.place(x=0,y=0, width=320,height=295)
scrollbar1 = Scrollbar(f2)
scrollbar1.place(x=320,y=0,height=300)
scrollbar1.configure(command=text1.yview)
text1.configure(yscrollcommand=scrollbar1.set)

#Frame N°3
f3=Frame(root,bg='gray',width=330,height=100,relief=GROOVE)
f3.place(x=10,y=370)
Button(f3, text='Ouvrir ', width=10,height=2,font='arial 14 bold', command=Aff_Image).place(x=20,y=30)
Button(f3, text='Sauvegarder ', width=10,height=2,font='arial 14 bold', command=sauv).place(x=180,y=30)

Label(f3, text='Image, Photo, Fichier',bg='#2f4155',fg='yellow').place(x=20,y=5)

#Frame N° 4
f4=Frame(root,bg='gray',width=330,height=100,relief=GROOVE)
f4.place(x=360,y=370)
Button(f4, text='cacher', width=10,height=2,font='arial 14 bold',command=cacher_Image).place(x=20,y=30)
Button(f4, text='afficher ', width=10,height=2,font='arial 14 bold', command=Aff_Img).place(x=180,y=30)

Label(f4, text='Image, Photo, Fichier',bg='#2f4155',fg='yellow').place(x=20,y=5)










root.mainloop()
