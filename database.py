# -*- coding: utf-8 -*-
"""
Created on Thu Mar  9 13:43:59 2023

@author: Freew
"""

from equation_sheet import equations as eq
import numpy as np

global positions
global years
positions = ['qb', 'rb', 'wr', 'te', 'k', 'dst']
years = eq.year(22)

def databaseAnnual():
    data1 = []
    for pos in range(0,6):
        data = eq.readEq('C:\\Users\\Freew\\OneDrive\\Desktop\\Python Projects\\Fantasy Football\\data\\annual_pos_data\\{} Data.json'.format(positions[pos]))
        
        names = []
        sort = []
        for i in range(0, len(data)):
            if(data[i]['name'] not in names):
                names.append(data[i]['name'])
                
                data_copy = []
                data_copy.append(data[i])
                sort.append(data_copy)
            else:
                data_copy = []
                data_copy.append(data[i])
                loc = names.index(data[i]['name'])
                sort[loc].extend(data_copy)
        data1.append(sort)
    
    database = []
    for pos in range(0, len(data1)):
        players = []
        
        
        for plr in range(0 , len(data1[pos])):
            individual = []
            individual.append(data1[pos][plr][0]['name'])
            
            if (positions[pos] == 'qb'):
                stats = ['year', 'rank', 'cmpPass', 'attPass', 'ydsPass', 'tdPass', 'pic', 'sacks',
                         'attRush', 'ydsRush', 'tdRush', 'fl']
                
                h, w = len(stats), len(data1[pos][plr])
                stat_list = [[None] * w for i in range(h)]
            
            elif (positions[pos] == 'rb'):
                stats = ['year', 'rank', 'attRush', 'ydsRush', 'long', 'twtyPls', 'tdRush', 'rec',
                         'tgt', 'ydsPass', 'tdPass', 'fl']
                
                h, w = len(stats), len(data1[pos][plr])
                stat_list = [[None] * w for i in range(h)]
            
            elif (positions[pos] == 'wr' or positions[pos] == 'te'):
                stats = ['year', 'rank', 'rec', 'tgt', 'ydsPass', 'long', 'twtyPls', 'tdPass', 
                         'attRush', 'ydsRush', 'tdRush', 'fl']
                
                h, w = len(stats), len(data1[pos][plr])
                stat_list = [[None] * w for i in range(h)]
                
            elif (positions[pos] == 'dst'):
                stats = ['year', 'rank', 'sacks', 'int', 'fr', 'ff', 'defTD', 'sfty', 'spcTD']
                
                h, w = len(stats), len(data1[pos][plr])
                stat_list = [[None] * w for i in range(h)]
            
            elif (positions[pos] == 'k'):
                stats = ['year', 'rank', 'fg', 'fga', 'long', 'u20', 'u30', 'u40', 'u50', 'p50', 'xpt', 'xpa']
                
                h, w = len(stats), len(data1[pos][plr])
                stat_list = [[None] * w for i in range(h)]
            
            for yr in range(0, len(data1[pos][plr])):
                for st in range(0, len(stats)):
                    if (len(data1[pos][plr]) == 0):
                        pass
                    else:
                        string = data1[pos][plr][yr]['{}'.format(stats[st])]
                        new_string = string.replace(",", "")
                        
                        stt = int(new_string)

                    stat_list[st][yr] = stt
                    
            individual.append(stat_list)
            players.append(individual)
        database.append(players)
    
    eq.writeEq('database_Annual.json', database)
    print('Annual Database Created')
    
def databaseWeekly():
    data1 = []
    for pos in range(0,6):
        data = eq.readEq('C:\\Users\\Freew\\OneDrive\\Desktop\\Python Projects\\Fantasy Football\\data\\weekly_pos_data\\{} Data.json'.format(positions[pos]))
        
        names = []
        sort = []
        for i in range(0, len(data)):
            if(data[i]['name'] not in names):
                names.append(data[i]['name'])
                
                data_copy = []
                data_copy.append(data[i])
                sort.append(data_copy)
            else:
                data_copy = []
                data_copy.append(data[i])
                loc = names.index(data[i]['name'])
                sort[loc].extend(data_copy)
        data1.append(sort)
    
    database = []
    for pos in range(0, len(data1)):
        players = []
        
        
        for plr in range(0 , len(data1[pos])):
            individual = []
            
            individual.append(data1[pos][plr][0]['name'])
            
            if (positions[pos] == 'qb'):
                stats = ['year', 'week', 'rank', 'cmpPass', 'attPass', 'ydsPass', 'tdPass', 'pic', 'sacks',
                         'attRush', 'ydsRush', 'tdRush', 'fl']
                
                h, w = len(stats), len(data1[pos][plr])
                stat_list = [[None] * w for i in range(h)]
            
            elif (positions[pos] == 'rb'):
                stats = ['year', 'week', 'rank', 'attRush', 'ydsRush', 'long', 'twtyPls', 'tdRush', 'rec',
                         'tgt', 'ydsPass', 'tdPass', 'fl']
                
                h, w = len(stats), len(data1[pos][plr])
                stat_list = [[None] * w for i in range(h)]
            
            elif (positions[pos] == 'wr' or positions[pos] == 'te'):
                stats = ['year', 'week', 'rank', 'rec', 'tgt', 'ydsPass', 'long', 'twtyPls', 'tdPass', 
                         'attRush', 'ydsRush', 'tdRush', 'fl']
                
                h, w = len(stats), len(data1[pos][plr])
                stat_list = [[None] * w for i in range(h)]
                
            elif (positions[pos] == 'dst'):
                stats = ['year', 'week', 'rank', 'sacks', 'int', 'fr', 'ff', 'defTD', 'sfty', 'spcTD']
                
                h, w = len(stats), len(data1[pos][plr])
                stat_list = [[None] * w for i in range(h)]
            
            elif (positions[pos] == 'k'):
                stats = ['year', 'week', 'rank', 'fg', 'fga', 'long', 'u20', 'u30', 'u40', 'u50', 'p50', 'xpt', 'xpa']
                
                h, w = len(stats), len(data1[pos][plr])
                stat_list = [[None] * w for i in range(h)]
            
            for wk in range(0, len(data1[pos][plr])):
                for st in range(0, len(stats)):
                    if (len(data1[pos][plr]) == 0):
                        pass
                    else:
                        string = str(data1[pos][plr][wk]['{}'.format(stats[st])])
                        new_string = string.replace(",", "")
                        
                        stt = int(new_string)
                        
                    stat_list[st][wk] = stt
            
            individual.append(stat_list)
            players.append(individual)
        database.append(players)

    eq.writeEq('database_Weekly.json', database)
    print('Weekly Database Created')

databaseAnnual()
databaseWeekly()
# positionPlayerListAnnual()
# positionPlayerListWeekly()