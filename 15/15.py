import random
class Field:

    def __init__(self):
        self.number_of_chips = 15
        self.field = self._create_field()
  
    def _create_field(self):
        field = random.sample(range(1, self.number_of_chips + 1), self.number_of_chips)
        field.append('X')
        return field

    def show_field(self):
        print('|-----------------|')
        for line_start in range(0,self.number_of_chips + 1,4):
            line_end = line_start + 4
            line = self.field[line_start:line_end]
            print('| {} {} {} {} |'.format(str(line[0]).ljust(3), str(line[1]).ljust(3), str(line[2]).ljust(3), str(line[3]).ljust(3)))
        print('|-----------------|')
   
    def move(self, key):
        dic = {'s': 4, 'd': 1, 'a': -1, 'w': -4}
        delta = dic[key]
        current = self.field.index('X')
        if key == 's' and current >= 12:
            print('Невозможно сделать ход')
        elif key == 'w' and current < 4:
            print('Невозможно сделать ход')
        elif key == 'd' and current % 4 == 3:
            print('Невозможно сделать ход')
        elif key == 'a' and current % 4 == 0:
            print('Невозможно сделать ход')
        else:
            self.field[current + delta], self.field[current] = self.field[current], self.field[current + delta]

        
class Game:

    def __init__(self):
        self.game_of = Field()
        self.game()
   
    def game(self):
        keys = ('w', 'a', 's', 'd')
        win_list = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 'X')
        while True:
            self.game_of.show_field()
            key = input('Сделайте ход (w,a,s,d): ')
            if key in keys:
                self.game_of.move(key)
            else:
                print('Введены неверные данные')        
            if self.game_of.field == win_list:
                print('Вы выиграли!')
                break

                
instance = Game()
