from time import sleep

import pyautogui


def double_click(button='left') -> None:
    pyautogui.click(button=button)
    pyautogui.click(button=button)


def open_gw2_launcher() -> None:
    pyautogui.press('win')
    pyautogui.write('Guild Wars 2')
    pyautogui.press('enter')


def login() -> None:
    pyautogui.moveTo(x=480, y=720)
    double_click()


def launch_game() -> None:
    pyautogui.moveTo(1200, 840)
    double_click()


def select_first_character() -> None:
    def enforce_click() -> None:
        # For whatever reason double clicking through pyautogui is not enough, but more clicks somehow works
        for _ in range(5):
            pyautogui.click()

    pyautogui.moveTo(380, 980)
    enforce_click()


def open_reward() -> None:
    top_right = (1860, 1030)
    bottom_right = (1860, 680)

    rewards_locations = [top_right, bottom_right]
    for location in rewards_locations:
        pyautogui.moveTo(*location)
        double_click(button='right')


def quit_game() -> None:
    pyautogui.keyDown('alt')
    pyautogui.press('F4')
    pyautogui.keyUp('alt')


def main() -> None:
    open_gw2_launcher()
    sleep(10)
    login()
    sleep(5)
    launch_game()
    sleep(20)
    select_first_character()
    sleep(20)
    open_reward()
    sleep(3)
    quit_game()


if __name__ == '__main__':
    main()
