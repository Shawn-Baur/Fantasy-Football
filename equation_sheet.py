# -*- coding: utf-8 -*-
"""
Created on Wed Feb  1 15:41:30 2023

@author: Freew
"""
import json
global positions, stats

positions = ['qb', 'rb', 'wr', 'te', 'k', 'dst']
stats = [['rank', 'cmpPass', 'attPass', 'ydsPass', 'tdPass', 'pic', 'sacks', 'attRush', 'ydsRush', 'tdRush', 'fl'], 
        ['rank', 'attRush', 'ydsRush', 'long', 'twtyPls', 'tdRush', 'rec', 'tgt', 'ydsPass', 'tdPass', 'fl'], 
        ['rank', 'rec', 'tgt', 'ydsPass', 'long', 'twtyPls', 'tdPass', 'attRush', 'ydsRush', 'tdRush', 'fl'], 
        ['rank', 'rec', 'tgt', 'ydsPass', 'long', 'twtyPls', 'tdPass', 'attRush', 'ydsRush', 'tdRush', 'fl'], 
        ['rank', 'fg', 'fga', 'long', 'u20', 'u30', 'u40', 'u50', 'p50', 'xpt', 'xpa'],
        ['rank', 'sacks', 'int', 'fr', 'ff', 'defTD', 'sfty', 'spcTD']]
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
    
    def pointsCalculator(position, plrstats):
        positionalStats = stats[positions.index(position)]
        
        perStat = []
        if (position == 'qb'):
            rushTD = (6 * plrstats[positionalStats.index('tdRush')])
            passingTD = (4 * plrstats[positionalStats.index('tdPass')])
            rushYDs = (1/10 * plrstats[positionalStats.index('ydsRush')])
            recYDs = (1/10 * plrstats[positionalStats.index('ydsPass')])
            interception = (-2 * plrstats[positionalStats.index('pic')])
        
            points = rushTD + passingTD + rushYDs + recYDs - interception
            perStat = recYDs, passingTD, rushYDs, rushTD, interception
            labels = 'passingYDs', 'passingTD', 'rushYds', 'rushTD', 'interceptions'
        
        elif (position == 'rb'):
            rushTD = (6 * plrstats[positionalStats.index('tdRush')])
            recTD = (6 * plrstats[positionalStats.index('tdPass')])
            rushYDs = (1/10 * plrstats[positionalStats.index('ydsRush')])
            recYDs = (1/10 * plrstats[positionalStats.index('ydsPass')])
            receptions = (.5 * plrstats[positionalStats.index('rec')])
            
            points = rushTD + recTD + rushYDs + recYDs + receptions
            perStat = rushYDs, rushTD, receptions, recYDs, recTD
            labels = 'rushYDs', 'rushTD', 'receptions', 'recYDs', 'recTD'
            
        elif (position == 'wr' or position == 'te'):
            rushTD = (6 * plrstats[positionalStats.index('tdRush')])
            recTD = (6 * plrstats[positionalStats.index('tdPass')])
            rushYDs = (1/10 * plrstats[positionalStats.index('ydsRush')])
            recYDs = (1/10 * plrstats[positionalStats.index('ydsPass')])
            receptions = (.5 * plrstats[positionalStats.index('rec')])
            
            points = rushTD + recTD + rushYDs + recYDs + receptions
            perStat = receptions, recYDs, recTD, rushYDs, rushTD
            labels = 'receptions', 'recYDs', 'recTD', 'rushYDs', 'rushTD'
            
        elif (position == 'k'):
            fg39 = (3 * (plrstats[positionalStats.index('u20')] + plrstats[positionalStats.index('u30')] + plrstats[positionalStats.index('u40')]))
            fg49 = (4 * plrstats[positionalStats.index('u50')])
            fg50 = (5 * plrstats[positionalStats.index('p50')])
            fgm = (-1 * (plrstats[positionalStats.index('fga')] - plrstats[positionalStats.index('fg')]))
            xpt = (1 * plrstats[positionalStats.index('xpt')])
            xpm = (-1 * (plrstats[positionalStats.index('xpa')] - plrstats[positionalStats.index('xpt')]))
            
            points = fg39 + fg49 + fg50 + fgm + xpt + xpm
            perStat = xpt, xpm, fg39, fg49, fg50, fgm
            labels = 'xpt', 'xpt missed', 'fg 0 - 39', 'fg 40 - 49', 'fg 50+', 'fg missed'
        
        else:
            pass
        
        return points, perStat, labels