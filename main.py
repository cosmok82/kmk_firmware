import board
#import digitalio

from kmk.kmk_keyboard import KMKKeyboard as _KMKKeyboard
from kmk.consts import LeaderMode, UnicodeMode
from kmk.matrix import DiodeOrientation
from kmk.handlers.sequences import send_string, compile_unicode_string_sequences
from kmk.keys import KC
#from kmk.led import led
#from kmk.matrix import MatrixScanner
#from kmk.matrix import intify_coordinate as ic
#from kmk.handlers.sequences import compile_unicode_string_sequences as cuss
#import kmk.handlers.modtap as modtap
#from kmk.keys import *


print(dir(board))


class KMKKeyboard(_KMKKeyboard):
    col_pins = (board.GP1, board.GP2, board.GP3, board.GP4,  board.GP5,  board.GP6,
                board.GP7, board.GP8, board.GP9, board.GP10, board.GP11, board.GP12)
    #col_pins = (board.GP12, board.GP11, board.GP10, board.GP9, board.GP8, board.GP7,
    #            board.GP6,  board.GP5,  board.GP4,  board.GP3, board.GP2, board.GP1)
    row_pins = (board.GP14, board.GP15, board.GP16, board.GP17)
    diode_orientation = DiodeOrientation.COLUMNS
    
    #uart_pin = board.SCL
    #extra_data_pin = board.SDA
    #rgb_pixel_pin = board.TX
    #rgb_num_pixels = 12
    led_pin = board.GP25
    
    #make_key(code=116, names=('LARROW_IT',';'))

keyboard = KMKKeyboard()

Lower   = KC.MO(1) #KC.MO(1) #KC.LT(1, KC.MINUS)
Higher  = KC.MO(2) #KC.MO(2) #KC.LT(2, KC.EQUAL)
_______ = KC.TRNS
XXXXXXX = KC.NO


# ------------------User level config variables ---------------------------------------
keyboard.unicode_mode = UnicodeMode.LINUX
keyboard.tap_time = 350
keyboard.leader_timeout = 2000
keyboard.debug_enabled = True

# ------------------Italian Re-Mapping ------------------------------------------------

#TEST00 = send_string(";")  #ò
#TEST01 = send_string(":")  #ç
#TEST02 = send_string("#")  #£
#TEST03 = send_string("%")  #%
#TEST04 = send_string("&")  #/
#TEST05 = send_string("\\") #ù
#TEST06 = send_string("\"") #°
#TEST07 = send_string("(")  #)
#TEST08 = send_string(")")  #=
#TEST09 = send_string("=")  #ì
#TEST10 = send_string("'")  #à
#TEST11 = send_string("^")  #&
#TEST12 = send_string("[")  #è
#TEST13 = send_string("]")  #+
#TEST14 = send_string("*")  #(
#TEST15 = send_string("+")  #^
#TEST16 = send_string("@")  #"
#TEST17 = send_string("{")  #é
#TEST18 = send_string("}")  #*
#TEST19 = send_string("<")  #;
#TEST20 = send_string(">")  #:
#TEST21 = send_string(".")  #.
#TEST22 = send_string("|")  #§
#TEST23 = send_string("!")  #!
#TEST24 = send_string("?")  #_
#TEST25 = send_string("-")  #'
#TEST26 = send_string(",")  #,
#TEST27 = send_string("$")  #$
#TEST28 = send_string("~")  #|
#TEST29 = send_string("_")  #?


