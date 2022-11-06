import pyautogui
import pyperclip


def double_click(button="left") -> None:
    pyautogui.click(button=button)
    pyautogui.click(button=button)


def clear_input() -> None:
    pyautogui.keyDown("ctrl")
    pyautogui.press("a")
    pyautogui.keyUp("ctrl")
    pyautogui.press("backspace")


def write_input(input: str) -> None:
    pyperclip.copy(input)
    paste()


def paste() -> None:
    pyautogui.keyDown("ctrl")
    pyautogui.press("v")
    pyautogui.keyUp("ctrl")
