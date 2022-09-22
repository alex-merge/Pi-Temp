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
    help = "The savepath of the file containing the results. (Default is False)")
arg_parser.add_argument(
    "--interval",
    "-i",
    dest = "interval",
    default = 5,
    type = int,
    required = False,
    help = "Data pull interval in seconds. (Default is 5)")
arg_parser.add_argument(
    "--log_time",
    "-lt",
    dest = "time",
    default = 72,
    type = int,
    required = False,
    help = "Logging time in hours. (Default is 72)")
arg_parser.add_argument(
    "--verbose",
    "-v",
    dest = "verbose",
    default = True,
    required = False,
    help = "Verbose option. (Default is True)")
arg_parser.add_argument(
    "--mode",
    "-m",
    dest = "mode",
    default = "averaged",
    type = str,
    required = False,
    help = "Method of logging : 'averaged' for logging averaged temps every 30 minutes"
    + "'normal' for logging temps at the data pulling rate.")
args = arg_parser.parse_args()

## General settings
record_time = args.time
data_interval = args.interval
max_pt_id = int(1800/data_interval)
savepath = args.savepath

## Getting the temperature object
cpu_temp = CPUTemperature()

pt_id = 0
condition = True
start_time = time.time()

while condition:
    with open(savepath, "a") as log:
        
        if args.mode == "averaged":
            temp_list = []
            
            for k in range(max_pt_id):
                temp_list.append(cpu_temp.temperature)
                time.sleep(data_interval)
            
            temp, std = np.mean(temp_list), np.std(temp_list)
            
        if args.mode == "normal":
            time.sleep(data_interval)
            temp, std = cpu_temp.temperature, 0
        
        ## Writting the data line
        timestamp = "{0},{1},{2}\n".format(time.strftime("%Y-%m-%d %H:%M:%S"), 
                                           temp, std)
        log.write(timestamp)
        
        if args.verbose:
            print("Data logged as "+timestamp)
        
        if time.time()-start_time >= record_time :
            condition = False
print("Logging done")