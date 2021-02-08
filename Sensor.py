import subprocess
import sys
import os
from multiprocessing import Process, Value, Array
import settings


import sensors.temperature as temp
import sensors.humidity as humidity
import sensors.gps as gps
import sensors.co2 as co2
import sensors.air_pressure as air_pressure
import sensors.motion as motion
import sensors.audio as audio
import sensors.uv as uv


class Sensor():

    def __init__(self, name):

        self.name=name
 #       self.on_or_off=on_or_off

    def start(self):
 #       self.on_or_off=True
 #       success_or_not = True
 #       return success_or_not
        if self.name == "temperature":
#            print("Here temp \n")
            settings.temp_process = Process(target=temp.getdata, args=(settings.temperature,))
            settings.temp_process.daemon = True
            settings.temp_process.start()
 #           self.process.join()
            print(settings.temperature.value)
        elif self.name == "humidity":
            settings.humidity_process = Process(target=humidity.getdata, args=(settings.humidity,))
            settings.humidity.daemon = True
            settings.humidity_process.start()

        elif self.name == "gps":
            settings.gps_process = Process(target=gps.getdata, args=(settings.gps,))
            settings.gps_process.daemon = True
            settings.gps_process.start()

        elif self.name == "air_pressure":
            settings.air_pressure_process = Process(target=air_pressure.getdata, args=(settings.air_pressure,))
            settings.air_pressure_process.daemon = True
            settings.air_pressure_process.start()

        elif self.name == "co2":
            settings.co2_process = Process(target=co2.getdata, args=(settings.co2,))
            settings.co2_process.daemon = True
            settings.co2_process.start()

        elif self.name == "motion":
            settings.motion_process = Process(target=motion.getdata, args=(settings.motion,))
            settings.motion_process.daemon = True
            settings.motion_process.start()    

        elif self.name == "uv":
            settings.uv_process = Process(target=uv.getdata, args=(settings.uv,))
            settings.uv_process.daemon = True
            settings.uv_process.start()
        
        elif self.name == "audio":
            settings.audio_process = Process(target=audio.getdata, args=(settings.audio,))
            settings.audio_process.daemon = True
            settings.audio_process.start()
 

    def stop(self):
        if self.name == "temperature":
            settings.temp_process.terminate()
        elif self.name == "humidity":
            settings.humidity_process.terminate()
        elif self.name == "gps":
            settings.gps_process.terminate()
        elif self.name == "co2":
            settings.co2_process.terminate()
        elif self.name == "air_pressure":
            settings.air_pressure_process.terminate()
        elif self.name == "motion":
            settings.motion_process.terminate()
        elif self.name == "uv":
            settings.uv_process.terminate()
        elif self.name == "audio":
            settings.audio_process.terminate()
        
#        filename = self.name+".py"
#        command = "pkill -f "+filename
#        p = subprocess.call([command],shell=True)
        
#        data_filename = "temp/"+self.name+".txt"
#        with open(data_filename,"w") as f:
#                f.close()
#        print("Sensor "+self.name.title()+" is now stopped.")
  #      self.on_or_off=False

   #     success_or_not = True
   #     return success_or_not
        
    def Read(self):
        data =1
        return data
