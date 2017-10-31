
def print_field():    # print empty field with nested lists
    for i in range(3):   
        print("| ", field[i][0], " | ", field[i][1], " | ", field[i][2], " |")


def check_empty(m):  # return true if board has empty cells
    empty = False
    if m == "7":
        if field[0][0] == " ":
            empty = True
    elif m == "8":
        if field[0][1] == " ":
            empty = True
    elif m == "9":
        if field[0][2] == " ":
            empty = True
    elif m == "4":
        if field[1][0] == " ":
            empty = True
    elif m == "5":
        if field[1][1] == " ":
            empty = True
    elif m == "6":
        if field[1][2] == " ":
            empty = True
    elif m == "1":
        if field[2][0] == " ":
            empty = True
    elif m == "2":
        if field[2][1] == " ":
            empty = True
    elif m == "3":
        if field[2][2] == " ":
            empty = True
    return empty


def move(player, m):  # place variable at chosen field via numpad
    if m == "7":
        field[0][0] = player
    elif m == "8":
        field[0][1] = player
    elif m == "9":
        field[0][2] = player
    elif m == "4":
        field[1][0] = player
    elif m == "5":
        field[1][1] = player
    elif m == "6":
        field[1][2] = player
    elif m == "1":
        field[2][0] = player
    elif m == "2":
        field[2][1] = player
    elif m == "3":
        field[2][2] = player


def full_check():     # return True if board has no more empty cells

    full = True
    for i in range(3):
        for j in range(3):
            if field[i][j] == " ":
                full = False

    return full


def win_check():      # return True if either player won the game
    winner = " "
    won = False
    for i in range(3):
        if (field[i][0] == field[i][1] and field[i][0] == field[i][2]) and (field[i][0] == "X" or field[i][0] == "O"):
            won = True
           
        if (field[0][i] == field[1][i] and field[1][i] == field[2][i]) and (field[0][i] == "X" or field[0][i] == "O"):
            won = True
          
    if (field[0][0] == field[1][1] and field[0][0] == field[2][2]) and (field[0][0] == "X" or field[0][0] == "O"):
        won = True
         
    if (field[0][2] == field[1][1] and field[0][2] == field[2][0]) and (field[0][2] == "X" or field[0][2] == "O"):
        won = True
    
    return won


def clear_board(): 
    for i in range(3):
        for j in range(3):
            field[i][j] = " "


def load_game():
    clear_board()

    print_field()
    winner = " "
    m= " "
    while True:
        while check_empty(m) == False:
            m = str(input("X move?"))
        move("X", m)

        print_field()

        if win_check() == True:
            print("X won")
            display_menu()

        if full_check() == True:
            print("DRAW")
            display_menu()

        while check_empty(m) == False:
            m = str(input("O move?"))
        move("O", m)
        print_field()

        if win_check() == True:
            print("0 won")
            display_menu()

        if full_check() == True:
            print("Draw.")
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

field = [[" "," "," "],
         [" "," "," "],
         [" "," "," "],]
display_menu()

