import board
import busio 
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.encoder import EncoderHandler
from kmk.extensions.peg_rgb_matrix import RGB
from kmk.extensions.display import Display, TextData, SSD1306

keyboard = KMKKeyboard()

i2c_bus = busio.I2C(scl=board.D5, sda=board.D4)
display_driver = SSD1306(i2c=i2c_bus, device_address=0x3C)
display = Display(
    display_driver=display_driver,
    entries=[
        TextData('HACKPAD', x=0, y=0),
        TextData('Ready!', x=0, y=12),
    ],
    width=128,
    height=32,
)
keyboard.extensions.append(display)


encoder_handler = EncoderHandler()
keyboard.modules.append(encoder_handler)
encoder_handler.pins = ((board.D1, board.D2, board.D3),)
encoder_handler.map = [
    ((KC.AUDIO_VOL_UP, KC.AUDIO_VOL_DOWN, KC.MUTE),),
]

keyboard.col_pins = (board.D8, board.D9, board.D10)
keyboard.row_pins = ()
keyboard.diode_orientation = DiodeOrientation.COL2ROW
keyboard.keymap = [
    [KC.C, KC.V, KC.SPACE]
]


rgb = RGB(pixel_pin=board.D0, num_pixels=1)
keyboard.extensions.append(rgb)

if __name__ == '__main__':
    keyboard.go()