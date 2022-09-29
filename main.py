# import GUI libraries
import random
from tkinter import *
from tkinter import ttk

random_integers = []
random_integers_products = []
first_rand_int = []
second_rand_int = []
equation_to_solve_number = 0
button_list = []
equation_to_solve_number_list = []


# defining functions
def new_window(window_to_close, window_to_open):
    window_to_open.configure(bg="cyan")
    window_to_close.grid_forget()
    window_to_open.grid(row=0, column=0)
    if window_to_open == level_selection_menu:
        level_GUI()


def back(current_window, previous_window):
    current_window.grid_forget()
    previous_window.grid(row=0, column=0)


def level_GUI():
    level_info_label = Label(level_selection_menu, text="Click on a Level below", font="Helvetica 30 bold")
    level_info_label.grid(row=0, column=0)
    back_button = Button(level_selection_menu, text="Back", command=lambda: back(level_selection_menu, ),
                         font="Helvetica 30 bold")
    back_button.grid(row=30, column=30, padx=850)
    level_one_button = Button(level_selection_menu, text="Level one", command=lambda: generate_level())
    level_one_button.grid(row=0, column=0)


def generate_level():
    global equation_to_solve
    bingo_menu.grid(row=0, column=0)
    level_selection_menu.grid_forget()

    global first_rand_int, second_rand_int, equation_to_solve_number, equation_to_solve_number_list
    text1 = Label(bingo_menu, textvariable=equation_to_solve, width=47, height=1, bg='grey')
    text1.pack()
    first_rand_int = []
    second_rand_int = []

    for i in range(25):
        first_rand_int.append(random.randint(1, 12))
        second_rand_int.append(random.randint(1, 12))
        first_and_second_product = first_rand_int[i] * second_rand_int[i]
        random_integers_products.append(first_and_second_product)
        equation_to_solve_number_list.insert(i, i)

    equation_to_solve_number = random.randint(0, 24)
    equation_to_solve.set(str(first_rand_int[equation_to_solve_number]) + "x"
                          + str(second_rand_int[equation_to_solve_number]))
    equation_to_solve_number_list.pop(equation_to_solve_number)

    can1 = Canvas(bingo_menu, width=100, height=70, bg='white')
    button_one = Button(can1, text=first_rand_int[0] * second_rand_int[0],
                        command=lambda: check_if_correct_table(0), width=10)
    button_one.pack()
    button_list.append(button_one)
    button_two = Button(can1, text=first_rand_int[1] * second_rand_int[1],
                        command=lambda: check_if_correct_table(1), width=10)
    button_two.pack()
    button_list.append(button_two)
    button_three = Button(can1, text=first_rand_int[2] * second_rand_int[2],
                          command=lambda: check_if_correct_table(2), width=10)
    button_three.pack()
    button_list.append(button_three)
    button_four = Button(can1, text=first_rand_int[3] * second_rand_int[3],
                         command=lambda: check_if_correct_table(3), width=10)
    button_four.pack()
    button_list.append(button_four)
    button_five = Button(can1, text=first_rand_int[4] * second_rand_int[4],
                         command=lambda: check_if_correct_table(4), width=10)
    button_five.pack()
    button_list.append(button_five)
    can1.pack(side=LEFT)
    # number set 2
    can2 = Canvas(bingo_menu, width=100, height=70, bg='white')
    button_six = Button(can2, text=first_rand_int[5] * second_rand_int[5],
                        command=lambda: check_if_correct_table(5), width=10)
    button_six.pack()
    button_list.append(button_six)
    button_seven = Button(can2, text=first_rand_int[6] * second_rand_int[6],
                          command=lambda: check_if_correct_table(6), width=10)
    button_seven.pack()
    button_list.append(button_seven)
    button_eight = Button(can2, text=first_rand_int[7] * second_rand_int[7],
                          command=lambda: check_if_correct_table(7), width=10)
    button_eight.pack()
    button_list.append(button_eight)
    button_nine = Button(can2, text=first_rand_int[8] * second_rand_int[8],
                         command=lambda: check_if_correct_table(8), width=10)
    button_nine.pack()
    button_list.append(button_nine)
    button_ten = Button(can2, text=first_rand_int[9] * second_rand_int[9],
                        command=lambda: check_if_correct_table(9), width=10)
    button_ten.pack()
    button_list.append(button_ten)
    can2.pack(side=LEFT)
    # number set 1
    can3 = Canvas(bingo_menu, width=100, height=70, bg='white')
    button_eleven = Button(can3, text=first_rand_int[10] * second_rand_int[10],
                           command=lambda: check_if_correct_table(10), width=10)
    button_eleven.pack()
    button_list.append(button_eleven)
    button_twelve = Button(can3, text=first_rand_int[11] * second_rand_int[11],
                           command=lambda: check_if_correct_table(11), width=10)
    button_twelve.pack()
    button_list.append(button_twelve)
    button_thirteen = Button(can3, text=first_rand_int[12] * second_rand_int[12],
                             command=lambda: check_if_correct_table(12), width=10)
    button_thirteen.pack()
    button_list.append(button_thirteen)
    button_fourteen = Button(can3, text=first_rand_int[13] * second_rand_int[13],
                             command=lambda: check_if_correct_table(13), width=10)
    button_fourteen.pack()
    button_list.append(button_fourteen)
    button_fifteen = Button(can3, text=first_rand_int[14] * second_rand_int[14],
                            command=lambda: check_if_correct_table(14), width=10)
    button_fifteen.pack()
    button_list.append(button_fifteen)
    can3.pack(side=LEFT)
    can4 = Canvas(bingo_menu, width=100, height=70, bg='white')
    button_sixteen = Button(can4, text=first_rand_int[15] * second_rand_int[15],
                            command=lambda: check_if_correct_table(15), width=10)
    button_sixteen.pack()
    button_list.append(button_sixteen)
    button_seventeen = Button(can4, text=first_rand_int[16] * second_rand_int[16],
                              command=lambda: check_if_correct_table(16), width=10)
    button_seventeen.pack()
    button_list.append(button_seventeen)
    button_eighteen = Button(can4, text=first_rand_int[17] * second_rand_int[17],
                             command=lambda: check_if_correct_table(17), width=10)
    button_eighteen.pack()
    button_list.append(button_eighteen)
    button_nineteen = Button(can4, text=first_rand_int[18] * second_rand_int[18],
                             command=lambda: check_if_correct_table(18), width=10)
    button_nineteen.pack()
    button_list.append(button_nineteen)
    button_twenty = Button(can4, text=first_rand_int[19] * second_rand_int[19],
                           command=lambda: check_if_correct_table(19), width=10)
    button_twenty.pack()
    button_list.append(button_twenty)
    can4.pack(side=LEFT)
    # number set 2
    can5 = Canvas(bingo_menu, width=100, height=70, bg='white')
    button_twentyone = Button(can5, text=first_rand_int[20] * second_rand_int[20],
                              command=lambda: check_if_correct_table(20), width=10)
    button_twentyone.pack()
    button_list.append(button_twentyone)
    button_twentytwo = Button(can5, text=first_rand_int[21] * second_rand_int[21],
                              command=lambda: check_if_correct_table(21), width=10)
    button_twentytwo.pack()
    button_list.append(button_twentytwo)
    button_twentythree = Button(can5, text=first_rand_int[22] * second_rand_int[22],
                                command=lambda: check_if_correct_table(22), width=10)
    button_twentythree.pack()
    button_list.append(button_twentythree)
    button_twentyfour = Button(can5, text=first_rand_int[23] * second_rand_int[23],
                               command=lambda: check_if_correct_table(23), width=10)
    button_twentyfour.pack()
    button_list.append(button_twentyfour)
    button_twentyfive = Button(can5, text=first_rand_int[24] * second_rand_int[24],
                               command=lambda: check_if_correct_table(24), width=10)
    button_twentyfive.pack()
    button_list.append(button_twentyfive)
    can5.pack(side=LEFT)


