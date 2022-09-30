# importing random library, so I can generate random numbers to generate the equations for the bingo grid
# importing Tkinter library, so I can use its functions to create a GUI
import random
from tkinter import *

#
random_integers = []
random_integers_products = []
first_rand_int = []
second_rand_int = []
equation_to_solve_number = 0
button_list = []
equation_to_solve_number_list = []


# function which takes the user from one window to the previous one
def back(current_window, previous_window):
    current_window.grid_forget()
    previous_window.grid(row=0, column=0)


# function which makes the bingo GUI
def generate_level():
    # declares global variables, so I can use them in other functions/the main code than runs once
    global equation_to_solve, bingo_menu, first_rand_int, second_rand_int, equation_to_solve_number, \
        equation_to_solve_number_list

    # clears the button list so that if it is the second or more time doing bingo it resets
    button_list.clear()

    # destroys the bingo menu so that if it is second or more time doing bingo it resets
    bingo_menu.destroy()
    # recreates the bingo menu so that it can be used again
    bingo_menu = Frame(root)
    # gives the bingo menu a location on the screen, so it is visible
    bingo_menu.grid(row=0, column=0)
    # using .grid_forget() to remove the main menu from the screen
    main_menu.grid_forget()

    # creates a label for the equation the user has to solve is going to be in
    equation_to_solve_label = Label(bingo_menu, textvariable=equation_to_solve, width=47, height=1, bg='grey')
    equation_to_solve_label.pack()

    # creates two lists which I will store my random numbers in
    # they are here, so they get reset each time this function is ran
    first_rand_int = []
    second_rand_int = []

    for i in range(25):
        # creates a boolean that is used to cancel out of an if statement when the product of
        # test_random_integer_one and two are not in the list so there are not multiple of the same number on the board
        unique_number_found = False
        while unique_number_found == False:
            test_random_integer_one = random.randint(1, 12)
            test_random_integer_two = random.randint(1, 12)
            first_and_second_product = test_random_integer_one * test_random_integer_two
            if first_and_second_product not in random_integers_products:
                # append integers that products are different to the others in the list
                first_rand_int.append(test_random_integer_one)
                second_rand_int.append(test_random_integer_two)
                random_integers_products.append(first_and_second_product)
                unique_number_found = True
        # appends 0-24 to a list so I can use it to determine which ones have been 'popped'
        equation_to_solve_number_list.append(i)
    # chooses a random number which will be the number of the equation called
    equation_to_solve_number = random.randint(0, 24)
    # sets equation to solve to two numbers with an x in the middle so the user knows which button is pressed
    equation_to_solve.set(str(first_rand_int[equation_to_solve_number]) + "x"
                          + str(second_rand_int[equation_to_solve_number]))
    # removes the used equation number from the list to prevent it getting called again
    equation_to_solve_number_list.pop(equation_to_solve_number)

    # creates a canvas for row one of my buttons to go on
    row_one_button_canvas = Canvas(bingo_menu, width=100, height=70, bg='white')
    # creates the five buttons for the row
    button_one = Button(row_one_button_canvas, text=first_rand_int[0] * second_rand_int[0],
                        command=lambda: check_if_correct_table(0), width=10)
    button_one.pack()
    # appends the buttons to a list, so I can change different buttons using generalised code
    button_list.append(button_one)
    button_two = Button(row_one_button_canvas, text=first_rand_int[1] * second_rand_int[1],
                        command=lambda: check_if_correct_table(1), width=10)
    button_two.pack()
    button_list.append(button_two)
    button_three = Button(row_one_button_canvas, text=first_rand_int[2] * second_rand_int[2],
                          command=lambda: check_if_correct_table(2), width=10)
    button_three.pack()
    button_list.append(button_three)
    button_four = Button(row_one_button_canvas, text=first_rand_int[3] * second_rand_int[3],
                         command=lambda: check_if_correct_table(3), width=10)
    button_four.pack()
    button_list.append(button_four)
    button_five = Button(row_one_button_canvas, text=first_rand_int[4] * second_rand_int[4],
                         command=lambda: check_if_correct_table(4), width=10)
    button_five.pack()
    button_list.append(button_five)
    row_one_button_canvas.pack(side=LEFT)
    # creates a canvas for row two of my buttons to go on
    row_two_button_canvas = Canvas(bingo_menu, width=100, height=70, bg='white')
    # creates the five buttons for the row
    button_six = Button(row_two_button_canvas, text=first_rand_int[5] * second_rand_int[5],
                        command=lambda: check_if_correct_table(5), width=10)
    button_six.pack()
    button_list.append(button_six)
    button_seven = Button(row_two_button_canvas, text=first_rand_int[6] * second_rand_int[6],
                          command=lambda: check_if_correct_table(6), width=10)
    button_seven.pack()
    button_list.append(button_seven)
    button_eight = Button(row_two_button_canvas, text=first_rand_int[7] * second_rand_int[7],
                          command=lambda: check_if_correct_table(7), width=10)
    button_eight.pack()
    button_list.append(button_eight)
    button_nine = Button(row_two_button_canvas, text=first_rand_int[8] * second_rand_int[8],
                         command=lambda: check_if_correct_table(8), width=10)
    button_nine.pack()
    button_list.append(button_nine)
    button_ten = Button(row_two_button_canvas, text=first_rand_int[9] * second_rand_int[9],
                        command=lambda: check_if_correct_table(9), width=10)
    button_ten.pack()
    button_list.append(button_ten)
    row_two_button_canvas.pack(side=LEFT)
    # creates a canvas for row three of my buttons to go on
    row_three_button_canvas = Canvas(bingo_menu, width=100, height=70, bg='white')
    # creates the five buttons for the row
    button_eleven = Button(row_three_button_canvas, text=first_rand_int[10] * second_rand_int[10],
                           command=lambda: check_if_correct_table(10), width=10)
    button_eleven.pack()
    button_list.append(button_eleven)
    button_twelve = Button(row_three_button_canvas, text=first_rand_int[11] * second_rand_int[11],
                           command=lambda: check_if_correct_table(11), width=10)
    button_twelve.pack()
    button_list.append(button_twelve)
    button_thirteen = Button(row_three_button_canvas, text=first_rand_int[12] * second_rand_int[12],
                             command=lambda: check_if_correct_table(12), width=10)
    button_thirteen.pack()
    button_list.append(button_thirteen)
    button_fourteen = Button(row_three_button_canvas, text=first_rand_int[13] * second_rand_int[13],
                             command=lambda: check_if_correct_table(13), width=10)
    button_fourteen.pack()
    button_list.append(button_fourteen)
    button_fifteen = Button(row_three_button_canvas, text=first_rand_int[14] * second_rand_int[14],
                            command=lambda: check_if_correct_table(14), width=10)
    button_fifteen.pack()
    button_list.append(button_fifteen)
    row_three_button_canvas.pack(side=LEFT)
    # creates a canvas for row four of my buttons to go on
    row_four_button_canvas = Canvas(bingo_menu, width=100, height=70, bg='white')
    # creates the five buttons for the row
    button_sixteen = Button(row_four_button_canvas, text=first_rand_int[15] * second_rand_int[15],
                            command=lambda: check_if_correct_table(15), width=10)
    button_sixteen.pack()
    button_list.append(button_sixteen)
    button_seventeen = Button(row_four_button_canvas, text=first_rand_int[16] * second_rand_int[16],
                              command=lambda: check_if_correct_table(16), width=10)
    button_seventeen.pack()
    button_list.append(button_seventeen)
    button_eighteen = Button(row_four_button_canvas, text=first_rand_int[17] * second_rand_int[17],
                             command=lambda: check_if_correct_table(17), width=10)
    button_eighteen.pack()
    button_list.append(button_eighteen)
    button_nineteen = Button(row_four_button_canvas, text=first_rand_int[18] * second_rand_int[18],
                             command=lambda: check_if_correct_table(18), width=10)
    button_nineteen.pack()
    button_list.append(button_nineteen)
    button_twenty = Button(row_four_button_canvas, text=first_rand_int[19] * second_rand_int[19],
                           command=lambda: check_if_correct_table(19), width=10)
    button_twenty.pack()
    button_list.append(button_twenty)
    row_four_button_canvas.pack(side=LEFT)
    # creates a canvas for row five of my buttons to go on
    row_five_button_canvas = Canvas(bingo_menu, width=100, height=70, bg='white')
    # creates the five buttons for the row
    button_twentyone = Button(row_five_button_canvas, text=first_rand_int[20] * second_rand_int[20],
                              command=lambda: check_if_correct_table(20), width=10)
    button_twentyone.pack()
    button_list.append(button_twentyone)
    button_twentytwo = Button(row_five_button_canvas, text=first_rand_int[21] * second_rand_int[21],
                              command=lambda: check_if_correct_table(21), width=10)
    button_twentytwo.pack()
    button_list.append(button_twentytwo)
    button_twentythree = Button(row_five_button_canvas, text=first_rand_int[22] * second_rand_int[22],
                                command=lambda: check_if_correct_table(22), width=10)
    button_twentythree.pack()
    button_list.append(button_twentythree)
    button_twentyfour = Button(row_five_button_canvas, text=first_rand_int[23] * second_rand_int[23],
                               command=lambda: check_if_correct_table(23), width=10)
    button_twentyfour.pack()
    button_list.append(button_twentyfour)
    button_twentyfive = Button(row_five_button_canvas, text=first_rand_int[24] * second_rand_int[24],
                               command=lambda: check_if_correct_table(24), width=10)
    button_twentyfive.pack()
    button_list.append(button_twentyfive)
    row_five_button_canvas.pack(side=LEFT)

    #
    back_button = Button(bingo_menu, text="Back", font="Helvetica 15", command=lambda: back(bingo_menu, main_menu),
                         fg="red")
    back_button.pack(side=BOTTOM, padx=20)


