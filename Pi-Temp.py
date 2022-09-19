# -*- coding: utf-8 -*-
"""
Pi-Temp

@author: alex-merge
@version: 1.0
"""

## Importing needed librairies
import numpy as np
from gpiozero import CPUTemperature
import time
import argparse

## Argument Parser
arg_parser = argparse.ArgumentParser(description='Log the temperatures.')
arg_parser.add_argument(
    "--output",
    "-o",
    dest = "savepath",
    default = r"cpu_temp.csv",
    required = False,
    help = "The savepath of the file containing the results.")
arg_parser.add_argument(
    "--interval",
    "-i",
    dest = "interval",
    default = 5,
    type = int,
    required = False,
    help = "Data pull interval in seconds.")
arg_parser.add_argument(
    "--log_time",
    "-lt",
    dest = "time",
    default = 14400,
    type = int,
    required = False,
    help = "Logging time in seconds.")

## General settings
record_time = arg_parser.time
data_interval = arg_parser.interval
max_pt_id = 1800/data_interval
savepath = arg_parser.savepath

## Getting the temperature object
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
