#!/usr/bin/env python3
import time, gpiod
from gpiod.line import Direction, Value
from mfrc522 import SimpleMFRC522

LED_GPIO  = 17
CHIP_PATH = "/dev/gpiochip0"

cfg = gpiod.LineSettings(direction=Direction.OUTPUT, output_value=Value.INACTIVE)
req = gpiod.request_lines(CHIP_PATH, consumer="rfid-led", config={LED_GPIO: cfg})

def led_on():  req.set_value(LED_GPIO, Value.ACTIVE)
def led_off(): req.set_value(LED_GPIO, Value.INACTIVE)
def flash_success(): led_on(); time.sleep(0.8); led_off()
def flash_fail():
    for _ in range(3):
        led_on(); time.sleep(0.12)
        led_off(); time.sleep(0.12)

AUTHORIZED_UIDS = {
    "33:CC:07:05:FD": "My Test Card"
}

def format_uid(uid_int):
    b = uid_int.to_bytes((uid_int.bit_length()+7)//8 or 4, "big")
    return ":".join(f"{x:02X}" for x in b)

def main():
    reader = SimpleMFRC522()
    print("RFID ready — tap a tag (Ctrl+C to quit)")
    try:
        while True:
            uid_int, text = reader.read()
            uid = format_uid(uid_int)
            print(f"Detected UID: {uid} | Tag text: {text!r}")
            if uid in AUTHORIZED_UIDS:
                print(f"Authorized: {AUTHORIZED_UIDS[uid]}")
                flash_success()
            else:
                print("Unknown tag.")
                flash_fail()
            time.sleep(0.5)
    except KeyboardInterrupt:
        pass
    finally:
        led_off(); req.release()

if __name__ == "__main__":
    main()
