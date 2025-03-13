import serial
import time
import serial.tools.list_ports
import sys

class GCodeHandler:
    """
    A class to handle communication with a gantry system using G-code commands over a serial connection.
    Attributes:
        port (str): The serial port to connect to.
        baudrate (int): The baud rate for the serial connection. Default is 115200.
        timeout (int): The timeout for the serial connection in seconds. Default is 1.
        speed (int): The speed of the gantry. Default is 1000.
        unit (str): The unit of measurement for the gantry. Default is "mm".
        serial_connection (serial.Serial): The serial connection object.
    Methods:
        connect():
            Establishes a serial connection to the gantry.
        disconnect():
            Closes the serial connection to the gantry.
        send_gcode(gcode):
            Sends G-code commands to the gantry and returns the responses.
        set_speed(newspeed):
            Sets the speed of the gantry.
        set_position(x, y):
            Sets the position of the gantry.
        get_position():
            Gets the current position of the gantry.
        is_finished():
            Checks if the gantry has finished its movement.
        motors_off():
            Turns off the motors of the gantry.
        auto_home():
            Homes all motors to their end stops.
        jog(x, y):
            Moves the gantry by a relative amount.
        wait():
            Waits for the gantry to finish its movement.
        error_handler(response):
            Handles errors in the response from the gantry.
    """

    def __init__(self, port, baudrate=115200, timeout=1):
        self.port = port
        self.baudrate = baudrate
        self.timeout = timeout
        self.speed=5000 #Gantry standard speed
        self.unit="mm"
        self.serial_connection = None
        #Set end stops

    def connect(self):
        try:
            self.serial_connection = serial.Serial(self.port, self.baudrate, timeout=self.timeout)
            time.sleep(2)  # Wait for the connection to establish
            if self.serial_connection.is_open:
                print(f"Connected to {self.port} at {self.baudrate} baud.")
            else:
                print(f"Failed to open serial connection to {self.port}.")
                sys.exit(0)
        except serial.SerialException as e:
            print(f"Error connecting to {self.port}: {e}")
            sys.exit(0)

    def disconnect(self):
        if self.serial_connection and self.serial_connection.is_open:
            self.serial_connection.close()
            print(f"Disconnected from {self.port}.")

    def send_gcode(self, gcode):
        if self.serial_connection and self.serial_connection.is_open:
            if isinstance(gcode, list):
                #If gcode is a list of commands
                for cmd in gcode:
                    self.serial_connection.write((cmd + '\n').encode())
                    responses = []
                    while True:
                        response = self.serial_connection.readline().decode().strip()
                        if not response:
                            break
                        responses.append(response)
                    print(f"Sent: {cmd}, Received: {' '.join(responses)}")
            else:    
                #If gcode is a string
                self.serial_connection.write((gcode + '\n').encode())
                responses = []
                while True:
                    response = self.serial_connection.readline().decode().strip()
                    if not response:
                        break
                    responses.append(response)
                print(f"Sent: {gcode}, Received: {' '.join(responses)}")
            return responses
        else:
            print("Serial connection is not open.")
            return None
    def set_speed(self, newspeed,unit="mm"):
        #Set speed and unit of gantry
        self.unit=unit
        self.speed=newspeed
        if self.unit=="mm":
            self.send_gcode("G21") #Set units to mm
        else:
            raise ValueError("Unit not supported")
        
    def set_position(self, x, y):
        #Set position of gantry
        self.send_gcode("G0 X{} Y{} F{}".format(x, y, self.speed))
    def get_position(self):
        #Get current position of gantry
        self.send_gcode("M114")
        return self.serial_connection.readline().decode().strip()
    def is_finished(self):
        #Determine if movement is finished
        self.send_gcode("M400")
        return self.serial_connection.readline().decode().strip()
    def motors_off(self):
        #Turn motors off
        self.send_gcode("M84")
    def auto_home(self):
        #home all motors to end stops
        self.send_gcode("G90") #Set absolute positioning
        res= self.send_gcode("G28 X Y") # for now, only home X. Change when both axes mounted!!
        self.wait()
        #self.send_gcode("G90") #Set relative positioning
        self.send_gcode("M666 X-0.5") #Set end stop offset for X
    def jog(self, x, y):
        #Jog the gantry
        self.send_gcode("G91") #Set relative positioning
        self.send_gcode("G0 X{} Y{} F{}".format(x, y, self.speed))
        self.send_gcode("G90")
    def wait(self):
        #Wait for gantry to finish movement
        t=self.send_gcode("M400")
        while "ok" not in t:
            t = self.send_gcode("M400")

    def error_handler(self, response):
        if "error" in response.lower():
            print("Error detected in response. Disconnecting...")
            self.disconnect()


def get_available_ports():
        ports = serial.tools.list_ports.comports()
        # return [port.device for port in ports]
        return ports

if __name__ == "__main__":
    

    available_ports = get_available_ports()
    print("Available ports:", available_ports)
    #port = 'COM3'
    #choose between available ports
    for i in range(len(available_ports)): print("port {}: {}".format(i, available_ports[i]))
    t=input("choose port:")
    port=available_ports[int(t)]
    gcode_handler = GCodeHandler(port)

    gcode_handler.connect()
    
    # Example G-code commands
    gcode_commands = [
        "G21",  # Set units to millimeters
        "G90",  # Absolute positioning
        "G0 X100 F200"  # Move to (100, 100) at 300 mm/min
        "G0 X000 F300",  # Move to (100, 100) at 300 mm/min
    ]
    #gcode_commands=["G0 X-200 Y-200 F300"]

    for command in gcode_commands:
        gcode_handler.send_gcode(command)

    gcode_handler.disconnect()