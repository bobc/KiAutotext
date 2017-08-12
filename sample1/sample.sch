EESchema Schematic File Version 2
LIBS:74xgxx
LIBS:74xx
LIBS:ac-dc
LIBS:actel
LIBS:adc-dac
LIBS:allegro
LIBS:Altera
LIBS:analog_devices
LIBS:analog_switches
LIBS:atmel
LIBS:audio
LIBS:battery_management
LIBS:bbd
LIBS:bosch
LIBS:brooktre
LIBS:cmos4000
LIBS:cmos_ieee
LIBS:conn
LIBS:contrib
LIBS:cypress
LIBS:dc-dc
LIBS:device
LIBS:digital-audio
LIBS:diode
LIBS:display
LIBS:dsp
LIBS:elec-unifil
LIBS:ESD_Protection
LIBS:ftdi
LIBS:gennum
LIBS:graphic
LIBS:hc11
LIBS:intel
LIBS:interface
LIBS:ir
LIBS:Lattice
LIBS:leds
LIBS:linear
LIBS:logo
LIBS:maxim
LIBS:mechanical
LIBS:memory
LIBS:microchip
LIBS:microchip_dspic33dsc
LIBS:microchip_pic10mcu
LIBS:microchip_pic12mcu
LIBS:microchip_pic16mcu
LIBS:microchip_pic18mcu
LIBS:microchip_pic24mcu
LIBS:microchip_pic32mcu
LIBS:microcontrollers
LIBS:modules
LIBS:motorola
LIBS:motors
LIBS:motor_drivers
LIBS:msp430
LIBS:nordicsemi
LIBS:nxp
LIBS:nxp_armmcu
LIBS:onsemi
LIBS:opto
LIBS:Oscillators
LIBS:philips
LIBS:power
LIBS:powerint
LIBS:Power_Management
LIBS:pspice
LIBS:references
LIBS:regul
LIBS:relays
LIBS:rfcom
LIBS:sensors
LIBS:silabs
LIBS:siliconi
LIBS:stm32
LIBS:stm8
LIBS:supertex
LIBS:switches
LIBS:texas
LIBS:transf
LIBS:transistors
LIBS:triac_thyristor
LIBS:ttl_ieee
LIBS:valves
LIBS:video
LIBS:wiznet
LIBS:Worldsemi
LIBS:Xicor
LIBS:xilinx
LIBS:zetex
LIBS:Zilog
LIBS:autotext
EELAYER 25 0
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
L text_F_SilkS M1
U 1 1 598F5935
P 2450 3050
F 0 "M1" H 2450 3150 60  0000 C CNN
F 1 "text_F_SilkS" H 2450 3050 60  0000 C CNN
F 2 "autotext:text_F_SilkS" H 2450 2950 60  0000 C CNN
F 3 "" H 2450 3050 60  0001 C CNN
	1    2450 3050
	1    0    0    -1  
$EndComp
$Comp
L text_F_Cu M4
U 1 1 598F59A4
P 2400 3750
F 0 "M4" H 2400 3850 60  0000 C CNN
F 1 "text_F_Cu" H 2400 3750 60  0000 C CNN
F 2 "autotext:text_F_Cu" H 2400 3650 60  0000 C CNN
F 3 "" H 2400 3750 60  0001 C CNN
	1    2400 3750
	1    0    0    -1  
$EndComp
$Comp
L text_auto_date M8
U 1 1 598F59C7
P 2450 4450
F 0 "M8" H 2450 4550 60  0000 C CNN
F 1 "text_auto_date" H 2450 4450 60  0000 C CNN
F 2 "autotext:text_auto_date" H 2450 4350 60  0000 C CNN
F 3 "" H 2450 4450 60  0001 C CNN
	1    2450 4450
	1    0    0    -1  
$EndComp
$Comp
L text_auto M2
U 1 1 598F5A25
P 5150 3100
F 0 "M2" H 5150 3200 60  0000 C CNN
F 1 "title=%T date=%D rev=%R comp=%Y file=%F" H 5150 3100 60  0000 C CNN
F 2 "autotext:text_auto" H 5150 3000 60  0000 C CNN
F 3 "" H 5150 3100 60  0001 C CNN
	1    5150 3100
	1    0    0    -1  
$EndComp
$Comp
L text_auto M5
U 1 1 598F5A8A
P 5100 3750
F 0 "M5" H 5100 3850 60  0000 C CNN
F 1 "Assembly %AsyPN, Rev %AsyRev" H 5100 3750 60  0000 C CNN
F 2 "autotext:text_auto" H 5100 3650 60  0000 C CNN
F 3 "" H 5100 3750 60  0001 C CNN
	1    5100 3750
	1    0    0    -1  
$EndComp
$Comp
L text_auto M7
U 1 1 598F5ABD
P 5100 4400
F 0 "M7" H 5100 4500 60  0000 C CNN
F 1 "%F.Cu:%PCBPN - %PCBRev" H 5100 4400 60  0000 C CNN
F 2 "autotext:text_auto" H 5100 4300 60  0000 C CNN
F 3 "" H 5100 4400 60  0001 C CNN
	1    5100 4400
	1    0    0    -1  
$EndComp
$Comp
L BarcodeCode39 M3
U 1 1 598F5B01
P 7600 3100
F 0 "M3" H 7600 3200 60  0000 C CNN
F 1 "%AsyPN" H 7600 3100 60  0000 C CNN
F 2 "autotext:auto_barcode39" H 7600 3000 60  0000 C CNN
F 3 "" H 7600 3100 60  0001 C CNN
	1    7600 3100
	1    0    0    -1  
$EndComp
$Comp
L BarcodeCode128 M6
U 1 1 598F5C37
P 7600 3750
F 0 "M6" H 7600 3850 60  0000 C CNN
F 1 "%T %PCBPN" H 7600 3750 60  0000 C CNN
F 2 "autotext:auto_barcode128" H 7600 3650 60  0000 C CNN
F 3 "" H 7600 3750 60  0001 C CNN
	1    7600 3750
	1    0    0    -1  
$EndComp
$Comp
L UserTitleBlock M9
U 1 1 598F5C9C
P 7000 5650
F 0 "M9" H 6400 5850 60  0000 C CNN
F 1 "UserTitleBlock" H 6650 5700 60  0000 C CNN
F 2 "" H 7000 5500 60  0000 C CNN
F 3 "" H 7000 5650 60  0000 C CNN
F 4 "A1234" H 7050 5600 60  0000 L CNN "AsyPN"
F 5 "A1" H 7050 5500 60  0000 L CNN "AsyRev"
F 6 "P1234" H 9050 5600 60  0000 L CNN "PCBPN"
F 7 "P1" H 9050 5500 60  0000 L CNN "PCBRev"
	1    7000 5650
	1    0    0    -1  
$EndComp
$EndSCHEMATC
