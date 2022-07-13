"""«Обратные крестики-нолики» в графическом окне.

Внесите параметры в объект game размер игрового поля и количество
повторений X-O для проигрыша.

Поле по умолчанию 10 x 10 с правилом «Пять в ряд» – проигрывает тот,
у кого получился вертикальный, горизонтальный или диагональный ряд
из пяти своих фигур (крестиков/ноликов).
"""
import random
import tkinter.messagebox as mb
from tkinter import Button, Tk


class App():
    """Класс для вывода информации."""

    def tkinter_win_out(self, win):
        """Вывод информации о победе."""
        if win == "X":
            msg = "Вы проиграли!"
            mb.showinfo("Эй, человек", msg)
            return True
        elif win == "O":
            msg = "Ну вот проиграл!"
            mb.showinfo("Компьютер проиграл", msg)
            return True

    def tk_nobody_winner(self):
        """В случаи ничьи."""
        msg = "Ничья!"
        mb.showinfo("Ничья!", msg)
        return True


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


class GameOnGUI:
    """Основная программа игры."""

    output_tkinter = App()

    def __init__(self, n, lengthXO):
        self.generator_game = Generator(n)
        self.game_over = False
        self.human = True
        self.maps_gen = self.generator_game.init_play_board()
        self.list_choice = self.generator_game.ai_grid()
        self.n = n
        self.lengthXO = lengthXO

    def start_game_gui(self):
        """Генерация игрвого поля."""
        self.buttons = [Button(window, text=i + 1, width=10, height=5, font=("Arial Bold", 10), command=lambda x=i: self.clicked(x)) for i in range(self.n * self.n)]
        row, col = 0, 0
        self.list_choice = []
        for i in range(len(self.buttons)):
            self.buttons[i].grid(row=row, column=col)
            col += 1
            self.list_choice.append(i + 1)
            if col == (self.n):
                row += 1
                col = 0

    def clicked(self, pressed_btn):
        """Основная программа, ходы игрока и AI."""
        # 1. Показываем карту, ход человека
        self.buttons[pressed_btn].config(text="X", font=("Arial Bold", 10), bg="blue", state="disabled")
        symbol = "X"
        step = pressed_btn + 1
        self.list_choice.remove(step)  # удаляем из списка вариантов для пк
        self.step_for_maps(self.maps_gen, step, symbol)  # делаем ход в указанную ячейку
        win = self.get_result()  # определим победителя
        self.check_winner(win)

        # 2. Если компьютер нашел куда сделать ход, то играем. Если нет, то ничья.
        symbol = "O"
        step = self.ai_choices(self.list_choice)
        # делаем ход в указанную ячейку для GUI и для терминала
        self.buttons[step - 1].config(text="O", font=("Arial Bold", 10), bg="yellow", state="disabled")
        self.step_for_maps(self.maps_gen, step, symbol)
        win = self.get_result()  # определим победителя
        self.check_winner(win)

    def check_winner(self, win):
        """Для проверки победителя."""
        if win:
            self.output_tkinter.tkinter_win_out(win)
        elif len(self.list_choice) == 0:
            self.output_tkinter.tk_nobody_winner()

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
                if self.check(i, j, (0, 1)) or self.check(i, j, (1, 0)) or self.check(i, j, (1, 1)) or self.check(i, j, (1, -1)):
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


window = Tk()
window.title("Добро пожаловать в приложение PythonRu")
window.geometry('900x920')

game_on_gui = GameOnGUI(10, 5)  # Внесите размер игрвого поля и количество повторений X-O для проигрыша
game_on_gui.start_game_gui()
window.mainloop()
