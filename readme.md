# Raspberry Pi 5 RFID Access System with LED Indicator

### Overview
A minimal RFID access-control demo for **Raspberry Pi 5** using:

- **MFRC522** RFID module (SPI0)
- **libgpiod v2** for GPIO (LED indicator)
- **rpi-lgpio** as the modern `RPi.GPIO` backend
- **Python 3.13 / Raspberry Pi OS Bookworm**

The system reads MIFARE cards, prints their UIDs, flashes an LED when a known tag is detected, and blinks rapidly for unknown tags.

---

## Features
- Works with **libgpiod v2** (`/dev/gpiochip0`)
- No deprecated `RPi.GPIO`
- Compatible with Bookworm / Python 3.13
- Simple authorized-UID list or external JSON file
- Fully self-contained virtual-environment setup

---

## Hardware

| Component | Raspberry Pi Pin | Function |
|------------|------------------|-----------|
| **MFRC522 VCC** | 1 (3V3) | Power |
| **MFRC522 GND** | 6 (GND) | Ground |
| **SDA / SS** | 24 (GPIO 8 / CE0) | SPI CS0 |
| **SCK** | 23 (GPIO 11) | SPI Clock |
| **MOSI** | 19 (GPIO 10) | SPI MOSI |
| **MISO** | 21 (GPIO 9) | SPI MISO |
| **RST** | 22 (GPIO 25) | Reset |
| **IRQ** | – | Unused |
| **LED Anode (+)** | 11 (GPIO 17) | Status LED |
| **LED Cathode (–)** | 9 (GND) | Ground |

LED wiring: **GPIO17 → 330 Ω → LED → GND**

---

## Software Setup

```bash
sudo apt update
sudo apt install -y python3-libgpiod python3-rpi-lgpio python3-spidev gpiod
sudo raspi-config nonint do_spi 0
sudo usermod -aG gpio,spi $USER
reboot

##creating the project environment
mkdir -p ~/projects/rfid-led
cd ~/projects/rfid-led
python3 -m venv --system-site-packages .venv
source .venv/bin/activate
pip install --upgrade pip
pip install mfrc522

