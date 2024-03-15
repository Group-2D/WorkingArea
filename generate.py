from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen


class TimetableApp(App):
    def build(self):
        # Main layout - vertical BoxLayout
        main_layout = BoxLayout(orientation='vertical', spacing=10, padding=(50, 50))

        # "Generate Timetable" label
        label = Label(text="Generate Timetable", font_size=20, size_hint_y=None, height=50)

        # Buttons layout - horizontal BoxLayout
        buttons_layout = BoxLayout(orientation='horizontal', spacing=10, size_hint_y=None, height=50)

        # View Timetable Button
        view_button = Button(text="View Timetable")

        # Generate New Timetable Button
        generate_button = Button(text="Generate New Timetable")

        # Adding buttons to the buttons layout
        buttons_layout.add_widget(view_button)
        buttons_layout.add_widget(generate_button)

        # Adding label and buttons layout to the main layout
        main_layout.add_widget(Label())
        main_layout.add_widget(label)
        main_layout.add_widget(Label())
        main_layout.add_widget(buttons_layout)
        main_layout.add_widget(Label())

        return main_layout


if __name__ == '__main__':
    TimetableApp().run()
