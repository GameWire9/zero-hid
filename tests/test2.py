from zero_hid import Mouse, Keyboard, KeyCodes
with Keyboard() as k, Mouse() as rel_mouse:
    # k.press([KeyCodes.MOD_LEFT_ALT, KeyCodes.MOD_LEFT_SHIFT, KeyCodes.KEY_TAB])
    k.press([KeyCodes.MOD_LEFT_GUI])