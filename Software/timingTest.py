from lib import gCodeHandler
import sys
import time
def connectGantry():
    available_ports = gCodeHandler.get_available_ports()
    print("Available ports:")
    #choose between available ports
    for i in range(len(available_ports)): print("port {}: {}".format(i, available_ports[i]))
    t=input("choose port: (typically shows board as USB serial device)")
    port=available_ports[int(t)].device
    print(port)
    try:
        gcode_handler = gCodeHandler.GCodeHandler(port)
        gcode_handler.connect()
    
    except:
        print("Error connecting to gantry")
        sys.exit()
    return gcode_handler

gCodeHandler=connectGantry()
gCodeHandler.auto_home()
start_time = time.time()
gCodeHandler.set_position(0,1000)
gCodeHandler.wait()
end_time = time.time()

print(f"Time taken to set position: {end_time - start_time} seconds")
