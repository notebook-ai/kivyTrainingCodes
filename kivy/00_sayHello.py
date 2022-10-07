import kivy
# kivy.require('2.1.0')
from kivy.app import App
from kivy.uix.label import Label

class helloApp(App):
    def build(self): # build method to override
        return Label(text='Hello man!')
    

# if this file is start the project and variable name has been equal  main then run application
if __name__ == '__main__':
    helloApp().run()