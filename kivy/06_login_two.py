from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget

class loginLayout(Widget):
	pass

class desginLoginTwoApp(App):
	def build(self):
		return loginLayout()

if __name__ == "__main__":
	desginLoginTwoApp().run()