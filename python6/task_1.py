from time import sleep
from itertools import cycle

class TrafficLight():
    __trafficLight_color = ["red", "yellow", "green"]
    def running(self):
        for el in cycle(TrafficLight.__trafficLight_color):
           print(TrafficLight.__trafficLight_color[0])
           sleep(7)
           print(TrafficLight.__trafficLight_color[1])
           sleep(2)
           print(TrafficLight.__trafficLight_color[2])
           sleep(4)
t = TrafficLight()
print(t.running())