# superCar
Bluetooth remote controlled car

Simple application - It is a double belt car from my childhood. Each side has its own 6V DC motor.
Hardware part contains only schematic because there are used conventional modules from ebay - read more in the hardware/desc.txt
Used microcontroler is STM32F100C8T6.

Firmware is based on ChibiOS stable version 2.6 - commit hash is in the Makefile - help yourself ;)
The firmware only takes data from the bluetooth module (behaves like a virtual COM port to the computer/tablet), decodes data and set speed of motors - nothing more.

GUI is written in python using PyQt4. It is a simple GUI with two sliders - you can control speed of each motor separately. 
It also contains building script to build it with pyinstaller for windows. Linux users do not need any builds - just run the main.py file
