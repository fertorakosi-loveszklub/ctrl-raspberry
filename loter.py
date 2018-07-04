import Config
import IPClient
import RadioClient
import RPi.GPIO as GPIO
import StateMachine

GPIO.setmode(GPIO.BCM)

config = Config.Config("config.json")
client = IPClient.IPClient(config)
radio = RadioClient.RadioClient(config)

container = {
    'config': config,
    'client': client,
    'radio': radio
}

client.connect()

stateMachine = StateMachine.StateMachine(container)
stateMachine.run()
