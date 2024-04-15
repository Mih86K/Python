import functools
from typing import Callable, Any


def cache_results(func: Callable) -> Callable:
    """
    декоратор, который кэширует результаты вызова функции и,
    при повторном вызове с теми же аргументами, возвращает сохранённый результат.
    """
    cache = {}  # словарь для кеширования результатов

    @functools.wraps(func)
    def wrapper(*args) -> Any:
        if args not in cache:
            cache[args] = func(*args)
        # print(cache)   Проверка кеширования результатов
        return cache[args]

    return wrapper


@cache_results
def fibonacci(number):
    if number <= 1:
        return number
    return fibonacci(number - 1) + fibonacci(number - 2)


print(fibonacci(10))
print(fibonacci(10))
print(fibonacci(5))
