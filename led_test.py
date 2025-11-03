import time, gpiod
from gpiod.line import Direction, Value

LED_GPIO = 17
CHIP = "/dev/gpiochip0"

cfg = gpiod.LineSettings(direction=Direction.OUTPUT, output_value=Value.INACTIVE)
req = gpiod.request_lines(CHIP, consumer="led-test", config={LED_GPIO: cfg})

req.set_value(LED_GPIO, Value.ACTIVE)
time.sleep(0.5)
req.set_value(LED_GPIO, Value.INACTIVE)
print("LED OK (libgpiod v2)")
req.release()
