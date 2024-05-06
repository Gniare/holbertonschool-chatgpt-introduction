#!/usr/bin/python3
import random
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

class Minesweeper:
    def __init__(self, width=10, height=10, mines=10):
        self.width = width
        self.height = height
        self.mines = set(random.sample(range(width * height), mines))
        self.field = [[' ' for _ in range(width)] for _ in range(height)]
        self.revealed = [[False for _ in range(width)] for _ in range(height)]
        self.marked = [[False for _ in range(width)] for _ in range(height)]

    def print_board(self, reveal=False):
        clear_screen()
        print('  ' + ' '.join(str(i) for i in range(self.width)))
        for y in range(self.height):
            print(y, end=' ')
            for x in range(self.width):
                if self.marked[y][x]:
                    print('F', end=' ')  # Marquée comme contenant une mine
                elif reveal or self.revealed[y][x]:
                    if (y * self.width + x) in self.mines:
                        print('*', end=' ')  # Mine
                    else:
                        count = self.count_mines_nearby(x, y)
                        print(count if count > 0 else ' ', end=' ')  # Nombre de mines voisines
                else:
                    print('.', end=' ')  # Case cachée
            print()

    def count_mines_nearby(self, x, y):
        count = 0
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < self.width and 0 <= ny < self.height:
                    if (ny * self.width + nx) in self.mines:
                        count += 1
        return count

    def reveal(self, x, y):
        if (y * self.width + x) in self.mines:
            return False
        self.revealed[y][x] = True
        if self.count_mines_nearby(x, y) == 0:
            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < self.width and 0 <= ny < self.height and not self.revealed[ny][nx]:
                        self.reveal(nx, ny)
        return True

    def toggle_mark(self, x, y):
        self.marked[y][x] = not self.marked[y][x]

    def play(self):
        while True:
            self.print_board()
            try:
                x = int(input("Enter x coordinate: "))
                y = int(input("Enter y coordinate: "))
                action = input("Enter 'r' to reveal or 'm' to mark/unmark: ")
                
                if action == 'r':
                    if not self.reveal(x, y):
                        self.print_board(reveal=True)
                        print("Game Over! You hit a mine.")
                        break
                elif action == 'm':
                    self.toggle_mark(x, y)
                else:
                    print("Invalid action. Please enter 'r' to reveal or 'm' to mark/unmark.")
                    continue
                
                # Check win condition
                if all(self.revealed[y][x] or (y * self.width + x) in self.mines for y in range(self.height) for x in range(self.width)):
                    self.print_board(reveal=True)
                    print("Congratulations! You won!")
                    break
            except ValueError:
                print("Invalid input. Please enter numbers only.")

if __name__ == "__main__":
    game = Minesweeper()
    game.play()
