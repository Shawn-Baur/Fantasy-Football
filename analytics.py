# -*- coding: utf-8 -*-
"""
Created on Tue Mar  7 00:55:32 2023

@author: Freew
"""
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
from numpy import savetxt
from equation_sheet import equations as eq
import os

global positions, stats, years, yearmax
years = eq.year(22)
positions = ['qb', 'rb', 'wr', 'te', 'k', 'dst']
stats = [['rank', 'cmpPass', 'attPass', 'ydsPass', 'tdPass', 'pic', 'sacks', 'attRush', 'ydsRush', 'tdRush', 'fl'], 
        ['rank', 'attRush', 'ydsRush', 'long', 'twtyPls', 'tdRush', 'rec', 'tgt', 'ydsPass', 'tdPass', 'fl'], 
        ['rank', 'rec', 'tgt', 'ydsPass', 'long', 'twtyPls', 'tdPass', 'attRush', 'ydsRush', 'tdRush', 'fl'], 
        ['rank', 'rec', 'tgt', 'ydsPass', 'long', 'twtyPls', 'tdPass', 'attRush', 'ydsRush', 'tdRush', 'fl'], 
        ['rank', 'fg', 'fga', 'long', 'u20', 'u30', 'u40', 'u50', 'p50', 'xpt', 'xpa'],
        ['rank', 'sacks', 'int', 'fr', 'ff', 'defTD', 'sfty', 'spcTD']]
  
def graphAnnualTargets():
    data = eq.readEq('database_Annual.json')
    
    plt.rcParams['figure.figsize'] = [30,20]
    
    guysPassed = 0
    pos = 2
    for plr in range(0, len(data[pos])):
        success = False
        arr = np.array(data[pos][plr][1])
        
        for i in range(0, len(arr[1])):
            if(arr[1][i] <= 10):
                success = True
                break
            
        if(success == True):
            year = arr[0]
            tgt = arr[2]
            
            plt.plot(year, tgt, label='{}'.format(data[pos][plr][0]))
            
        else:
            guysPassed = guysPassed + 1
            pass
    
    SMALL_SIZE = 15
    MEDIUM_SIZE = 40
    BIGGER_SIZE = 50
    
    plt.legend()
    plt.xlabel('Year', fontsize=MEDIUM_SIZE)
    plt.ylabel('Number of Targets', fontsize=MEDIUM_SIZE)
    plt.title('Targets Over Careers', fontsize=BIGGER_SIZE)
    plt.show()
    
    print(guysPassed)
    
def heatMap():
    data = eq.readEq('database_Annual.json')
    indexPos = []
    
    for pos in range(0, len(positions)-1):
        players = []
        sts = []
        playedyrs = []
        for plr in range(0, len(data[pos])):
            players.append(data[pos][plr][0])
            sts.append(data[pos][plr][1])
            playedyrs.append(data[pos][plr][1][0])
        
        indexAnnual = []
        for yrs in range(0, len(years)):
            index = []
            for plr in range(0 , len(data[pos])):
                value = []
                try:
                    value.append(playedyrs[plr].index(int(years[yrs])))
                    value.insert(0, data[pos][plr][0])
                    index.append(value)
                except:
                    pass
            
            indexAnnual.append(index)
        indexPos.append(indexAnnual)
    
    for pos in range(0, len(positions)):
        if (positions[pos] != 'dst'):
            for yrs in range(0, len(years)):
                file = "C:\\Users\\Freew\\OneDrive\\Desktop\\Python Projects\\Fantasy Football\\Graphs\\HeatMaps\\{}\\{} {} Heatmap.png".format(positions[pos], years[yrs], positions[pos])
                directory = os.path.isfile(file)
                if (directory == False):
                    player = indexPos[pos][yrs]
                    
                    plrName = []
                    plrIndex = []
                    for i in range(0, len(player)):
                        plrName.append(player[i][0])
                        plrIndex.append(player[i][1])
                    
                    dataIndex = []
                    for i in range(0, len(plrName)):
                        compName = plrName[i]
                        
                        for plr in range(0, len(data[pos])):
                            plrNameData = data[pos][plr][0]
                            
                            if (plrNameData == compName):
                                dataIndex.append(plr)
                            else:
                                pass
                    
                    # print(dataIndex)
                    plrData = []
                    for i in range(0, len(dataIndex)):
                        individualData = []
                        for st in range(1, len(stats[pos])+1):
                            individualData.append(data[pos][dataIndex[i]][1][st][plrIndex[i]])
                        plrData.append(individualData)
                    
                    rank = []
                    for i in range(0, len(plrData)):
                        rank.append(plrData[i][0])
                    
                    pltData = []
                    for i in range(0, len(plrData)):
                        points, eachStat, labels = eq.pointsCalculator(positions[pos], plrData[i])
                        eachStat = list(eachStat)
                        labels = list(labels)
                        
                        affectRating = []
                        for j in range(0, len(eachStat)):
                            if points > 0:
                                affectRating.append(eachStat[j] / points)
                            else:
                                affectRating.append(0)
                            
                        pltData.append(affectRating)
                        
                    for i in range(0, len(pltData)):
                        pltData[i].insert(0, rank[i])
                    
                    
                    rank, pltData, plrName = zip(*sorted(zip(rank, pltData, plrName)))
                    
                    maxRank = 100
                    
                    if(positions[pos] == 'k'):
                        maxRank = 50
                    
                    rank = rank[:maxRank]
                    pltData = pltData[:maxRank]
                    plrName = plrName[:maxRank]
                    
                    plotinfo = np.array(pltData)
                    plotinfo = np.round(plotinfo, decimals=2)
                    # plotinfo = plotinfo[plotinfo[:, 0].argsort()]
                    
                    plotinfo = plotinfo[:, 1:]
                    
                    # Modified code to generate the heatmap with bigger figure size and smaller font
                    fig, ax = plt.subplots(figsize=(len(stats[pos])*2, maxRank//2))
                    im = ax.imshow(plotinfo)
                    
                    # Show all ticks and label them with the respective list entries
                    ax.set_xticks(np.arange(len(labels)), labels=labels)
                    ax.set_yticks(np.arange(len(plrName)), labels=plrName)
                    
                    # Rotate the tick labels and set their alignment.
                    plt.setp(ax.get_xticklabels(), rotation=45, ha="right",
                              rotation_mode="anchor", fontsize=10)
                    
                    # Set font size for y-axis tick labels
                    plt.setp(ax.get_yticklabels(), fontsize=10)
                    
                    # Loop over data dimensions and create text annotations.
                    for i in range(len(plrName)):
                        for j in range(len(labels)):
                            text = ax.text(j, i, plotinfo[i, j], ha="center", va="center", color="w", fontsize=10)
                    
                    ax.set_title("{}: {} Heatmap".format(years[yrs], positions[pos]), fontsize=16)
                    fig.tight_layout()
                    
                    # Save the figure to a file
                    file = "C:\\Users\\Freew\\OneDrive\\Desktop\\Python Projects\\Fantasy Football\\Graphs\\HeatMaps\\{}\\{} {} Heatmap.png".format(positions[pos], years[yrs], positions[pos])
                    plt.savefig(file, dpi=300, bbox_inches='tight')
                    
                    # Display the figure
                    plt.show()
                    
                    complete = '{} {} Heatmap Completed'.format(years[yrs], positions[pos])
                    print(complete)
                else:
                    complete = '{} {} Heatmap Completed'.format(years[yrs], positions[pos])
                    print(complete)

heatMap()
#graphAnnualTargets()