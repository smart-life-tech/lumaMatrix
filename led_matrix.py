from luma.led_matrix.device import max7219
from luma.core.interface.serial import spi, noop
from luma.core.render import canvas
import time

# Define the GPIO pins for each MAX7219 module
gpio_pins = [14, 15, 18, 23, 24, 25, 8, 7]  # Example GPIO pins, adjust as needed

# Initialize each MAX7219 module
serial = spi(port=0, device=0, gpio=noop())
devices = [max7219(serial, cascaded=8, gpio=pin) for pin in gpio_pins]

# Define a simple animation
frames = [
    [0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],
    [0x18, 0x3C, 0x7E, 0xFF, 0xFF, 0x7E, 0x3C, 0x18],
    [0x3C, 0x7E, 0xDB, 0xFF, 0xFF, 0xDB, 0x7E, 0x3C],
    [0x7E, 0xDB, 0xA5, 0xFF, 0xFF, 0xA5, 0xDB, 0x7E],
    [0xFF, 0xA5, 0x81, 0xFF, 0xFF, 0x81, 0xA5, 0xFF],
    [0x7E, 0xDB, 0xA5, 0xFF, 0xFF, 0xA5, 0xDB, 0x7E],
    [0x3C, 0x7E, 0xDB, 0xFF, 0xFF, 0xDB, 0x7E, 0x3C],
    [0x18, 0x3C, 0x7E, 0xFF, 0xFF, 0x7E, 0x3C, 0x18]
]

# Display the animation
while True:
    for frame in frames:
        for device in devices:
            with canvas(device) as draw:
                for i in range(8):
                    draw.point((i, 0), fill="white" if frame[i] & (1 << i) else "black")
        time.sleep(0.2)
