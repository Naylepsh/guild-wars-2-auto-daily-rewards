from typing import Union
from time import sleep
import pyautogui
import pyperclip
from pynput.keyboard import Key, Controller

keyboard = Controller()


def double_click(button="left") -> None:
    pyautogui.click(button=button)
    pyautogui.click(button=button)


def clear_input() -> None:
    with keyboard.pressed(Key.ctrl_l):
        _press("a")
    _press(Key.backspace)


def write_input(input: str) -> None:
    pyperclip.copy(input)
    paste()


def paste() -> None:
    with keyboard.pressed(Key.ctrl_l):
        _press("v")


def _press(key: Union[str, Key]) -> None:
    keyboard.press(key)
    sleep(1)
    keyboard.release(key)
