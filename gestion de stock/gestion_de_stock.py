import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector
from tkinter import *
from playsound import playsound
from tkVideoPlayer import TkinterVideo

def GetValue(event):
    e1.delete(0, END)
    e2.delete(0, END)
    e3.delete(0, END)
    e4.delete(0, END)
    e5.delete(0, END)
    e6.delete(0, END)
    row_id = listBox.selection()[0]
    select = listBox.set(row_id)
    e1.insert(0, select['id'])
    e2.insert(0, select['nom'])
    e3.insert(0, select['description'])
    e4.insert(0, select['prix'])
    e5.insert(0, select['quantité'])
    e6.insert(0, select['id_catégorie'])


def Add():
    studid = e1.get()
    studname = e2.get()
    coursename = e3.get()
    feee = e4.get()
    price = e5.get()
    idcat = e6.get()

    mysqldb = mysql.connector.connect(host="localhost", user="root", password="laplateforme.io", database="boutique")
    mycursor = mysqldb.cursor()

    try:
        sql = "INSERT INTO  produit (id, nom,description,prix,quantité,id_catégorie) VALUES (%s, %s, %s, %s, %s, %s)"
        val = (studid, studname, coursename, feee, price, idcat)
        mycursor.execute(sql, val)
        mysqldb.commit()
        lastid = mycursor.lastrowid
        messagebox.showinfo("information", "Produit inséré avec succès ")
        e1.delete(0, END)
        e2.delete(0, END)
        e3.delete(0, END)
        e4.delete(0, END)
        e5.delete(0, END)
        e6.delete(0, END)
        e1.focus_set()
    except Exception as e:
        print(e)
        mysqldb.rollback()
        mysqldb.close()


def update():
    studid = e1.get()
    studname = e2.get()
    coursename = e3.get()
    feee = e4.get()
    price = e5.get()
    idcat = e6.get()
    mysqldb = mysql.connector.connect(host="localhost", user="root", password="laplateforme.io", database="boutique")
    mycursor = mysqldb.cursor()

    try:
        sql = "Update  produit set nom= %s,description= %s,prix= %s,quantité= %s,id_catégorie= %s where id= %s"
        val = (studname, coursename, feee, price, idcat, studid)
        mycursor.execute(sql, val)
        mysqldb.commit()
        lastid = mycursor.lastrowid
        messagebox.showinfo("information", "Produit modifié avec succès")

        e1.delete(0, END)
        e2.delete(0, END)
        e3.delete(0, END)
        e4.delete(0, END)
        e5.delete(0, END)
        e6.delete(0, END)
        e1.focus_set()

    except Exception as e:

        print(e)
        mysqldb.rollback()
        mysqldb.close()


def delete():
    studid = e1.get()

    mysqldb = mysql.connector.connect(host="localhost", user="root", password="laplateforme.io", database="boutique")
    mycursor = mysqldb.cursor()

    try:
        sql = "delete from produit where id = %s"
        val = (studid,)
        mycursor.execute(sql, val)
        mysqldb.commit()
        lastid = mycursor.lastrowid
        messagebox.showinfo("information", "Produit supprimé avec succès")

        e1.delete(0, END)
        e2.delete(0, END)
        e3.delete(0, END)
        e4.delete(0, END)
        e5.delete(0, END)
        e6.delete(0, END)
        e1.focus_set()

    except Exception as e:

        print(e)
        mysqldb.rollback()
        mysqldb.close()


def show():
    mysqldb = mysql.connector.connect(host="localhost", user="root", password="laplateforme.io", database="boutique")
    mycursor = mysqldb.cursor()
    mycursor.execute("SELECT id,nom,description,prix,quantité,id_catégorie FROM produit")
    records = mycursor.fetchall()
    print(records)

    for i, (id, nom, desc, prix, quant, catég) in enumerate(records, start=1):
        listBox.insert("", "end", values=(id, nom, desc, prix, quant, catég))
        mysqldb.close()

def play():
    playsound('test.mp3')

root = Tk()
root.geometry("1200x500")
root.title("Gestionnaire base de données Greg DEJOUX")

photo = PhotoImage(file='test.png')

global e1
global e2
global e3
global e4
global e5
global e6

tk.Label(root, text="Veuillez entrer les informations dans les champs à gauche", fg= "red", font=(None, 30)).place(x=350, y=5)
tk.Label(root, text="ID Catégorie : Cosmétique = 1, Alimentaire = 2, Vetements = 3", font=(None, 30)).place(x=350, y=420)


tk.Label(root, text="ID Produit").place(x=10, y=10)
Label(root, text="Nom produit").place(x=10, y=40)
Label(root, text="Description").place(x=10, y=70)
Label(root, text="Prix").place(x=10, y=100)
Label(root, text="Quantité").place(x=10, y=130)
Label(root, text="Id Catégorie").place(x=10, y=160)

e1 = Entry(root)
e1.place(x=140, y=10)

e2 = Entry(root)
e2.place(x=140, y=40)

e3 = Entry(root)
e3.place(x=140, y=70)

e4 = Entry(root)
e4.place(x=140, y=100)

e5 = Entry(root)
e5.place(x=140, y=130)

e6 = Entry(root)
e6.place(x=140, y=160)

Button(root, text="Ajouter", command=Add, height=3, width=13).place(x=350, y=130)
Button(root, text="Modifier", command=update, height=3, width=13).place(x=460, y=130)
Button(root, text="Supprimer", command=delete, height=3, width=13).place(x=570, y=130)
Button(root, image=photo, text="JulButton", command=play, height=100, width=100).place(x=1200, y=1)

cols = ('id', 'nom', 'description', 'prix', 'quantité', 'id_catégorie')
listBox = ttk.Treeview(root, columns=cols, show='headings')

for col in cols:
    listBox.heading(col, text=col)
    listBox.grid(row=1, column=0, columnspan=2)
    listBox.place(x=10, y=200)

show()
listBox.bind('<Double-Button-1>', GetValue)

root.mainloop()
