from lib.thingspeak import Channel
from include.secrets import THINGSPEAK_WRITE_KEYS


channel_wipy_pyboard = 'Jayananda'
channel_wipy_pysense = 'Mukunda'
channel_esp32 = 'Sudhama'
channel_esp32D = 'Sridama'
active_channel = channel_wipy_pyboard

field_moisture = 'Moisture'
field_temperature = 'Temperature'
field_humidity = 'Humidity'


channels = [
    Channel(channel_esp32, THINGSPEAK_WRITE_KEYS[channel_esp32],
            [
            field_moisture,
            field_temperature,
            field_humidity
            ]
            ),

    Channel(channel_esp32D, THINGSPEAK_WRITE_KEYS[channel_esp32D],
            [
            field_moisture,
            field_temperature,
            field_humidity
            ]
            ),

    Channel(channel_wipy_pyboard, THINGSPEAK_WRITE_KEYS[channel_wipy_pyboard],
            [
            field_moisture,
            field_temperature,
            field_humidity
            ]
            ),

    Channel(channel_wipy_pysense, THINGSPEAK_WRITE_KEYS[channel_wipy_pysense],
            [
            field_moisture,
            field_temperature,
            field_humidity
            ]
            )

]
