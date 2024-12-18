from zero_hid import Keyboard, KeyCodes
import math
with Keyboard() as k:
    pi = 0
    for i in range(1001):
        sign = (-1) ** i
        pi += sign * 4 / (2 * i + 1)
        # k.type(str(abs(math.pi - pi)))
        k.type(str(abs(pi)))
        k.press([], KeyCodes.KEY_ENTER)