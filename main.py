import board

from kmk.kmk_keyboard import KMKKeyboard as _KMKKeyboard, InternalState
from kmk.consts import LeaderMode, UnicodeMode
from kmk.matrix import DiodeOrientation
from kmk.handlers.sequences import *
from kmk.keys import KC, make_key
from keymap_italian import *
from kmk import led, RGB


print(dir(board))


class KMKKeyboard(_KMKKeyboard):
    col_pins = (board.GP1, board.GP2, board.GP3, board.GP4,  board.GP5,  board.GP6,
                board.GP7, board.GP8, board.GP9, board.GP10, board.GP11, board.GP12)
    row_pins = (board.GP14, board.GP15, board.GP16, board.GP17)
    diode_orientation = DiodeOrientation.COLUMNS

keyboard = KMKKeyboard()

keyboard.rgb_pixel_pin = board.GP28

keyboard.rgb_config['num_pixels'] = 48
keyboard.rgb_config['val_limit'] = 255
keyboard.rgb_config['rgb_order'] = (1, 0, 2)

keyboard.rgb_config['hue_step'] = 360
keyboard.rgb_config['sat_step'] = 100
keyboard.rgb_config['val_step'] = 100

keyboard.rgb_config['hue_default'] = 0
keyboard.rgb_config['sat_default'] = 0
keyboard.rgb_config['val_default'] = 100

keyboard.rgb_config['knight_effect_length'] = 1
keyboard.rgb_config['animation_mode'] = 'static'
keyboard.rgb_config['animation_speed'] = 10


# ------------------User level config variables ---------------------------------------
keyboard.unicode_mode = UnicodeMode.WINC
keyboard.tap_time = 350
keyboard.leader_timeout = 2000
#keyboard.debug_enabled = True

# ------------------Italian Re-Mapping ------------------------------------------------
# imported #

# ------------------Alias Re-Mapping --------------------------------------------------
_______ = KC.TRNS
XXXXXXX = KC.NO

# ------------------Animation Machine -------------------------------------------------
class StateControll:
    PreState = 100 # initialization is different from any possible layer value
    
def Led_Array(keycaps):
    temp_keycaps = keycaps[36:48] + \
                   keycaps[24:36][::-1] + \
                   keycaps[12:24] + \
                   keycaps[0:12][::-1]
    
    leds_on  = [i for i in range(0,len(temp_keycaps)) if temp_keycaps[i] not in [XXXXXXX]]
    leds_off = [i for i in range(0,len(temp_keycaps)) if temp_keycaps[i] in [XXXXXXX]]
    
    return [leds_on, leds_off]

def Level_Animation(self):
    State = InternalState.active_layers[0] # State Machine Values
    
    if StateControll.PreState != State:
        
        if State == 0:
            
            # white
            self.hue = 0
            self.sat = 0
            self.val = 100
            
            for item in list(range(0,48)):
                keyboard.pixels.set_hsv(self.hue, self.sat, self.val, item)
            
            StateControll.PreState = State
            
            if keyboard.debug_enabled == True:
                print(StateControll.PreState)
            
        elif State == 1:
            [leds_on, leds_off] = Led_Array(LowerK)
            
            # orange
            self.hue = 30
            self.sat = 100
            self.val = 50
            
            for item in leds_on:
                keyboard.pixels.set_hsv(self.hue, self.sat, self.val, item)
            
            # dark blue
            self.hue = 240
            self.sat = 100
            self.val = 100
            
            leds_off += [4,7] # cut-off the Layer Keycaps
            
            for item in leds_off:
                keyboard.pixels.set_hsv(self.hue, self.sat, self.val, item)
            
            StateControll.PreState = State
            
            if keyboard.debug_enabled == True:
                print(StateControll.PreState)
            
        elif State == 2:
            [leds_on, leds_off] = Led_Array(HigherK)
            
            # yellow
            self.hue = 60
            self.sat = 100
            self.val = 50
            
            for item in leds_on:
                keyboard.pixels.set_hsv(self.hue, self.sat, self.val, item)
            
            # purple
            self.hue = 290
            self.sat = 100
            self.val = 80
            
            leds_off += [4,7] # cut-off the Layer Keycaps
            
            for item in leds_off:
                keyboard.pixels.set_hsv(self.hue, self.sat, self.val, item)
            
            StateControll.PreState = State
            
            if keyboard.debug_enabled == True:
                print(StateControll.PreState)
    
    return self

