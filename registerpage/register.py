import kivy
kivy.require('2.1.0')

from kivy.app import App
from kivy.uix.textinput import TextInput
from kivy.uix.floatlayout import FloatLayout
from kivy.graphics import Rectangle
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.screenmanager import Screen

# Window Size
from kivy.core.window import Window
Window.size = (567, 588)
generalcenter = 0.5

# Methods
def _register_pressed(instance):
    App.get_running_app().screen_manager.current = "Customer"

def _cancel_pressed(instance):
    App.get_running_app().screen_manager.current = "Login"
    pass

# Register Page

class RegisterPage(Screen, FloatLayout):
    def _update_bg(self, instance, value):
        self.bg.pos = instance.pos
        self.bg.size = instance.size

    def __init__(self, **kwargs):
        super(RegisterPage, self).__init__(**kwargs)
        with self.canvas.before:
            self.bg = Rectangle(source=
                                "assets/register-static-background.png",
                                size=self.size,
                                pos=self.pos)

        self.bind(size=self._update_bg, pos=self._update_bg)

        # Images
        # Gray Bar
        self.gbar = Image(source="assets/login-gray-bar.png",
                    size_hint = (1,1),
                    allow_stretch = True,
                    pos_hint={"center_x": generalcenter, "center_y": .85})
        self.add_widget(self.gbar)
        # Library Logo
        self.logo = Image(source="assets/login-ejustlibrary-logo.png",
                    size_hint = (0.28,0.28),
                    pos_hint={"center_x": generalcenter, "center_y": .85})
        self.add_widget(self.logo)
        # SWE Text
        self.swetext = Image(source="assets/login-ejust-swetext.png",
            size_hint = (1,1),
            pos_hint={"center_x": 0.5, "center_y": .04})
        self.add_widget(self.swetext)

        # Labels
        # Welcome Label
        # self.welcomelabel = Label(text="[b]Registration Form[/b]\nSign up to continue!",
        #                         markup = True,
        #                         halign='center',
        #                         color=(0,0,0),
        #                         font_size=14,
        #                         size_hint=(.2,.04),
        #                         outline_width=2,
        #                         outline_color=(1,1,1),
        #                         pos_hint={"center_x": generalcenter, "center_y": .75})
        # self.add_widget(self.welcomelabel)
        # Textboxes
        # Username Textbox
        self.uicon = Image(source="assets/user-icon.png",
                    size_hint = (.5,.5),
                    pos_hint={"center_x": 0.27, "center_y": .65})
        self.add_widget(self.uicon)
        self.userBox = TextInput(multiline=False,
                        hint_text = "Username",
                        size_hint = (.45,.06),
                        pos_hint = {"center_x": .55, "center_y": .65})
        self.add_widget(self.userBox)
        # E-Mail Textbox
        self.eicon = Image(source="assets/email-icon.png",
                    size_hint = (.5,.5),
                    pos_hint={"center_x": 0.27, "center_y": .55})
        self.add_widget(self.eicon)
        self.emailBox = TextInput(multiline=False,
                        size_hint = (.45,.06),
                        hint_text = "Email",
                        pos_hint = {"center_x": .55, "center_y": .55})
        self.add_widget(self.emailBox)
        # Password Textbox
        self.picon = Image(source="assets/password-lock-icon.png",
                    size_hint = (1,1),
                    pos_hint={"center_x": 0.27, "center_y": .45})
        self.add_widget(self.picon)
        self.passBox = TextInput(multiline=False,
                        size_hint = (.45,.06),
                        hint_text = "Password",
                        password = True,
                        pos_hint = {"center_x": .55, "center_y": .45}) 
        self.add_widget(self.passBox)
        # Confirm Password Textbox
        self.picon2 = Image(source="assets/password-lock-icon.png",
                    size_hint = (.5,.5),
                    pos_hint={"center_x": 0.27, "center_y": .35})
        self.add_widget(self.picon2)
        self.cpassBox = TextInput(multiline=False,
                        size_hint = (.45,.06),
                        hint_text = "Confirm Password",
                        password = True,
                        pos_hint = {"center_x": .55, "center_y": .35}) 
        self.add_widget(self.cpassBox)

        # Buttons
        # Register Button
        self.registerbut = Button(text="REGISTER",color=(0,0,0),bold=True,outline_width=3,outline_color=(1,1,1),
                                size_hint=(.23,.1),
                                font_size=14,
                                pos_hint={"center_x": .65, "center_y": .22},
                                background_normal=
                                "assets/login-ejust-buttontemplate.png",
                                background_down=
                                "assets/login-ejust-buttontemplate-down.png")
        self.registerbut.bind(on_press=_register_pressed)
        self.add_widget(self.registerbut)
        # Cancel Button
        self.cancelbut = Button(text="CANCEL",color=(0,0,0),bold=True,outline_width=3,outline_color=(1,1,1),
                                font_size=14,
                                size_hint=(.23,.1),
                                pos_hint={"center_x": .35, "center_y": .22},
                                background_normal=
                                "assets/login-ejust-buttontemplate.png",
                                background_down=
                                "assets/login-ejust-buttontemplate-down.png")
        self.cancelbut.bind(on_press=_cancel_pressed)
        self.add_widget(self.cancelbut)