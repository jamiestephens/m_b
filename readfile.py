# -*- coding: utf-8 -*-
"""
Created on Tue May 25 00:40:40 2021

@author: Administrator
"""
import pandas as pd
import csv
import numpy

def readfile():
    df = pd.read_csv('accepted.csv')
    print(df.head())
    print(len(df))

    df = df[df['issue_d'].notna()]

    df = df[(df['issue_d'].str.contains("2015"))]
    
    df = df.sample(n=20000,replace=False)
    
    df.to_csv('acepted-randomsample-2015.csv')
    
if __name__ == "__main__":
    readfile()

