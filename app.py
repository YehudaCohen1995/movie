import json
import tkinter as tk
from tkinter import *
import test

with open('moviedata.json') as name:
    data = json.load(name)
root = tk.Tk()


def deletes_movie(delete):
     del one


def delete_button(x_index):  # dateles button
    delete_movie = tk.Button(root, text="delete", command=deletes_movie)
    delete_movie.pack()
    delete_movie.place(height=20, width=50, x=500, y=x_index)


canvas = tk.Canvas(root, height=600, width=600, bg="#263D42")
canvas.pack()

webMovie = Label(root, text=" Movie websites", font=('Arial', 30, 'bold'), fg="#fc2c03")
webMovie.pack()
webMovie.place(height=50, width=300, x=170, y=20)

xMovie = 100
for one in data['movie']:
    delete_button(xMovie)
    name_movies = Label(root, text=one['name_movie'] + "-"+one['TypeNovie'] + " - " + one['date'])

    name_movies.pack()
    name_movies.place(height=20, width=400, x=100, y=xMovie)

    xMovie += 30

root.mainloop()
