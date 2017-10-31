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
    if m == "start":
        coordinates = [0,0]
    else:
        alphabet = string.ascii_lowercase
        x = int(alphabet.index(m[0]))
        y = int(m[1]) - 1
        coordinates = [x, y]
    return coordinates


def check_empty(m):  # TO BE UPDATED
    check_empty = False
    coordinates = move_interpreter(m)
    if field[coordinates[0]][coordinates[1]] == " ":
        check_empty = True
    
    return check_empty


'''
def full_check():     # TO BE UPDATED

    full = True
    for i in range(3):
        for j in range(3):
            if field[i][j] == " ":
                full = False

    return full
'''

def move(player, m):  # TO BE UPDATED
    coordinates = move_interpreter(m)
    field[coordinates[0]][coordinates[1]] = player



'''
def win_check():      # TO BE UPDATED
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
'''
'''
#def clear_board():    # TO BE UPDATED
 #   for i in range(3):
  #      for j in range(3):
   #         field[i][j] = " "
'''

def load_game():
    global field_size
    field_size = int(input("Set field size(3-4-5): "))

  #  clear_board()

    print_field()
    winner = " "
    m = "start"

    while True:
        while check_empty(m) == False:
            m = str(input("X move?"))
        move("X", m)
        print_field()
        '''
        if win_check() == True:
            print("X won")
            display_menu()

        if full_check() == True:
            print("DRAW")
            display_menu()
        '''

        while check_empty(m) == False:
            m = str(input("O move?"))
        move("O", m)
        print_field()
        '''
        if win_check() == True:
            print("0 won")
            display_menu()

        if full_check() == True:
            print("Draw.")
            display_menu()
        '''

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