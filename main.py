from hisDataComp import annualFantasyData as annual
from weeklyDataComp import weeklyFantasyData as weekly
from equation_sheet import equations as eq
from pathlib import Path
import json

def historicData():
    yearMax = 22
    position = ['qb', 'rb', 'wr', 'te', 'k', 'dst']
    
    year = []
    yrPlayers = []
    x = range(0,100)
    for y in range(2, yearMax+1):
            if x[y] < 10:
                years = '200{}'.format(x[y])
            else:
                years = '20{}'.format(x[y])
            year.append(years)
            
    for pos in range(0,6):
        posPlayers = []
        for y in range(0, len(year)):
            file = 'C:\\Users\\Freew\\OneDrive\\Desktop\\Python Projects\\Fantasy Football\\annual_raw\\{} {} stats.txt'.format(year[y], position[pos])
            path = Path(file)
            
            if path.is_file() == False:
                annual.historicalDataScraper(annual.tablePosition(position[pos], year[y]), position[pos], year[y])
            
            posPlayers.extend(annual.formatData(file, position[pos], year[y]))
        yrPlayers.append(posPlayers)

    file2 = 'C:\\Users\\Freew\\OneDrive\\Desktop\\Python Projects\\Fantasy Football\\raw data.txt'
    path2 = Path(file2)

    if path2.is_file() == False:
        annual.createFile(yrPlayers)

def weeklyData():
    yearMax = 22
    position = ['qb', 'rb', 'wr', 'te', 'k', 'dst']
    
    year = []
    x = range(0,100)
    for y in range(2, yearMax+1):
            if x[y] < 10:
                years = '200{}'.format(x[y])
            else:
                years = '20{}'.format(x[y])
            year.append(years)
    
    yrPlayers = []
    current = year[len(year)-1]
    for pos in range(0, 6):
        posPlayers = []
        for y in range(0,len(year)):
            if year[y] < '2021':
                w = 17
            if year[y] == current:
                w = 17
            else:
                w = 18
            for week in range(1, w):
                file = 'C:\\Users\\Freew\\OneDrive\\Desktop\\Python Projects\\Fantasy Football\\weekly_raw\\{} {} {} stats.json'.format(year[y], week, position[pos])
                path = Path(file)
                
                if path.is_file() == True:
                    data = eq.readEq(file)
                else:
                    data = weekly.weeklyDataScraper(weekly.tablePosition(position[pos], year[y], week), position[pos], year[y], week)

                posPlayers.extend(weekly.formatData(data, position[pos], year[y], week))
                print('{} {} {} file complete'.format(year[y], week, position[pos]))
                
            yrPlayers.append(posPlayers)
            file = 'Data.json'
            eq.writeEq(file, yrPlayers)

def test():
    year = '2021'
    position = 'te'
    week = 3
    posPlayers =[]
    
    data = weekly.weeklyDataScraper(weekly.tablePosition(position, year, week), position, year, week)
    posPlayers.extend(weekly.formatData(data, position, year, week))
    
    print(posPlayers)
    
#test()
#historicData()
weeklyData()