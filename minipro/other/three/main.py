from kivymd.app import MDApp

from searchpopupmenu import SearchPopupMenu
from servicesmapview import ServicesMapView
from gpshelper import GpsHelper

import sqlite3

class MainApp(MDApp):
    database = None
    cursor = None
    search_pop = None

    def on_start(self):
        self.database = sqlite3.connect("mydb.sqlite")
        self.cursor = self.database.cursor()
        GpsHelper().run()
        self.search_pop = SearchPopupMenu()
        self.theme_cls.primary_palette = "DeepPurple"



MainApp().run()