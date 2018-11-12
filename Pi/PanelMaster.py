import smbus
import time

import urllib.request

from ServerConnector import Connector
from Panel import Panel

bus = smbus.SMBus(1)
ADDR = 0x04


WHITE_PIXEL = [0x1, 0x1, 0x1]
BLACK_PIXEL = [0x0, 0x0, 0x0]


panel = Panel(bus, ADDR)

panels = [[panel]]
    
#panel.fill_rect([0,0], [32,32], WHITE_PIXEL)

connector = Connector("http://pathealy.pythonanywhere.com/get_grid")


while True:
    data = connector.get_dump()

    for x in range(len(panels)):
        for y in range(len(panels[x])):
            if(panel is not None):
                grid = data[x][y]
                for i in range(len(grid)):
                    for j in range(len(grid[i])):
                        panels[x][y].draw_pixel([j, i], grid[j][i])
                        time.sleep(0.0001)

    time.sleep(0)
