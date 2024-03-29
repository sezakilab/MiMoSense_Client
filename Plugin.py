
class Plugin():

    def __init__(self,name,on_or_off=False):

        self.name=name
        self.on_or_off=on_or_off

    def start(self):
        print("Plugin "+self.name.title() + " is now working.")
        self.on_or_off = True

    def stop(self):
        print("Plugin "+self.name.title() + " is now stopped.")
        self.on_or_off = False