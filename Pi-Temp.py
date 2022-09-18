# -*- coding: utf-8 -*-
"""
Pi-Temp

@author: alex-merge
@version: 1.0
"""

# Importing needed librairies
import numpy as np
from gpiozero import CPUTemperature
import time

# General settings
record_time = 14400
data_interval = 5
max_pt_id = 1800/data_interval
savepath = r"cpu_temp.csv"

# Getting the temperature object
cpu_temp = CPUTemperature()

pt_id = 0
condition = True
start_time = time.time()

with open(savepath, "a") as log:
    while condition:
        temp_list = []
        
        for k in range(max_pt_id):
            temp_list.append(cpu_temp.temperature)
            time.sleep(data_interval)
        
        temp, std = np.mean(temp_list), np.std(temp_list)
        log.write("{0},{1},{2}\n".format(time.strftime("%Y-%m-%d %H:%M:%S"),
                                     str(temp), str(std)))

        if time.time()-start_time >= record_time :
            condition = False