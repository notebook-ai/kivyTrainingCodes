from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class pageLayout(BoxLayout):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		# define widgets
		self.ti_result = TextInput(hint_text="which button is click", multiline=False, font_size=14, size_hint=(1,0.3)) 
		self.btn_login = Button(text="login", font_size=16, size_hint=(1,0.4))
		self.btn_back = Button(text="back", font_size=16, size_hint=(1,0.4))
		self.btn_forward = Button(text="forward", font_size=16, size_hint=(1,0.4))
		# define callback some widgets	
		self.btn_login.bind(on_press=self.callback) 
		self.btn_back.bind(on_press=self.callback) 
		self.btn_forward.bind(on_press=self.callback) 
		# add_widgets on page
		self.add_widget(self.ti_result)
		self.add_widget(self.btn_login)	
		self.add_widget(self.btn_back)	
		self.add_widget(self.btn_forward)	

	def callback(self, instance):
		print('The button <%s> is being pressed' % instance.text)
		val = instance.text
		if val == "login":
			self.ti_result.text = "you click on login button"
			#print( "you click on login button")
		elif val == "back":
			self.ti_result.text = "you click on back button"
			#print("you click on back button")
		else:
			self.ti_result.text = "you click on forward button"
			#print("you click on forward button")
		
  
class localPage(App):
	def build(self):
		return pageLayout()

if __name__ == "__main__":
	localPage().run()