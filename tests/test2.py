from zero_hid import Mouse, Keyboard, KeyCodes
from time import sleep
with Keyboard() as k, Mouse() as rel_mouse:
    sleep(2)
    k.press([KeyCodes.MOD_LEFT_GUI], KeyCodes.KEY_TAB, False)
    sleep(1)
    k.press([], KeyCodes.KEY_LEFT)
    sleep(1)
    k.press([], KeyCodes.KEY_ENTER)
    sleep(0.5)