from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.core.window import Window

class LoginScreen(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = [50, 50, 50, 0]  # Changed padding to accommodate the back button
        self.spacing = 20
        self.size_hint = (None, None)
        self.size = (400, 350)  # Increased the width to accommodate the back button
        self.center = Window.center

        # Username Input
        self.username_label = Label(text='Username:', size_hint=(None, None), size=(100, 30), halign='left')
        self.username_input = TextInput(size_hint=(None, None), size=(300, 50), multiline=False, halign='left')

        # Password Input
        self.password_label = Label(text='Password:', size_hint=(None, None), size=(100, 30), halign='left')
        self.password_input = TextInput(password=True, size_hint=(None, None), size=(300, 50), halign='left')

        # Login Button
        self.login_button = Button(text='Login here', size_hint=(None, None), size=(200, 50))
        self.login_button.bind(on_press=self.login)

        # Back Button
        self.back_button = Button(text='Back', size_hint=(None, None), size=(100, 50))
        self.back_button.bind(on_press=self.go_back)

        # Container for the login and back buttons
        button_container = BoxLayout(size_hint=(None, None), size=(400, 50))
        button_container.add_widget(self.login_button)
        button_container.add_widget(self.back_button)

        # Add widgets to the layout
        self.add_widget(self.username_label)
        self.add_widget(self.username_input)
        self.add_widget(self.password_label)
        self.add_widget(self.password_input)
        self.add_widget(button_container)

    def login(self, instance):
        username = self.username_input.text
        password = self.password_input.text
        # Implement your login logic here

    def go_back(self, instance):
        # Handle going back to the previous screen or action
        pass  # Replace pass with your actual implementation


class LoginApp(App):
    def build(self):
        return LoginScreen()


if __name__ == '__main__':
    LoginApp().run()
