import kivy
kivy.require('2.1.0')

from kivy.app import App
import loginpage.login
import registerpage.register
import customerpage.customer
import config
from kivy.uix.screenmanager import ScreenManager, FadeTransition

class MainApp(App):
    def build(self):
        self.title = config.projecttitle
        self.icon = "assets/ejust-project-icon.png"
        self.login_screen = loginpage.login.LoginPage(name="Login")
        self.register_screen = registerpage.register.RegisterPage(name="Register")
        self.customer_screen = customerpage.customer.CustomerPage(name="Customer")
        self.screen_manager = ScreenManager(transition = FadeTransition())

        for screen in [self.login_screen,self.register_screen,self.customer_screen]:
            self.screen_manager.add_widget(screen)
        
        return self.screen_manager

if __name__ == '__main__':
    MainApp().run()