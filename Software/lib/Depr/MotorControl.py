import tkinter as tk
import serial
import time

def send_command():
    spd = speedEntry.get().zfill(3)
    dir = directionEntry.get()
    dir = 0 if dir == "CW" else 1
    rev = revEntry.get().zfill(3)
    motor = motorEntry.get().zfill(3)
    try:
        bin(int(motor,2))
    except:
        print("Motor number must be binary")
        return
    motor=int(motor,2) #convert to binary to send
    cmd = str(dir) + ";" + rev + ";" + spd + ";" + str(motor)
    ser = serial.Serial('COM4', 9600, timeout=0,parity=serial.PARITY_NONE, rtscts=0)
    print("motor: ", motor)
    time.sleep(2)
    ser.write(cmd.encode())
    time.sleep(2)
    res = ser.read()
    res=(res.decode('utf-8'))
    print("serial response: ",res)
    ser.close()
def emergency_stop():
    ser = serial.Serial('COM4', 9600, timeout=0,parity=serial.PARITY_NONE, rtscts=0)
    time.sleep(2)
    cmd = "0;000;000"
    ser.write(cmd.encode())
    ser.close()
#Set up GUI https://jalals.medium.com/how-to-control-stepper-motor-with-gui-written-in-python-feat-arduino-8e77139f6852
root = tk.Tk()
root.title("Stepper Motor Control GUI")
root.geometry("400x100")

root.minsize(500,100)
root.maxsize(500,100)

#Motor
motorLabel = tk.Label(root, text =  "Motor # enabled (1111 for all, 0000 for none)")
motorEntry = tk.Entry(root)
motorEntry.insert(0, "1111")
motorLabelComment = tk.Label(root, text = "x1x2y1y2")

motorLabel.grid(row=0, column=0)
motorEntry.grid(row=0, column=1)
motorLabelComment.grid(row = 0, column = 2)
#Speed
speedLabel = tk.Label(root, text =  "Speed")
speedEntry = tk.Entry(root)
speedEntry.insert(0, "100")
speedLabelComment = tk.Label(root, text = "1..100 %")

speedLabel.grid(row=1, column=0)
speedEntry.grid(row=1, column=1)
speedLabelComment.grid(row = 1, column = 2)

#Direction
directionLabel = tk.Label(root, text =  "Direction")
directionEntry = tk.Entry(root)
directionEntry.insert(0,"CW")
directionLabelComment = tk.Label(root, text = "CW/CCW")

directionLabel.grid(row=2, column=0)
directionEntry.grid(row = 2, column= 1)
directionLabelComment.grid(row = 2, column =2)

#Rev
revLabel = tk.Label(root, text =  "Revolutions")
revEntry = tk.Entry(root)
revEntry.insert(0,"1")
revLabelComment = tk.Label(root, text = "0..100 revs")

revLabel.grid(row = 3, column=0)
revEntry.grid(row = 3, column= 1)
revLabelComment.grid(row = 3, column =2)

sendCommandButton = tk.Button(root, text="Send Command", command=send_command)
sendCommandButton.grid(row=4, column=1)
emergencyStop = tk.Button(root, text = "STOP!", command = emergency_stop)
emergencyStop.grid(row=4, column = 2)
root.mainloop()

