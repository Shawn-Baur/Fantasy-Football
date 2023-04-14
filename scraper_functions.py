# -*- coding: utf-8 -*-
"""
Created on Thu Mar  9 13:02:43 2023

@author: Freew
"""

from equation_sheet import equations as eq
from bs4 import BeautifulSoup as bs
import requests

def tablePositionAnnual(position, year):
    URL = 'https://www.fantasypros.com/nfl/stats/{}.php?year={}'.format(position, year)
    return URL

def tablePositionWeekly(position, year, week):
    URL = 'https://www.fantasypros.com/nfl/stats/{}.php?week={}&range=week&year={}'.format(position, week, year)
    return URL

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
    
    file = 'C:\\Users\\Freew\\OneDrive\\Desktop\\Python Projects\\Fantasy Football\\data\\annual_raw\\{} {} stats.json'.format(year, position)
    eq.writeEq(file, data)
    return data

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
    
    file = 'C:\\Users\\Freew\\OneDrive\\Desktop\\Python Projects\\Fantasy Football\\data\\weekly_raw\\{} {} {} stats.json'.format(year, week, position)
    eq.writeEq(file, data)
    return data

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