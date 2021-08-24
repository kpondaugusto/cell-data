#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 17 11:57:33 2021

@author: kierapond
"""


import pandas as pd 
import matplotlib.pyplot as plt

############################# Read files #############################

df = pd.read_csv('cell-12.csv',sep='\t', lineterminator='\r')

keep_col = ['Date','Ts']
new_df = df[keep_col]
print(df)

data_out= pd.concat([new_df],axis=1)


x='Date'

data_out.plot(x,style='.')

plt.axvline(1,color='r')
plt.axvline(3,color='r')


plt.show()