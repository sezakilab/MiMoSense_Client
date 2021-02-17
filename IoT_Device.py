#import bluetooth
import time

class Device:
    #Set up a device name before running, much easier to find.
    device_name = ""
    server_sock=bluetooth.BluetoothSocket( bluetooth.RFCOMM ) 
    port = 1
    client_sock = null

    def wait_connection():
        Device.server_sock.bind(("",port)) 
        Device.server_sock.listen(1) 
        Device.client_sock,address = server_sock.accept() 
        print ("Accepted connection from ",address)

    def receive_message():
        recvdata = client_sock.recv(1024) 
        print "Received \"%s\" through Bluetooth" % recvdata 
        print (recvdata)

    def send_message(data):
        timestamp = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
        Device.client_sock.send(data)

class Sensor:
    #Run the sensor's script according to the frequency.

if __name__ == '__main__':
    #Start waitting for connection
    while True:
        device = Device()
        print ("Waitting for connection...")
        device.wait_connection() 
        #If connection stopped, print "connection lost.", and wait for another connection.