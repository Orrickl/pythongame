# import GUI libraries
from tkinter import *


# defining functions
def new_window(window_to_open):
    window_to_open.configure(bg="cyan")
    main_menu.grid_forget()
    window_to_open.grid(row=0, column=0)
    back_button = Button(window_to_open, text="Back", command=lambda: back(window_to_open), font="Helvetica 30 bold")
    back_button.grid(row=30, column=1, padx=1750)
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
    play_button = Label(level_difficulty_menu, text="Click on a difficulty below")
    play_button.grid(row=0, column=0)


def leaderboard_GUI():
    play_button = Button(leaderboard_menu, text="work")
    play_button.grid(row=0, column=0)


def custom_game_GUI():
    play_button = Button(custom_game_menu, text="work")
    play_button.grid(row=0, column=0)


def collectibles_GUI():
    play_button = Button(collectibles_menu, text="work")
    play_button.grid(row=0, column=0)


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

# defining buttons and labels
game_label = Label(main_menu, text="Welcome To Math Bingo!", font="Helvetica 40 bold")
game_label.configure(bg="cyan")
game_label.grid(row=1, column=2, padx=300)

levels_button = Button(main_menu, text="Levels", font="Helvetica 25", command=lambda: new_window(level_difficulty_menu))
levels_button.grid(row=5, column=20, pady=100)

leaderboard_button = Button(main_menu, text="leaderboards", font="Helvetica 25",
                            command=lambda: new_window(leaderboard_menu))
leaderboard_button.grid(row=10, column=20)

collectibles_button = Button(main_menu, text="collectibles", font="Helvetica 25",
                             command=lambda: new_window(collectibles_menu))
collectibles_button.grid(row=15, column=20)

custom_game_button = Button(main_menu, text="custom game", font="Helvetica 25",
                            command=lambda: new_window(custom_game_menu))
custom_game_button.grid(row=20, column=20)

root.mainloop()
