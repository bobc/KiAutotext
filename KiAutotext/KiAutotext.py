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

# Copyright Bob Cousins 2017

import sys
import os
from datetime import datetime
import pcbnew

import BarcodeGenerator
import BarcodeCode39
import BarcodeCode128

# console commands
"""
sys.path.append("c:/git_bobc/kiautotext/kiautotext")
execfile ("c:/git_bobc/kiautotext/kiautotext/KiAutotext.py")

reload(BarcodeGenerator)
reload(BarcodeCode39)
reload(BarcodeCode128)
execfile ("c:/git_bobc/kiautotext/kiautotext/KiAutotext.py")
"""

"""
Special component names 
-----------------------
UserTitleBlock  User fields in UserTitleBlock are added to list of substitution 
                macros.
  
Special footprint names
-----------------------
text_F_SilkS    the Value field is placed on F_SilkS layer
                (similar to %F.SilkS:text)

text_F_Cu       the Value field is placed on F_Cu layer
                (similar to %F.Cu:text)

text_auto_date  the Value field is replaced with today's date and placed on
                F_SilkS.
                (similar to %F.SilkS:%DT)

text_auto       the Value field is used as a formatting string. Macro keys are
                substituted as follows.
                
                Standard keys:
                %F    the file base name
                %DT   today's date
                
                The following are read from the title block of the corresponding 
                schematic file:
                %T    Project title
                %R    Revision
                %D    Issue Date
                %Y    Company
                %C0   Comment 1
                %C1   Comment 2
                %C2   Comment 3
                %C3   Comment 4
                
                Additional substitutions are made according to user defined 
                fields from component "UserTitleBlock" if it exists.

auto_barcode39 
                The Value field is used to create a Code39 barcode. Invalid 
                characters are stripped out, and guard characters added to start
                and end.
                
auto_barcode128 
                The Value field is used to create a Code128 barcode.
                  
"""   

layertable = {}

class TitleBlock:

  filename = ""
  date = ""
  title = ""
  company = ""
  revision = ""
  comment1 = ""
  comment2 = ""
  comment3 = ""
  comment4 = ""
         
class Schematic:

  titleBlock = TitleBlock()
  userfield = {}
    
  def __init__(self, filename):

    sch_name = os.path.splitext(filename)[0] + ".sch"
    
    self.titleBlock.filename = os.path.basename(filename)
    self.titleBlock.filename = os.path.splitext(self.titleBlock.filename)[0] 
    
    f = open (sch_name, "r")
    line = f.readline()
    while line:
      line = line.rstrip()
      value = line[line.find(' ')+1:]
      # strip ".." quotes
      value = value[1:-1]
  
      if line.startswith ("Title"):
        self.titleBlock.title = value
      elif line.startswith ("Rev"):
        self.titleBlock.revision = value
      elif line.startswith ("Date"):
        self.titleBlock.date = value
      elif line.startswith ("Comp"):
        self.titleBlock.company = value
      elif line.startswith ("Comment1"):
        self.titleBlock.comment1 = value
      elif line.startswith ("Comment2"):
        self.titleBlock.comment2 = value
      elif line.startswith ("Comment3"):
        self.titleBlock.comment3 = value
      elif line.startswith ("Comment4"):
        self.titleBlock.comment4 = value
        
      elif line.startswith ("Text"):
        line = f.readline().rstrip()
        if line.startswith('%'):
          key = line[0:line.find('=')]
          value = line[line.find('=')+1:]
          self.userfield [key] = value

      elif line.startswith ("$Comp"):
        line = f.readline().rstrip()
        tokens = filter(bool, line.split())

        if tokens[1] == "UserTitleBlock":
          while not tokens[0] == "$EndComp":
            if tokens[0]== "F" and int(tokens[1]) >= 4:  
              key = tokens[10]
              key = '%'+key[1:-1]
              value = tokens[2]
              value = value[1:-1]
              self.userfield [key] = value
            line = f.readline().rstrip()
            tokens = filter(bool, line.split())
        
      line = f.readline()  
    f.close()
         
def addToken (s, is_macro, tok, fields):
    if tok:
        if is_macro:
            if tok in fields:
                s += fields[tok]
            else:
                s += tok
        else:
            s += tok
    return s

def macroReplace (s, fields):
  result = ""
  tok = ""
  in_macro = False
  j = 0
  while j < len(s):
    c = s[j]
    if in_macro:
      if c.isalpha():
        tok = tok + c
      else:
        result = addToken (result, in_macro, tok, fields)
        in_macro = False
        tok = c  
    else:
      if c=='%':
        if j < len(s) and s[j+1] == '%':
          tok = tok + c
          j = j+1
        else:
          result = addToken (result, in_macro, tok, fields)
          in_macro = True
          tok = c
      else:
        tok = tok + c
    j = j +1
  # end for
  result = addToken (result, in_macro, tok, fields)
  return result  


