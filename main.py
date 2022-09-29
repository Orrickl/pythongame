# import GUI libraries
import random
from tkinter import *
from tkinter import ttk
random_integers = []
random_integers_products = []
first_rand_int = []
second_rand_int = []
equation_to_solve_number = 0
label_list = []
equation_to_solve_number_list = []
a = 0

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
        level_difficulty_menu.grid_forget()
        One_Easy.grid(row=0, column=0)
        generate_level(level_number)


def generate_level(level_num):
    global first_rand_int, second_rand_int, equation_to_solve_number, equation_to_solve_number_list
    text1 = Label(One_Easy, textvariable=equation_to_solve, width=47, height=1, bg='grey')
    text1.pack()
    print("help")
    first_rand_int = []
    second_rand_int = []
    first_and_second_product = 0

    for i in range(25):
        first_rand_int.append(random.randint(1, 12))
        second_rand_int.append(random.randint(1, 12))
        first_and_second_product = first_rand_int[i] * second_rand_int[i]
        random_integers_products.append(first_and_second_product)
        equation_to_solve_number_list.insert(i, i)

    equation_to_solve_number = random.randint(0, 24)
    equation_to_solve.set(str(first_rand_int[equation_to_solve_number]) + "x" + str(second_rand_int[equation_to_solve_number]))
    equation_to_solve_number_list.pop(equation_to_solve_number)

    can1=Canvas(One_Easy,width=100,height=70,bg='white')
    lab1=Button(can1, text=first_rand_int[0]*second_rand_int[0], command=lambda: check_if_correct_table(0), width=10)
    lab1.pack()
    label_list.append(lab1)
    lab2=Button(can1, text=first_rand_int[1]*second_rand_int[1], command=lambda: check_if_correct_table(1), width=10,)
    lab2.pack()
    label_list.append(lab2)
    lab3=Button(can1, text=first_rand_int[2]*second_rand_int[2], command=lambda: check_if_correct_table(2),width=10)
    lab3.pack()
    label_list.append(lab3)
    lab4=Button(can1, text=first_rand_int[3]*second_rand_int[3], command=lambda: check_if_correct_table(3),width=10,)
    lab4.pack()
    label_list.append(lab4)
    lab5=Button(can1, text=first_rand_int[4]*second_rand_int[4], command=lambda: check_if_correct_table(4),width=10)
    lab5.pack()
    label_list.append(lab5)
    can1.pack(side=LEFT)
    #number set 2
    can2=Canvas(One_Easy,width=100,height=70,bg='white')
    lab6=Button(can2, text=first_rand_int[5]*second_rand_int[5], command=lambda: check_if_correct_table(5),width=10)
    lab6.pack()
    label_list.append(lab6)
    lab7=Button(can2, text=first_rand_int[6]*second_rand_int[6], command=lambda: check_if_correct_table(6),width=10)
    lab7.pack()
    label_list.append(lab7)
    lab8=Button(can2, text=first_rand_int[7]*second_rand_int[7], command=lambda: check_if_correct_table(7),width=10)
    lab8.pack()
    label_list.append(lab8)
    lab9=Button(can2, text=first_rand_int[8]*second_rand_int[8], command=lambda: check_if_correct_table(8),width=10,)
    lab9.pack()
    label_list.append(lab9)
    lab10=Button(can2, text=first_rand_int[9]*second_rand_int[9], command=lambda: check_if_correct_table(9),width=10)
    lab10.pack()
    label_list.append(lab10)
    can2.pack(side=LEFT)
    #number set 1
    can3=Canvas(One_Easy,width=100,height=70,bg='white')
    lab11=Button(can3, text=first_rand_int[10]*second_rand_int[10], command=lambda: check_if_correct_table(10),width=10)
    lab11.pack()
    label_list.append(lab11)
    lab12=Button(can3, text=first_rand_int[11]*second_rand_int[11], command=lambda: check_if_correct_table(11),width=10)
    lab12.pack()
    label_list.append(lab12)
    lab13=Button(can3, text=first_rand_int[12]*second_rand_int[12], command=lambda: check_if_correct_table(12),width=10)
    lab13.pack()
    label_list.append(lab13)
    lab14=Button(can3, text=first_rand_int[13]*second_rand_int[13], command=lambda: check_if_correct_table(13),width=10,)
    lab14.pack()
    label_list.append(lab14)
    lab15=Button(can3, text=first_rand_int[14]*second_rand_int[14], command=lambda: check_if_correct_table(14),width=10)
    lab15.pack()
    label_list.append(lab15)
    can3.pack(side=LEFT)
    can4=Canvas(One_Easy,width=100,height=70,bg='white')
    lab16=Button(can4, text=first_rand_int[15]*second_rand_int[15], command=lambda: check_if_correct_table(15),width=10)
    lab16.pack()
    label_list.append(lab16)
    lab17=Button(can4, text=first_rand_int[16]*second_rand_int[16], command=lambda: check_if_correct_table(16), width=10,)
    lab17.pack()
    label_list.append(lab17)
    lab18=Button(can4, text=first_rand_int[17]*second_rand_int[17], command=lambda: check_if_correct_table(17),width=10)
    lab18.pack()
    label_list.append(lab18)
    lab19=Button(can4, text=first_rand_int[18]*second_rand_int[18], command=lambda: check_if_correct_table(18),width=10,)
    lab19.pack()
    label_list.append(lab19)
    lab20=Button(can4, text=first_rand_int[19]*second_rand_int[19], command=lambda: check_if_correct_table(19),width=10)
    lab20.pack()
    label_list.append(lab20)
    can4.pack(side=LEFT)
    #number set 2
    can5=Canvas(One_Easy,width=100,height=70,bg='white')
    lab21=Button(can5, text=first_rand_int[20]*second_rand_int[20], command=lambda: check_if_correct_table(20), width=10)
    lab21.pack()
    label_list.append(lab21)
    lab22=Button(can5, text=first_rand_int[21]*second_rand_int[21], command=lambda: check_if_correct_table(21), width=10)
    lab22.pack()
    label_list.append(lab22)
    lab23=Button(can5, text=first_rand_int[22]*second_rand_int[22], command=lambda: check_if_correct_table(22), width=10)
    lab23.pack()
    label_list.append(lab23)
    lab24=Button(can5, text=first_rand_int[23]*second_rand_int[23], command=lambda: check_if_correct_table(23), width=10,)
    lab24.pack()
    label_list.append(lab24)
    lab25=Button(can5, text=first_rand_int[24]*second_rand_int[24], command=lambda: check_if_correct_table(24), width=10)
    lab25.pack()
    label_list.append(lab25)
    can5.pack(side=LEFT)


def check_if_correct_table(equation_number):
    global equation_to_solve_number
    if first_rand_int[equation_to_solve_number] * second_rand_int[equation_to_solve_number] == first_rand_int[equation_number] * second_rand_int[equation_number]:
        label_list[equation_number]["state"] = "disabled"
        label_list[equation_number]["bg"] = "red"

        equation_to_solve_number = random.choice(equation_to_solve_number_list)
        equation_to_solve.set(str(first_rand_int[equation_to_solve_number]) + "x" + str(second_rand_int[equation_to_solve_number]))
        print(equation_to_solve_number)
        print(equation_to_solve_number_list)
        i = 0
        while True:
            i += 1
            if equation_to_solve_number_list[i] == equation_to_solve_number:
                print(equation_to_solve_number_list[i])
                equation_to_solve_number_list.pop(i)
                break


        print(equation_to_solve_number_list)

        check_if_five_in_row(label_list[equation_number])


def check_if_five_in_row(label_num):
    print("hi")





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
equation_to_solve = StringVar()

root.mainloop()
