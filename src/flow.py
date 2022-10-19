from time import sleep
from typing import Generator, Tuple
import pyautogui
from src.inputs import clear_input, double_click, write_input
from src.credentials import Credentials


def _open_program(name: str) -> None:
    pyautogui.press("win")
    pyautogui.write(name)
    pyautogui.press("enter")


def _open_gw2_launcher() -> None:
    _open_program("Guild Wars 2")


def _login(credentials: Credentials) -> None:
    def enter_input(data: str) -> None:
        double_click()
        sleep(1)
        clear_input()
        sleep(1)
        write_input(data)
        sleep(1)

    def enter_email() -> None:
        pyautogui.moveTo(520, 560)
        enter_input(credentials.email)

    def enter_password() -> None:
        pyautogui.moveTo(520, 640)
        enter_input(credentials.password)

    def confirm() -> None:
        pyautogui.moveTo(480, 720)
        double_click()

    enter_email()
    enter_password()
    confirm()


def _launch_game() -> None:
    pyautogui.moveTo(1200, 840)
    double_click()


def _select_first_character() -> None:
    def enforce_click() -> None:
        # For whatever reason double clicking through pyautogui is not enough,
        # but more clicks somehow works
        for _ in range(5):
            pyautogui.click()

    pyautogui.moveTo(755, 980)
    enforce_click()


def _open_reward() -> None:
    def generate_locations() -> Generator[Tuple[int, int], None, None]:
        x = 1880
        top_y = 680
        bottom_y = 1030
        reward_icon_size = 50
        y_delta = reward_icon_size // 2

        for y in range(top_y, bottom_y + y_delta, y_delta):
            yield x, y

    for location in generate_locations():
        pyautogui.moveTo(*location)
        double_click(button="right")


def _quit_game() -> None:
    pyautogui.keyDown("alt")
    pyautogui.press("F4")
    pyautogui.keyUp("alt")


def _check_for_remind_me_later() -> None:
    if pyautogui.locateOnScreen("RemindMeLater.png") is not None:
        location = pyautogui.locateOnScreen("RemindMeLater.png")
        pyautogui.click(location)
        sleep(5)


def run(credentials: Credentials) -> None:
    _open_gw2_launcher()
    sleep(10)
    _login(credentials)
    sleep(5)
    _check_for_remind_me_later()
    _launch_game()
    sleep(20)
    _select_first_character()
    sleep(20)
    _open_reward()
    sleep(3)
    _quit_game()
    sleep(5)