keyboard.rgb_config['animation_mode'] = 'user'
keyboard.rgb_config['user_animation'] = Level_Animation


""" Default
    ┌──────┬──────┬──────┬──────┬──────┬──────┬──────┬──────┬──────┬──────┬──────┬──────┐
    │ ESCC │   Q  │   W  │   E  │   R  │   T  │   Y  │   U  │   I  │   O  │   P  │ Bksp │
    ├──────┼──────┼──────┼──────┼──────┼──────┼──────┼──────┼──────┼──────┼──────┼──────┤
    │ Tab  │   A  │   S  │   D  │   F  │   G  │   H  │   J  │   K  │   L  │   ;  │ Del  │
    ├──────┼──────┼──────┼──────┼──────┼──────┼──────┼──────┼──────┼──────┼──────┼──────┤
    │Shift │   Z  │   X  │   C  │   V  │   B  │   N  │   M  │   ,  │   .  │   /  │ ENTS │
    ├──────┼──────┼──────┼──────┼──────┼──────┼──────┼──────┼──────┼──────┼──────┼──────┤
    │ Ctrl │ GUI  │ Alt  │CPSLCK│Lower │Space │Space │Rise  │ Left │  Up  │ Down │Right │
    └──────┴──────┴──────┴──────┴──────┴──────┴──────┴──────┴──────┴──────┴──────┴──────┘
"""
DefaultK = [
       KC.ESC,   IT_Q,     IT_W,     IT_E,     IT_R,     IT_T,     IT_Y,     IT_U,     IT_I,     IT_O,     IT_P,     KC.BKSP,
       KC.TAB,   IT_A,     IT_S,     IT_D,     IT_F,     IT_G,     IT_H,     IT_J,     IT_K,     IT_L,     IT_SCLN,  KC.DEL,
       KC.LSFT,  IT_Z,     IT_X,     IT_C,     IT_V,     IT_B,     IT_N,     IT_M,     IT_COMM,  IT_DOT,   IT_SLSH,  KC.ENT,
       KC.LCTL,  KC.LGUI,  KC.LALT,  KC.CLCK,  KC.MO(1), KC.SPC,   KC.SPC,   KC.MO(2), KC.LEFT,  KC.UP,    KC.DOWN,  KC.RGHT
]

""" Lower
    ┌──────┬──────┬──────┬──────┬──────┬──────┬──────┬──────┬──────┬──────┬──────┬──────┐
    │      │   -  │   _  │   è  │   |  │   !  │   @  │   ù  │   ì  │   ò  │   *  │   +  │
    ├──────┼──────┼──────┼──────┼──────┼──────┼──────┼──────┼──────┼──────┼──────┼──────┤
    │      │   à  │      │   #  │   $  │   %  │   ^  │   &  │   (  │   )  │   :  │   =  │
    ├──────┼──────┼──────┼──────┼──────┼──────┼──────┼──────┼──────┼──────┼──────┼──────┤
    │  F1  │  F2  │  F3  │  F4  │  F9  │  F10 │  F11 │  F12 │   <  │   >  │   ?  │ Next │
    ├──────┼──────┼──────┼──────┼──────┼──────┼──────┼──────┼──────┼──────┼──────┼──────┤
    │  F5  │  F6  │  F7  │  F8  │      │   {  │   }  │      │ Play │ Vol+ │ Vol- │ Prev │
    └──────┴──────┴──────┴──────┴──────┴──────┴──────┴──────┴──────┴──────┴──────┴──────┘
"""
LowerK = [
       XXXXXXX,  IT_MINS,  IT_UNDS,  IT_EGRV,  IT_PIPE,  IT_EXLM,  IT_AT,    IT_UGRV,  IT_IGRV,  IT_OGRV,  IT_ASTR,  IT_PLUS,
       XXXXXXX,  IT_AGRV,  XXXXXXX,  IT_HASH,  IT_DLR,   IT_PERC,  IT_CIRC,  IT_AMPR,  IT_LPRN,  IT_RPRN,  IT_COLN,  IT_EQL,
       KC.F1,    KC.F2,    KC.F3,    KC.F4,    KC.F9,    KC.F10,   KC.F11,   KC.F12,   IT_LABK,  IT_RABK,  IT_QUES,  KC.MNXT,
       KC.F5,    KC.F6,    KC.F7,    KC.F8,    KC.MO(0), IT_LCBR,  IT_RCBR,  KC.MO(2), KC.MPLY,  KC.VOLU,  KC.VOLD,  KC.MPRV
]

