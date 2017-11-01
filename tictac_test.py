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

    for j in range(field_size):
        for i in range(field_size):   
            line = line + str(field[i][j]) + " | "
        line = line + str(j + 1)
        print(line)
        line = "| "
    
def move_interpreter(m):

    alphabet = string.ascii_lowercase
    x = int(alphabet.index(m[0]))
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
    field[coordinates[0]][coordinates[1]] = player


def win_check():      
    winner = " "
    won = False
    for i in range(field_size):
        for j in range(field_size):
            if field[i][j] == "X" or field[i][j] == "O":
                try:
                    if field[i][j] == field[i+1][j] and field[i][j] == field[i+2][j]:
                        won = True
                    elif field[i][j] == field[i][j+1] and field[i][j] == field[i][j+2]:
                        won = True    
                    elif field[i][j] == field[i+1][j+1] and field[i][j] == field[i+2][j+2]:
                        won = True
                    elif field[i][j] == field[i-1][j-1] and field[i][j] == field[i-2][j-2]:
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
        field_size = input("\nSet field size (3x3 - 8x8). Enter only one digit: ")
        if field_size.isnumeric() == True:
            field_size = int(field_size)
            if field_size in range(3, 9):
                break
            else:
                print("Please enter a valid value!")
                continue
        else:
            print("Please enter a digit between 3 and 8!")
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

    while True:
        print("\ns: Start game")
        print("q: Quit game\n")
        user_input = str(input("Select menu item: "))

        if user_input == "s":
            load_game()
        elif user_input == "q":
            print("\nThe final score is: " + player_x + ": " + str(player_x_win) + " - " + player_o + ": " + str(player_o_win))
            print("Good bye!")
            exit()
        elif user_input == "r":
            continue

def add_name():
    global player_x
    global player_o
    player_x = input("Please enter Player X name: ")
    player_o = input("Please enter Player O name: ")
    display_menu()


add_name()