
import random

current_list = [1, 2, 3, 4,"X", 6, 7, 8, 9]

def TicTacToe():
    def display_board():
        global current_list
        a = current_list[0]
        b = current_list[1]
        c = current_list[2]
        d = current_list[3]
        e = current_list[4]
        f = current_list[5]
        g = current_list[6]
        h = current_list[7]
        i = current_list[8]

        print("""                +-------+-------+-------+
                |       |       |       |
                |  """, a, """  |  """, b, """  |  """, c, """  |
                |       |       |       |
                +-------+-------+-------+
                |       |       |       |
                |  """, d, """  |  """, e, """  |  """, f, """  |
                |       |       |       |
                +-------+-------+-------+
                |       |       |       |
                |  """, g, """  |  """, h, """  |  """, i, """  |
                |       |       |       |
                +-------+-------+-------+""")

    def enter_move():
        global current_list
        while True:
            try:
                value = int(input('Enter your move: '))
                if value not in current_list:
                    print("Please choose a number from the table!")
                else:
                    return value
                    break
            except:
                print('That is not a number. Please enter a number:')

    def computer_move():
        remaining_nums = []
        global current_list
        for a in current_list:
            if type(a) == int:
                remaining_nums.append(a)
        ran_ID = random.randrange(len(remaining_nums))
        choice = remaining_nums[ran_ID]
        return choice
    def victory_for():
        global current_list
        if current_list[0] == "O" and current_list[1] == "O" and current_list[2] == "O":
            print("You won!")
            return True
        elif current_list[6] == "O" and current_list[7] == "O" and current_list[8] == "O":
            print("You won!")
            return True
        elif current_list[0] == "O" and current_list[3] == "O" and current_list[6] == "O":
            print("You won!")
            return True
        elif current_list[2] == "O" and current_list[5] == "O" and current_list[8] == "O":
            print("You won!")
            return True
        elif current_list[0] == "X" and current_list[1] == "X" and current_list[2] == "X":
            print("We won!")
            return True
        elif current_list[3] == "X" and current_list[4] == "X" and current_list[5] == "X":
            print("We won!")
            return True
        elif current_list[6] == "X" and current_list[7] == "X" and current_list[8] == "X":
            print("We won!")
            return True
        elif current_list[0] == "X" and current_list[3] == "X" and current_list[6] == "X":
            print("We won!")
            return True
        elif current_list[1] == "X" and current_list[4] == "X" and current_list[7] == "X":
            print("We won!")
            return True
        elif current_list[2] == "X" and current_list[5] == "X" and current_list[8] == "X":
            print("We won!")
            return True
        elif current_list[0] == "X" and current_list[4] == "X" and current_list[8] == "X":
            print("We won!")
            return True
        elif current_list[6] == "X" and current_list[4] == "X" and current_list[2] == "X":
            print("We won!")
            return True
        else:
            return False


    while victory_for() is False:
        display_board()
        val_of_user = enter_move()
        current_list[val_of_user - 1] = "O"
        if victory_for() is True:
            display_board()
            break
        elif victory_for() is False:
            val_of_comp = computer_move()
            current_list[computer_move() - 1] = "X"
            if victory_for() is True:
                display_board()
                break
            continue
        elif all([isinstance(val, str) for val in current_list]):
            display_board()
            print("It is a Tie!")
            break
TicTacToe()


