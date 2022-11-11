#task1
def deleter(s, char_combination="абв"):
    word_list = s.lower().split()
    removable_words = [word for word in word_list if char_combination in word]
    for word in removable_words:
        word_list.remove(word)
    return " ".join(word_list)

# print(deleter("абвага абв абв нуль АБВ"))

import random
#task2
def check_winner(candies):
    if candies <= 0:
        return True
    return False

def turn_changer(turn):
    if turn == 0:
        return 1
    else:
        return 0

def who_is_first():
    player = random.randint(0,1)
    return player

def validation(turn):
    player = 0
    while not player in range(1,29):
        player = int(input(f"Ход игрока {turn + 1}. Пожалуйста, введите число в диапозоне от 1 до 28 включительно: "))
    return player

def candy_game():
    turn = who_is_first()
    players = [1, 2]
    candies = 49
    winner = ""
    while candies > 0:
        # Если играем против человека:
        # player1 = int(input(f"Ход игрока {players[turn]}: "))
        if turn == 0:
            #Если играем против бота
            # player1 = random.randint(1, 28)
            player1 = validation(turn)       
            candies -= player1
            print(candies)
            if check_winner(candies):
                print(f"Победил игрок {turn + 1}")
            turn = turn_changer(turn)
        else:
            player2 = validation(turn)
            candies -= player2
            print(candies)
            if check_winner(candies):
                print(f"Победил игрок {turn + 1}")
            turn = turn_changer(turn) 

candy_game()

#Task3
class XO_game():

    def __init__(self):
        self.board = list(range(1, 10))

    def print_board(self):
        for i in range(3):
            print(self.board[0 + i * 3], "|", self.board[1 + i * 3], "|", self.board[2 + i * 3])

    def xo_winner(self):
        win_combinations = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
        for combination in win_combinations:
            if self.board[combination[0]] == self.board[combination[1]] == self.board[combination[2]]:
                return self.board[combination[0]]
        return False

    def make_turn(self, symbol):
        valid = False
        while not valid:
            try:
                n = int(input("Выберите клетку "))
                if 1 <= n <= 9:
                    if (str(self.board[n - 1])) not in "XO":
                        self.board[n - 1] = symbol
                        valid = True
                    else:
                        print("Клетка уже занята")
                else:
                    print("Такой клетки нет")
            except:
                print("Похоже Вы ввели не число")

    def play(self):
        counter = 0
        win = False
        while not win:
            self.print_board()
            if counter % 2 == 0:
                self.make_turn("X")
            else:
                self.make_turn("O")
            counter += 1
            win = self.xo_winner()
            if win:
                print("Победил игрок ", win)
                break
            if counter == 9:
                print("Ничья")
                break

# XO_game().play()

