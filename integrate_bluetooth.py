import serial
def bluetooth_call():
    uart_channel = serial.Serial("/dev/ttyAMA0", baudrate=9600, timeout=2)
    
    data = ""
    data1 = ""
    while True:
        data = uart_channel.read(1)
        data1 += data
        print(data1)
        
        uart_channel.flush()
        data = ""
        data1 = ""
    
