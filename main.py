from dataclasses import dataclass
from time import sleep
from typing import Optional, Iterable, Generator, Tuple

import pyautogui
import yaml


@dataclass
class Credentials:
    email: str
    password: str


def get_credentials() -> Iterable[Credentials]:
    with open('./accounts.yml', 'r', encoding='utf-8') as f:
        credentials = yaml.full_load(f)
        return map(lambda creds: Credentials(email=creds['email'], password=creds['password']), credentials)  # noqa


def double_click(button='left') -> None:
    pyautogui.click(button=button)
    pyautogui.click(button=button)


def clear_input() -> None:
    pyautogui.keyDown('ctrl')
    pyautogui.press('a')
    pyautogui.keyUp('ctrl')
    pyautogui.press('backspace')


def open_gw2_launcher() -> None:
    pyautogui.press('win')
    pyautogui.write('Guild Wars 2')
    pyautogui.press('enter')


def login(credentials: Optional[Credentials] = None) -> None:
    def enter_input(data: str) -> None:
        double_click()
        sleep(1)
        clear_input()
        sleep(1)
        pyautogui.write(data)
        sleep(1)

    def enter_email() -> None:
        pyautogui.moveTo(520, 560)
        enter_input(credentials.email)

    def enter_password() -> None:
        pyautogui.moveTo(520, 640)
        enter_input(credentials.password)

    if credentials:
        enter_email()
        enter_password()

    pyautogui.moveTo(x=480, y=720)
    double_click()


def launch_game() -> None:
    pyautogui.moveTo(1200, 840)
    double_click()


def select_first_character() -> None:
    def enforce_click() -> None:
        # For whatever reason double clicking through pyautogui is not enough, but more clicks somehow works # noqa
        for _ in range(5):
            pyautogui.click()

    pyautogui.moveTo(380, 980)
    enforce_click()


def open_reward() -> None:
    def generate_locations() -> Generator[Tuple[int, int], None, None]:
        x = 1860
        top_y = 680
        bottom_y = 1030
        reward_icon_size = 50
        y_delta = reward_icon_size // 2

        for y in range(top_y, bottom_y + y_delta, y_delta):
            yield x, y

    for location in generate_locations():
        pyautogui.moveTo(*location)
        double_click(button='right')


def quit_game() -> None:
    pyautogui.keyDown('alt')
    pyautogui.press('F4')
    pyautogui.keyUp('alt')


def main() -> None:
    for credentials in get_credentials():
        open_gw2_launcher()
        sleep(10)
        login(credentials)
        sleep(5)
        launch_game()
        sleep(20)
        select_first_character()
        sleep(20)
        open_reward()
        sleep(3)
        quit_game()
        sleep(5)


if __name__ == '__main__':
    main()
