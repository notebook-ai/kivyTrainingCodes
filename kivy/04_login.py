from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class LoginLayout(BoxLayout):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		self.orientation = "vertical"
		self.spacing = 10
		self.padding = [10, 10]

		self.ti_username = TextInput(hint_text="Username", multiline=False, font_size=14, size_hint=(1,0.3)) 
		self.ti_password = TextInput(hint_text="Password", multiline=False, font_size=14, password=True, size_hint=(1,0.3))
		self.btn_login = Button(text="LOGIN", font_size=16, size_hint=(1,0.4))
		self.btn_login.bind(on_press=self.callback) # callback function for login button

		self.add_widget(self.ti_username)
		self.add_widget(self.ti_password)	
		self.add_widget(self.btn_login)	
  
	def callback(self, instance):
		print(f"{instance}")
		# print(f"Username: {self.ti_username.text}\nPassword: {self.ti_password.text}")
		self.ti_username.text = ""
		self.ti_password.text = ""

class LoginPage(App):
	def build(self):
		return LoginLayout()

if __name__ == "__main__":
	LoginPage().run()