def check_if_correct_table(equation_number):
    global equation_to_solve_number, equation_to_solve
    print(str(equation_number) + " = equation number")
    if equation_to_solve_number == equation_number:
        button_list[equation_number]["state"] = "disabled"
        button_list[equation_number]["bg"] = "red"
        check_if_five_in_row(button_list[equation_number])
        equation_to_solve_number = random.choice(equation_to_solve_number_list)
        equation_to_solve_number_list.remove(equation_to_solve_number)
        equation_to_solve.set(
            str(first_rand_int[equation_to_solve_number]) + "x" + str(second_rand_int[equation_to_solve_number]))


def check_if_five_in_row(label_num):
    for i in range(0, 21, 5):
        if i not in equation_to_solve_number_list and \
                i + 1 not in equation_to_solve_number_list \
                and i + 2 not in equation_to_solve_number_list \
                and i + 3 not in equation_to_solve_number_list \
                and i + 4 not in equation_to_solve_number_list:
            print("column")
            button_list[i]["bg"] = "yellow"
            button_list[i + 1]["bg"] = "yellow"
            button_list[i + 2]["bg"] = "yellow"
            button_list[i + 3]["bg"] = "yellow"
            button_list[i + 4]["bg"] = "yellow"
            won_bingo()
    for i in range(0, 5):
        if i not in equation_to_solve_number_list and \
                i + 5 not in equation_to_solve_number_list \
                and i + 10 not in equation_to_solve_number_list \
                and i + 15 not in equation_to_solve_number_list \
                and i + 20 not in equation_to_solve_number_list:
            print("row")
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
        print("diagnol top left")
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
        print("diagnol bottom right")
        button_list[4]["bg"] = "yellow"
        button_list[8]["bg"] = "yellow"
        button_list[12]["bg"] = "yellow"
        button_list[16]["bg"] = "yellow"
        button_list[20]["bg"] = "yellow"
        won_bingo()


