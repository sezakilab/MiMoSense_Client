import bluetooth

class bt_device:
    s = bluetooth.BluetoothSocket( bluetooth.RFCOMM ) 
    port = 1

    # Need to turn on the bluetooth first.
    def get_all_bluetooth_devices(self):
        print("Performing inquiry...")
        nearby_devices = bluetooth.discover_devices(lookup_names = True)
        print("found %d devices" % len(nearby_devices))
        return nearby_devices

    def connect_device(device_name,device_addr):
        success_or_not = 0
        try:
            bt_device.s.connect((device_addr,bt_device.port))
            success_or_not = 1
            return success_or_not
        except bluetooth.btcommon.BluetoothError as err:
            # If error happened, get back to the name display. 
            print("connection failed")
            return success_or_not 

    def send_info(info):
        bt_device.s.send(info)

    def receive_info():
        data = bt_device.s.recv(1024)
        return data

    def close_connection():
        bt_device.s.close()