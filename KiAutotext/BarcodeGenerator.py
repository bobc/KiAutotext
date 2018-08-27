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


import pcbnew

class Barcode(object):
  
  def __init__(self, module, layer):
    self.module = module
    self.layer = layer    
    
  def Line (self, x1, y1, x2, y2):
    seg = pcbnew.EDGE_MODULE(self.module)
    seg.SetWidth(pcbnew.FromMM(self.X))
    seg.SetLayer(self.layer)
    seg.SetShape(pcbnew.S_SEGMENT)
    seg.SetStartEnd( pcbnew.wxPoint( pcbnew.FromMM(x1)+self.position.x, pcbnew.FromMM(y1)+self.position.y),
                     pcbnew.wxPoint( pcbnew.FromMM(x2)+self.position.x, pcbnew.FromMM(y2)+self.position.y) )
    self.module.Add(seg)
    
    
  def __drawBar__(self, width, x):
    offset = width * self.X
    return x + offset
  
  def __drawSpace__(self, width, x, y):
    if width <=0:
      return x
    self.Line(x, y, x, y + self.H)
    width = width - 1
    while width:
      self.Line(x + self.X/2, y, x + self.X/2, y+self.H)
      x = x + self.X
      self.Line(x, y, x, y+self.H)
      width = width -1
    x = x + self.X
    offset = width * self.X
    return x
    
  def drawQuietZone(self, x0, y0, width, height):
    # vertical lines
    offset = 0
    while offset < x0 - self.X:
      xoffset = offset + self.X
      self.Line(x0 - xoffset,          self.X/2, x0-xoffset,      height + y0*2 - self.X/2)
      self.Line(x0 + width + xoffset,  self.X/2, x0+width+xoffset, height + y0*2 - self.X/2)
      offset += self.X/2
    
    # horizontal lines
    offset = 0
    yoffset = 0
    while offset < y0:
      self.Line(self.X/2, y0-offset,        width+x0*2-self.X/2, y0-offset)
      self.Line(self.X/2, y0+height+offset, width+x0*2-self.X/2, y0+height+offset)
      offset += self.X/2
    
  def drawBarcode (self, text, pos):
      self.position = pos
      #todo : height and thickness should be parameters
      self.X = 0.20 
      self.H = 3
      self.Q = 10 * self.X
      if self.Q < 6.35:
        self.Q = 6.35
      self.Vmargin = self.X * 2
      
      # Draw bars
      width = self.drawBars (text)
      
      # Draw quiet zone
      self.drawQuietZone(self.Q, self.Vmargin, width, self.H)
      
      # add text corresponding to actual barcode data, including guard characters
      textSize = self.module.Value().GetTextSize()
      x1 = width + self.Q * 2
      y1 = self.H + self.Vmargin * 2 + pcbnew.ToMM(textSize[1]) * 1.1 + 0.5
      p = self.module.GetPosition()
      px = p[0]
      py = p[1]
      text = pcbnew.TEXTE_MODULE(self.module)
      text.SetPosition (pcbnew.wxPoint(  px + pcbnew.FromMM(x1/2), py + pcbnew.FromMM(y1 - 0.25) - textSize[1]/2))
      text.SetLayer (self.layer)
      text.SetVisible (True)
      text.SetTextSize (textSize)
      text.SetText (self.labelText)
      self.module.Add (text) 
      
      # add an outline on courtyard layer
      self.layer = pcbnew.F_CrtYd
      self.X = 0.05
      self.Line (0, 0, x1, 0)
      self.Line (x1, 0, x1, y1)
      self.Line (x1, y1, 0, y1)
      self.Line (0, y1, 0, 0)
