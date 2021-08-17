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

keep_col = ['Cell10']
new_df = df[keep_col]


data_out = pd.concat([df],axis=1)


data_out.plot()


plt.show()