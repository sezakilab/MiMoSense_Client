import UI
import config

if __name__ == '__main__':
    #Load all global parameters and settings.
    Config = config.global_var()
    Config.setup_global_paremeters()
    #Render the ui for software.
    ui = UI.UI()