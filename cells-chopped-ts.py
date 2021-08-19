#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 17 13:44:41 2021

@author: kierapond
"""


import pandas as pd 
import matplotlib.pyplot as plt

#All cells that have been baked where left of the red line
#is before baking, red line = baking, right of red line = after bake

############################# Read files #############################

df = pd.read_csv('allcells.csv')
#print(df)


keep_col = ['Cell10bake1','Cell10bake2','Cell10bake3','Cell12bake1',
           'Cell13bake1','Cell13bake2','Cell14bake1',
            'Cell16bake1']
df_bake = df[keep_col]




data_out = pd.concat([df_bake],axis=1)



data_out.plot.line(style='.',color={"Cell10bake1": "pink", "Cell10bake2": "blue",
                                    "Cell10bake3": "pink", 
                                    "Cell12bake1": "blue", 
                                    "Cell13bake1": "blue",
                                    "Cell13bake2": "blue",  
                                    "Cell14bake1": "pink",
                                    "Cell16bake1": "pink"}, legend=False,
                   xlabel='Time', ylabel='Lifetime (ms)')

#blue = short bake (1 - 8 hrs in oven or water bath)
#pink = long bake (23 + hrs in oven)

plt.axvline(3.5,color='r')

plt.tick_params(
    axis='x',          # changes apply to the x-axis
    which='both',      # both major and minor ticks are affected
    bottom=False,      # ticks along the bottom edge are off
    top=False,         # ticks along the top edge are off
    labelbottom=False)  # labels along the bottom edge are off

#All cells that have not been baked where left of the red line
#is before baking, red line = baking, right of red line = after bake

keep_col2 = ['Cell11','Cell15','Cell17']
df_nobake = df[keep_col2]


data_out = pd.concat([df_nobake],axis=1)

data_out.plot(style='.',xlabel='Time', ylabel='Lifetime (ms)')

plt.tick_params(
    axis='x',          # changes apply to the x-axis
    which='both',      # both major and minor ticks are affected
    bottom=False,      # ticks along the bottom edge are off
    top=False,         # ticks along the top edge are off
    labelbottom=False)  # labels along the bottom edge are off




plt.show()

#If you want to see one individual cell and bake where left of the red line
#is before baking, red line = baking, right of red line = after bake


keep_col3 = ['Cell10bake1']
df_onecell = df[keep_col3]

data_out = pd.concat([df_onecell],axis=1)

data_out.plot(style='.',xlabel='Time', ylabel='Lifetime (ms)')

plt.axvline(3.5,color='r')

plt.show()







