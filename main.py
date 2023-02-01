from hisDataComp import annualFantasyData as annual
from weeklyDataComp import weeklyFantasyData as weekly
from equation_sheet import equations as eq
from pathlib import Path

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
                data = annual.historicalDataScraper(annual.tablePosition(position[pos], year[y]), position[pos], year[y])
                
            playerDictionary = annual.formatData(data, position[pos], year[y])
            txtyear = 'Player Year: {}'.format(year[y])
            dictionary[txtyear] = playerDictionary
            
            print('{} {} file complete'.format(year[y], position[pos]))
        
        file = 'C:\\Users\\Freew\\OneDrive\\Desktop\\Python Projects\\Fantasy Football\\annual_pos_data\\{} Data.json'.format(position[pos])
        eq.writeEq(file, dictionary)
        
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
    
    current = year[len(year)-1]
    masterDictionary = {}
    for pos in range(0, 6):
        dictionary = {}
        for y in range(2,len(year)):
            if year[y] < '2021':
                w = 17
            if year[y] == current:
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
                    data = weekly.weeklyDataScraper(weekly.tablePosition(position[pos], year[y], week), position[pos], year[y], week)
                    
                playerDictionary = weekly.formatData(data, position[pos], year[y], week)
                txtweek = 'Player Week: {}'.format(week)
                weekDictionary[txtweek] = playerDictionary
                
                print('{} {} {} file complete'.format(year[y], week, position[pos]))
            
            txtyear = 'Player Year: {}'.format(year[y])
            dictionary[txtyear] = weekDictionary
            
            file = 'C:\\Users\\Freew\\OneDrive\\Desktop\\Python Projects\\Fantasy Football\\weekly_pos_data\\{} Data.json'.format(position[pos])
            eq.writeEq(file, dictionary)
        
        txtpos = 'Player Position: {}'.format(position[pos])
        masterDictionary[txtpos] = dictionary
        
        file = 'C:\\Users\\Freew\\OneDrive\\Desktop\\Python Projects\\Fantasy Football\\Weekly Master Database.json'
        eq.writeEq(file, masterDictionary)

historicData()
weeklyData()