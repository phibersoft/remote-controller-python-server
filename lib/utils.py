from typing import Union
from colorama import init
from termcolor import colored

init()


def logger(message: str, level: Union["info", "warning", "error"] = 'info') -> None:
    if level == "info":
        print(colored(message, 'green'))
    elif level == "warning":
        print(colored(message, 'yellow'))
    elif level == "error":
        print(colored(message, 'red'))
    else:
        print(colored(message, 'white'))
