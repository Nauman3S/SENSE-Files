import plotly.plotly as py # plotly library
import random
from plotly.graph_objs import Scatter, Layout, Figure # plotly graph objects
import time # timer functions
import datetime

username = 'NaumanShakir'
api_key = '118u5ryvjm'
stream_token = 'g95c6135ot'

py.sign_in(username, api_key)


trace1 = Scatter(
    x=[],
    y=[],
    stream=dict(
       
        token=stream_token,
        maxpoints=200
    )
    
    
)

layout = Layout(
    title='Raspberry Pi Streaming Sensor Data'
)

fig = Figure(data=[trace1], layout=layout)

print py.plot(fig, filename='Raspberry Pi Streaming Example Values')

sensor_pin = 0
#readadc.initialize()
stream = py.Stream(stream_token)
stream.open()

while True:
    sensor_data =random.uniform(10,100)# readadc.readadc(sensor_pin, readadc.PINS.SPICLK, readadc.PINS.SPIMOSI, readadc.PINS.SPIMISO, readadc.PINS.SPICS)
    stream.write({'x': datetime.datetime.now(), 'y': sensor_data})
    time.sleep(0.1) # delay between stream posts
