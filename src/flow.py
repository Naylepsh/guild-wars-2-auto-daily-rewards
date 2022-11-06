from time import sleep
from typing import Generator, Tuple
import pyautogui
from src.inputs import clear_input, double_click, write_input
from src.credentials import Credentials
from src.resolution import Coordinates, ResolutionCoordinates


def _login(credentials: Credentials, coordinates: ResolutionCoordinates) -> None:
    def enter_input(data: str) -> None:
        double_click()
        sleep(1)
        clear_input()
        sleep(1)
        write_input(data)
        sleep(1)

    def enter_email() -> None:
        pyautogui.moveTo(*coordinates.email)
        enter_input(credentials.email)

    def enter_password() -> None:
        pyautogui.moveTo(*coordinates.password)
        enter_input(credentials.password)

    def confirm() -> None:
        pyautogui.moveTo(*coordinates.login)
        double_click()

    enter_email()
    enter_password()
    confirm()


def _launch_game(coordinates: ResolutionCoordinates) -> None:
    pyautogui.moveTo(*coordinates.play)
    double_click()


def _select_first_character(coordinates: ResolutionCoordinates) -> None:
    def enforce_click() -> None:
        # For whatever reason double clicking through pyautogui is not enough,
        # but more clicks somehow works
        for _ in range(5):
            pyautogui.click()

    pyautogui.moveTo(*coordinates.character)
    enforce_click()


def _open_reward(coordinates: Coordinates) -> None:
    def generate_locations() -> Generator[Tuple[int, int], None, None]:
        reward_icon_size = 50
        y_delta = reward_icon_size // 2

        for y in range(
            coordinates.rewards.top_y,
            coordinates.rewards.bottom_y + y_delta,
            y_delta,
        ):
            yield coordinates.rewards.x, y

    for location in generate_locations():
        pyautogui.moveTo(*location)
        double_click(button="right")


def _open_program(name: str) -> None:
    pyautogui.press("win")
    pyautogui.write(name)
    # A slight delay before confirming selection is needed.
    # Otherwise, either a different program may be opened
    # (or nothing at all can happen as well)
    sleep(2)
    pyautogui.press("enter")


def _open_gw2_launcher() -> None:
    _open_program("Guild Wars 2")


def _quit_game() -> None:
    pyautogui.keyDown("alt")
    pyautogui.press("F4")
    pyautogui.keyUp("alt")


def _check_for_remind_me_later() -> None:
    location = pyautogui.locateOnScreen("RemindMeLater.png")
    if location is not None:
        pyautogui.click(location)
        sleep(5)


def run(credentials: Credentials, coordinates: ResolutionCoordinates) -> None:
    _open_gw2_launcher()
    sleep(10)
    _login(credentials, coordinates)
    sleep(5)
    _check_for_remind_me_later()
    _launch_game(coordinates)
    sleep(20)
    _select_first_character(coordinates)
    sleep(20)
    _open_reward(coordinates)
    sleep(3)
    _quit_game()
    sleep(5)
