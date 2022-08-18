# import GUI libraries
from tkinter import *


# defining functions
def level_open():
    main_menu.grid_forget()
    level_menu.grid(row=0, column=0)


# defining windows
root = Tk()
root.geometry('1980x1080')
root.configure(bg='cyan')

main_menu = Frame(root)
main_menu.grid(row=0, column=0)

level_menu = Frame(root)
level_menu.grid(row=0, column=0)
level_menu.grid_forget()

main_menu = Frame(root)
main_menu.grid(row=1, column=2)

# defining buttons and labels
game_label = Label(main_menu, text="Welcome To Math Bingo!", font="Helvetica 40 bold")
game_label.grid(row=1, column=2)

levels_button = Button(main_menu, text="Levels", command=level_open, font="Helvetica 25")
levels_button.grid(row=5, column=20)

leaderboard_button = Button(main_menu, text="leaderboards", font="Helvetica 25")
leaderboard_button.grid(row=10, column=20)

collectibles_button = Button(main_menu, text="collectibles", font="Helvetica 25")
collectibles_button.grid(row=15, column=20)

custom_game_button = Button(main_menu, text="custom game", font="Helvetica 25")
custom_game_button.grid(row=20, column=20)

back_button = Button()

root.mainloop()
