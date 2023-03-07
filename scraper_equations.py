# -*- coding: utf-8 -*-
"""
Created on Mon Mar  6 19:42:38 2023

@author: Freew
"""
from bs4 import BeautifulSoup as bs
from equation_sheet import equations as eq
import requests
from pathlib import Path

class scraperEquations:
    def historicalDataScraper(URL, position, year):
        data = requests.get(URL).text
        soup = bs(data, 'html.parser')
        
        data = []
        table = soup.find('table')
        table_body = table.find('tbody')

        rows = table_body.find_all('tr')
        for row in rows:
            cols = row.find_all('td')
            cols = [ele.text.strip() for ele in cols]
            data.append([ele for ele in cols if ele])
        
        file = 'C:\\Users\\Freew\\OneDrive\\Desktop\\Python Projects\\Fantasy Football\\annual_raw\\{} {} stats.json'.format(year, position)
        eq.writeEq(file, data)
        return data

    def tablePosition(position, year):
        URL = 'https://www.fantasypros.com/nfl/stats/{}.php?year={}'.format(position, year)
        return URL
    
    def formatDataWeekly(table, position, year, week):
        unfilNames = []
        for i in range(0, len(table)):
            unfilNames.append(table[i][1])
        
        names =[]
        for i in range(0, len(unfilNames)):
            names.append(unfilNames[i].split(' '))
        
        teams = []
        for i in range(0, len(names)):
            teams.append(names[i].pop())
        
        if position == 'qb':
            dictionary = {}
            for i in range(0, len(table)):
                rank = table[i][0]
                name = names[i]
                team = teams[i]
                cmpPass = table[i][2]
                attPass = table[i][3]
                ydsPass = table[i][5]
                tdPass = table[i][7]
                pic = table[i][8]
                sacks = table[i][9]
                attRush = table[i][10]
                ydsRush = table[i][11]
                tdRush = table[i][12]
                fl = table[i][13]
                
                formatName = '{} {}'.format(name[0], name[1])
                
                txtrank = 'Player Rank: {}'.format(rank)
                dictionary[txtrank] = {
                            'year': year,
                            'week': week,
                            'name': formatName,
                            'position': position, 
                            'rank': rank,
                            'team': team,
                            'cmpPass': cmpPass,
                            'attPass': attPass,
                            'ydsPass': ydsPass, 
                            'tdPass': tdPass,
                            'pic': pic,
                            'sacks': sacks,
                            'attRush': attRush, 
                            'ydsRush': ydsRush, 
                            'tdRush': tdRush,
                            'fl': fl
                            }
    
        if position == 'rb':
            dictionary = {}
            for i in range(0, len(table)):
                rank = table[i][0]
                name = names[i]
                team = teams[i]
                attRush = table[i][2]
                ydsRush = table[i][3]
                long = table[i][5]
                twtyPls = table[i][6]
                tdRush = table[i][7]
                rec = table[i][8]
                tgt = table[i][9]
                ydsPass = table[i][10]
                tdPass = table[i][12]
                fl = table[i][13]
                
                formatName = '{} {}'.format(name[0], name[1])
                
                txtrank = 'Player Rank: {}'.format(rank)
                dictionary[txtrank] = {
                            'year': year,
                            'week': week,
                            'name': formatName,
                            'position': position, 
                            'rank': rank,
                            'team': team,
                            'attRush': attRush, 
                            'ydsRush': ydsRush,
                            'long': long,
                            'twtyPls': twtyPls,
                            'tdRush': tdRush,
                            'rec': rec,
                            'tgt': tgt,
                            'ydsPass': ydsPass, 
                            'tdPass': tdPass,
                            'fl': fl
                            }
    
        if position == 'wr' or position == 'te':
            dictionary = {}
            for i in range(0, len(table)):
                rank = table[i][0]
                name = names[i]
                team = teams[i]
                rec = table[i][2]
                tgt = table[i][3]
                ydsPass = table[i][4]
                long = table[i][6]
                twtyPls = table[i][7]
                tdPass = table[i][8]
                attRush = table[i][9]
                ydsRush = table[i][10]
                tdRush = table[i][11]
                fl = table[i][12]
                
                formatName = '{} {}'.format(name[0], name[1])
                
                txtrank = 'Player Rank: {}'.format(rank)
                dictionary[txtrank] = {
                            'year': year,
                            'week': week,
                            'name': formatName,
                            'position': position, 
                            'rank': rank,
                            'team': team,
                            'rec': rec,
                            'tgt': tgt,
                            'ydsPass': ydsPass,
                            'long': long,
                            'twtyPls': twtyPls,
                            'tdPass': tdPass,
                            'attRush': attRush, 
                            'ydsRush': ydsRush,
                            'tdRush': tdRush,
                            'fl': fl
                            }
        
        if position == 'k':
            dictionary = {}
            for i in range(0, len(table)):
                rank = table[i][0]
                name = names[i]
                team = teams[i]
                fg = table[i][2]
                fga = table[i][3]
                long = table[i][5]
                u20 = table[i][6]
                u30 = table[i][7]
                u40 = table[i][8]
                u50 = table[i][9]
                p50 = table[i][10]
                xpt = table[i][11]
                xpa = table[i][12]

                formatName = '{} {}'.format(name[0], name[1])
                
                txtrank = 'Player Rank: {}'.format(rank)
                dictionary[txtrank] = {
                            'year': year,
                            'week': week,
                            'name': formatName,
                            'position': position, 
                            'rank': rank,
                            'team': team,
                            'fg': fg,
                            'fga': fga,
                            'long': long,
                            'u20': u20,
                            'u30': u30,
                            'u40': u40,
                            'u50': u50,
                            'p50': p50,
                            'xpt': xpt,
                            'xpa': xpa
                            }
    
        if position == 'dst':
            dictionary = {}
            for i in range(0, len(table)):
                rank = table[i][0]
                name = names[i]
                team = teams[i]
                sacks = table[i][2]
                pic = table[i][3]
                fr = table[i][4]
                ff = table[i][5]
                defTD = table[i][6]
                sfty = table[i][7]
                spcTD = table[i][8]
                
                formatName = '{} {}'.format(name[0], name[1])
                
                txtrank = 'Player Rank: {}'.format(rank)
                dictionary[txtrank] = {
                            'year': year,
                            'week': week,
                            'name': formatName,
                            'position': position, 
                            'rank': rank,
                            'team': team,
                            'sacks': sacks,
                            'int': pic,
                            'fr': fr,
                            'ff': ff,
                            'defTD': defTD,
                            'sfty': sfty,
                            'spcTD': spcTD
                            }
        
        return dictionary
    
    def formatDataAnnual(table, position, year):
        unfilNames = []
        for i in range(0, len(table)):
            unfilNames.append(table[i][1])
        
        names =[]
        for i in range(0, len(unfilNames)):
            names.append(unfilNames[i].split(' '))
        
        teams = []
        for i in range(0, len(names)):
            teams.append(names[i].pop())
        
        if position == 'qb':
            dictionary = {}
            for i in range(0, len(table)):
                rank = table[i][0]
                name = names[i]
                team = teams[i]
                cmpPass = table[i][2]
                attPass = table[i][3]
                ydsPass = table[i][5]
                tdPass = table[i][7]
                pic = table[i][8]
                sacks = table[i][9]
                attRush = table[i][10]
                ydsRush = table[i][11]
                tdRush = table[i][12]
                fl = table[i][13]
                
                formatName = '{} {}'.format(name[0], name[1])
                
                txtrank = 'Player Rank: {}'.format(rank)
                dictionary[txtrank] = {
                            'year': year,
                            'name': formatName,
                            'position': position, 
                            'rank': rank,
                            'team': team,
                            'cmpPass': cmpPass,
                            'attPass': attPass,
                            'ydsPass': ydsPass, 
                            'tdPass': tdPass,
                            'pic': pic,
                            'sacks': sacks,
                            'attRush': attRush, 
                            'ydsRush': ydsRush, 
                            'tdRush': tdRush,
                            'fl': fl
                            }
    
        if position == 'rb':
            dictionary = {}
            for i in range(0, len(table)):
                rank = table[i][0]
                name = names[i]
                team = teams[i]
                attRush = table[i][2]
                ydsRush = table[i][3]
                long = table[i][5]
                twtyPls = table[i][6]
                tdRush = table[i][7]
                rec = table[i][8]
                tgt = table[i][9]
                ydsPass = table[i][10]
                tdPass = table[i][12]
                fl = table[i][13]
                
                formatName = '{} {}'.format(name[0], name[1])
                
                txtrank = 'Player Rank: {}'.format(rank)
                dictionary[txtrank] = {
                            'year': year,
                            'name': formatName,
                            'position': position, 
                            'rank': rank,
                            'team': team,
                            'attRush': attRush, 
                            'ydsRush': ydsRush,
                            'long': long,
                            'twtyPls': twtyPls,
                            'tdRush': tdRush,
                            'rec': rec,
                            'tgt': tgt,
                            'ydsPass': ydsPass, 
                            'tdPass': tdPass,
                            'fl': fl
                            }
    
        if position == 'wr' or position == 'te':
            dictionary = {}
            for i in range(0, len(table)):
                rank = table[i][0]
                name = names[i]
                team = teams[i]
                rec = table[i][2]
                tgt = table[i][3]
                ydsPass = table[i][4]
                long = table[i][6]
                twtyPls = table[i][7]
                tdPass = table[i][8]
                attRush = table[i][9]
                ydsRush = table[i][10]
                tdRush = table[i][11]
                fl = table[i][12]
                
                formatName = '{} {}'.format(name[0], name[1])
                
                txtrank = 'Player Rank: {}'.format(rank)
                dictionary[txtrank] = {
                            'year': year,
                            'name': formatName,
                            'position': position, 
                            'rank': rank,
                            'team': team,
                            'rec': rec,
                            'tgt': tgt,
                            'ydsPass': ydsPass,
                            'long': long,
                            'twtyPls': twtyPls,
                            'tdPass': tdPass,
                            'attRush': attRush, 
                            'ydsRush': ydsRush,
                            'tdRush': tdRush,
                            'fl': fl
                            }
        
        if position == 'k':
            dictionary = {}
            for i in range(0, len(table)):
                rank = table[i][0]
                name = names[i]
                team = teams[i]
                fg = table[i][2]
                fga = table[i][3]
                long = table[i][5]
                u20 = table[i][6]
                u30 = table[i][7]
                u40 = table[i][8]
                u50 = table[i][9]
                p50 = table[i][10]
                xpt = table[i][11]
                xpa = table[i][12]

                formatName = '{} {}'.format(name[0], name[1])
                
                txtrank = 'Player Rank: {}'.format(rank)
                dictionary[txtrank] = {
                            'year': year,
                            'name': formatName,
                            'position': position, 
                            'rank': rank,
                            'team': team,
                            'fg': fg,
                            'fga': fga,
                            'long': long,
                            'u20': u20,
                            'u30': u30,
                            'u40': u40,
                            'u50': u50,
                            'p50': p50,
                            'xpt': xpt,
                            'xpa': xpa
                            }
    
        if position == 'dst':
            dictionary = {}
            for i in range(0, len(table)):
                rank = table[i][0]
                name = names[i]
                team = teams[i]
                sacks = table[i][2]
                pic = table[i][3]
                fr = table[i][4]
                ff = table[i][5]
                defTD = table[i][6]
                sfty = table[i][7]
                spcTD = table[i][8]
                
                formatName = '{} {}'.format(name[0], name[1])
                
                txtrank = 'Player Rank: {}'.format(rank)
                dictionary[txtrank] = {
                            'year': year,
                            'name': formatName,
                            'position': position, 
                            'rank': rank,
                            'team': team,
                            'sacks': sacks,
                            'int': pic,
                            'fr': fr,
                            'ff': ff,
                            'defTD': defTD,
                            'sfty': sfty,
                            'spcTD': spcTD
                            }
        
        return dictionary
    
    def weeklyDataScraper(URL, position, year, week):
        data = requests.get(URL).text
        soup = bs(data, 'html.parser')
        
        data = []
        table = soup.find('table')
        table_body = table.find('tbody')

        rows = table_body.find_all('tr')
        for row in rows:
            cols = row.find_all('td')
            cols = [ele.text.strip() for ele in cols]
            data.append([ele for ele in cols if ele])
        
        file = 'C:\\Users\\Freew\\OneDrive\\Desktop\\Python Projects\\Fantasy Football\\weekly_raw\\{} {} {} stats.json'.format(year, week, position)
        eq.writeEq(file, data)
        return data
    
    def historicData():
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
                file = 'C:\\Users\\Freew\\OneDrive\\Desktop\\Python Projects\\Fantasy Football\\annual_raw\\{} {} stats.json'.format(year[y], position[pos])
                path = Path(file)
                
                if path.is_file() == True:
                    data = eq.readEq(file)
                    
                else:
                    data = scraperEquations.historicalDataScraper(scraperEquations.tablePosition(position[pos], year[y]), position[pos], year[y])
                    
                playerDictionary = scraperEquations.formatDataAnnual(data, position[pos], year[y])
                txtyear = 'Player Year: {}'.format(year[y])
                dictionary[txtyear] = playerDictionary
                
                print('{} {} file complete'.format(year[y], position[pos]))
            
            txtpos = 'Player Position: {}'.format(position[pos])
            masterDictionary[txtpos] = dictionary
            
            file = 'C:\\Users\\Freew\\OneDrive\\Desktop\\Python Projects\\Fantasy Football\\Annual Master Database.json'
            eq.writeEq(file, masterDictionary)
            
    def weeklyData():
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
                    file = 'C:\\Users\\Freew\\OneDrive\\Desktop\\Python Projects\\Fantasy Football\\weekly_raw\\{} {} {} stats.json'.format(year[y], week, position[pos])
                    path = Path(file)
                    
                    if path.is_file() == True:
                        data = eq.readEq(file)
                        
                    else:
                        data = scraperEquations.weeklyDataScraper(scraperEquations.tablePosition(position[pos], year[y], week), position[pos], year[y], week)
                        
                    playerDictionary = scraperEquations.formatDataWeekly(data, position[pos], year[y], week)
                    txtweek = 'Player Week: {}'.format(week)
                    weekDictionary[txtweek] = playerDictionary
                    
                    print('{} {} {} file complete'.format(year[y], week, position[pos]))
                
                txtyear = 'Player Year: {}'.format(year[y])
                dictionary[txtyear] = weekDictionary
            
            txtpos = 'Player Position: {}'.format(position[pos])
            masterDictionary[txtpos] = dictionary
            
            file = 'C:\\Users\\Freew\\OneDrive\\Desktop\\Python Projects\\Fantasy Football\\Weekly Master Database.json'
            eq.writeEq(file, masterDictionary)