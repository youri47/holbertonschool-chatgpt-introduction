#!/usr/bin/python3
import random
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

class Minesweeper:
    def __init__(self, width=10, height=10, mines=10):
        self.width = width
        self.height = height
        # Génération des mines
        self.mines = set(random.sample(range(width * height), mines))
        self.field = [[' ' for _ in range(width)] for _ in range(height)]
        self.revealed = [[False for _ in range(width)] for _ in range(height)]

    def print_board(self, reveal=False):
        clear_screen()
        print('  ' + ' '.join(str(i) for i in range(self.width)))
        for y in range(self.height):
            print(y, end=' ')
            for x in range(self.width):
                if reveal or self.revealed[y][x]:
                    if (y * self.width + x) in self.mines:
                        print('X', end=' ')
                    else:
                        count = self.count_mines_nearby(x, y)
                        print(count if count > 0 else ' ', end=' ')
                else:
                    print('.', end=' ')
            print()

    def count_mines_nearby(self, x, y):
        count = 0
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if dx == 0 and dy == 0:
                    continue
                nx, ny = x + dx, y + dy
                if 0 <= nx < self.width and 0 <= ny < self.height:
                    if (ny * self.width + nx) in self.mines:
                        count += 1
        return count

    def reveal(self, x, y):
        # Vérifie si on tombe sur une mine
        if (y * self.width + x) in self.mines:
            return False
        
        # Si la case est déjà révélée, on ne fait rien
        if self.revealed[y][x]:
            return True

        self.revealed[y][x] = True
        
        # Si aucune mine autour (0), on révèle récursivement les voisins
        if self.count_mines_nearby(x, y) == 0:
            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    nx, ny = x + dx, y + dy
                    # CORRECTION ICI: vérification des limites et si pas déjà révélé
                    if 0 <= nx < self.width and 0 <= ny < self.height and not self.revealed[ny][nx]:
                        self.reveal(nx, ny)
        return True

    # NOUVELLE MÉTHODE : Vérifier la victoire
    def check_win(self):
        # Compter le nombre de cases révélées
        count_revealed = sum(row.count(True) for row in self.revealed)
        # Calculer le nombre total de cases "sûres" (sans mines)
        total_safe_cells = (self.width * self.height) - len(self.mines)
        
        # Si le nombre de cases révélées égale le nombre de cases sûres, on a gagné
        return count_revealed == total_safe_cells

    def play(self):
        while True:
            self.print_board()
            try:
                x = int(input("Enter x coordinate: "))
                y = int(input("Enter y coordinate: "))
                
                # Vérification de l'entrée utilisateur pour rester dans la grille
                if not (0 <= x < self.width and 0 <= y < self.height):
                    print("Coordinates out of bounds.")
                    continue

                if not self.reveal(x, y):
                    self.print_board(reveal=True)
                    print("Game Over! You hit a mine.")
                    break
                
                # AJOUT ICI : Vérification de la victoire après chaque coup
                if self.check_win():
                    self.print_board(reveal=True)
                    print("Congratulations! You won!")
                    break

            except ValueError:
                print("Invalid input. Please enter numbers only.")

if __name__ == "__main__":
    game = Minesweeper()
    game.play()