""" Higher
    ┌──────┬──────┬──────┬──────┬──────┬──────┬──────┬──────┬──────┬──────┬──────┬──────┐
    │      │      │      │   é  │  7 / │  8 ( │  9 ) │  0 = │      │      │      │      │
    ├──────┼──────┼──────┼──────┼──────┼──────┼──────┼──────┼──────┼──────┼──────┼──────┤
    │      │      │      │   *  │  4 $ │  5 % │  6 & │   -  │      │      │      │      │
    ├──────┼──────┼──────┼──────┼──────┼──────┼──────┼──────┼──────┼──────┼──────┼──────┤
    │      │      │      │   :  │  1 ! │  2 " │  3 £ │   +  │Insert│ Del  │      │      │
    ├──────┼──────┼──────┼──────┼──────┼──────┼──────┼──────┼──────┼──────┼──────┼──────┤
    │Shift │ Ctrl │      │ Alt  │      │   [  │   ]  │      │ Home │Pg Up │Pg Dwn│ End  │
    └──────┴──────┴──────┴──────┴──────┴──────┴──────┴──────┴──────┴──────┴──────┴──────┘
"""
HigherK = [
       XXXXXXX,  XXXXXXX,  XXXXXXX,  IT_EACU,  IT_7,     IT_8,     IT_9,     IT_0,     XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,
       XXXXXXX,  XXXXXXX,  XXXXXXX,  IT_ASTR,  IT_4,     IT_5,     IT_6,     IT_MINS,  XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,
       XXXXXXX,  XXXXXXX,  XXXXXXX,  IT_COLN,  IT_1,     IT_2,     IT_3,     IT_PLUS,  KC.INSERT,KC.DEL,   XXXXXXX,  XXXXXXX,
       KC.LSFT,  KC.LCTL,  XXXXXXX,  KC.LALT,  KC.MO(0), IT_LBRC,  IT_RBRC,  KC.MO(1), KC.HOME,  KC.PGUP,  KC.PGDN,  KC.END
]

""" Adjust (Lower + Raise) <TODO>
    ┌──────┬──────┬──────┬──────┬──────┬──────┬──────┬──────┬──────┬──────┬──────┬──────┐
    │      │ Reset│ Debug│RGBTog│RGBMod│RGBHUI│RGBSAI│RGBVAI│      │      │      │  Del │
    ├──────┼──────┼──────┼──────┼──────┼──────┼──────┼──────┼──────┼──────┼──────┼──────┤
    │      │      │Mu Mod│Aud on│Audoff│RGBHUD│RGBSAD│RGBVAD│      │      │      │      │
    ├──────┼──────┼──────┼──────┼──────┼──────┼──────┼──────┼──────┼──────┼──────┼──────┤
    │      │Voice-│Voice+│Mus on│Musoff│MIDIon│MIDIof│TermOn│TermOf│      │      │      │
    ├──────┼──────┼──────┼──────┼──────┼──────┼──────┼──────┼──────┼──────┼──────┼──────┤
    │      │      │      │      │      │      │      │      │      │      │      │      │
    └──────┴──────┴──────┴──────┴──────┴──────┴──────┴──────┴──────┴──────┴──────┴──────┘
"""
AdjustK = [
 #      XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,
 #      XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,
 #      XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,
 #      XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,
]


keyboard.keymap = [
    DefaultK,
    LowerK,
    HigherK,
    AdjustK
]


if __name__ == '__main__':
    keyboard.go()

