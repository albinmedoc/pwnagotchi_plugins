from pwnagotchi.ui.components import LabeledValue
from pwnagotchi.ui.view import BLACK
import pwnagotchi.ui.fonts as fonts
import pwnagotchi.plugins as plugins
import pwnagotchi
import logging
import datetime

class PwnClock(plugins.Plugin):
    __author__ = 'https://github.com/albinmedoc'
    __version__ = '1.0.0'
    __license__ = 'GPL3'
    __description__ = 'Clock/Calendar for pwnagotchi with configurable screen positions'

    date_format = '%m/%d/%y'
    date_pos = (100, 0)
    time_format = '%I:%M%p'
    time_pos = (100, 95)

    def on_loaded(self):
        logging.info("Pwnagotchi Clock Plugin v.2 loaded.")

    def on_ui_setup(self, ui):
        if 'date_format' in self.options:
            self.date_format = self.options['date_format']
        if 'date_pos' in self.options:
            date_pos = self.options['date_pos'].split(',')
            self.date_pos = tuple(int(x.strip()) for x in date_pos)

        if 'time_format' in self.options:
            self.time_format = self.options['time_format']
        if 'clock_pos' in self.options:
            clock_pos = self.options['clock_pos'].split(',')
            self.time_pos = tuple(int(x.strip()) for x in clock_pos)

        ui.add_element('date', LabeledValue(color=BLACK, label='', value=self.date_format,
                                                position=self.date_pos,
                                                label_font=fonts.Small, text_font=fonts.Small))

        ui.add_element('clock', LabeledValue(color=BLACK, label='', value=self.time_format,
                                                position=self.time_pos,
                                                label_font=fonts.Small, text_font=fonts.Small))
        
    def on_ui_update(self, ui):
        now = datetime.datetime.now()

        datenow = now.strftime(self.date_format)
        ui.set('date', datenow)

        timenow = now.strftime(self.time_format)
        ui.set('clock', timenow)

    def on_unload(self, ui):
        with ui._lock:
            ui.remove_element('date')
            ui.remove_element('clock')
