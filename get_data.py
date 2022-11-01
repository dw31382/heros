#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import psutil

# create csv file with labels cpu, freq, fan, load, temp
with open("log.csv", "w") as f:
    f.write("cpu,freq,fan,load,temp\n")

while True:
    cpu = psutil.cpu_percent(interval=1)
    freq = round(psutil.cpu_freq().current, 2)
    fan = psutil.sensors_fans()['thinkpad'][0].current
    load = len(psutil.pids())
    temp = psutil.sensors_temperatures()['coretemp'][0].current
    # append to csv file
    with open("log.csv", "a") as f:
        f.write(f"{cpu},{freq},{fan},{load},{temp}\n")
    f.close