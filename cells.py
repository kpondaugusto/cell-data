#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 17 12:57:05 2021

@author: kierapond
"""


import pandas as pd 
import matplotlib.pyplot as plt

############################# Read files #############################

df10 = pd.read_csv('cell-10.csv',sep='\t', lineterminator='\r')
df11 = pd.read_csv('cell-11.csv',sep='\t', lineterminator='\r')
df12 = pd.read_csv('cell-12.csv',sep='\t', lineterminator='\r')
df13 = pd.read_csv('cell-13.csv',sep='\t', lineterminator='\r')
df14 = pd.read_csv('cell-14.csv',sep='\t', lineterminator='\r')
df15 = pd.read_csv('cell-15.csv',sep='\t', lineterminator='\r')
df16 = pd.read_csv('cell-16.csv',sep='\t', lineterminator='\r')
df17 = pd.read_csv('cell-17.csv',sep='\t', lineterminator='\r')


############################# Keep Ts Column #############################


keep_col10 = ['Ts']
new_df10 = df10[keep_col10]

keep_col11 = ['Ts']
new_df11 = df11[keep_col11]

keep_col12 = ['Ts']
new_df12 = df12[keep_col12]

keep_col13 = ['Ts']
new_df13 = df10[keep_col13]

keep_col14 = ['Ts']
new_df14 = df14[keep_col14]

keep_col15 = ['Ts']
new_df15 = df15[keep_col15]

keep_col16 = ['Ts']
new_df16 = df16[keep_col16]

keep_col17 = ['Ts']
new_df17 = df17[keep_col17]


############################# Rename Columns #############################

new_df10.columns = ['Cell 10']

new_df11.columns = ['Cell 11']

new_df12.columns = ['Cell 12']

new_df13.columns = ['Cell 13']

new_df14.columns = ['Cell 14']

new_df15.columns = ['Cell 15']

new_df16.columns = ['Cell 16']

new_df17.columns = ['Cell 17']


############################# Put Data Together #############################


data_out = pd.concat([new_df10,new_df11,new_df12,new_df13,new_df14,new_df15,new_df16,new_df17],axis=1)
#print(data_out)

data_out.to_csv(r'/Users/kierapond/Documents/GitHub/cell-data/cells.csv', index=False)

# x='Date'

data_out.plot(style='.')


plt.show()