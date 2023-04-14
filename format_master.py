from equation_sheet import equations as eq

global positions
global years
positions = ['qb', 'rb', 'wr', 'te', 'k', 'dst']
years = eq.year(22)

class formatMaster():
    def positionPlayerListAnnual():
        data = eq.readEq('C:\\Users\\Freew\\OneDrive\\Desktop\\Python Projects\\Fantasy Football\\data\\Annual Master Database.json')
        
        for pos in range(0, 6):
            position = 'Player Position: {}'.format(positions[pos])
            info = []
            
            for y in range(0, len(years)):
                year = 'Player Year: {}'.format(years[y])
                
                for r in range(1, len(data[position][year]) + 1):
                    rank = 'Player Rank: {}'.format(r)
                    info.append(data[position][year][rank])
            
            file = 'C:\\Users\\Freew\\OneDrive\\Desktop\\Python Projects\\Fantasy Football\\data\\annual_pos_data\\{} Data.json'.format(positions[pos])
            eq.writeEq(file, info)
            print('Annual {} Complete'.format(position))
            
    def positionPlayerListWeekly():
        data = eq.readEq('C:\\Users\\Freew\\OneDrive\\Desktop\\Python Projects\\Fantasy Football\\data\\Weekly Master Database.json')
        
        for pos in range(0, 6):
            position = 'Player Position: {}'.format(positions[pos])
            info = []
            
            for y in range(0, len(years)):
                year = 'Player Year: {}'.format(years[y])
                weekLen = len(data[position][year])
                
                for w in range(1, weekLen):
                    week = 'Player Week: {}'.format(w)
                    
                    for r in range(1, len(data[position][year][week])):
                        rank = 'Player Rank: {}'.format(r)
                        info.append(data[position][year][week][rank])
            
            file = 'C:\\Users\\Freew\\OneDrive\\Desktop\\Python Projects\\Fantasy Football\\data\\weekly_pos_data\\{} Data.json'.format(positions[pos])
            eq.writeEq(file, info)
            print('Weekly {} Complete'.format(position))
            
    def formatMasterAnnual():
        data = eq.readEq('C:\\Users\\Freew\\OneDrive\\Desktop\\Python Projects\\Fantasy Football\\data\\Annual Master Database.json')
        
        for pos in range(0, 6):
            position = 'Player Position: {}'.format(positions[pos])
            info = []
            
            for y in range(0, len(years)):
                year = 'Player Year: {}'.format(years[y])
                
                for r in range(1, len(data[position][year]) + 1):
                    rank = 'Player Rank: {}'.format(r)
                    info.append(data[position][year][rank])
            
            file = 'C:\\Users\\Freew\\OneDrive\\Desktop\\Python Projects\\Fantasy Football\\data\\annual_pos_data\\{} Data.json'.format(positions[pos])
            eq.writeEq(file, info)
            print('Annual {} Complete'.format(position))
            
    def formatMasterWeekly():
        data = eq.readEq('C:\\Users\\Freew\\OneDrive\\Desktop\\Python Projects\\Fantasy Football\\data\\Weekly Master Database.json')
        
        for pos in range(0, 6):
            position = 'Player Position: {}'.format(positions[pos])
            info = []
            
            for y in range(0, len(years)):
                year = 'Player Year: {}'.format(years[y])
                weekLen = len(data[position][year])
                
                for w in range(1, weekLen):
                    week = 'Player Week: {}'.format(w)
                    
                    for r in range(1, len(data[position][year][week])):
                        rank = 'Player Rank: {}'.format(r)
                        info.append(data[position][year][week][rank])
            
            file = 'C:\\Users\\Freew\\OneDrive\\Desktop\\Python Projects\\Fantasy Football\\data\\weekly_pos_data\\{} Data.json'.format(positions[pos])
            eq.writeEq(file, info)
            print('Weekly {} Complete'.format(position))
    
    def playerSorted():
        allplayers = []
        
        for pos in range(0, 6):
            player = []
            
            data = eq.readEq('C:\\Users\\Freew\\OneDrive\\Desktop\\Python Projects\\Fantasy Football\\data\\weekly_pos_data\\{} Data.json'.format(positions[pos]))
            data2 = eq.readEq('C:\\Users\\Freew\\OneDrive\\Desktop\\Python Projects\\Fantasy Football\\data\\annual_pos_data\\{} Data.json'.format(positions[pos]))

            for i in range(0, len(data)):
                if data[i]['name'] not in player:
                    player.append(data[i]['name'])
            
            for i in range(0, len(data2)):
                if data2[i]['name'] not in player:
                    player.append(data2[i]['name'])
            
            allplayers.append(player)
            
            for i in range(0, len(player)):
                singlePlayer = []
                
                for j in range(0, len(data)):
                    if data[j]['name'] == player[i]:
                        singlePlayer.append(data[j])
                        
                for j in range(0, len(data2)):
                    if data2[j]['name'] == player[i]:
                        pass
                
                eq.writeEq('C:\\Users\\Freew\\OneDrive\\Desktop\\Python Projects\\Fantasy Football\\data\\players stats\\{} stats.json'.format(player[i]), singlePlayer)
                
            print('Player Names: {} Complete'.format(positions[pos]))
        
        eq.writeEq('Players.json', allplayers)