#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 24 10:24:58 2021

@author: kierapond
"""


import pandas as pd 
import matplotlib.pyplot as plt

############################# Read files #############################

df = pd.read_csv('allcells_abspeak.csv')


############################# Keep Ts Column #############################


keep_col = ['Cell10',#'Cell11','Cell12',
            'Cell13'#,'Cell14','Cell15',
            #'Cell16','Cell17'
            ]
new_df = df[keep_col]





############################# Put Data Together #############################


data_out = pd.concat([new_df],axis=1)

data_out.plot(style='.-',xlabel='Measurement Number', ylabel='Absorption Peak',
              legend=False)


plt.axvline(3.5,color='r')

plt.axvline(7.5,color='r')



plt.show()