import pyautogui

from lib.utils import logger

screens = {
    "1536x864": {
        "accept-match-movement": {
            "x": 765,
            "y": 613,
        },
        "choose-hero-movement": {
            "x": 761,
            "y": 653,
        },
        "select-hero-first-movement": {
            "x": 928,
            "y": 158,
        },
        "select-hero-last-movement": {
            "x": 505,
            "y": 221,
        },
    },
    "1920x1080": {
        "accept-match-movement": {
            "x": 950,
            "y": 710,
        },
        "choose-hero-movement": {
            "x": 970,
            "y": 770,
        },
        "select-hero-first-movement": {
            "x": 1080,
            "y": 258,
        },
        "select-hero-last-movement": {
            "x": 710,
            "y": 321,
        },
    },
}


def lol(action: str, hero: str) -> None:
    # Get screen size
    screen_size = pyautogui.size()
    screen = f"{screen_size[0]}x{screen_size[1]}"

    # Check if screen size is supported
    if screen not in screens:
        logger(f"Screen size not supported: {screen}", "error")
    else:
        logger(f"LoL Action: {action} {hero if hero else ''}")
        # Switch case for actions "select-hero", "choose-hero", "accept-match"
        if action == "select-hero":
            pyautogui.moveTo(screens[screen]["select-hero-first-movement"]["x"],
                             screens[screen]["select-hero-first-movement"]["y"])
            pyautogui.leftClick()
            # press control + a
            pyautogui.keyDown("ctrl")
            pyautogui.press("a")
            pyautogui.keyUp("ctrl")

            # type hero name
            pyautogui.typewrite(hero)

            # move mouse to select area
            pyautogui.moveTo(screens[screen]["select-hero-last-movement"]["x"],
                             screens[screen]["select-hero-last-movement"]["y"])
            pyautogui.leftClick()
        elif action == "choose-hero":
            pyautogui.moveTo(screens[screen]["choose-hero-movement"]["x"], screens[screen]["choose-hero-movement"]["y"])
            pyautogui.leftClick()
        elif action == "accept-match":
            pyautogui.moveTo(screens[screen]["accept-match-movement"]["x"],
                             screens[screen]["accept-match-movement"]["y"])
            pyautogui.leftClick()
        else:
            logger(f"Action not supported: {action}", "error")
