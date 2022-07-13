"""Декоратор с кешированием результата.

В качестве базы данных для хранения используется Redis.

Необходимо, чтобы в вашей системе был установлен Docker.
Введите следующие команды в терминал для создания docker контейнера:
1.  `docker pull redis`
После выполняем загрузку образа Redis:
2.  `docker run --name server-redis -p 6379:6379 -d redis`

Сервис запущен на порту 6379; к нему можно обращаться по имени server-redis.
"""
import redis


def decorator_multiplier(func):
    """Декоратор с кешированием результата."""
    redis_client = redis.Redis(host='127.0.0.1', port=6379, db=0, decode_responses=True)

    def wrapper(number: int):
        """Внутренний метод декоратора для получения аргументов декорируемой функции."""
        try:
            cache_value = redis_client.get(number)
            if cache_value is not None:
                print("Вывод из Redis -", cache_value)
                return cache_value
            else:
                result_func = func(number)
                print("Запись в БД -", result_func)
                redis_client.set(number, result_func)
                return result_func
        except Exception:
            print("Ошибка подключения к контейнеру Redis")
    redis_client.close()
    return wrapper


@decorator_multiplier
def multiplier(number: int):
    """Чистая функция."""
    print("Работает чистая функция.")
    return number * 2


list_check = [2, 3, 4, 5, 8, 2, 3, 4, 14, 15]

if __name__ == "__main__":
    for i in list_check:
        multiplier(i)
