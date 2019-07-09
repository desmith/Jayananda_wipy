from machine import ADC, Pin
from lib.dht22 import device

led = Pin('G16', mode=Pin.OUT, value=1)

dht = device(Pin.exp_board.G22)

adc = ADC()
# vegeTronixPin = adc.channel(id=1, pin='GP3', attn=ADC.ATTN_11DB)
vegeTronixPin = adc.channel(id=1)

# 11DB attenuation allows for a maximum input voltage
#  of approximately 3.6v (default is 0-1.0v)

valve = Pin('P8', mode=Pin.OUT, value=0)