PIPE_IT    = KC.TILDE         #|
BCKSLSH_IT = KC.ZKHK          #\
EXLM_IT    = KC.EXLM          #!
DQUO_IT    = KC.AT            #"
POUND_IT   = KC.HASH          #£
DOLLAR_IT  = KC.DOLLAR        #$
PERC_IT    = KC.PERC          #%
AMPR_IT    = KC.CIRC          #&
SLASH_IT   = KC.AMPR          #/
LPRN_IT    = KC.ASTR          #(
RPRN_IT    = KC.LPRN          #)
EQL_IT     = KC.RPRN          #=
UNDS_IT    = KC.QUES          #?
QUOT_IT    = KC.MINS          #'
CIRC_IT    = KC.PLUS          #^
I_ACC_IT   = KC.EQUAL         #ì
E_RACC_IT  = KC.LCBR          #é
E_LACC_IT  = KC.LBRC          #è
LBRC_IT    = KC.RALT(KC.LBRC) #[
ASTR_IT    = KC.RCBR          #*
PLUS_IT    = KC.RBRC          #+
RBRC_IT    = KC.RALT(KC.RBRC) #]
U_ACC_IT   = KC.BSLASH        #ù
C_QUOT_IT  = KC.COLN          #ç
O_ACC_IT   = KC.SCLN          #ò
AT_IT      = KC.RALT(KC.AT)   #@
DEG_IT     = KC.DQUO          #°
A_ACC_IT   = KC.QUOT          #à
HASH_IT    = KC.RALT(KC.HASH) ##
SCLN_IT    = KC.LABK          #;
COMM_IT    = KC.COMMA         #,
COLN_IT    = KC.RABK          #:
DOT_IT     = KC.DOT           #.
UNDS_IT    = KC.QUES          #_
MINUS_IT   = KC.SLSH          #-
LCBR_IT    = KC.RALT(KC.LCBR) #{
RCBR_IT    = KC.RALT(KC.RCBR) #}
#LARROW_IT  = KC.LSFT(XXXXXXX) #< TODO
#RARROW_IT  = KC.LSFT(XXXXXXX) #> TODO
#TILDE_IT   = KC.LSFT(XXXXXXX) #~ TODO


""" Default
    ,-----------------------------------------------------------------------------------.
    | ESCC |   Q  |   W  |   E  |   R  |   T  |   Y  |   U  |   I  |   O  |   P  | Bksp |
    |------+------+------+------+------+------+------+------+------+------+------+------|
    | Tab  |   A  |   S  |   D  |   F  |   G  |   H  |   J  |   K  |   L  |   ;  | Del  |
    |------+------+------+------+------+------+------+------+------+------+------+------|
    |CPSLCK|   Z  |   X  |   C  |   V  |   B  |   N  |   M  |   ,  |   .  |   /  | ENTS |
    |------+------+------+------+------+------+------+------+------+------+------+------|
    |Shift | Ctrl | GUI  | Alt  |Lower |Space |Space |Rise  | Left |  Up  | Down |Right |
    `-----------------------------------------------------------------------------------'
                                |  +   |             |  -   |
                                `------'             `------'
"""
DefaultK = [
       KC.ESC,   KC.Q,     KC.W,     KC.E,     KC.R,     KC.T,     KC.Y,     KC.U,     KC.I,     KC.O,     KC.P,     KC.BKSP,
       KC.TAB,   KC.A,     KC.S,     KC.D,     KC.F,     KC.G,     KC.H,     KC.J,     KC.K,     KC.L,     SCLN_IT,  KC.DEL,
       KC.CLCK,  KC.Z,     KC.X,     KC.C,     KC.V,     KC.B,     KC.N,     KC.M,     COMM_IT,  DOT_IT,   SLASH_IT, KC.ENT,
       KC.LSFT,  KC.LCTL,  KC.LGUI,  KC.LALT,  Lower,    KC.SPC,   KC.SPC,   Higher,   KC.LEFT,  KC.UP,    KC.DOWN,  KC.RGHT,
]

