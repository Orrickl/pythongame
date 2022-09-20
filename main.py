# import GUI libraries
from tkinter import *
from tkinter import ttk


# defining functions
def new_window(window_to_close, window_to_open):
    window_to_open.configure(bg="cyan")
    window_to_close.grid_forget()
    window_to_open.grid(row=0, column=0)
    if window_to_open == level_difficulty_menu:
        level_GUI()
    elif window_to_open == leaderboard_menu:
        leaderboard_GUI()
    elif window_to_open == custom_game_menu:
        custom_game_GUI()
    elif window_to_open == collectibles_menu:
        collectibles_GUI()


def back(current_window):
    current_window.grid_forget()
    main_menu.grid(row=0, column=0)


def level_GUI():
    global chosen_difficulty
    send_to_level(0)
    play_button = Label(level_difficulty_menu, text="Click on a difficulty below", font="Helvetica 30 bold")
    play_button.grid(row=0, column=0)
    back_button = Button(level_difficulty_menu, text="Back", command=lambda: back(level_difficulty_menu),
                         font="Helvetica 30 bold")
    back_button.grid(row=30, column=30, padx=850)
    difficulty_names = ["Easy", "Medium", "Hard"]
    difficulty_box = ttk.Combobox(level_difficulty_menu, textvariable=chosen_difficulty, state="readonly",
                                  font="Helvetica 30 bold")
    difficulty_box['values'] = difficulty_names
    difficulty_box.grid(row=3, column=1, padx=10, pady=3, sticky="WE")
    level_one_button = Button(level_difficulty_menu, text="Level one", command=lambda: send_to_level(One_Easy))
    level_one_button.grid(row=0, column=0)


def leaderboard_GUI():
    play_button = Button(leaderboard_menu, text="work")
    play_button.grid(row=0, column=0)
    back_button = Button(leaderboard_menu, text="Back", command=lambda: back(leaderboard_menu),
                         font="Helvetica 30 bold")
    back_button.grid(row=30, column=30, padx=1650)


def custom_game_GUI():
    play_button = Button(custom_game_menu, text="work")
    play_button.grid(row=0, column=0)
    back_button = Button(custom_game_menu, text="Back", command=lambda: back(custom_game_menu),
                         font="Helvetica 30 bold")
    back_button.grid(row=30, column=30, padx=1650)


def collectibles_GUI():
    play_button = Button(collectibles_menu, text="work")
    play_button.grid(row=0, column=0)
    back_button = Button(collectibles_menu, text="Back", command=lambda: back(collectibles_menu),
                         font="Helvetica 30 bold")
    back_button.grid(row=30, column=30, padx=1650)


def send_to_level(level_number):
    global chosen_difficulty
    print(chosen_difficulty.get())
    if chosen_difficulty.get() == "":
        chosen_difficulty.set("please enter a difficulty")
    elif chosen_difficulty.get() == "Easy":
        One_Easy.grid(row=0, column=0)
        generate_level(level_number)
        level_difficulty_menu.grid_forget()

def generate_level(level_num):
    text1 = Text(One_Easy, width=47, height=1, bg='grey')
    text1.pack()
    #number set 1
    can1=Canvas(One_Easy,width=100,height=70,bg='white')
    lab1=Label(can1, text=listo[0],width=10)
    lab1.pack()
    lab2=Label(can1, text=listo[1],width=10,)
    lab2.pack()
    lab3=Label(can1, text=listo[2],width=10)
    lab3.pack()
    can1.pack(side=LEFT)
    #number set 2
    can2=Canvas(One_Easy,width=100,height=70,bg='white')
    lab4=Label(can2, text=listo[3],width=10)
    lab4.pack()
    lab5=Label(can2, text=listo[4],width=10)
    lab5.pack()
    lab6=Label(can2, text=listo[5],width=10)
    lab6.pack()
    can2.pack(side=LEFT)
    #number set 1
    can3=Canvas(One_Easy,width=100,height=70,bg='white')
    lab7=Label(can3, text=listo[6],width=10)
    lab7.pack()
    lab8=Label(can3, text=listo[7],width=10)
    lab8.pack()
    lab9=Label(can3, text=listo[8],width=10)
    lab9.pack()
    can3.pack(side=LEFT)




# defining windows
root = Tk()
root.geometry('1980x1080')
root.configure(bg='cyan')

main_menu = Frame(root)
main_menu.configure(bg="cyan")
main_menu.grid(row=0, column=0)

level_difficulty_menu = Frame(root)
level_difficulty_menu.grid(row=0, column=0)
level_difficulty_menu.grid_forget()

leaderboard_menu = Frame(root)
leaderboard_menu.grid(row=0, column=0)
leaderboard_menu.grid_forget()

custom_game_menu = Frame(root)
custom_game_menu.grid(row=0, column=0)
custom_game_menu.grid_forget()

collectibles_menu = Frame(root)
collectibles_menu.grid(row=0, column=0)
collectibles_menu.grid_forget()

One_Easy = Frame(root)
One_Easy.grid(row=0, column=0)
One_Easy.grid_forget()

# defining buttons and labels
game_label = Label(main_menu, text="Welcome To Math Bingo!", font="Helvetica 40 bold")
game_label.configure(bg="cyan")
game_label.grid(row=1, column=2, padx=300)

levels_button = Button(main_menu, text="Levels", font="Helvetica 25",
                       command=lambda: new_window(main_menu, level_difficulty_menu))
levels_button.grid(row=5, column=20, pady=100)

leaderboard_button = Button(main_menu, text="leaderboards", font="Helvetica 25",
                            command=lambda: new_window(main_menu, leaderboard_menu))
leaderboard_button.grid(row=10, column=20)

collectibles_button = Button(main_menu, text="collectibles", font="Helvetica 25",
                             command=lambda: new_window(main_menu, collectibles_menu))
collectibles_button.grid(row=15, column=20)

custom_game_button = Button(main_menu, text="custom game", font="Helvetica 25",
                            command=lambda: new_window(main_menu, custom_game_menu))

custom_game_button.grid(row=20, column=20)

chosen_difficulty = StringVar()
chosen_difficulty.set("")

root.mainloop()
