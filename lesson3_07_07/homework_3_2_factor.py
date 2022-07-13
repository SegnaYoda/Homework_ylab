"""Декоратор с параметрами.

Предназначен для повторного выполнения декорируемой функции через некоторое время.
Использует наивный экспоненциальный рост времени повтора (factor) до граничного
времени ожидания (border_sleep_time).
"""
import functools
import time


def decorator_with_params(call_count, start_sleep_time, factor, border_sleep_time):
    """Декоратор с параметрами."""
    print("Кол-во запусков =", call_count)

    def decorator_repeat(func):
        """Принимаем в качестве аргумента основную декорируемую функцию."""
        @functools.wraps(func)
        def wrapper_repeat(number: int):
            """Используя декоратор «functool.wraps» декорируем внутреннюю функцию."""
            t = start_sleep_time
            if call_count != 0:
                print("Начало работы")
                for i in range(1, call_count + 1):
                    if t < border_sleep_time:
                        t = t * factor
                        if t >= border_sleep_time:
                            t = border_sleep_time
                    rslt = func(number)
                    time.sleep(t)
                    print(f"Запуск номер {i}. Ожидание: {t} секунд. Результат декорируемой функций = {rslt}.")
                print("Конец работы")
                return rslt
        return wrapper_repeat
    return decorator_repeat


@decorator_with_params(call_count=4, start_sleep_time=0.1, factor=2, border_sleep_time=2)
def multiplier(number: int):
    """Чистая функция."""
    return number * 2


if __name__ == "__main__":
    multiplier(21)
