from serial.tools import list_ports
import serial
import json


def read_serial(port):
    """Read data from serial port and return as string."""
    line = port.read(1000)
    return line.decode()

def update_neopixel():
    with open("storage/myFriends.json", "r") as file:
        data_jsonfile = json.load(file)
        data = data_jsonfile
    online = 0
    total = 0
    for friend in data["friendslist"]["friends"]:
        if friend["response"]["players"][0]["personastate"] == 1:
            online+=1

        total+=1
    data = f"0;{total}-{online}\r"
    serial_port.write(data.encode())
    pico_output = read_serial(serial_port)
    pico_output = pico_output.replace('\r\n', ' ')
    print("[PICO] " + pico_output)



# First manually select the serial port that connects to the Pico
serial_ports = list_ports.comports()

pico_port = serial_ports[0].device

# Open a connection to the Pico
with serial.Serial(port=pico_port, baudrate=115200, bytesize=8, parity='N', stopbits=1, timeout=1) as serial_port:
    if serial_port.isOpen():
        print("[INFO] Using serial port", serial_port.name)
    else:
        print("[INFO] Opening serial port", serial_port.name, "...")
        serial_port.open()

    try:
        # Request user input
        commands = ['off', 'on', 'exit']
        while True:
            choice = input("Command? [" + ", ".join(commands) + "] ")

            if choice == 'neopixel update':
                update_neopixel()
            elif choice == 'on':
                # Turn led on by sending a '1'
                data = "1\r"
                serial_port.write(data.encode())
                pico_output = read_serial(serial_port)
                pico_output = pico_output.replace('\r\n', ' ')
                print("[PICO] " + pico_output)
            elif choice == 'exit':
                # Exit user input loop
                break
            else:
                print("[WARN] Unknown command.")

    except KeyboardInterrupt:
        print("[INFO] Ctrl+C detected. Terminating.")
    finally:
        # Close connection to Pico
        serial_port.close()
        print("[INFO] Serial port closed. Bye.")

