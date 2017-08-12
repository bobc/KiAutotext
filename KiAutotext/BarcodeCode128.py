#! /usr/bin/env python2

# Copyright (c) 2014-2015 Felix Knopf <felix.knopf@arcor.de>
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License in the LICENSE.txt for more details.
#
# This part of the library is based on code128.py by Erik Karulf,
# found at https://gist.github.com/ekarulf/701416
# His original copyright and permission notice:
#    Copyright (c) 2010 Erik Karulf <erik@karulf.com>
#  
#    Permission to use, copy, modify, and/or distribute this software for any
#    purpose with or without fee is hereby granted, provided that the above
#    copyright notice and this permission notice appear in all copies.
#
# Modifications for KiCad Copyright Bob Cousins 2017

import re

from BarcodeGenerator import *

# Copied from http://en.wikipedia.org/wiki/Code_128
# Value Weights 128A    128B    128C
CODE128_CHART = """
0       212222  space   space   00
1       222122  !       !       01
2       222221  "       "       02
3       121223  #       #       03
4       121322  $       $       04
5       131222  %       %       05
6       122213  &       &       06
7       122312  '       '       07
8       132212  (       (       08
9       221213  )       )       09
10      221312  *       *       10
11      231212  +       +       11
12      112232  ,       ,       12
13      122132  -       -       13
14      122231  .       .       14
15      113222  /       /       15
16      123122  0       0       16
17      123221  1       1       17
18      223211  2       2       18
19      221132  3       3       19
20      221231  4       4       20
21      213212  5       5       21
22      223112  6       6       22
23      312131  7       7       23
24      311222  8       8       24
25      321122  9       9       25
26      321221  :       :       26
27      312212  ;       ;       27
28      322112  <       <       28
29      322211  =       =       29
30      212123  >       >       30
31      212321  ?       ?       31
32      232121  @       @       32
33      111323  A       A       33
34      131123  B       B       34
35      131321  C       C       35
36      112313  D       D       36
37      132113  E       E       37
38      132311  F       F       38
39      211313  G       G       39
40      231113  H       H       40
41      231311  I       I       41
42      112133  J       J       42
43      112331  K       K       43
44      132131  L       L       44
45      113123  M       M       45
46      113321  N       N       46
47      133121  O       O       47
48      313121  P       P       48
49      211331  Q       Q       49
50      231131  R       R       50
51      213113  S       S       51
52      213311  T       T       52
53      213131  U       U       53
54      311123  V       V       54
55      311321  W       W       55
56      331121  X       X       56
57      312113  Y       Y       57
58      312311  Z       Z       58
59      332111  [       [       59
60      314111  \       \       60
61      221411  ]       ]       61
62      431111  ^       ^       62
63      111224  _       _       63
64      111422  \N{NUL} `       64
65      121124  \N{SOH} a       65
66      121421  \N{STX} b       66
67      141122  \N{ETX} c       67
68      141221  \N{EOT} d       68
69      112214  \N{ENQ} e       69
70      112412  \N{ACK} f       70
71      122114  \N{BEL} g       71
72      122411  \N{BS}  h       72
73      142112  HT      i       73
74      142211  LF      j       74
75      241211  VT      k       75
76      221114  FF      l       76
77      413111  CR      m       77
78      241112  \N{SO}  n       78
79      134111  \N{SI}  o       79
80      111242  \N{DLE} p       80
81      121142  \N{DC1} q       81
82      121241  \N{DC2} r       82
83      114212  \N{DC3} s       83
84      124112  \N{DC4} t       84
85      124211  \N{NAK} u       85
86      411212  \N{SYN} v       86
87      421112  \N{ETB} w       87
88      421211  \N{CAN} x       88
89      212141  \x19    y       89
90      214121  \N{SUB} z       90
91      412121  \N{ESC} {       91
92      111143  FS      |       92
93      111341  GS      }       93
94      131141  RS      ~       94
95      114113  US      DEL     95
96      114311  FNC3    FNC3    96
97      411113  FNC2    FNC2    97
98      411311  ShiftB  ShiftA  98
99      113141  CodeC   CodeC   99
100     114131  CodeB   FNC4    CodeB
101     311141  FNC4    CodeA   CodeA
102     411131  FNC1    FNC1    FNC1
103     211412  StartA  StartA  StartA
104     211214  StartB  StartB  StartB
105     211232  StartC  StartC  StartC
106     2331112 Stop    Stop    Stop
""".split()

VALUES   = [int(value) for value in CODE128_CHART[0::5]]
WEIGHTS  = dict(zip(VALUES, CODE128_CHART[1::5]))
CODE128A = dict(zip(CODE128_CHART[2::5], VALUES))
CODE128B = dict(zip(CODE128_CHART[3::5], VALUES))
CODE128C = dict(zip(CODE128_CHART[4::5], VALUES))

