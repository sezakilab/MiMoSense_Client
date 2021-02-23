from multiprocessing import Process, Value, Array
import subprocess
import sys
import os
import config
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
        # self.on_or_off=on_or_off

    def start(self,frequency):
        # self.on_or_off=True
        # success_or_not = True
        # return success_or_not
        if self.name == "temperature":
            # print("Here temp \n")
            config.temp_process = Process(target=temp.getdata, args=(config.temperature,frequency,))
            config.temp_process.daemon = True
            config.temp_process.start()
 #           self.process.join()
            print(config.temperature.value)
        elif self.name == "humidity":
            config.humidity_process = Process(target=humidity.getdata, args=(config.humidity,frequency,))
            config.humidity.daemon = True
            config.humidity_process.start()

        elif self.name == "gps":
            config.gps_process = Process(target=gps.getdata, args=(config.gps,frequency,))
            config.gps_process.daemon = True
            config.gps_process.start()

        elif self.name == "air_pressure":
            config.air_pressure_process = Process(target=air_pressure.getdata, args=(config.air_pressure,frequency,))
            config.air_pressure_process.daemon = True
            config.air_pressure_process.start()

        elif self.name == "co2":
            config.co2_process = Process(target=co2.getdata, args=(config.co2,frequency,))
            config.co2_process.daemon = True
            config.co2_process.start()

        elif self.name == "motion":
            config.motion_process = Process(target=motion.getdata, args=(config.motion,frequency,))
            config.motion_process.daemon = True
            config.motion_process.start()    

        elif self.name == "uv":
            config.uv_process = Process(target=uv.getdata, args=(config.uv,frequency,))
            config.uv_process.daemon = True
            config.uv_process.start()
        
        elif self.name == "audio":
            config.audio_process = Process(target=audio.getdata, args=(config.audio,frequency,))
            config.audio_process.daemon = True
            config.audio_process.start()
 

    def stop(self):
        if self.name == "temperature":
            config.temp_process.terminate()
        elif self.name == "humidity":
            config.humidity_process.terminate()
        elif self.name == "gps":
            config.gps_process.terminate()
        elif self.name == "co2":
            config.co2_process.terminate()
        elif self.name == "air_pressure":
            config.air_pressure_process.terminate()
        elif self.name == "motion":
            config.motion_process.terminate()
        elif self.name == "uv":
            config.uv_process.terminate()
        elif self.name == "audio":
            config.audio_process.terminate()
        
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
