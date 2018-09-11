import random

class Field:
    def __init__(self):
        self.field = self._generate_field()

    def _generate_field(self):
        field = ['-' for _ in range(1, 10)]
        return field

    def field_translation(self, key, to_do=False):
        dictionary = {'a1': 6, 'b1': 7, 'c1': 8, 'a2': 3, 'b2': 4, 'c2': 5, 'a3': 0, 'b3': 1, 'c3': 2}
        if to_do is False:
            if key in dictionary:
                return dictionary[key]
            else:
                return 'False'
        elif to_do is True:
            for k, v in dictionary.items():
                if v == key:
                    return k
        else:
            return 'False'

    def make_a_move(self, key, label):
        if self.field[key] == '-':
            self.field[key] = label
        else:
            print('Невозможно сделать ход!')
            return False

    def show_field(self):
        print(' ---------')
        print('3|{}  {}  {}|'.format(self.field[0], self.field[1], self.field[2]))
        print('2|{}  {}  {}|'.format(self.field[3], self.field[4], self.field[5]))
        print('1|{}  {}  {}|'.format(self.field[6], self.field[7], self.field[8]))
        print(' -A--B--C-')


class Game(Field):
    def __init__(self):
        super().__init__()
        self.game(self.input_move())

    def move_selection(self):
        lst = []
        for index, value in enumerate(self.field):
            if value == '-':
                lst.append(index)
        key = random.sample(lst, 1)
        return key[0]

    def win(self):
        win_list = [[0, 1, 2], [2, 5, 8], [6, 7, 8], [0, 3, 6], [1, 4, 7], [0, 4, 8], [2, 4, 6], [3, 4, 5]]
        player_list = []
        computer_list = []
        for index, value in enumerate(self.field):
            if value == 'X':
                player_list.append(index)
            elif value == 'O':
                computer_list.append(index)
        for row in win_list:
            victory_player = []
            victory_computer = []
            for x in row:
                if x in player_list:
                    victory_player.append(True)
                else:
                    victory_player.append(False)
                if x in computer_list:
                    victory_computer.append(True)
                else:
                    victory_computer.append(False)
            if False not in victory_player:
                print('Победил игрок!')
                return True
            elif False not in victory_computer:
                print('Победил компьютер!')
                return True

    def input_move(self):
        while True:
            print('1 - Игрок')
            print('2 - Компьютер')
            move = input('Введите кто ходит первый (1 или 2): ')
            if move == '1' or move == '2':
                return move
            print('Вы можете ввести только 1 или 2')

    def game(self, move):
        while True:
            if move == '1':
                self.show_field()
                key = input('Сделайте ход (например: a1 или с2): ')
                row = self.field_translation(key)
                if row == 'False':
                    print('Введены неверные данные')
                    continue
                if self.make_a_move(row, 'X') is False:
                    continue
                if self.win() is True:
                    self.show_field()
                    break
                self.show_field()
                self.make_a_move(self.move_selection(), 'O')
                if self.win() is True:
                    self.show_field()
                    break
            elif move == '2':
                self.make_a_move(self.move_selection(), 'O')
                if self.win() is True:
                    self.show_field()
                    break
                self.show_field()
                key = input('Сделайте ход (например: a1 или с2): ')
                row = self.field_translation(key)
                if row == 'False':
                    print('Введены неверные данные')
                    continue
                if self.make_a_move(row, 'X') is False:
                    continue
                if self.win() is True:
                    self.show_field()
                    break
                self.show_field()

asd = Game()