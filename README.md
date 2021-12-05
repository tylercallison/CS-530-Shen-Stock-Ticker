# CS-530-Shen-Stock-Ticker
Stock Ticker for Final Project for CS-530 with Professor Shen at SDSU

LED Screens that use the MAX7219 Chipset required.

Installing necessary software:

1. Enable SPI on raspberry pi
2. Install Necessary Drivers

$ sudo usermod -a -G spi,gpio pi
$ sudo apt install build-essential python3-dev python3-pip libfreetype6-dev libjpeg-dev libopenjp2-7 libtiff5

3. Install the latest luma.led_matrix library

$ sudo python3 -m pip install --upgrade luma.led_matrix