def getLayer (s, layer):
  if s.startswith ('%') and ':' in s:  
    t = s[1:s.find(':')]
    s = s[s.find(':')+1:]
    if t in layertable:
      layer = layertable [t]
  return s, layer  
           
def pcbTitleBlock(board):
  titleBlock = TitleBlock()
  pcb_title = board.GetTitleBlock()
  titleBlock.revision = pcb_title.GetRevision()
  titleBlock.date = pcb_title.GetDate() 
  titleBlock.title = pcb_title.GetTitle()
  titleBlock.company = pcb_title.GetCompany()
  titleBlock.comment1 = pcb_title.GetComment1()
  titleBlock.comment2 = pcb_title.GetComment2()
  titleBlock.comment3 = pcb_title.GetComment3()
  titleBlock.comment4 = pcb_title.GetComment4()

  titleBlock.filename = os.path.basename(board.GetFileName())
  titleBlock.filename = os.path.splitext(titleBlock.filename)[0] 
  return titleBlock
             
def autoFillFields():
  # if True, read titleblock form schematic file
  # else read titleblock for kicad_pcb file
  opt_schematic_titleblock = True
  
  my_board = pcbnew.GetBoard()

  numlayers = pcbnew.LAYER_ID_COUNT
  for i in range(numlayers):
    layertable[my_board.GetLayerName(i)] = i
  
  sch = Schematic (my_board.GetFileName())
  if opt_schematic_titleblock:
    # get title block fields from schematic file  
    titleBlock = sch.titleBlock
  else:
    titleBlock = pcbTitleBlock(my_board)

  date_now = "{:%Y-%m-%d}".format(datetime.now())

  allfields = {}
  allfields ["%DT"] = date_now
  allfields ["%T"] = titleBlock.title
  allfields ["%R"] = titleBlock.revision
  allfields ["%D"] = titleBlock.date
  allfields ["%Y"] = titleBlock.company
  allfields ["%F"] = titleBlock.filename
  allfields ["%C0"] = titleBlock.comment1
  allfields ["%C1"] = titleBlock.comment2
  allfields ["%C2"] = titleBlock.comment3
  allfields ["%C3"] = titleBlock.comment4
  
  allfields.update (sch.userfield)
  
  # scan modules    
  for module in my_board.GetModules():
    fpid = module.GetFPID()
    p = module.GetPosition()
    px = p[0]
    py = p[1]

    if fpid.GetFootprintName() == "text_F_Cu":
      module.Value().SetLayer(pcbnew.F_Cu)
                                      
    elif fpid.GetFootprintName() == "text_auto_date":
      new_text = date_now
      print ("Setting module %s Value to '%s' " % ( module.GetReference(), new_text ) )
      module.Value().SetText(new_text)
      
    elif fpid.GetFootprintName() == "text_auto":
      # set some defaults
      layer = pcbnew.F_SilkS
      pos = pcbnew.wxPoint (px,py)
      textsize = pcbnew.wxSize (pcbnew.FromMM(1), pcbnew.FromMM(1)) 
      thickness = pcbnew.FromMM(0.15)

      # remove existing text
      gfx = module.GraphicalItems()
      for g in gfx:
        if isinstance (g, pcbnew.TEXTE_MODULE):
          layer = g.GetLayer()
          pos = g.GetTextPosition()
          textsize = g.GetSize()
          thickness = g.GetThickness()
          # italic, orientation 
          module.GraphicalItems().Remove (g)

      s = module.GetValue()
      s, layer = getLayer (s ,layer) 
      # substitute for key strings
      s = macroReplace (s, allfields)

      print ("Setting module %s to '%s' " % ( module.GetReference(), s ) )
      
      # add text
      text = pcbnew.TEXTE_MODULE(module)
      text.SetPosition (pos)
      text.SetLayer (layer)
      text.SetVisible (True)
      text.SetSize (textsize)
      text.SetThickness (thickness)
      text.SetText (s)
      module.Add (text) 
      
      module.SetPosition (module.GetPosition())
      
    elif (fpid.GetFootprintName() == "auto_barcode39" or
      fpid.GetFootprintName() == "auto_barcode128"):

      layer = pcbnew.F_SilkS
      s = module.GetValue()
      s, layer = getLayer (s, layer) 
      # substitute for key strings
      s = macroReplace (s, allfields)
      
      print ("Setting module %s barcode to '%s'" % ( module.GetReference(), s ) )
      
      # remove existing lines
      gfx = module.GraphicalItems()
      for g in gfx:
        if g.GetLayer() == layer or g.GetLayer() == pcbnew.F_CrtYd:
          module.GraphicalItems().Remove (g)

      if fpid.GetFootprintName() == "auto_barcode128":
        barcode = BarcodeCode128.Code128 (module, layer)
      else:
        barcode = BarcodeCode39.Code39 (module, layer)
      barcode.drawBarcode(s)
      
      # for some reason, this is required to reset the graphic lines to the right position  
      module.SetPosition (module.GetPosition())
        
  # requires version > 4
  #my_board.Refresh()
        
autoFillFields()
