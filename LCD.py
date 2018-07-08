from Lib import I2C_LCD_driver
import time

class LCD:
    def __init__(self):
        self.screen = I2C_LCD_driver.lcd()

    def write_default(self):
        self.write_new('Fertorakosi', 'Loveszklub')

    def message_and_reset(self, message, message2=None, timeout=1.5):
        self.write_new(message, message2)
        time.sleep(timeout)
        self.write_default()

    def write_new(self, first_row, second_row=''):
        self.clear()
        self.write(first_row, 1)
        self.write(second_row, 2)

    def write(self, text, row=1):
        if text:
            self.screen.lcd_display_string(text, row)

    def clear(self):
        self.screen.lcd_clear()