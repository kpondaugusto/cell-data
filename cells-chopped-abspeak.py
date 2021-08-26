#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 19 14:06:03 2021

@author: kierapond
"""


import pandas as pd 
import matplotlib.pyplot as plt

#All cells that have been baked where left of the red line
#is before baking, red line = baking, right of red line = after bake

############################# Read files #############################

df = pd.read_csv('allcells_abspeak.csv')
#sprint(df)


keep_col = ['Cell10bake1','Cell10bake2','Cell10bake3','Cell12bake1',
           'Cell13bake1','Cell13bake2','Cell14bake1','Cell15bake1',
            'Cell16bake1','Cell17bake1']
df_bake = df[keep_col]




data_out = pd.concat([df_bake],axis=1)



data_out.plot.line(style='.',color={"Cell10bake1": "pink", "Cell10bake2": "blue",
                                    "Cell10bake3": "pink", 
                                    "Cell12bake1": "blue", 
                                    "Cell13bake1": "blue",
                                    "Cell13bake2": "blue",  
                                    "Cell14bake1": "pink","Cell15bake1": "green",
                                    "Cell16bake1": "pink","Cell17bake1": "green"}, legend=False,
                   xlabel='Measurement Number', ylabel='Absorption Peak')

#blue = short bake (1 - 8 hrs in oven or water bath)
#pink = long bake (23 + hrs in oven)

plt.axvline(3.5,color='r')


#All cells that have not been baked where left of the red line
#is before baking, red line = baking, right of red line = after bake

keep_col2 = ['Cell11']
df_nobake = df[keep_col2]


data_out = pd.concat([df_nobake],axis=1)

data_out.plot(style='.',xlabel='Measurement Number', ylabel='Absorption Peak')




plt.show()

#If you want to see one individual cell and bake where left of the red line
#is before baking, red line = baking, right of red line = after bake


keep_col3 = ['Cell10bake1']
df_onecell = df[keep_col3]

data_out = pd.concat([df_onecell],axis=1)

data_out.plot(style='.',xlabel='Measurement Number', ylabel='Absorption Peak')

plt.axvline(3.5,color='r')

plt.show()







