import kivy
kivy.require('2.1.0')

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.floatlayout import FloatLayout
from kivy.graphics import Rectangle
from kivy.uix.image import Image
from kivy.uix.button import Button
import config

# Window Size
from kivy.core.window import Window
Window.size = (567, 558)
generalcenter = (0.87+0.67)/2
# Methods
def _login_pressed(instance):
    pass
    
def _register_pressed(instance):
    pass

def _fgtpwdbut_pressed(instance):
    instance.color=(0.5,0.73,1)
    
def _fgtpwdbut_released(instance):
    instance.color=(0.2,0.43,0.77)

# Login Page
class LoginPage(FloatLayout):
    def _update_bg(self, instance, value):
        self.bg.pos = instance.pos
        self.bg.size = instance.size

    def __init__(self, **kwargs):
        super(LoginPage, self).__init__(**kwargs)

        with self.canvas.before:
            self.bg = Rectangle(source=
                                "assets/login-static-background.png",
                                size=self.size,
                                pos=self.pos)

        self.bind(size=self._update_bg, pos=self._update_bg)

        # Images
        # Main Library Logo
        self.logo = Image(source="assets/login-ejustlibrary-logo.png",
                            size_hint = (0.37,0.37),
                            pos_hint={"center_x": .26, "center_y": .62})
        self.add_widget(self.logo)
        # Text Logo
        self.dlogo = Image(source="assets/login-ejustdetailed-logo.png",
                    size_hint = (1,1),
                    pos_hint={"center_x": generalcenter, "center_y": .83})
        self.add_widget(self.dlogo)
        # SWE Text
        self.swetext = Image(source="assets/login-ejust-swetext.png",
            size_hint = (1,1),
            pos_hint={"center_x": 0.5, "center_y": .04})
        self.add_widget(self.swetext)

        # Labels
        # Welcome Label
        self.welcomelabel = Label(text="[b]Welcome to E-Library![/b]\nKindly enter your credentials.",
                                markup = True,
                                halign='center',
                                color=(0,0,0),
                                font_size=14,
                                size_hint=(.2,.04),
                                outline_width=2,
                                outline_color=(1,1,1),
                                pos_hint={"center_x": generalcenter, "center_y": .67})
        self.add_widget(self.welcomelabel)
        # Textboxes
        # Username Textbox
        self.userBox = TextInput(multiline=False,
                    size_hint = (.23,.06),
                    pos_hint = {"center_x": .85, "center_y": .57})
        self.add_widget(Label(text="USERNAME:",
                        font_size = 14,
                        color = (0,0,0),
                        outline_width = 2,
                        outline_color = (1,1,1),
                        pos_hint = {"center_x": .65, "center_y": .57}))
        self.add_widget(self.userBox)
        # Password Textbox
        self.passBox = TextInput(multiline=False,
                    size_hint = (.23,.06),
                    password = True,
                    pos_hint = {"center_x": .85, "center_y": .47}) 
        self.add_widget(Label(text="PASSWORD:",
                        font_size = 14,
                        color = (0,0,0),
                        outline_width = 2,
                        outline_color = (1,1,1),
                        pos_hint = {"center_x": .65, "center_y": .47}))
        self.add_widget(self.passBox)

        # Buttons
        # Login Button
        self.loginbut = Button(text="LOGIN",color=(0,0,0),bold=True,outline_width=3,outline_color=(1,1,1),
                                size_hint=(.18,.1),
                                font_size=14,
                                pos_hint={"center_x": .67, "center_y": .35},
                                background_normal=
                                "assets/login-ejust-buttontemplate.png",
                                background_down=
                                "assets/login-ejust-buttontemplate-down.png")
        self.loginbut.bind(on_press=_login_pressed)
        self.add_widget(self.loginbut)
        # Register Button
        self.registerbut = Button(text="REGISTER",color=(0,0,0),bold=True,outline_width=3,outline_color=(1,1,1),
                                font_size=14,
                                size_hint=(.18,.1),
                                pos_hint={"center_x": .87, "center_y": .35},
                                background_normal=
                                "assets/login-ejust-buttontemplate.png",
                                background_down=
                                "assets/login-ejust-buttontemplate-down.png")
        self.registerbut.bind(on_press=_register_pressed)
        self.add_widget(self.registerbut)
        # Forgot Password Button
        self.fgtpwdbut = Button(text="Forgot password?",
                                color=(0.2,0.43,0.77), # P.S: I got this shade randomly first try.
                                bold=True,
                                font_size=14,
                                size_hint=(.2,.04),
                                outline_width=2,
                                outline_color=(1,1,1),
                                pos_hint={"center_x": generalcenter, "center_y": .25},
                                background_normal="assets/login-ejust-buttonempty.png",
                                background_down="assets/login-ejust-buttonempty.png")
        self.fgtpwdbut.bind(on_press=_fgtpwdbut_pressed)
        self.fgtpwdbut.bind(on_release=_fgtpwdbut_released)
        self.add_widget(self.fgtpwdbut)

class MainApp(App): 
    def build(self):
        self.title = config.projectitle
        return LoginPage()  

if __name__ == '__main__':
    MainApp().run()