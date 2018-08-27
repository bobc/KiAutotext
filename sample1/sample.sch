EESchema Schematic File Version 4
LIBS:sample-cache
EELAYER 26 0
EELAYER END
$Descr A4 11693 8268
encoding utf-8
Sheet 1 1
Title "Test Project"
Date "2017-08-10"
Rev "Rev 1"
Comp "World Enterprises"
Comment1 "comment1"
Comment2 "comment2"
Comment3 "comment3"
Comment4 "comment4"
$EndDescr
$Comp
L autotext:text_F_SilkS M1
U 1 1 598F5935
P 2150 1600
F 0 "M1" H 2150 1700 60  0000 C CNN
F 1 "text_F_SilkS" H 2150 1600 60  0000 C CNN
F 2 "autotext:text_F_SilkS" H 2150 1500 60  0000 C CNN
F 3 "" H 2150 1600 60  0001 C CNN
	1    2150 1600
	1    0    0    -1  
$EndComp
$Comp
L autotext:text_F_Cu M4
U 1 1 598F59A4
P 2100 2300
F 0 "M4" H 2100 2400 60  0000 C CNN
F 1 "text_F_Cu" H 2100 2300 60  0000 C CNN
F 2 "autotext:text_F_Cu" H 2100 2200 60  0000 C CNN
F 3 "" H 2100 2300 60  0001 C CNN
	1    2100 2300
	1    0    0    -1  
$EndComp
$Comp
L autotext:text_auto_date M8
U 1 1 598F59C7
P 2200 2900
F 0 "M8" H 2200 3000 60  0000 C CNN
F 1 "text_auto_date" H 2200 2900 60  0000 C CNN
F 2 "autotext:text_auto_date" H 2200 2800 60  0000 C CNN
F 3 "" H 2200 2900 60  0001 C CNN
	1    2200 2900
	1    0    0    -1  
$EndComp
$Comp
L autotext:text_auto M2
U 1 1 598F5A25
P 5450 1600
F 0 "M2" H 5450 1700 60  0000 C CNN
F 1 "title=%T date=%D rev=%R comp=%Y file=%F" H 5450 1600 60  0000 C CNN
F 2 "autotext:text_auto" H 5450 1500 60  0000 C CNN
F 3 "" H 5450 1600 60  0001 C CNN
	1    5450 1600
	1    0    0    -1  
$EndComp
$Comp
L autotext:text_auto M5
U 1 1 598F5A8A
P 5400 2250
F 0 "M5" H 5400 2350 60  0000 C CNN
F 1 "Assembly %AsyPN, Rev %AsyRev" H 5400 2250 60  0000 C CNN
F 2 "autotext:text_auto" H 5400 2150 60  0000 C CNN
F 3 "" H 5400 2250 60  0001 C CNN
	1    5400 2250
	1    0    0    -1  
$EndComp
$Comp
L autotext:text_auto M7
U 1 1 598F5ABD
P 5400 2900
F 0 "M7" H 5400 3000 60  0000 C CNN
F 1 "%F.Cu:%PCBPN - %PCBRev" H 5400 2900 60  0000 C CNN
F 2 "autotext:text_auto" H 5400 2800 60  0000 C CNN
F 3 "" H 5400 2900 60  0001 C CNN
	1    5400 2900
	1    0    0    -1  
$EndComp
$Comp
L autotext:BarcodeCode39 M3
U 1 1 598F5B01
P 9200 1600
F 0 "M3" H 9200 1700 60  0000 C CNN
F 1 "%AsyPN" H 9200 1600 60  0000 C CNN
F 2 "autotext:auto_barcode39" H 9200 1500 60  0000 C CNN
F 3 "" H 9200 1600 60  0001 C CNN
	1    9200 1600
	1    0    0    -1  
$EndComp
$Comp
L autotext:BarcodeCode128 M6
U 1 1 598F5C37
P 9200 2250
F 0 "M6" H 9200 2350 60  0000 C CNN
F 1 "%T %PCBPN" H 9200 2250 60  0000 C CNN
F 2 "autotext:auto_barcode128" H 9200 2150 60  0000 C CNN
F 3 "" H 9200 2250 60  0001 C CNN
	1    9200 2250
	1    0    0    -1  