""" Lower
    ,-----------------------------------------------------------------------------------.
    |   ~  |   -  |   _  |   è  |   |  |   !  |   @  |   ù  |   ì  |   ò  |   *  |   +  |
    |------+------+------+------+------+------+------+------+------+------+------+------|
    |      |   à  |      |   #  |   $  |   %  |   ^  |   &  |   (  |   )  |   :  |   =  |
    |------+------+------+------+------+------+------+------+------+------+------+------|
    |  F1  |  F2  |  F3  |  F4  |  F9  |  F10 |  F11 |  F12 |   <  |   >  |   ?  | Next |
    |------+------+------+------+------+------+------+------+------+------+------+------|
    |  F5  |  F6  |  F7  |  F8  |      |   {  |   }  |      | Play | Vol+ | Vol- | Prev |
    `-----------------------------------------------------------------------------------'
"""
LowerK = [
       XXXXXXX,  MINUS_IT, UNDS_IT,  E_LACC_IT,PIPE_IT,  EXLM_IT,  AT_IT,    U_ACC_IT, I_ACC_IT, O_ACC_IT, ASTR_IT,  PLUS_IT,
       XXXXXXX,  A_ACC_IT, XXXXXXX,  HASH_IT,  DOLLAR_IT,PERC_IT,  CIRC_IT,  AMPR_IT,  LPRN_IT,  RPRN_IT,  COLN_IT,  EQL_IT,
       KC.F1,    KC.F2,    KC.F3,    KC.F4,    KC.F9,    KC.F10,   KC.F11,   KC.F12,   XXXXXXX,  XXXXXXX,  UNDS_IT,  KC.MNXT,
       KC.F5,    KC.F6,    KC.F7,    KC.F8,    KC.MO(0), LCBR_IT,  RCBR_IT,  KC.MO(0), KC.MPLY,  KC.VOLU,  KC.VOLD,  KC.MPRV,
]

""" Higher
    ,-----------------------------------------------------------------------------------.
    |      |      |      |   é  |  7 / |  8 ( |  9 ) |  0 = |   =  |      |      |      |
    |------+------+------+------+------+------+------+------+------+------+------+------|
    |      |      |      |   *  |  4 $ |  5 % |  6 & |   -  |      |      |      |      |
    |------+------+------+------+------+------+------+------+------+------+------+------|
    |      |      |      |   :  |  1 ! |  2 " |  3 £ |   +  |Insert| Del  |      |      |
    |------+------+------+------+------+------+------+------+------+------+------+------|
    |Shift | Ctrl |      | Alt  |      |   [  |   ]  |      | Home |Pg Up |Pg Dwn| End  |
    `-----------------------------------------------------------------------------------'
"""
HigherK = [
       XXXXXXX,  XXXXXXX,  XXXXXXX,  E_RACC_IT,KC.N7,    KC.N8,    KC.N9,    KC.N0,    XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,
       XXXXXXX,  XXXXXXX,  XXXXXXX,  ASTR_IT,  KC.N4,    KC.N5,    KC.N6,    MINUS_IT, XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,
       XXXXXXX,  XXXXXXX,  XXXXXXX,  COLN_IT,  KC.N1,    KC.N2,    KC.N3,    PLUS_IT,  KC.INSERT,KC.DEL,   XXXXXXX,  XXXXXXX,
       KC.LSFT,  KC.LCTL,  XXXXXXX,  KC.LALT,  KC.MO(0), LBRC_IT,  RBRC_IT,  KC.MO(0), KC.HOME,  KC.PGUP,  KC.PGDN,  KC.END,
]

""" Adjust (Lower + Raise) TODO
    ,-----------------------------------------------------------------------------------.
    | ENC  | Reset| Debug|RGBTog|RGBMod|RGBHUI|RGBSAI|RGBVAI|      |      |      |  Del |
    |------+------+------+------+------+-------------+------+------+------+------+------|
    |      |      |Mu Mod|Aud on|Audoff|RGBHUD|RGBSAD|RGBVAD|      |      |      |      |
    |------+------+------+------+------+------|------+------+------+------+------+------|
    |      |Voice-|Voice+|Mus on|Musoff|MIDIon|MIDIof|TermOn|TermOf|      |      |      |
    |------+------+------+------+------+------+------+------+------+------+------+------|
    |      |      |      |      |      |      |      |      |      |      |      |      |
    `-----------------------------------------------------------------------------------'
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

print(dir(board.LED))



if __name__ == '__main__':
    keyboard.go()




