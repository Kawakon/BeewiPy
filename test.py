from BeewiPy import BeewiPy
import time

MAC_ADDRESS = "7C:EC:79:67:81:A2"       # Here you should put the MAC address of your device
myBulb = BeewiSmartBulb(MAC_ADDRESS)    # This will create a new BeewiSmartBulb object and connect to the device
myBulb.turnOn()                         # This will turn on your bulb
time.sleep(5)                           # This will wait 5 seconds
myBulb.turnOff()