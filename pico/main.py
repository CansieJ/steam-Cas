from machine import Pin
import time
import neopixel

# Use on-board led
led = Pin(25, Pin.OUT)

# Blink led to confirm succesful flashing
for _ in range(5):
    led(0)
    time.sleep(.1)
    led(1)
    time.sleep(.1)


time.sleep(5)
# Wait for data from the connection
while True:
    data = input() #'{choise};{data}'
    data = data.split(';')

    if data[0] == '0':
        berekening = data[1].split('-')
        aantal_neopixel = (int(berekening[1]) / int(berekening[0])) * 8
        np = neopixel.NeoPixel(machine.Pin(13), 8)
        for j in range(8):
            np[j] = [0, 0, 0]
        np.write()
        for i in range(aantal_neopixel):
            np[i] = [255, 0, 0]
            np.write()
            time.sleep(1)
    elif data[0] == '1':

        time.sleep(1)
        print("Turning led on.")
        led(1)
    else:
        print("Unknown command.")