def check_if_correct_table(equation_number):
    global equation_to_solve_number, equation_to_solve
    print(equation_number)
    if equation_to_solve_number == equation_number:
        button_list[equation_number]["state"] = "disabled"
        button_list[equation_number]["bg"] = "red"
        check_if_five_in_row(button_list[equation_number])
        equation_to_solve_number = random.choice(equation_to_solve_number_list)
        equation_to_solve.set(
            str(first_rand_int[equation_to_solve_number]) + "x" + str(second_rand_int[equation_to_solve_number]))
        i = -1
        while True:
            i += 1
            if equation_to_solve_number_list[i] == equation_to_solve_number:
                print(equation_to_solve_number_list[i])
                equation_to_solve_number_list.pop(i)
                break


def check_if_five_in_row(label_num):
    print(equation_to_solve_number_list)
    for i in range(0, 21, 5):
        if i not in equation_to_solve_number_list and \
                i + 1 not in equation_to_solve_number_list \
                and 1 + 2 not in equation_to_solve_number_list \
                and i + 3 not in equation_to_solve_number_list \
                and i + 4 not in equation_to_solve_number_list:
            button_list[i]["bg"] = "yellow"
            button_list[i + 1]["bg"] = "yellow"
            button_list[i + 2]["bg"] = "yellow"
            button_list[i + 3]["bg"] = "yellow"
            button_list[i + 4]["bg"] = "yellow"
            won_bingo()
    for i in range(0, 5):
        if i not in equation_to_solve_number_list and \
                i + 5 not in equation_to_solve_number_list \
                and 1 + 10 not in equation_to_solve_number_list \
                and i + 15 not in equation_to_solve_number_list \
                and i + 20 not in equation_to_solve_number_list:
            button_list[i]["bg"] = "yellow"
            button_list[i + 5]["bg"] = "yellow"
            button_list[i + 10]["bg"] = "yellow"
            button_list[i + 15]["bg"] = "yellow"
            button_list[i + 20]["bg"] = "yellow"
            won_bingo()
    if 0 not in equation_to_solve_number_list \
            and 6 not in equation_to_solve_number_list \
            and 12 not in equation_to_solve_number_list \
            and 18 not in equation_to_solve_number_list \
            and 24 not in equation_to_solve_number_list:
        button_list[0]["bg"] = "yellow"
        button_list[6]["bg"] = "yellow"
        button_list[12]["bg"] = "yellow"
        button_list[18]["bg"] = "yellow"
        button_list[24]["bg"] = "yellow"
        won_bingo()

    elif 4 not in equation_to_solve_number_list \
            and 8 not in equation_to_solve_number_list \
            and 12 not in equation_to_solve_number_list \
            and 16 not in equation_to_solve_number_list \
            and 20 not in equation_to_solve_number_list:
        button_list[4]["bg"] = "yellow"
        button_list[8]["bg"] = "yellow"
        button_list[12]["bg"] = "yellow"
        button_list[16]["bg"] = "yellow"
        button_list[20]["bg"] = "yellow"
        won_bingo()


