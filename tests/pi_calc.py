from zero_hid import Keyboard, KeyCodes
with Keyboard() as k:
    pi = 0
    for i in range(10):
        sign = (-1) ** i
        pi += sign * 4 / (2 * i + 1)
    k.type(str(pi))
    k.press([], KeyCodes.KEY_ENTER)