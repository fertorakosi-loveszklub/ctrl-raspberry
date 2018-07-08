import Config
import Container
import Keypad
import LCD
import IPClient
import RadioClient
import RPi.GPIO as GPIO
import StateMachine
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

container = Container.Container()

config = Config.Config('config.json')
client = IPClient.IPClient(config, container)
radio = RadioClient.RadioClient(config)
screen = LCD.LCD()
keypad = Keypad.Keypad(config)

container.bind('config', config)
container.bind('client', client)
container.bind('radio', radio)
container.bind('screen', screen)
container.bind('keypad', keypad)

screen.write_new("Csatlakozas az", "50m egyseghez...")

while True:
    try:
        client.connect()
        break
    except:
        time.sleep(0.1)
        pass

screen.write_new("Fertorakosi", "Loveszklub")

stateMachine = StateMachine.StateMachine(container)
stateMachine.run()
