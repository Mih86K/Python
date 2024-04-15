import functools
import time
from typing import Callable, Any


def slow_func(func: Callable) -> Callable:
    """декоратор, который перед выполнением декорируемой функции ждёт несколько секунд."""

    @functools.wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        print('Ожидайте, идет загрузка . . . . .')
        time.sleep(5)
        timing = func()
        return timing

    return wrapper


@slow_func
def test():
    print('\nГотово!')


test()