def won_bingo():
    equation_to_solve.set("congratulations")
    bingo_menu.destroy()
    continue_menu.grid(row=0, column=0)
    continue_label = Label(continue_menu, text="Do you want to continue?", font="Helvetica 15")
    continue_label.grid(row=0, column=0)
    continue_button = Button(continue_menu, text="Yes!", font="Helvetica 15", command=lambda: back(continue_menu, main_menu))
    continue_button.grid(row=1, column=5)
    back_to_home_button = Button(continue_menu, text="No", font="Helvetica 15", command=lambda: level_GUI())
    back_to_home_button.grid(row=1, column=0)


# defining windows
root = Tk()
root.geometry('1980x1080')
root.configure(bg='cyan')

main_menu = Frame(root)
main_menu.configure(bg="cyan")
main_menu.grid(row=0, column=0)

level_selection_menu = Frame(root)
level_selection_menu.grid(row=0, column=0)
level_selection_menu.grid_forget()

bingo_menu = Frame(root)
bingo_menu.grid(row=0, column=0)
bingo_menu.grid_forget()

continue_menu = Frame(root)
continue_menu.grid(row=0, column=0)
continue_menu.grid_forget()

# defining buttons and labels
game_label = Label(main_menu, text="Welcome To Math Bingo!", font="Helvetica 40 bold")
game_label.configure(bg="cyan")
game_label.grid(row=1, column=2, padx=300)

levels_button = Button(main_menu, text="Levels", font="Helvetica 25",
                       command=lambda: new_window(main_menu, level_selection_menu))
levels_button.grid(row=5, column=20, pady=100)

equation_to_solve = StringVar()

root.mainloop()
