import logging
import socket
from pwnagotchi.ui.components import LabeledValue
from pwnagotchi.ui.view import BLACK
import pwnagotchi.ui.fonts as fonts
import pwnagotchi.plugins as plugins

class InternetConnectionPlugin(plugins.Plugin):
    __author__ = 'https://github.com/albinmedoc'
    __version__ = '1.0.0'
    __license__ = 'GPL3'
    __description__ = 'A plugin that displays the Internet connection status on the pwnagotchi display.'

    position = (0, 40)

    def _is_internet_available(self):
        try:
            socket.create_connection(('www.google.com', 80), timeout=1)
            return True
        except socket.timeout:
            logging.error("Connection timed out")
            return False
        except socket.error as e:
            logging.error(f"Socket error: {e}")
            return False
    
    def on_loaded(self):
        logging.info("Pwnagotchi Internet-Connection v.1.0.0 loaded.")

    def on_ui_setup(self, ui):
        ui.add_element('connection_status', LabeledValue(color=BLACK, label='', value='',
                                            position=self.position,
                                            label_font=fonts.Small, text_font=fonts.Bold))

    def on_ui_update(self, ui):
        is_connected = self._is_internet_available()
        if is_connected:
            ui.set('connection_status', 'WWW')
        else:
            ui.set('connection_status', '')

    def on_unload(self, ui):
        with ui._lock:
            ui.remove_element('connection_status')
