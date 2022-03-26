import numpy as np
import pandas as pd
from tkinter import *

root = Tk()
root.title("Film & Dizi Öneri Sistemi")
root.geometry("700x300+500+200")
root.resizable(width=False, height=False)
backgroundColor = Label(bg="#2F4F4F", width=700, height=500)
backgroundColor.place(x=0, y=0)
root.iconbitmap("popcorn.ico")

filmler = pd.read_csv("filmler.csv")
filmlerDf = pd.DataFrame(filmler)

#Fonksiyonlar

def Aksiyonlar():
    film1 = np.random.randint(1,283907)
    sonuc1 = filmlerDf["title"][film1] + " " + str(filmlerDf["genre"][film1])

    film2 = np.random.randint(1,283907)
    sonuc2 = filmlerDf["title"][film2] + " " + str(filmlerDf["genre"][film2])

    film3 = np.random.randint(1,283907)
    sonuc3 = filmlerDf["title"][film3] + " " + str(filmlerDf["genre"][film3])

    film4 = np.random.randint(1,283907)
    sonuc4 = filmlerDf["title"][film4] + " " + str(filmlerDf["genre"][film4])

    film5 = np.random.randint(1,283907)
    sonuc5 = filmlerDf["title"][film5] + " " + str(filmlerDf["genre"][film5])

    Label1["text"]="Sonuç 1 : "+sonuc1
    Label2["text"]="Sonuç 2 : "+sonuc2
    Label3["text"]="Sonuç 3 : "+sonuc3
    Label4["text"]="Sonuç 4 : "+sonuc4
    Label5["text"]="Sonuç 5 : "+sonuc5



aksiyonButon = Button(text="Film & Dizi Öner", font="Bold", command=Aksiyonlar)
aksiyonButon.place(x=150, y=12)

Label1 = Label(text="FazzTech", font="Arial 20", bg="#2F4F4F", fg="white")
Label1.place(x=10, y=12)

Label1 = Label(text="Sonuç 1 : ", font="24", bg="#2F4F4F", fg="white")
Label1.place(x=10, y=50+20)

Label2 = Label(text="Sonuç 2 : ", font="24", bg="#2F4F4F")
Label2.place(x=10, y=75+30)

Label3 = Label(text="Sonuç 3 : ", font="24", bg="#2F4F4F", fg="white")
Label3.place(x=10, y=100+40)

Label4 = Label(text="Sonuç 4 : ", font="24", bg="#2F4F4F")
Label4.place(x=10, y=125+50)

Label5 = Label(text="Sonuç 5 : ", font="24", bg="#2F4F4F", fg="white")
Label5.place(x=10, y=150+60)






root.mainloop()