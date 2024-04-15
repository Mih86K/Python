import functools
import logging
import datetime
from typing import Callable, Any


logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s - %(message)s",
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler("function_errors.log")
    ]
)

def logging_decorator(func: Callable) -> Callable:
    """"
    декоратор logging, который будет отвечать за логирование функций.
    На экран выводится название функции и её документация.
    Если во время выполнения декорируемой функции возникла ошибка, то в файл function_errors.log
    записываются названия функции и ошибки.
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        logging.info(f"Function: {func.__name__}")
        logging.info(f"Documentation: {func.__doc__}")

        try:
            return func(*args, **kwargs)
        except Exception as e:
            error_message = f"{func.__name__}: {str(e)} \n"
            error_message += f"Time: {datetime.datetime.now()} \n"
            logging.error(error_message, exc_info=True, stack_info=True)

    return wrapper


@logging_decorator
def test() -> None:
    print('<Тут что-то происходит...>')


test()


