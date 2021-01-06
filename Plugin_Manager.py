import Plugin

class Plugin_Manager():

    def __init__(self):

        self.current_plugins=[]

    def num_of_plugins(self):

        return len(self.current_plugins)

    def add_plugin(self,plugin):

        self.current_plugins.append(plugin)

    def remove_plugin(self,plugin):

        self.current_plugins.remove(plugin)