for charset in (CODE128A, CODE128B):
    charset[' '] = charset.pop('space')

CODE128A['\t'] = CODE128A.pop('HT')
CODE128A['\n'] = CODE128A.pop('LF')
CODE128A['\v'] = CODE128A.pop('VT')
CODE128A['\f'] = CODE128A.pop('FF')
CODE128A['\r'] = CODE128A.pop('CR')
CODE128A['\x1C'] = CODE128A.pop('FS')
CODE128A['\x1D'] = CODE128A.pop('GS')
CODE128A['\x1E'] = CODE128A.pop('RS')
CODE128A['\x1F'] = CODE128A.pop('US')

def code128_format(data, thickness):
    """
    Generate an optimal barcode from a string, full latin_1-charset is supported
    """

    text    = str(data).encode('latin_1', 'replace').decode('latin_1')
    pos     = 0
    length  = len(text)

    p_function = re.compile("["+"".join(chr(i) for i in range(32))+"]")
    p_a = re.compile(r"\A[^"+"".join(chr(i) for i in range(96,128))+"]*\Z")

    def fit_a(text,pos):
        try:
            pos2 = p_function.search(text,pos).start()
        except AttributeError:
            return False
        return p_a.search(text[pos:pos2]) is not None

    # Start Code
    if (text[:2].isdigit() and length == 2) \
        or (text[:4].isdigit() and length >= 4):
        #print("start with C")
        charset = CODE128C
        codes   = [charset['StartC']]
    elif fit_a(text,0):
        #print("start with A")
        charset = CODE128A
        codes   = [charset['StartA']]
    else:
        #print("start with B")
        charset = CODE128B
        codes   = [charset['StartB']]

    # Data
    while pos < length:
        if text[pos] == '~' and length - pos > 1:    # internal escape sequence
            if text[pos+1] in ("1","2","3","4"):
                if text[pos+1] == '1':
                    codes.append(charset['FNC1'])
                elif text[pos+1] == '2':
                    codes.append(charset['FNC2'])
                elif text[pos+1] == '3':
                    codes.append(charset['FNC3'])
                elif text[pos+1] == '4':
                    codes.append(charset['FNC4'])
                    print("FNC4 appended")
                pos+=2
            else: pos+=1

        if (charset is CODE128A or charset is CODE128B) and ord(text[pos])>=128:
            # Using FNC4 to encode a following high (128-255) characters
            codes.append(charset['FNC4'])
            text = text.replace(text[pos], chr(ord(text[pos])-128), 1)
            #print("FNC4 placed to encode high character")

        if charset is CODE128C and text[pos:pos+2].isdigit() and length - pos > 1:
            # Encode Code C two characters at a time
            codes.append(int(text[pos:pos+2]))
            pos += 2

        elif (charset is CODE128A or charset is CODE128B) \
               and ( (text[pos:pos+6].isdigit() and length - pos >= 6) \
                or  (text[pos:pos+4].isdigit() and length - pos == 4) ):
            # Switch to Code C
            #print("switch to C")
            codes.append(charset['CodeC'])
            charset = CODE128C

        elif (charset is CODE128B or charset is CODE128C) and fit_a(text, pos):
            # Switch to Code A
            #print("switch to A",pos)
            codes.append(charset['CodeA'])
            charset = CODE128A

        elif charset is CODE128C or (charset is CODE128A and ord(text[pos]) >= 96):
            # Switch to Code B
                #print("switch to B",pos)
                codes.append(charset['CodeB'])
                charset = CODE128B
        else:
            # Encode Code A or B one character at a time
            codes.append(charset[text[pos]])
            pos += 1


    # Checksum
    checksum = 0
    for weight, code in enumerate(codes):
        checksum += max(weight, 1) * code
    codes.append(checksum % 103)

    # Stop Code
    codes.append(charset['Stop'])

    # calculate bars
    barcode_widths = []
    for code in codes:
        for weight in WEIGHTS[code]:
            barcode_widths.append(int(weight) * thickness)

    return barcode_widths



class Code128 (Barcode):

  def __init__(self, module, layer):
    super(Code128, self).__init__(module, layer)

  def drawBars(self, text):
    bars = code128_format (text, 1)
    self.labelText = text

    x = self.Q
    y = self.Vmargin    
    for index in range(0, len(bars), 2):
      # Draw bar
      bar = bars[index]
      x = self.__drawBar__(bar, x)
      # Draw space
      if index < len(bars)-1:
        space = bars[index + 1]
        x = self.__drawSpace__(space, x, y)
    return x - self.X - self.Q       
