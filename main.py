import UI
import config

# Control system's sensed data upload or not.
upload_or_not = False
# System's upload frequency. (second as unit)
upload_frequency = 1
# Control system store data into database or not.
stored_or_not = False

# Sensing frequency for gps module. (take only one data in one second)
gps_frequency = 1
temperature_frequency = 1
humidity_frequency = 1
motion_frequency = 10
head_motion_frequency = 10

if __name__ == '__main__':
    #Load all global parameters and settings.
    Config = config.global_var()
    Config.setup_global_paremeters()
    #Render the ui for software.
    ui = UI.UI()