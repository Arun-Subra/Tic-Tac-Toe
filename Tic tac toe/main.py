import time as t # To make it look clean (time between outputs etc)

def main():
    choice = ""
    while choice != "q":
        choice = menu()
        # Instruction
        if choice == "1":
            print("\nGoogle 'How To Play Tic Tac Toe'\n")
            t.sleep(1)
        # PvP
        elif choice == "2":
            play_again = True
            p1 = input("\nEnter Player 1 name\n")
            p2 = input("\nEnter Player 2 name\n")
            p = [p1, p2]
            while play_again:
                grid = [
                    ["1", "2", "3"],
                    ["4", "5", "6"],
                    ["7", "8", "9"],
                ]
                game_over = False
                player = 0
                while game_over == False:
                    output_grid(grid)
                    print(f"{p[player]}'s turn")
                    player_input(grid, p, player)
                    check = check_grid(grid)
                    game_over, winner = check
                    # Switch between P1 and P2
                    player += 1
                    player = player % 2
                # Output who won or if there was a draw
                output_grid(grid)
                if winner == "Draw":
                    print("\nDraw! Nobody Won!\n")
                elif winner == "X":
                    print(f"\n{p[0]} won!\n")
                elif winner == "O":
                    print(f"\n{p[1]} won!\n")
                validating = True
                # See if they want to play again or not
                while validating:
                    again = input("Play again? (y/n)\n")
                    if again.lower() == "y":
                        validating = False
                    elif again.lower() == "n":
                        print("\nThat's a shame!\n")
                        play_again = False
                        validating = False
                        t.sleep(1)
                    else:
                        print("Invalid input. Please try again")
                        t.sleep(1)
        # PvE
        elif choice == "3":
            print("\nComing Soon!\n")
            t.sleep(1)
    print("\nThanks for playing!\n")
    t.sleep(1)

# Display options to choose from
def menu():
    validating = True
    while validating:
        print("Choose one of the options below by entering the number\n")
        print("1. Instructions")
        print("2. Play against another player")
        print("3. Play against the computer")
        print("(Press 'q' to quit)\n")
        choice = input()
        if choice not in "123q":
            print("Invalid input. Please try again\n")
            t.sleep(1)
        else:
            validating = False
            return choice

# Print the grid
def output_grid(grid):
    print(" _________________ ")
    for i in range(3):
        print("|     |     |     |")
        print(f"|  {grid[i][0]}  |  {grid[i][1]}  |  {grid[i][2]}  |")
        print("|_____|_____|_____|")

# Get the player's input and put it in the grid
def player_input(grid, p, player):
    XO = ["X", "O"]
    validating = True
    while validating:
        option = input()
        if option not in "123456789":
            print("Invalid Input. Please try again")
        elif grid[(int(option) - 1) // 3][(int(option) - 1) % 3] != option:
            print(f"That's already been taken, {p[player]}! Try again")
        else:
            # Place nought / cross
            grid[(int(option) - 1) // 3][(int(option) - 1) % 3] = XO[player]
            validating = False

# Check if all boxes filled / if there is 3 in a row
def check_grid(grid):
    game_over = False
    winner = "Draw"
    # Check diagonals
    if grid[0][0] == grid[1][1] == grid[2][2]:
        winner = grid[0][0]
        game_over = True
    elif grid[0][2] == grid[1][1] == grid[2][0]:
        winner = grid[0][2]
        game_over = True
    else:
        # Check if every box has been filled
        game_over = True
        for y in range(3):
            for x in range(3):
                if grid[y][x] not in "XO":
                    game_over = False
    # Check rows and columns
    for i in range(3):
        if grid[i][0] == grid[i][1] == grid[i][2]:
            winner = grid[i][0]
            game_over = True
        elif grid[0][i] == grid[1][i] == grid[2][i]:
            winner = grid[0][i]
            game_over = True
    return [game_over, winner]

if __name__ == "__main__":
    main()
