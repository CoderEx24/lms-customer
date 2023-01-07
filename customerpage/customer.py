import kivy
kivy.require('2.1.0')

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView
from kivy.graphics import Rectangle
from kivy.uix.image import Image
from kivy.uix.behaviors import ButtonBehavior
import config

# Window Size
from kivy.core.window import Window

Window.size = (891, 559)
sidebarcenter = 0.138

def reSize(*args):
   Window.size = (891, 559)
   return True
Window.bind(on_resize = reSize)

# Methods
def _add_book(instance):
    pass
def _search_pressed(instance):
    pass

class searchButton(ButtonBehavior, FloatLayout, Image):
    def __init__(self, **kwargs):
        self.padding = (50,50)
        super(searchButton, self).__init__(**kwargs)
        self.source = "assets/search-icon.png"
        self.sresult = Label(text = "Search the catalog by clicking on the lens icon!",
                                color = kivy.utils.get_color_from_hex("c10b13"),
                                font_size = 18,
                                pos_hint = {'x': 6, 'y': 2.9},
                                halign='center')
        self.add_widget(self.sresult)

    def on_press(self):
        self.source = "assets/search-icon-down.png"
        self.sresult.text = "Search Results: "

    def on_release(self):
        self.source = "assets/search-icon.png"


class Book(BoxLayout):
    def __init__(self,book,**kwargs):
        super(Book, self).__init__(**kwargs)
        self.orientation = 'vertical'
        bookimg = Image(source = book[0],
                    height = 225,
                    pos_hint = {'center_x':.5,'center_y':.5},
                    size_hint_y=None)
        booktext = Label(text = book[3],
                    color = kivy.utils.get_color_from_hex("c10b13"),
                    font_size = 16,
                    pos_hint = {'center_x': .47,'center_y':.5},
                    halign = 'center')
        self.add_widget(bookimg)
        self.add_widget(booktext)
        # self.add_widget(bookrent)
        # self.add_widget(bookbuy)
        # self.add_widget(bookwishlist)

# Grid
class ItemsGrid(ScrollView, FloatLayout):
    def __init__(self, **kwargs):
        super(ItemsGrid, self).__init__(**kwargs)
        grid = GridLayout(size_hint_x=1,cols=2, spacing = (150,350), padding=(50,50), size_hint_y=None)
        grid.bind(minimum_height=grid.setter('height'))
        Books = [["assets/books/book1.png",5,1,"Probability & Statistics",["Mathematics","Engineering"],12.5,300],
                ["assets/books/book2.png",4,2,"Software Engineering",["Computer Science"],14,350]]
        
        for i in range(5):
            for book in Books:
                grid.add_widget(Book(book))


        self.size_hint=(0.7,None)
        self.size=(Window.width, Window.height-110)
        self.pos_hint = {'center_x': 0.65, 'center_y': 0.5}
        self.bar_color = kivy.utils.get_color_from_hex("242525")
        self.bar_width = 10
        self.scroll_type = ['content']  
        self.add_widget(grid)

# Customer Page
class CustomerPage(FloatLayout):
    def _update_bg(self, instance, value):
        self.bg.pos = instance.pos
        self.bg.size = instance.size

    def __init__(self, **kwargs):
        super(CustomerPage, self).__init__(**kwargs)
        with self.canvas.before:
            self.bg = Rectangle(color = (1,1,1),
                                size=self.size,
                                pos=self.pos)
        self.bind(size=self._update_bg, pos=self._update_bg)

        # Grid
        self.add_widget(ItemsGrid())
        # Images
        # Side Bar
        self.sidebar = Image(source="assets/customer-ejust-sidebar.png",
                                size_hint = (1,1),
                                allow_stretch = True,
                                pos_hint={"center_x": sidebarcenter, "y": 0})
        self.add_widget(self.sidebar)
        # Library Logo
        self.logo = Image(source="assets/login-ejustlibrary-logo.png",
                                size_hint = (0.14,0.14),
                                pos_hint={"center_x": sidebarcenter, "center_y": .91})
        self.add_widget(self.logo)
        # Gray Bar
        self.gbar = Image(source="assets/login-gray-bar.png",
                                size_hint = (1,0.5),
                                allow_stretch = True,
                                pos_hint={"center_x": 0.5, "center_y": .02})
        self.add_widget(self.gbar)
        # SWE Text
        self.swetext = Image(source="assets/login-ejust-swetext.png",
            size_hint = (1,1),
            pos_hint={"center_x": 0.5, "center_y": .04})
        self.add_widget(self.swetext)

        # Labels
        # Welcome Text
        self.welcometext = Label(text = "Welcome! {user}".format(user="320210207"),
                        color = (1,1,1),
                        font_size = 16,
                        pos_hint = {"center_x": sidebarcenter, "center_y": 0.82},
                        halign='center')
        self.add_widget(self.welcometext)
        # Search Results Text

        

        # Textboxes
        # Search Box
        self.searchBox = TextInput(multiline=False,
                                size_hint = (.2,.06),
                                hint_text = "Search",
                                pos_hint = {"center_x": sidebarcenter-0.03, "center_y": .75})
        self.add_widget(self.searchBox)

        # Buttons
        # Search Lens Button
        self.searchbut = searchButton()
        self.searchbut.size_hint = (.07,.07)
        self.searchbut.pos_hint = {"center_x": 0.244, "center_y": .75}
        self.add_widget(self.searchbut)

class MainApp(App): 
    def build(self):
        self.title = config.projecttitle
        self.icon = "assets/ejust-project-icon.png"
        return CustomerPage()

if __name__ == '__main__':
    MainApp().run()