$EndComp
$Comp
L autotext:UserTitleBlock M9
U 1 1 598F5C9C
P 7550 5950
F 0 "M9" H 6950 6150 60  0000 C CNN
F 1 "UserTitleBlock" H 7200 6000 60  0000 C CNN
F 2 "" H 7550 5800 60  0000 C CNN
F 3 "" H 7550 5950 60  0000 C CNN
F 4 "A1234" H 7600 5900 60  0000 L CNN "AsyPN"
F 5 "A1" H 7600 5800 60  0000 L CNN "AsyRev"
F 6 "P1234" H 9600 5900 60  0000 L CNN "PCBPN"
F 7 "P1" H 9600 5800 60  0000 L CNN "PCBRev"
	1    7550 5950
	1    0    0    -1  
$EndComp
Text Notes 4900 6200 0    50   ~ 0
Put whatever fields and layout you like here\nonly rule is that the component must \nbe called "UserTitleBlock"
Text Notes 1400 1200 0    80   ~ 16
Simple text fields
Text Notes 4900 1200 0    80   ~ 16
Formatted text fields
Text Notes 8300 1250 0    80   ~ 16
Code 39 and Code 128 Barcodes
Text Notes 500  3000 0    50   ~ 0
Value field is replaced \nby today's date\n
Wire Notes Line
	1800 2900 1500 2900
Wire Notes Line
	1500 2800 1500 3050
Wire Notes Line
	1400 2800 1500 2800
Wire Notes Line
	1500 3050 1400 3050
Wire Notes Line
	3500 950  3500 5600
Wire Notes Line
	7600 950  7600 5500
Wire Notes Line
	7600 5500 7650 5500
Wire Notes Line
	6800 6850 6700 6750
Wire Notes Line
	6700 6750 6700 6950
Wire Notes Line
	6700 6950 6800 6850
Text Notes 4150 5100 0    50   ~ 0
The following substitutions are performed:\n\nStandard keys:\n  %F    the file base name\n  %DT   today's date\n                \nThe following are read from the title block of the corresponding schematic file:\n  %T    Project title\n  %R    Revision\n  %D    Issue Date\n  %Y    Company\n  %C0   Comment 1\n  %C1   Comment 2\n  %C2   Comment 3\n  %C3   Comment 4\n                \nAdditional substitutions are made according to user defined  \nfields from component "UserTitleBlock" if it exists.\n                \nIf the Value field has a prefix "%layer:", where layer is a layer\nname in the current PCB (e.g. "F.Cu") then the text will be placed\non that layer.
Wire Notes Line
	4800 6050 4000 6050
Wire Notes Line
	4000 6050 4000 4700
Wire Notes Line
	4000 4700 4100 4700
Wire Notes Line
	4000 3900 3950 3900
Wire Notes Line
	3950 3900 3950 4500
Wire Notes Line
	3950 4500 4000 4500
Wire Notes Line
	3950 4200 3800 4200
Wire Notes Line
	3800 4200 3800 6850
Wire Notes Line
	3800 6850 6800 6850
Wire Notes Line
	4800 6050 4750 6000
Wire Notes Line
	4750 6000 4750 6100
Wire Notes Line
	4750 6100 4800 6050
Wire Notes Line
	6650 5950 6650 6250
Wire Notes Line
	6650 6250 4850 6250
Wire Notes Line
	4850 6250 4850 5950
Wire Notes Line
	4850 5950 6650 5950
Wire Notes Line
	6650 6100 6800 6100
Wire Notes Line
	6800 6100 6750 6050
Wire Notes Line
	6750 6050 6750 6150
Wire Notes Line
	6750 6150 6800 6100
Text Notes 8100 3000 0    50   ~ 0
The same substitutions as for formatted text fields are performed.\n
$EndSCHEMATC
