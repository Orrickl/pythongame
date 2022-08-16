from tkinter import *
from tkinter import ttk
import tkinter.font as font

Main_menu = Tk()
Main_menu.geometry('350x90')
Main_menu.configure(bg='cyan')

Main_main_menu = ttk.Frame()
Main_main_menu.grid(row=1, column=0)
Levels_frame = ttk.Frame(Main_menu)
Levels_frame.grid(row=1, column=0)
Levels_frame.grid_forget()

def Levels_open():
    Main_main_menu.grid_forget()
    Levels_frame.grid(row=0, column=0)

Game_label = ttk.Label(Main_menu, text= "Welcome To Math Bingo!", font="Helvetica 10 bold")
Game_label.config(background="cyan")
Game_label.place(x=92, y=25)


Levels_button = ttk.Button(Main_menu, text="Levels", command=Levels_open)
Levels_button.place(x=10, y=15)

Leaderboard_button = ttk.Button(Main_menu, text="leaderboards", command=Levels_open)
Leaderboard_button.place(x=260, y=50)

Collectibles_button = ttk.Button(Main_menu, text="collectibles", command=Levels_open)
Collectibles_button.place(x=260, y=15)

Custom_Game_button = ttk.Button(Main_menu, text="custom game", command=Levels_open)
Custom_Game_button.place(x=10, y=50)

Main_menu.mainloop()
