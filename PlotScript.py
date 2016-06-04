import plotly.plotly as py # plotly library
from plotly import tools
import random
from plotly.graph_objs import Scatter, Layout, Figure,Data # plotly graph objects
import time # timer functions
import datetime
import serial

username = 'NaumanShakir'
api_key = '118u5ryvjm'
stream_token0 = 'g95c6135ot'
stream_token1 = '7x3rmft35c'
stream_token2 = '58zfwzke7m'
stream_token3 = 'f2kg1n8dpf'

py.sign_in(username, api_key)


trace1 = Scatter(
    x=[],
    y=[],
    name='Real Power',
    stream=dict(
       
        token=stream_token0,
        maxpoints=200
    ),
    yaxis='y'
    
    
)
trace2 = Scatter(
    x=[],
    y=[],
    name='Apparent Power',
    stream=dict(
       
        token=stream_token1,
        maxpoints=200
    ),
    yaxis='y2'
    
    
)
trace3 = Scatter(
    x=[],
    y=[],
    name='Voltage',
    stream=dict(
       
        token=stream_token2,
        maxpoints=200
    ),
    yaxis='y3'
    
    
)
trace4 = Scatter(
    x=[],
    y=[],
    name='Current',
    stream=dict(
       
        token=stream_token3,
        maxpoints=200
    ),
    yaxis='y4'
    
    
)

layout = Layout(
    title='Real,Apparent Powers and Current, Voltage'
    
)
fig = tools.make_subplots(rows=2, cols=2, subplot_titles=('Real Power', 'Apparent Power','Voltage', 'Current'))
fig.append_trace(trace1, 1, 1)
fig.append_trace(trace2, 1, 2)
fig.append_trace(trace3, 2, 1)
fig.append_trace(trace4, 2, 2)

fig['layout'].update(height=600, width=600, title='Power, Voltage' +'and Current Plots')
###data=Data([trace1,trace2,trace3,trace4])
###fig = Figure(data=data, layout=layout)

print py.plot(fig, filename='make-subplots-multiple-with-title')

stream0=py.Stream(stream_token0)
stream0.open()

stream1=py.Stream(stream_token1)
stream1.open()

stream2=py.Stream(stream_token2)
stream2.open()

stream3=py.Stream(stream_token3)
stream3.open()
def get_num(x):
    return float(''.join(ele for ele in x if ele.isdigit() or ele == '.'))

#readadc.initialize()
ser = serial.Serial('/dev/ttyACM0',9600)
volts=0
while True:
    
    try:
        
        incoming=ser.readline()
        
        ArduinoData=incoming.split(',')

        volts=(get_num(ArduinoData[3])+209)
        
        print(get_num(ArduinoData[0]))
        print(get_num(ArduinoData[1]))
        print(volts)
        print(get_num(ArduinoData[4]))
        stream0.write({'x': datetime.datetime.now(), 'y': get_num(ArduinoData[0])})#real
        stream1.write({'x': datetime.datetime.now(), 'y': get_num(ArduinoData[1])})#apparent
        stream2.write({'x': datetime.datetime.now(), 'y': volts})#voltage
        stream3.write({'x': datetime.datetime.now(), 'y': get_num(ArduinoData[3])})#current
        time.sleep(0.1) 
   
    except:
            
        print('exception')
stream0.close()
stream1.close()
stream2.close()
stream3.close()