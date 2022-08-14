class Tomato:
    states = {0: '_', 1: 'цветок', 2: 'зеленый', 3: 'красный'}
    def __init__(self, index):
        self._index = index
        self._state = 0
    def grow(self):
        self._change_state()
    def is_ripe(self):
        if self._state == 3:
            return True
        return False
    def _change_state(self):
        if self._state < 3:
            self._state += 1
        self._print_state()
    def _print_state(self):
        print(f'Томат {self._index} стал {Tomato.states[self._state]}')

class TomatoBush:
    def __init__(self, num):
        self.tomatoes = [Tomato(index) for index in range(1, num)]
    def grow_all(self):
        for tomato in self.tomatoes:
            tomato.grow()
    def all_are_ripe(self):
        return all([tomato.is_ripe() for tomato in self.tomatoes])
    def give_away_all(self):
        self.tomatoes = []

class Gardener:
    def __init__(self, name, plant):
        self.name = name
        self._plant = plant
    def work(self):
        print('Садовник ухаживает за томатами.')
        self._plant.grow_all()
        print('Садовник закончил ухаживать за томатами.')
    def harvest(self):
        print('Садовник должен собрать урожай.')
        if self._plant.all_are_ripe():
            self._plant.give_away_all()
            print('Сбор урожая окончен.')
        else:
            print('Собирать урожай рано, томат еще не созрел.')

def main():
    print('Справка: томаты необходимо собирать, если они достигли стадии "зеленый".')
    great_tomato_bush = TomatoBush(7)
    gardener = Gardener('Эд', great_tomato_bush)
    gardener.work()
    gardener.work()
    gardener.harvest()
    gardener.work()
    gardener.harvest()

main()