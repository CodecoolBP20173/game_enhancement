import string


def init_variables():
    ''' Initialize variables: 
    field = nested list initialized based on chosen field size
    m = player's move given as coordinates
    player_o_win: counter variable for player o's wins 
    player_x_win: counter variable for player x's wins
    player_x: player_x's name given in add_name fuction
    player_o: player_o's name given in add_name fuction
    '''
    global field
    global m
    field = []
    for i in range(field_size):
        field.append([" "])
        for j in range(field_size):
            field[i].append(" ")


def print_field():
    ''' Prints field via field nested list
    '''
    alphabet = string.ascii_lowercase
    print("\n" * 50)

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
    '''Interprets given move from alphabet + number type coordinates to nested list coordinates.
    '''
    alphabet = string.ascii_lowercase
    x = int(alphabet.index(m[0]))
    if len(m) > 2:
        y = int(m[1:]) - 1
    else:
        y = int(m[1]) - 1
    coordinates = [x, y]
    return coordinates


def check_empty(m):  
    ''' Takes m argument and converts it into field coordinates, then checks wheter field list item is empty. 
    Returns true if given field is empty.
    '''
    if m == "start":
        check_empty = False
    else:
        check_empty = False
        coordinates = move_interpreter(m)
        if field[coordinates[0]][coordinates[1]] == " ":
            check_empty = True
    
    return check_empty


def full_check():     
    ''' Iterates through the field to search for empty positions.
    Returns True if entire field is full.
    '''
    full = True
    for i in range(field_size):
        for j in range(field_size):
            if field[i][j] == " ":
                full = False

    return full


def exit_game():
    print("\nThe final score is: " + player_x + ": " + str(player_x_win) + " - " + player_o + ": " + str(player_o_win))
    print("Thank you for playing. Good bye!")
    exit()    


def move(player, m, player_name):
    ''' Takes player and m as arguments. Places given player's sign to chosen field spot.
    The two player's signs are printed via different color.
    '''

    # Checks before move
    while check_empty(m) == False:
        while True:
            m = str(input(player_name + " move? (" + player + ") -- for exit press \"r\"  "))

            if m == "r":
                exit_game()
            
            else:
                if len(m) == 2 and m[0] in string.ascii_lowercase and m[1].isnumeric():
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
    coordinates = move_interpreter(m)
    
    # The move itself
    if player == "X":
        field[coordinates[0]][coordinates[1]] = "\033[1;31m" + player + "\033[0m"
    else:
        field[coordinates[0]][coordinates[1]] = "\033[1;32m" + player + "\033[0m"


def win_check():
    ''' Iterates through the entire field searching for 5-in-a-row signs. First two if statements search vertically and horizontally
    while last two if statements search diagonally. 
    '''
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
    ''' Clears board via placing spaces to every field spot via iteration.
    '''
    for i in range(field_size):
        for j in range(field_size):
            field[i][j] = " "


def load_game():
    global field_size
    global player_x_win
    global player_o_win
    global player_x
    global player_o

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
    init_variables()
    print_field()
    winner = " "
    m = "start"

    while True:

        move("X", m, player_x)
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
                
        move("O", m, player_o)
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
    ''' 
    '''
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
    ''' Asks for two names to set the two player variables.
    '''
    global player_o_win
    global player_x_win
    global player_x
    global player_o
    player_x_win = 0
    player_o_win = 0
    player_x = " "
    player_o = " "

    print("\033[1;31m" + "Tic" + "\033[0m")
    print("      Tac")
    print("            \033[1;32m" + "Toe" + "\033[0m")
    print("                  five-in-a-row edition\n")
    player_x = input("Please enter Player 'X' name: ")
    while True:
        player_o = input("Please enter Player 'O' name: ")
        if player_o == player_x:
            print("This name is occuped. Please enter another one.")
            continue
        else:
            break
    

def main():

    add_name()
    display_menu()

if __name__ == '__main__':
    main()