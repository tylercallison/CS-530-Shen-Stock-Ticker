# CS-530-Shen-Stock-Ticker
Stock Ticker for Final Project for CS-530 with Professor Shen at SDSU

## Summary
Our project was to create a working prototype of a stock ticker with near-real-time stock information. Since stock tickers are extremely expensive, we wanted to create an affordable, product by creating our own. We successfully created a working prototype with near-real-time stock information provided by Yahoo Finance data. Our Python script runs on any Rasberry Pi that can connect to an LED panel (MAX7219 Chipset required) through GPIO pins to scrape stock information from Yahoo’s REST API and convert the processed text to visual output that can be displayed on an LED screen in a rolling format. We completed all of the necessary tasks for a working prototype.

## Requirements
1. LED Screens that use the MAX7219 Chipset required.
2. Any Raspberry Pi with GPIO pins

## Installing necessary software:

1. Enable SPI on Raspberry Pi
2. Install Necessary Drivers

`sudo usermod -a -G spi,gpio pi`<br />
`sudo apt install build-essential python3-dev python3-pip libfreetype6-dev libjpeg-dev libopenjp2-7 libtiff5`

3. Install the latest luma.led_matrix library

`sudo python3 -m pip install --upgrade luma.led_matrix`

