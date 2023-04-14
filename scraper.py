# -*- coding: utf-8 -*-
"""
Created on Thu Mar  9 13:16:37 2023

@author: Freew
"""
from equation_sheet import equations as eq
from format_master import formatMaster as fm
from scraper_functions import*
from pathlib import Path

def historicRawData():
    yearMax = 22
    position = ['qb', 'rb', 'wr', 'te', 'k', 'dst']
    
    year = []
    x = range(0,100)
    for y in range(0, yearMax+1):
            if x[y] < 10:
                years = '200{}'.format(x[y])
            else:
                years = '20{}'.format(x[y])
            year.append(years)
    
    masterDictionary = {}
    for pos in range(0, 6):
        dictionary = {}
        for y in range(2,len(year)):
            file = 'C:\\Users\\Freew\\OneDrive\\Desktop\\Python Projects\\Fantasy Football\\data\\annual_raw\\{} {} stats.json'.format(year[y], position[pos])
            path = Path(file)
            
            if path.is_file() == True:
                data = eq.readEq(file)
                
            else:
                data = historicalDataScraper(tablePositionAnnual(position[pos], year[y]), position[pos], year[y])
                
            playerDictionary = formatDataAnnual(data, position[pos], year[y])
            txtyear = 'Player Year: {}'.format(year[y])
            dictionary[txtyear] = playerDictionary
            
            print('{} {} file complete'.format(year[y], position[pos]))
        
        txtpos = 'Player Position: {}'.format(position[pos])
        masterDictionary[txtpos] = dictionary
        
        file = 'C:\\Users\\Freew\\OneDrive\\Desktop\\Python Projects\\Fantasy Football\\data\\annual_raw\\Annual Master Database.json'
        eq.writeEq(file, masterDictionary)
        
    fm.formatMasterAnnual()
    fm.positionPlayerListAnnual()
        
def weeklyRawData():
    yearMax = 22
    position = ['qb', 'rb', 'wr', 'te', 'k', 'dst']
    
    year = []
    x = range(0,100)
    for y in range(0, yearMax+1):
            if x[y] < 10:
                years = '200{}'.format(x[y])
            else:
                years = '20{}'.format(x[y])
            year.append(years)
    
    masterDictionary = {}
    for pos in range(0, 6):
        dictionary = {}
        for y in range(2,len(year)):
            if year[y] < '2021':
                w = 17
            else:
                w = 18
            
            weekDictionary = {}
            for week in range(1, w):
                file = 'C:\\Users\\Freew\\OneDrive\\Desktop\\Python Projects\\Fantasy Football\\data\\weekly_raw\\{} {} {} stats.json'.format(year[y], week, position[pos])
                path = Path(file)
                
                if path.is_file() == True:
                    data = eq.readEq(file)
                    
                else:
                    data = weeklyDataScraper(tablePositionWeekly(position[pos], year[y], week), position[pos], year[y], week)
                    
                playerDictionary = formatDataWeekly(data, position[pos], year[y], week)
                txtweek = 'Player Week: {}'.format(week)
                weekDictionary[txtweek] = playerDictionary
                
                print('{} {} {} file complete'.format(year[y], week, position[pos]))
            
            txtyear = 'Player Year: {}'.format(year[y])
            dictionary[txtyear] = weekDictionary
        
        txtpos = 'Player Position: {}'.format(position[pos])
        masterDictionary[txtpos] = dictionary
        
        file = 'C:\\Users\\Freew\\OneDrive\\Desktop\\Python Projects\\Fantasy Football\\data\\annual_raw\\Weekly Master Database.json'
        eq.writeEq(file, masterDictionary)
        
    fm.formatMasterWeekly()
    fm.positionPlayerListWeekly()

historicRawData()
weeklyRawData()