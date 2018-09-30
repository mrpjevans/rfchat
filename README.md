# rfchat
A simple chat app for demonstrating communication over 433Mhz. Accompanies the tutorial in MagPi #75. See [https://www.raspberrypi.org/magpi/]() for further details.

Also includes send and receive utilties based on [https://github.com/milaq/rpi-rf/]() where more information can be found on using the Raspberry Pi for 433Mhz communication.

## System Requirements
* Raspberry Pi (any model)
* Raspian Stretch (including Lite) 

## Installation

Pre-requisities:

```bash
$ cd
$ sudo apt install python3-pip
$ pip3 install rpi-rf
```

Main install:

```bash
$ cd
$ git clone https://github.com/mrpjevans/rfchat.git
```

## Usage

#### Chat app

```bash
python3 ~/rfchat/rfchat.py
```
Ctrl+c to exit

#### Test Receive

```bash
python3 ~/rfchat/receive.py
```
Ctrl+c to exit

#### Test Send

```bash
python3 ~/rfchat/send.py n
```
Where 'n' is an integer