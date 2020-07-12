"""Fedorenko Dmitriy"""
EMPTY = 0
ROCK = 1
FISH = 2
SHRIMP = 3
class LifeGame():
    """
    Class for Game life
    """
    def __init__(self, pole):
        self.len_x = len(pole)
        if self.len_x != 0:
            self.len_y = len(pole[0])
        else:
            self.len_y = 0
        self.pole = [[0 for i in range(self.len_y + 2)] for j in range(self.len_x + 2)]
        for i in range(self.len_x + 2):
            for j in range(self.len_y + 2):
                if i > 0 and j > 0 and i < self.len_x + 1 and j < self.len_y + 1:
                    self.pole[i][j] = pole[i - 1][j - 1]
                if i == 0:
                    self.pole[i][j] = ROCK
                if i == self.len_x + 1:
                    self.pole[i][j] = ROCK
                if j == 0:
                    self.pole[i][j] = ROCK
                if j == self.len_y + 1:
                    self.pole[i][j] = ROCK

    def _get_next_generation_for_the_animal(self, animal, mas):
        for i in range(1, self.len_x + 1):
            for j in range(1, self.len_y + 1):
                if self.pole[i][j] == ROCK:
                    mas[i - 1][j - 1] = ROCK
                number = self._number_of_neighbors(i, j, animal)
                if (number < 2 or number > 3) and self.pole[i][j] == animal:
                    mas[i - 1][j - 1] = EMPTY
                elif (number == 2 or number == 3) and self.pole[i][j] == animal:
                    mas[i - 1][j - 1] = animal
                elif number == 3 and self.pole[i][j] == EMPTY and mas[i - 1][j - 1] == EMPTY:
                    mas[i - 1][j - 1] = animal
        return mas

    def _number_of_neighbors(self, x, y, animal):
        number = 0
        if self.pole[x + 1][y] == animal:
            number += 1
        if self.pole[x + 1][y + 1] == animal:
            number += 1
        if self.pole[x][y + 1] == animal:
            number += 1
        if self.pole[x - 1][y + 1] == animal:
            number += 1
        if self.pole[x - 1][y] == animal:
            number += 1
        if self.pole[x -1][y - 1] == animal:
            number += 1
        if self.pole[x][y - 1] == animal:
            number += 1
        if self.pole[x + 1][y - 1] == animal:
            number += 1
        return number

    def get_next_generation(self):
        """
        New eneration of all cells
        """
        new_generation = [[0 for i in range(self.len_y)] for j in range(self.len_x)]
        new_generation = self._get_next_generation_for_the_animal(FISH, new_generation)
        new_generation = self._get_next_generation_for_the_animal(SHRIMP, new_generation)
        for i in range(1, self.len_x + 2):
            for j in range(1, self.len_y + 2):
                if i < self.len_x + 1 and j < self.len_y + 1:
                    self.pole[i][j] = new_generation[i - 1][j - 1]
        return new_generation
