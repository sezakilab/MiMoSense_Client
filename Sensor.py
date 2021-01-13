
class Sensor():

    def __init__(self, name, on_or_off=False):

        self.name=name
        self.on_or_off=on_or_off

    def start(self):

        print("Sensor "+self.name.title()+" is now working.")
        self.on_or_off=True
        success_or_not = True
        return success_or_not

    def stop(self):

        print("Sensor "+self.name.title()+" is now stopped.")
        self.on_or_off=False

        success_or_not = True
        return success_or_not

    def Read(self):
        data =1
        return data