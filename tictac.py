import string

field = []


def print_field():    # print empty field with nested lists


    for i in range(field_size):
        field.append([" "])
        for j in range(field_size):
            field[i].append(" ")   
    

    line = "| "

    for j in range(field_size):
        for i in range(field_size):   
            line = line + str(field[i][j]) + " | "
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
    field_size = int(input("Set field size(3-4-5): "))


    print_field()
    winner = " "
    m = "start"

    while True:
        while check_empty(m) == False:
            m = str(input("X move?"))
        move("X", m)
        print_field()
        
        if win_check() == True:
            print("X won")
            clear_board()
            display_menu()
        
        if full_check() == True:
            print("DRAW")
            clear_board()
            display_menu()
        

        while check_empty(m) == False:
            m = str(input("O move?"))
        move("O", m)
        print_field()
        
        if win_check() == True:
            print("0 won")
            clear_board()
            display_menu()
        

        if full_check() == True:
            print("Draw.")
            clear_board()
            display_menu()
        

def display_menu():
    menu_dict= {"s: ":"Start game", "q: ":"Quit game"}

    while True:
        for key in menu_dict:
            print(key, menu_dict[key])
        user_input = str(input("Select menu item"))

        if user_input == "s":
            load_game()
        elif user_input == "q":
            exit()
        elif user_input == "r":
            continue


display_menu()