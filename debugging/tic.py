#!/usr/bin/python3

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board):
    # Vérification des lignes
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != " ":
            return True

    # Vérification des colonnes
    for col in range(len(board[0])):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return True

    # Vérification des diagonales
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return True

    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return True

    return False

def is_full(board):
    # Vérifie si la grille est pleine (match nul)
    for row in board:
        if " " in row:
            return False
    return True

def tic_tac_toe():
    board = [[" "]*3 for _ in range(3)]
    player = "X"
    
    print("Welcome to Tic Tac Toe!")
    print_board(board)

    while True:
        try:
            print(f"Player {player}'s turn")
            row = int(input("Enter row (0, 1, or 2): "))
            col = int(input("Enter column (0, 1, or 2): "))

            # Vérification que les coordonnées sont valides
            if row not in range(3) or col not in range(3):
                print("Invalid coordinates! Use 0, 1, or 2.")
                continue

            if board[row][col] == " ":
                board[row][col] = player
                print_board(board)
                
                # 1. Vérifier la victoire AVANT de changer de joueur
                if check_winner(board):
                    print(f"Player {player} wins!")
                    break
                
                # 2. Vérifier le match nul
                if is_full(board):
                    print("It's a tie!")
                    break

                # 3. Changer de joueur seulement si personne n'a gagné
                player = "O" if player == "X" else "X"
            else:
                print("That spot is already taken! Try again.")

        except ValueError:
            print("Invalid input! Please enter numbers only.")

if __name__ == "__main__":
    tic_tac_toe()
