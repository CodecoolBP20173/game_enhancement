import string



field = []
player_x_win = 0
player_o_win = 0



def print_field():    # print empty field with nested lists
    alphabet = string.ascii_lowercase
    print("\n" * 50)

    for i in range(field_size):
        field.append([" "])
        for j in range(field_size):
            field[i].append(" ")   
    

    line = "| "
    letters = "  "
    for i in range(field_size):
        letters += alphabet[i] + "   "
    
    print(letters)
    print("-" * (field_size * 4))

    for j in range(field_size):
        for i in range(field_size):   
            line = line + str(field[i][j]) + " | "
        line = line + str(j + 1) + "\n" + "-" * (field_size * 4)
        print(line)
        line = "| "
    
def move_interpreter(m):

    alphabet = string.ascii_lowercase
    x = int(alphabet.index(m[0]))
    if len(m) > 2:
        y = int(m[1:]) - 1
    else:
        y = int(m[1]) - 1
    coordinates = [x, y]
    return coordinates


def check_empty(m):  
    if m == "start":
        check_empty = False
    else:
        check_empty = False
        coordinates = move_interpreter(m)
        if field[coordinates[0]][coordinates[1]] == " ":
            check_empty = True
    
    return check_empty


def full_check():     

    full = True
    for i in range(field_size):
        for j in range(field_size):
            if field[i][j] == " ":
                full = False

    return full


def move(player, m):
    coordinates = move_interpreter(m)
    if player == "X":
        field[coordinates[0]][coordinates[1]] = "\033[1;31m" + player + "\033[0m"
    else:
        field[coordinates[0]][coordinates[1]] = "\033[1;32m" + player + "\033[0m"


def win_check():      
    winner = " "
    won = False
    for i in range(field_size):
        for j in range(field_size):
            if field[i][j] == "\033[1;31m" + "X" + "\033[0m" or field[i][j] == "\033[1;32m" + "O" + "\033[0m":
                try:
                    if field[i][j] == field[i+1][j] and field[i][j] == field[i+2][j] and field[i][j] == field[i+3][j] and field[i][j] == field[i+4][j]:
                        won = True
                    elif field[i][j] == field[i][j+1] and field[i][j] == field[i][j+2] and field[i][j] == field[i][j+3] and field[i][j] == field[i][j+4]:
                        won = True    
                    elif field[i][j] == field[i+1][j+1] and field[i][j] == field[i+2][j+2] and field[i][j] == field[i+3][j+3] and field[i][j] == field[i+4][j+4]:
                        won = True
                    elif field[i][j] == field[i+1][j-1] and field[i][j] == field[i+2][j-2] and field[i][j] == field[i+3][j-3] and field[i][j] == field[i+4][j-4]:
                        won = True
                except IndexError:
                    continue    
    return won


def clear_board():    
    for i in range(field_size):
        for j in range(field_size):
            field[i][j] = " "


def load_game():
    global field_size
    global player_x_win
    global player_o_win
    while True:
        field_size = input("\nSet field size (5x5 - 12x12). Enter digits only: ")
        if field_size.isnumeric() == True:
            field_size = int(field_size)
            if field_size in range(5, 13):
                break
            else:
                print("Please enter a valid value!")
                continue
        else:
            print("Please enter a digit between 5 and 12!")
            continue

    print_field()
    winner = " "
    m = "start"

    while True:
        while check_empty(m) == False:
            while True:
                m = str(input(player_x + " move? (X) -- for exit press \"r\"  "))
                if m == "r":
                    print("\nThe final score is: " + player_x + ": " + str(player_x_win) + " - " + player_o + ": " + str(player_o_win))
                    print("Thank you for playing. Good bye!")
                    exit()
                else:
                    if len(m) == 2 and m[0].isalpha() and m[1].isnumeric():
                        coordinates = move_interpreter(m)
                        if coordinates[0] < field_size and coordinates[1] < field_size:
                            break
                        else:
                            print("Please enter a valid field position!")
                            continue
                    elif len(m) == 3 and m[0].isalpha() and m[1].isnumeric() and m[2].isnumeric():
                        coordinates = move_interpreter(m)
                        if coordinates[0] < field_size and coordinates[1] < field_size:
                            break
                        else:
                            print("Please enter a valid field position!")
                            continue
                    else:
                        print("Please enter a valid field position!")
            print("This position is already taken. Please choose another one.")

        move("X", m)
        print_field()
        
        if win_check() == True:
            player_x_win += 1
            print(player_x + " won!")
            print(player_x + ": " + str(player_x_win) + " - " + player_o + ": " + str(player_o_win))
            clear_board()
            display_menu()
        
        if full_check() == True:
            print("DRAW")
            clear_board()
            display_menu()
        

        while check_empty(m) == False:
            while True:
                m = str(input(player_o + " move? (O) -- for exit press \"r\"  "))
                if m == "r":
                    print("\nThe final score is: " + player_x + ": " + str(player_x_win) + " - " + player_o + ": " + str(player_o_win))
                    print("Thank you for playing. Good bye!")
                    exit()
                else:
                    if len(m) == 2 and m[0].isalpha() and m[1].isnumeric():
                        coordinates = move_interpreter(m)
                        if coordinates[0] < field_size and coordinates[1] < field_size:
                            break
                        else:
                            print("Please enter a valid field position!")
                            continue
                    elif len(m) == 3 and m[0].isalpha() and m[1].isnumeric() and m[2].isnumeric():
                        coordinates = move_interpreter(m)
                        if coordinates[0] < field_size and coordinates[1] < field_size:
                            break
                        else:
                            print("Please enter a valid field position!")
                            continue
                    else:
                        print("Please enter a valid field position!")
            print("This position is already taken. Please choose another one.")
                
        move("O", m)
        print_field()
        
        if win_check() == True:
            player_o_win += 1
            print(player_o +  " won!")
            print(player_x + ": " + str(player_x_win) + " - " + player_o + ": " + str(player_o_win))
            clear_board()
            display_menu()
        

        if full_check() == True:
            print("Draw.")
            clear_board()
            display_menu()
        

def display_menu():

    print("\ns: Start game")
    print("q: Quit game\n")
    
    while True:
        user_input = str(input("Select menu item: "))
        if user_input == "s":
            load_game()
        elif user_input == "q":
            print("\nThe final score is: " + player_x + ": " + str(player_x_win) + " - " + player_o + ": " + str(player_o_win))
            print("Good bye!")
            exit()
        else:
            print("Please use 's' or 'q' buttons.")

def add_name():
    global player_x
    global player_o
    player_x = input("Please enter Player X name: ")
    while True:
        player_o = input("Please enter Player O name: ")
        if player_o == player_x:
            print("This name is occuped. Please enter another one.")
            continue
        else:
            break
    display_menu()


add_name()
