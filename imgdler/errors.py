from rich.console import Console
from rich.text import Text

INFO_COLOR = "#b3b3ff"
WARNING_COLOR = "#f0f033"
ERROR_COLOR = "#fb0a0a"
SUCCESS_COLOR = "#57ff57"


def info(message: str):
    Console().print(Text(message, INFO_COLOR))

def warning(message: str):
    Console().print(Text(message, WARNING_COLOR))

def error(message: str):
    Console().print(Text(message, ERROR_COLOR))

def success(message: str):
    Console().print(Text(message, SUCCESS_COLOR))
