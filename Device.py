import publicip

class Device():

    def __init__(self,device_name,device_id,device_kind):
        self.device_name=device_name
        self.device_id=device_id
        self.device_kind=device_kind
        #Get device's IP for sending to server side.
        self.device_ip=publicip.get()