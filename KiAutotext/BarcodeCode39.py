#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.

# Code 39 barcode functions from uss39_barcode.py footprint wizard (authors: ejohns, LordBlick)  
# Modifications Copyright Bob Cousins 2017

from BarcodeGenerator import *

# in the following table, 0 means narrow bar/space, 1 means wide bar/space
# the min rato of narrow:wide recommended for Code39 is 1:2  
ptd = {
  '0': '000110100', '1': '100100001', '2': '001100001', '3': '101100000',
  '4': '000110001', '5': '100110000', '6': '001110000', '7': '000100101',
  '8': '100100100', '9': '001100100', 'A': '100001001', 'B': '001001001',
  'C': '101001000', 'D': '000011001', 'E': '100011000', 'F': '001011000',
  'G': '000001101', 'H': '100001100', 'I': '001001100', 'J': '000011100',
  'K': '100000011', 'L': '001000011', 'M': '101000010', 'N': '000010011',
  'O': '100010010', 'P': '001010010', 'Q': '000000111', 'R': '100000110',
  'S': '001000110', 'T': '000010110', 'U': '110000001', 'V': '011000001',
  'W': '111000000', 'X': '010010001', 'Y': '110010000', 'Z': '011010000',
  '-': '010000101', '.': '110000100', ' ': '011000100', '*': '010010100',
  '$': '010101000', '/': '010100010', '+': '010001010', '%': '000101010'}

class Uss39:
  def __init__(self, text):
    self.Text = self.makePrintable(text)

  __str__ = lambda self: self.Text
  # note : * is not a valid user char, it is reserved for the guard characters
  makePrintable = lambda self, text: ''.join((c for c in text.upper() if ptd.has_key(c)))

  def getBarCodePattern(self, text = None):
    text = text if not(text is None) else self.Text
    # Reformated text with start and end characters
    return reduce(lambda a1, a2: a1 + [0] + a2, [map(int, ptd[c]) for c in ("*%s*" % self.makePrintable(text))])

class Code39 (Barcode):

  def __init__(self, module, layer):
    super(Code39, self).__init__(module, layer)

  def drawBars(self, text):
    self.Barcode = Uss39(text)
    bars = self.Barcode.getBarCodePattern()
    self.labelText = "*"+self.Barcode.Text+"*"
    
    x = self.Q
    y = self.Vmargin    
    for index in range(0, len(bars), 2):
      # Draw bar
      bar = bars[index] + 1
      x = self.__drawBar__(bar, x)
      # Draw space
      if index < len(bars)-1:
        space = bars[index + 1] + 1
        x = self.__drawSpace__(space, x, y)
    return x - self.X - self.Q       
    
