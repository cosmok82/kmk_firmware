""" Copyright 2015-2016 Matthias Schmidtt
  
   This program is free software: you can redistribute it and/or modify
   it under the terms of the GNU General Public License as published by
   the Free Software Foundation, either version 2 of the License, or
   (at your option) any later version.
  
   This program is distributed in the hope that it will be useful,
   but WITHOUT ANY WARRANTY; without even the implied warranty of
   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
   GNU General Public License for more details.
  
   You should have received a copy of the GNU General Public License
   along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

from kmk.keys import KC


"""
   ┌───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───────┐
   │ \ │ 1 │ 2 │ 3 │ 4 │ 5 │ 6 │ 7 │ 8 │ 9 │ 0 │ ' │ ì │       │
   ├───┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─────┤
   │     │ Q │ W │ E │ R │ T │ Y │ U │ I │ O │ P │ è │ + │     │
   ├─────┴┬──┴┬──┴┬──┴┬──┴┬──┴┬──┴┬──┴┬──┴┬──┴┬──┴┬──┴┬──┴┐    │
   │      │ A │ S │ D │ F │ G │ H │ J │ K │ L │ ò │ à │ ù │    │
   ├────┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴───┴────┤
   │    │ < │ Z │ X │ C │ V │ B │ N │ M │ , │ . │ - │          │
   ├────┼───┴┬──┴─┬─┴───┴───┴───┴───┴───┴──┬┴───┼───┴┬────┬────┤
   │    │    │    │                        │    │    │    │    │
   └────┴────┴────┴────────────────────────┴────┴────┴────┴────┘
"""
# Row 1
IT_BSLS = KC.GRV  # (backslash) \
IT_1    = KC.N1   # 1
IT_2    = KC.N2   # 2
IT_3    = KC.N3   # 3
IT_4    = KC.N4   # 4
IT_5    = KC.N5   # 5
IT_6    = KC.N6   # 6
IT_7    = KC.N7   # 7
IT_8    = KC.N8   # 8
IT_9    = KC.N9   # 9
IT_0    = KC.N0   # 0
IT_QUOT = KC.MINS # '
IT_IGRV = KC.EQL  # ì
# Row 2
IT_Q    = KC.Q    # Q
IT_W    = KC.W    # W
IT_E    = KC.E    # E
IT_R    = KC.R    # R
IT_T    = KC.T    # T
IT_Y    = KC.Y    # Y
IT_U    = KC.U    # U
IT_I    = KC.I    # I
IT_O    = KC.O    # O
IT_P    = KC.P    # P
IT_EGRV = KC.LBRC # è
IT_PLUS = KC.RBRC # +
# Row 3
IT_A    = KC.A    # A
IT_S    = KC.S    # S
IT_D    = KC.D    # D
IT_F    = KC.F    # F
IT_G    = KC.G    # G
IT_H    = KC.H    # H
IT_J    = KC.J    # J
IT_K    = KC.K    # K
IT_L    = KC.L    # L
IT_OGRV = KC.SCLN # ò
IT_AGRV = KC.QUOT # à
IT_UGRV = KC.NUHS # ù
# Row 4
IT_LABK = KC.NUBS # <
IT_Z    = KC.Z    # Z
IT_X    = KC.X    # X
IT_C    = KC.C    # C
IT_B    = KC.B    # B
IT_V    = KC.V    # V
IT_N    = KC.N    # N
IT_M    = KC.M    # M
IT_COMM = KC.COMM # ,
IT_DOT  = KC.DOT  # .
IT_MINS = KC.SLSH # -

""" Shifted symbols
   ┌───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───────┐
   │ | │ ! │ " │ £ │ $ │ % │ & │ / │ ( │ ) │ = │ ? │ ^ │       │
   ├───┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─────┤
   │     │   │   │   │   │   │   │   │   │   │   │ é │ * │     │
   ├─────┴┬──┴┬──┴┬──┴┬──┴┬──┴┬──┴┬──┴┬──┴┬──┴┬──┴┬──┴┬──┴┐    │
   │      │   │   │   │   │   │   │   │   │   │ ç │ ° │ § │    │
   ├────┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴───┴────┤
   │    │ > │   │   │   │   │   │   │   │ ; │ : │ _ │          │
   ├────┼───┴┬──┴─┬─┴───┴───┴───┴───┴───┴──┬┴───┼───┴┬────┬────┤
   │    │    │    │                        │    │    │    │    │
   └────┴────┴────┴────────────────────────┴────┴────┴────┴────┘
