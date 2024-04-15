import functools
from typing import Callable, Any


def how_are_you(func: Callable) -> Callable:
    """
    Декоратор:
    при вызове декорируемой функции спрашивает у пользователя «Как дела?»,
    вне зависимости от ответа отвечает что-то вроде «А у меня не очень!»
     и только потом запускает саму функцию.
    """

    @functools.wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        no_used = input('Как дела? ')
        print('А у меня не очень! Ладно, держи свою функцию.')
        call = func(*args, **kwargs)
        return call

    return wrapper


@how_are_you
def test() -> None:
    print('<Тут что-то происходит...>')


@how_are_you
def test_2(x, y) -> None:
    result = x + y
    print(result)


test()
test_2(5, 7)
