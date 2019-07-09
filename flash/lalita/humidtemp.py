"""The DHT driver is implemented in software and works on all pins:"""
from lalita.pins import dht


def main():
    print("humidtemp.py->main()")

    temp_c = 0
    temp_f = 0
    humidity = 0.0

    if dht.trigger() == True:
        temp_c = dht22.temperature  # eg. 23.6 (°C)
        humidity = dht22.humidity     # eg. 41.3 (% RH)
        temp_f = temp_c * (9 / 5) + 32.0

    print('Temperature: %3.1f C' % temp_c)
    print('Temperature: %3.1f F' % temp_f)
    print('Humidity: %3.1f %%' % humidity)

    '''
    for _ in range(5):
        if dht.trigger() == True:
            print("RH = {}%  T = {}C".format(dht.humidity, dht.temperature))
        else:
            print(dht.status)
    '''

    return (temp_f, humidity)


print('humidtemp imported')
