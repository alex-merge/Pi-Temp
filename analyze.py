# -*- coding: utf-8 -*-
"""
Pi-Temp - Analyzing module

@author: alex-merge
@version: 1.0
"""

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import argparse
import pandas as pd

## Argument Parser
arg_parser = argparse.ArgumentParser(description='Analyze logs.')
arg_parser.add_argument(
    "--output",
    "-o",
    dest = "savepath",
    default = r"Temp_graphs.png",
    required = False,
    type = str,
    help = "Savepath of the graph. (Default is \Temp_graphs.png)")
arg_parser.add_argument(
    "--input",
    "-i",
    dest = "input",
    default = None,
    type = str,
    required = True,
    help = "Input file (.csv file).")
args = arg_parser.parse_args()

data = pd.read_csv(args.input)
data.columns = ["Date", "Temp", "Std"]
data["Date"] = pd.to_datetime(data["Date"])
data[["Temp", "Std"]] = data[["Temp", "Std"]].astype(float)

## Drawing the graph
sns.set_theme(style="darkgrid")
graph = sns.lineplot(y="Temp", x="Date",
                     #errorbar = "Std",
                     data=data)

fig = graph.get_figure()
fig.savefig(args.savepath, dpi = 400)

print(data["Date"], type(data["Date"]))
print(data["Temp"], type(data["Temp"]))
print(data)