"""
# Row 1
IT_PIPE = KC.LSFT(IT_BSLS) # |
IT_EXLM = KC.LSFT(IT_1)    # !
IT_DQUO = KC.LSFT(IT_2)    # "
IT_PND  = KC.LSFT(IT_3)    # £
IT_DLR  = KC.LSFT(IT_4)    # $
IT_PERC = KC.LSFT(IT_5)    # %
IT_AMPR = KC.LSFT(IT_6)    # &
IT_SLSH = KC.LSFT(IT_7)    # /
IT_LPRN = KC.LSFT(IT_8)    # (
IT_RPRN = KC.LSFT(IT_9)    # )
IT_EQL  = KC.LSFT(IT_0)    # =
IT_QUES = KC.LSFT(IT_QUOT) # ?
IT_CIRC = KC.LSFT(IT_IGRV) # ^
# Row 2
IT_EACU = KC.LSFT(IT_EGRV) # é
IT_ASTR = KC.LSFT(IT_PLUS) # *
# Row 3
IT_CCED = KC.LSFT(IT_OGRV) # ç
IT_DEG  = KC.LSFT(IT_AGRV) # °
IT_SECT = KC.LSFT(IT_UGRV) # §
# Row 4
IT_RABK = KC.LSFT(IT_LABK) # >
IT_COLN = KC.LSFT(IT_DOT)  # :
IT_SCLN = KC.LSFT(IT_COMM) # ;
IT_UNDS = KC.LSFT(IT_MINS) # _

""" AltGr symbols
   ┌───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───────┐
   │   │   │   │   │   │   │   │   │   │   │   │   │   │       │
   ├───┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─────┤
   │     │   │   │ € │   │   │   │   │   │   │   │ [ │ ] │     │
   ├─────┴┬──┴┬──┴┬──┴┬──┴┬──┴┬──┴┬──┴┬──┴┬──┴┬──┴┬──┴┬──┴┐    │
   │      │   │   │   │   │   │   │   │   │   │ @ │ # │   │    │
   ├────┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴───┴────┤
   │    │   │   │   │   │   │   │   │   │   │   │   │          │
   ├────┼───┴┬──┴─┬─┴───┴───┴───┴───┴───┴──┬┴───┼───┴┬────┬────┤
   │    │    │    │                        │    │    │    │    │
   └────┴────┴────┴────────────────────────┴────┴────┴────┴────┘
"""
# Row 2
IT_EURO = KC.RALT(IT_E)       # €
IT_LBRC = KC.RALT(IT_EGRV)    # [
IT_RBRC = KC.RALT(IT_PLUS)    # ]
# Row 3
IT_AT   = KC.RALT(IT_OGRV)    # @
IT_HASH = KC.RALT(IT_AGRV)    # #

""" Shift+AltGr symbols
   ┌───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───────┐
   │   │   │   │   │   │   │   │   │   │   │   │   │   │       │
   ├───┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─────┤
   │     │   │   │   │   │   │   │   │   │   │   │ { │ } │     │
   ├─────┴┬──┴┬──┴┬──┴┬──┴┬──┴┬──┴┬──┴┬──┴┬──┴┬──┴┬──┴┬──┴┐    │
   │      │   │   │   │   │   │   │   │   │   │   │   │   │    │
   ├────┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴───┴────┤
   │    │   │   │   │   │   │   │   │   │   │   │   │          │
   ├────┼───┴┬──┴─┬─┴───┴───┴───┴───┴───┴──┬┴───┼───┴┬────┬────┤
   │    │    │    │                        │    │    │    │    │
   └────┴────┴────┴────────────────────────┴────┴────┴────┴────┘
"""
# Row 2
IT_LCBR = KC.LSFT(KC.RALT(IT_EGRV)) # {
IT_RCBR = KC.LSFT(KC.RALT(IT_PLUS)) # }

# DEPRECATED
IT_BKSL = IT_BSLS
IT_APOS = IT_QUOT
IT_IACC = IT_IGRV
IT_EACC = IT_EGRV
IT_OACC = IT_OGRV
IT_AACC = IT_AGRV
IT_UACC = IT_UGRV
IT_LESS = IT_LABK
IT_DQOT = IT_DQUO
IT_STRL = IT_PND
IT_QST  = IT_QUES
IT_CRC  = IT_CIRC
IT_MORE = IT_RABK
IT_SHRP = IT_HASH

IT_X_PLUS = X_RBRACKET
