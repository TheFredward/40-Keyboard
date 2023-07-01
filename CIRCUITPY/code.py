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
LYR_1 = KC.MO(1)
LYR_2 = KC.MO(2)
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
          KC.LSFT,KC.Z,KC.X,KC.C,KC.V,KC.B,KC.N,KC.M,KC.COMM,KC.DOT,
          KC.TAB,KC.LCTL,KC.LALT,KC.LGUI,LYR_1,KC.SPC,LYR_2,KC.BSPC,KC.DEL,KC.ENT

        ],
        #Layer 1
        [
            KC.N1,KC.N2,KC.N3,KC.HOME,KC.END,KC.PGUP,KC.PGDN,KC.PSLS,KC.PMNS,KC.PAST,
            KC.N4,KC.N5,KC.N6,KC.LEFT,KC.DOWN,KC.UP,KC.RIGHT,KC.SLSH,KC.GRV,KC.CAPS,
            KC.N7,KC.N8,KC.N9,
            KC.N0,
        ]
        
]

if __name__ == '__main__':
    keyboard.go()

