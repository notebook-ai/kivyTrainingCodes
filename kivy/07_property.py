from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty

class MyLayout(Widget):
	username = ObjectProperty(None) #observation
	password = ObjectProperty(None) #observation

	def btnLogin(self):
		print("username: " + self.username.text + "\n" + "Password: " + self.password.text)
		self.username.text = ""
		self.password.text = ""


class designProperty(App):

	def build(self):
		return MyLayout()

if __name__ == "__main__":
	designProperty().run()