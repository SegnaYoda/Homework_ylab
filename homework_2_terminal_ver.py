"""«Обратные крестики-нолики».

Внесите параметры в объект game размер игрвого поля и количество
повторений X-O для проигрыша.

Поле по умолчанию 10 x 10 с правилом «Пять в ряд» – проигрывает тот,
у кого получился вертикальный, горизонтальный или диагональный ряд
из пяти своих фигур (крестиков/ноликов).
"""
import random


class ConsoleInfoOutput:
    """Класс для вывода информации в терминал."""

    def print_maps(self, maps_gen):
        """Вывод игровой сетки в терминал."""
        self.maps_gen = maps_gen
        last_number = len(str(len(self.maps_gen)**2))
        """Вывод карты на экран."""
        for i in self.maps_gen:
            a = ''
            for j in i:
                a += (' ') * (last_number - len(str(j))) + str(j) + " | "
            print(a)
        self.line = '_' * len(a)  # нижнее подчеркивание для вывода результатов игры

    def start_info(self):
        print("Приветствую, человек! Ты играешь в игру «Обратные крестики-нолики». \
               \nПравила тебе знакомы, так что приступим, ты начинаешь.")

    def comp_turn(self, step):
        """Вывод хода компьютера."""
        print(f"Компьютер делает ход: {step}")

    def winner_output(self, win):
        """Вывод информации о победителе."""
        if win == "X":
            print(self.line, '\n', "Человек, вы проиграли!")
            self.print_maps(self.maps_gen)
            return True
        elif win == "O":
            print(self.line, '\n', "Компьютер проиграл!")
            self.print_maps(self.maps_gen)
            return True

    def nobody_winner(self):
        """В случаи ничьи."""
        print(self.line, '\n', "Ничья!")
        return True

    def warning_msg(self):
        """Предостережение, человек."""
        print("Человек, будьте внимательнее.")
        print("Вы выбрали ранее заполненную или несуществующую клетку.")


class Generator:
    """Инициализация игровой сетки и списка доступных ходов.

    Объект класса принимает размер сетки.
    По умолчанию 10.
    """

    def __init__(self, n=10):
        """Инициализация игровой сетки и списка доступных ходов.

        Размер сетки по умолчанию 10."""
        self.maps_gen = [[0] * n for i in range(n)]
        self.pc_choice = []  # Инициализация списка доступных ходов.
        self.n = n
        d = 0
        for i in range(len(self.maps_gen)):
            for j in range(len(self.maps_gen[i])):
                d += 1
                self.maps_gen[i][j] = d
                self.pc_choice.append(d)

    def init_play_board(self):
        """Инициализация игровой сетки."""
        return self.maps_gen

    def ai_grid(self):
        """Инициализация списка доступных ходов."""
        return self.pc_choice

    def gui_config(self):
        return self.n


class GameXO:
    """Основная программа игры."""

    output_msg = ConsoleInfoOutput()
    output_msg.start_info()

    def __init__(self, n, lengthXO):
        self.generator_game = Generator(n)    # можно задать размер сетки, 10 по умолчанию
        self.game_over = False
        self.human = True
        self.maps_gen = self.generator_game.init_play_board()  # генерация игрового поля
        self.list_choice = self.generator_game.ai_grid()   # генерация списка оставшихся доступных клеток для хода
        self.n = n
        self.lengthXO = lengthXO

    def start_game(self):
        """Основная программа, ходы игрока и AI."""
        while self.game_over is False:
            # 1. Показываем карту
            self.output_msg.print_maps(self.maps_gen)
            # 2. Спросим у играющего куда делать ход
            if self.human:
                symbol = "X"
                step = input("Человек, ваш ход: ")
                if step.isnumeric():
                    step = int(step)
                while step not in self.list_choice:
                    self.output_msg.warning_msg()
                    step = input("Человек, ваш повторный ход: ")
                    if step.isnumeric():
                        step = int(step)
                self.list_choice.remove(step)  # удаляем из списка вариантов для пк
            else:
                symbol = "O"
                step = self.ai_choices(self.list_choice)
                self.output_msg.comp_turn(step)
            # 3. Если компьютер нашел куда сделать ход, то играем. Если нет, то ничья.
            if step:
                self.step_for_maps(self.maps_gen, step, symbol)  # делаем ход в указанную ячейку
                win = self.get_result()  # определим победителя
                if win:
                    return self.output_msg.winner_output(win)
                elif len(self.list_choice) == 1:
                    return self.output_msg.nobody_winner()

            self.human = not(self.human)

    def ai_choices(self, list_choice):
        """Искусственный интеллект использует рандом: выбор хода."""
        ai_choice_is = random.choice(list_choice)
        list_choice.remove(ai_choice_is)
        return ai_choice_is

    def step_for_maps(self, maps_gen, step, symbol):
        """Сделать ход в ячейку."""
        for i in range(self.n):
            for j in range(self.n):
                if step == maps_gen[i][j]:
                    maps_gen[i][j] = symbol

    def get_result(self):
        """Поиск линии с нужным количеством X и O на победных линиях."""
        for i in range(self.n):
            for j in range(self.n):
                if self.check(i, j, (0, 1)) or self.check(i, j, (1, 0)) or self.check(i, j, (1, 1)):
                    return self.maps_gen[i][j]

        return ""

    def check(self, i, j, direction):
        """Проверка совпадений Х или О."""
        for k in range(self.lengthXO):
            ii = i + direction[0] * k
            jj = j + direction[1] * k
            if ii >= self.n or jj >= self.n or self.maps_gen[i][j] != self.maps_gen[ii][jj]:
                return False
        return True


game = GameXO(10, 5)    # Внесите размер игрвого поля и количество повторений X-O для проигрыша
game.start_game()
