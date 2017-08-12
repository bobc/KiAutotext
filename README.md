# KiAutotext
Script to place fields from title block and user fields onto PCB

# Features

- Easily place text on F_SilkS or F_Cu layers
- User fields can be placed in a special UserTitleBlock component
- Insert any field from the schematic title block, filename, today's date or user title block fields
- Place text on any layer 
- Generate Code39 and Code128 barcodes from text fields

# Customisation

- text fields on the PCB can be moved to any position or layer, the text size changed, and the changes will be preserved.

# Caveats

Placing text fields on copper layers is officially deprecated as it is not handled by the push and shove router or DRC. It is recommended to place keep out zones around text fields.

![sample](https://github.com/bobc/KiAutotext/raw/master/sample1/sample.png "sample")

# Installation
- copy the libraries to a suitable folder and add them to your project
- copy the python files to a path accessible from KiCad e.g. c:/kicad_utils/KiAutotext

# Running the script
- In pcbnew, open the Python scripting console (Tools->Scripting Console)
- type the command `sys.path.append("c:/kicad_utils/KiAutotext")` into the console (replace with actual path)
- **NB always save any changed files in KiCad before running the script**
- type the command `execfile("c:/kicad_utils/KiAutotext/KiAutotext.py")` whenever you need to update the PCB fields

# Detailed Usage

Special component names 
-----------------------
```
UserTitleBlock  User fields in UserTitleBlock are added to list of substitution 
                macros.
```  
Special footprint names
-----------------------
```
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
                
                If the Value field has a prefix "%layer:", where layer is a layer
                name in the current PCB (e.g. "F.Cu") then the text will be placed
                on that layer.


auto_barcode39 
                The Value field is used to create a Code39 barcode. Invalid 
                characters are stripped out, and guard characters added to start
                and end.
                
auto_barcode128 
                The Value field is used to create a Code128 barcode.
                  
```
