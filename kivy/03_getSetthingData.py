import kivy
from kivy.app import App
from kivy.uix.label import Label
import settings

class getSetthingsApp(App):
    def build(self): # build method to override
        connectionString = "Server ip: {ip} \nDatabase Name: {dbName}".format(
            ip = settings.SERVER_IP,
            dbName = settings.DATABASE_NAME,
            )
        return Label(text= connectionString)
       
    

# if this file is start the project and variable name has been equal  main then run application
if __name__ == '__main__':
    getSetthingsApp().run()