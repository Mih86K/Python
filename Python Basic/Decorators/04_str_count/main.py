import functools
from typing import Callable, Any


def counter(func: Callable) -> Callable:
    """ декоратор, считающий и выводящий количество вызовов декорируемой функции."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        wrapper.calls += 1
        print(f'Функция {func.__name__} была вызвана {wrapper.calls} раз')
        return func(*args, **kwargs)

    wrapper.calls = 0
    return wrapper


@counter
def add(a, b):
    return a + b


print(add(2, 3))
print(add(4, 5))
