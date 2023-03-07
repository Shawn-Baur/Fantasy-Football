# -*- coding: utf-8 -*-
"""
Created on Wed Feb  1 15:41:30 2023

@author: Freew
"""
import json

class equations:
    def writeEq(file, data):
        with open(file, 'w') as file:
            json.dump(data, file)
            
    def readEq(file):
        with open(file) as file:
            data = json.load(file)
             
        return data
    
    def year(yearMax):
        year = []
        x = range(0,100)
        
        for y in range(2, yearMax+1):
                if x[y] < 10:
                    years = '200{}'.format(x[y])
                else:
                    years = '20{}'.format(x[y])
                year.append(years)
        
        return year