def won_bingo():
    equation_to_solve.set("You Won!!!")

    continue_label = Label(bingo_menu, text="Play again?", font="Helvetica 15")
    continue_label.pack()
    continue_button = Button(bingo_menu, text="Yes!", font="Helvetica 15",
                             command=lambda: generate_level())
    continue_button.pack(side=BOTTOM)
    back_to_home_button = Button(bingo_menu, text="No", font="Helvetica 15",
                                 command=lambda: back(bingo_menu, main_menu))
    back_to_home_button.pack(side=BOTTOM)


# defining windows
root = Tk()
root.geometry('650x330')
root.configure(bg='cyan')

main_menu = Frame(root)
main_menu.configure(bg="cyan")
main_menu.grid(row=0, column=0)

bingo_menu = Frame(root)
bingo_menu.grid(row=0, column=0)
bingo_menu.grid_forget()

# defining buttons and labels
game_label = Label(main_menu, text="Welcome To Math Bingo!", font="Helvetica 40 bold")
game_label.configure(bg="cyan")
game_label.grid(row=0, column=0)

play_button = Button(main_menu, text="Play!", font="Helvetica 25",
                     command=lambda: generate_level())
play_button.grid(row=3, column=0, pady=50)

quit_button = Button(main_menu, text="Quit", font="Helvetica 25", command=lambda: quit())
quit_button.grid(row=6, column=0)

equation_to_solve = StringVar()

root.mainloop()
