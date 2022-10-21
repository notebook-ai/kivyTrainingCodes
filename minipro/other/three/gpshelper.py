from kivy.app import App
from kivy.utils import platform
from kivymd.uix.dialog import MDDialog

class GpsHelper():

    def run(self):
        gps_blinker = App.get_running_app().root.ids.mapview.ids.blinker
        gps_blinker.blink()

        if platform == 'android':
            from android.permissions import Permission, request_permissions
            def callback(permissions, results):
                if all([res for res in results]):
                    print("GOT ALL PERMISSIONS!")
                else:
                    print("DID NOT GET ALL PERMISSIONS!")

            request_permissions([Permission.ACCESS_COARSE_LOCATION,
                                 Permission.ACCESS_FINE_LOCATION], callback)

        #Run GPS
        if platform == 'android' or platform == 'ios':
            from plyer import gps
            gps.configure(on_location=self.update_gps_position,
                          on_status=self.on_auth_status)
            gps.start(minTime=1000, minDistance=1)

    def update_gps_position(self, *args, **kwargs):
        my_lat = kwargs['lat']
        my_lon= kwargs['lon']
        print("GPS Position: ", my_lat, my_lon)
        gps_blinker = App.get_running_app().root.ids.mapview.ids.blinker
        map = App.get_running_app().root.ids.mapview
        gps_blinker.lat = my_lat
        gps_blinker.lon = my_lon
        if map.lat != my_lat and map.lon != my_lon:
            map.center_on(my_lat, my_lon)

    def on_auth_status(self, general_status, status_message):
        if general_status == 'provider-enabled':
            pass
        else:
            self.open_gps_access_popup()

    def open_gps_access_popup(self):
        dialog = MDDialog(title="GPS Error", text="You need to enable GPS access to the app function properly!")
        dialog.size_hint = [0.8, 0.8]
        dialog.pos_hint = {'center_x': 0.5, 'center_y': 0.5}
        dialog.open()
