import pyautogui

from lib.utils import logger

robotjs_translations = {
    'audio_vol_up': 'volumeup',
    'audio_vol_down': 'volumedown',
    'audio_mute': 'volumemute',
    'audio_play': 'mediaplaypause',
    'audio_next': 'nexttrack',
    'audio_prev': 'prevtrack',
    'audio_stop': 'stop',
    'audio_pause': 'pause',
    'brightness_up': 'brightnessup',
    'brightness_down': 'brightnessdown',
}


def action_keypress(key: str, modifs: list[str] | str) -> None:
    if isinstance(modifs, str):
        if modifs == "[]":
            modifs = []
        if modifs == "[shift]":
            modifs = ["shift"]

    logger(f'Key Pressed: {key} {modifs if modifs else ""}')

    if len(modifs) != 0:
        pyautogui.hotkey(*modifs, key)
    else:
        pyautogui.keyDown(robotjs_translations[key] if key in robotjs_translations else key)
