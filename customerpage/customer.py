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
from kivy.uix.behaviors import ToggleButtonBehavior
from kivy.uix.screenmanager import Screen

# Window Size
from kivy.core.window import Window

Window.size = (891, 559)
sidebarcenter = 0.138

def reSize(*args):
   Window.size = (891, 559)
   return True
Window.bind(on_resize = reSize)

# Methods
def _rent_pressed(instance):
    pass

# Button Classes
# Search Button Class
class searchButton(ButtonBehavior, FloatLayout, Image):
    def __init__(self, **kwargs):
        self.padding = (50,50)
        super(searchButton, self).__init__(**kwargs)
        self.source = "assets/search-icon.png"
        self.sresult = Label(text = "Search the catalog by clicking on the lens icon!",
                                color = kivy.utils.get_color_from_hex("c10b13"),
                                markup = True,
                                font_size = 18,
                                pos_hint = {'x': 6, 'y': 2.9},
                                halign='center')
        self.add_widget(self.sresult)

    def on_press(self):
        self.source = "assets/search-icon-down.png"

    def on_release(self):
        self.source = "assets/search-icon.png"
        self.sresult.text = "Search Results:\n{no} result(s) have been found!".format(no=str("$temp"))

# Wishlist Button Class
class wishlistButton(ToggleButtonBehavior, FloatLayout, Image):
    def __init__(self, **kwargs):
        self.padding = (50,50)
        super(wishlistButton, self).__init__(**kwargs)
        self.source = "assets/wishlist-icon.png"

    def on_state(self, widget, value):
        if value == 'down':
            self.source = self.source = "assets/wishlist-icon-on.png"
        else:
            self.source = self.source = "assets/wishlist-icon.png"

# Logout Button Class
class logoutButton(ButtonBehavior,FloatLayout, Image):
    def __init__(self, **kwargs):
        self.padding = (50,50)
        super(logoutButton, self).__init__(**kwargs)
        self.source = "assets/logout-icon.png"  

    def on_press(self):
        self.source = "assets/logout-icon-down.png"

    def on_release(self):
        self.source = "assets/logout-icon.png"
        App.get_running_app().screen_manager.current = "Login"

# Wishlist Menu Button Class
class wishlistMenuButton(ButtonBehavior,FloatLayout, Image):
    def __init__(self, **kwargs):
        self.padding = (50,50)
        super(wishlistMenuButton, self).__init__(**kwargs)
        self.source = "assets/wishlist-menu-icon.png"  

    def on_press(self):
        self.source = "assets/wishlist-menu-icon-down.png"

    def on_release(self):
        self.source = "assets/wishlist-menu-icon.png"

# Checkbox Button Class
class checkboxButton(ToggleButtonBehavior, FloatLayout, Image):
    def __init__(self, **kwargs):
        self.padding = (50,50)
        super(checkboxButton, self).__init__(**kwargs)
        self.source = "assets/checkbox.png"

    def on_state(self, widget, value):
        if value == 'down':
            self.source = "assets/checkbox-on.png"
        else:
            self.source = "assets/checkbox.png"


