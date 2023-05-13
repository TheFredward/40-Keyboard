print("Starting")

import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.layers import Layers
from kmk.handlers.sequences import send_string, simple_key_sequence

keyboard = KMKKeyboard()
keyboard.modules.append(Layers())
keyboard.debug_enabled =True
keyboard.row_pins = (board.GP18,board.GP19,board.GP20,board.GP21)
keyboard.col_pins = (board.GP2,board.GP3,board.GP4,board.GP5,board.GP6,board.GP7,board.GP8,board.GP9,board.GP10,board.GP11)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

# Layer keys
Temp = KC.MO(1)
# Custom key combos
C_EDGE = send_string("msedge")
RUN_EDGE = simple_key_sequence( ( KC.LWIN(KC.R), KC.MACRO_SLEEP_MS(1000), C_EDGE, KC.MACRO_SLEEP_MS(1000), KC.ENT) )
TST= send_string("layer 1")
TSK_MGR = KC.LCTRL(KC.LSFT(KC.ESC))

keyboard.keymap = [
        #BASE Layer
        [ 
          KC.Q,KC.W,KC.E,KC.R,KC.T,KC.Y,KC.U,KC.I,KC.O,KC.P,
          KC.A,KC.S,KC.D,KC.F,KC.G,KC.H,KC.J,KC.K,KC.L,KC.QUOT,
          KC.Z,KC.X,KC.C,KC.V,KC.B,KC.N,KC.M,KC.COMM,KC.DOT,KC.ENT,

        ],
        #Layer 1
        [
           TST, 
        ]
        
]

if __name__ == '__main__':
    keyboard.go()

