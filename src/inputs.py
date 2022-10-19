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
    for char in input:
        if char in SPECIAL_CHARS:
            pyperclip.copy(char)
            paste()
        else:
            pyautogui.write(char)


def paste() -> None:
    pyautogui.keyDown("ctrl")
    pyautogui.press("v")
    pyautogui.keyUp("ctrl")


SPECIAL_CHARS = "+"
