#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 17 13:44:41 2021

@author: kierapond
"""


import pandas as pd 
import matplotlib.pyplot as plt

############################# Read files #############################

df = pd.read_csv('cells.csv')
print(df)


keep_col = ['Cell10bake1','Cell10bake2','Cell10bake3','Cell12bake1',
           'Cell13bake1','Cell13bake2','Cell14bake1',
            'Cell16bake1']
df_bake = df[keep_col]

keep_col2 = ['Cell11','Cell15','Cell17']
df_nobake = df[keep_col2]



data_out = pd.concat([df_bake],axis=1)


data_out.plot.line(style='.',color={"Cell10bake1": "blue", "Cell10bake2": "blue",
                                    "Cell10bake3": "pink", 
                                    "Cell12bake1": "pink", "Cell13bake1": "blue",
                                    "Cell13bake2": "blue",  
                                    "Cell14bake1": "pink",
                                    "Cell16bake1": "pink"}, legend=False)

plt.axvline(3.5,color='r')


data_out = pd.concat([df_nobake],axis=1)

data_out.plot(style='.')




plt.show()





