import random

class Field:
    def __init__(self):
        self.field = self._create_field()
        self.number_of_chips = 15

    def _create_field(self):
        self.number_of_chips = 15
        some_field = random.sample(range(1, self.number_of_chips + 1), self.number_of_chips)
        some_field.append('X')
        return some_field

    def show_field(self):
        start = 0
        end = 0
        while end < (self.number_of_chips + 1):
            end += 4
            field = self.field[start:end]
            if start == 0:
                print('|-----------------|')
            print('| {} {} {} {} |'.format(str(field[0]).ljust(3), str(field[1]).ljust(3), str(field[2]).ljust(3), str(field[3]).ljust(3)))
            start += 4
            if end == (self.number_of_chips + 1):
                print('|-----------------|')

    def move(self, key):
        dic = {'s': 4, 'd': 1, 'a': -1, 'w': -4}
        delta = dic[key]
        current = self.field.index('X')
        if key == 's' and current >= 12:
            print('Невозможно сделать ход')
            return
        if key == 'w' and current < 4:
            print('Невозможно сделать ход')
            return
        if key == 'd' and (current == 3 or current == 7 or current == 11 or current == 15):
            print('Невозможно сделать ход')
            return
        if key == 'a' and (current == 0 or current == 4 or current == 8 or current == 12):
            print('Невозможно сделать ход')
            return
        self.field[current + delta], self.field[current] = self.field[current], self.field[current + delta]


class Game:
    def __init__(self):
        self.game_of = Field()

    def game(self):
        keys = ['w', 'a', 's', 'd']
        win_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 'X']
        while True:
            if self.game_of.field == win_list:
                print('Вы выиграли!')
                break
            self.game_of.show_field()
            key = input('Сделайте ход (w,a,s,d): ')
            if key in keys:
                self.game_of.move(key)
            else:
                print('Введены неверные данные')


asd = Game()
asd.game()