# Book Item
class Book(BoxLayout,FloatLayout):
    def __init__(self,book,**kwargs):
        super(Book, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.spacing = 30
        # Book Texture
        bookimg = Image(source = book[0],
                    pos_hint = {'center_x':.5,'center_y':.5},
                    height = 180,
                    size_hint_y=None)
        # Book Name Label
        booktext = Label(text = book[3],
                    color = kivy.utils.get_color_from_hex("c10b13"),
                    font_size = 16,
                    pos_hint = {'center_x': .5,'center_y':.5},
                    halign = 'center')
        # Price Tag Label
        bookprice = Label(text = "Borrow price/week: £{rent}".format(rent=book[5],buy=book[6]),
                    color = kivy.utils.get_color_from_hex("c10b13"),
                    font_size = 14,
                    pos_hint = {'center_x': .5,'center_y':.5},
                    halign = 'center')

        bookbutbar = FloatLayout(size_hint_x=1,size_hint_y=None)
        # Rent Button
        bookrentbut = Button(text="BORROW",color=(0,0,0),bold=True,outline_width=3,outline_color=(1,1,1),
                                font_size=14,
                                size_hint_x=.7,
                                size_hint_y=.5,
                                pos_hint = {'center_x': 0.35,'center_y':.85},
                                background_normal=
                                "assets/login-ejust-buttontemplate.png",
                                background_down=
                                "assets/login-ejust-buttontemplate-down.png")
        bookrentbut.bind(on_press=_rent_pressed)
        bookwishlistbut = wishlistButton()
        bookwishlistbut.size_hint = (.2,.35)
        bookwishlistbut.pos_hint = {"center_x": 0.85, "center_y": .85}
        # Adding all widgets
        bookbutbar.add_widget(bookrentbut)
        bookbutbar.add_widget(bookwishlistbut)
        self.add_widget(bookimg)
        self.add_widget(booktext)
        self.add_widget(bookprice)
        self.add_widget(bookbutbar)

# Category Item
class Category(BoxLayout,FloatLayout, Label):
    def __init__(self,category,**kwargs):
        super(Category, self).__init__(**kwargs)
        self.orientation = 'horizontal'
        self.checkbut = checkboxButton()
        self.checkbut.size_hint = (1,1)

        categorytext = Label(text=category,
                            size_hint = (1,1),
                            halign = "left",
                            shorten = True,
                            text_size = (130,None),
                            bold=True,
                            font_size=14)
        self.height = 35
        self.size_hint = (0.7,None)
        self.add_widget(self.checkbut)
        self.add_widget(categorytext)

# Grid Class
class ItemsGrid(ScrollView, FloatLayout):
    def __init__(self, **kwargs):
        super(ItemsGrid, self).__init__(**kwargs)
        grid = GridLayout(cols=2, spacing = (150,350), padding=(50,50), size_hint_y=None)
        grid.bind(minimum_height=grid.setter('height'))

        Books = [["assets/books/book1.png",5,1,"Probability & Statistics",["Mathematics","Engineering"],12.49,299.9],
                ["assets/books/book2.png",4,2,"Software Engineering",["Computer Science"],14.99,349.9]]
        
        #  Ignore the two lines below
        grid.add_widget(Image(source="assets/login-ejust-buttonempty.png"))
        grid.add_widget(Image(source="assets/login-ejust-buttonempty.png"))

        for i in range(5):
            for book in Books:
                grid.add_widget(Book(book))
        
        self.size_hint=(0.7,None)
        self.size=(Window.width, Window.height-110)
        self.pos_hint = {'center_x': 0.65, 'center_y': 0.5}
        self.bar_color = kivy.utils.get_color_from_hex("242525")
        self.bar_inactive_color = kivy.utils.get_color_from_hex("757575")
        self.bar_width = 10
        self.scroll_type = ['bars','content']  
        self.add_widget(grid)

class CategoriesBox(ScrollView, FloatLayout):
    def __init__(self,**kwargs):
        super(CategoriesBox, self).__init__(**kwargs)
        box = BoxLayout(orientation='vertical',size_hint_y=None)
        box.bind(minimum_height=box.setter('height'))

        Categories = ["Computer Science","Engineering","Pharma-D","International Business","Humanities",
                        "Liberal Arts","Digital Logic","Mathematics","Embedded Systems","Electronics","Algorithms Analysis"]
        
        for genre in Categories:
            box.add_widget(Category(genre))
        
        self.size_hint=(0.27,None)
        self.size=(Window.width, Window.height-325)
        self.bar_color = (1,1,1)
        self.pos_hint = {'center_y': 0.4}
        self.bar_inactive_color = kivy.utils.get_color_from_hex("757575")
        self.bar_width = 5
        self.scroll_type = ['bars','content']  
        self.add_widget(box)

# Customer Page
class CustomerPage(Screen, FloatLayout):
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

        # Grids & Boxes
        self.add_widget(ItemsGrid(),2)
        self.add_widget(CategoriesBox(),0)

        # Images
        # Side Bar
        self.sidebar = Image(source="assets/customer-ejust-sidebar.png",
                                size_hint = (1,1),
                                allow_stretch = True,
                                pos_hint={"center_x": sidebarcenter, "y": 0})
        self.add_widget(self.sidebar,1)
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
        self.welcometext = Label(text = "Welcome! {user}".format(user="user320210207"),
                        color = (1,1,1),
                        font_size = 16,
                        pos_hint = {"center_x": sidebarcenter, "center_y": 0.82},
                        halign='center')
        self.add_widget(self.welcometext)
        # Categories Text
        self.categorytext = Label(text= "CATEGORIES:",
                        bold = True,
                        color = (1,1,1),
                        font_size = 18,
                        pos_hint = {"center_x": sidebarcenter-0.07, "center_y": 0.655},
                        halign='center')
        self.add_widget(self.categorytext)

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

        # Wishlist Menu Button
        self.wishlistbut = wishlistMenuButton()
        self.wishlistbut.size_hint = (.07,.07)
        self.wishlistbut.pos_hint = {"center_x": 0.244, "center_y": .135}
        self.add_widget(self.wishlistbut)

        # Logout Button
        self.logoutbut = logoutButton()
        self.logoutbut.size_hint = (.07,.07)
        self.logoutbut.pos_hint = {"center_x": 0.194, "center_y": .135}
        self.add_widget(self.logoutbut)