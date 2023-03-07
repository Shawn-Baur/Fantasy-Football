from equation_sheet import equations as eq

global positions
global years
positions = ['qb', 'rb', 'wr', 'te', 'k', 'dst']
years = eq.year(22)

class formatMaster():
    def formatMasterAnnual():
        data = eq.readEq('C:\\Users\\Freew\\OneDrive\\Desktop\\Python Projects\\Fantasy Football\\Annual Master Database.json')
        
        for pos in range(0, 6):
            position = 'Player Position: {}'.format(positions[pos])
            info = []
            
            for y in range(0, len(years)):
                year = 'Player Year: {}'.format(years[y])
                
                for r in range(1, len(data[position][year]) + 1):
                    rank = 'Player Rank: {}'.format(r)
                    info.append(data[position][year][rank])
            
            file = 'C:\\Users\\Freew\\OneDrive\\Desktop\\Python Projects\\Fantasy Football\\annual_pos_data\\{} Data.json'.format(positions[pos])
            eq.writeEq(file, info)
            print('Annual {} Complete'.format(position))
            
    def formatMasterWeekly():
        data = eq.readEq('C:\\Users\\Freew\\OneDrive\\Desktop\\Python Projects\\Fantasy Football\\Weekly Master Database.json')
        
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
            
            file = 'C:\\Users\\Freew\\OneDrive\\Desktop\\Python Projects\\Fantasy Football\\weekly_pos_data\\{} Data.json'.format(positions[pos])
            eq.writeEq(file, info)
            print('Weekly {} Complete'.format(position))
    
    def playerSorted():
        allplayers = []
        
        for pos in range(0, 6):
            player = []
            
            data = eq.readEq('C:\\Users\\Freew\\OneDrive\\Desktop\\Python Projects\\Fantasy Football\\weekly_pos_data\\{} Data.json'.format(positions[pos]))
            data2 = eq.readEq('C:\\Users\\Freew\\OneDrive\\Desktop\\Python Projects\\Fantasy Football\\annual_pos_data\\{} Data.json'.format(positions[pos]))

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
                
                eq.writeEq('C:\\Users\\Freew\\OneDrive\\Desktop\\Python Projects\\Fantasy Football\\players stats\\{} stats.json'.format(player[i]), singlePlayer)
                
            print('Player Names: {} Complete'.format(positions[pos]))
        
        eq.writeEq('Players.json', allplayers)
    
    def PlotableData():
        playerNames = eq.readEq("C:\\Users\\Freew\\OneDrive\\Desktop\\Python Projects\\Fantasy Football\\Analytics\\Players.json")
        
        qbGraphData = []
        rbGraphData = []
        wrGraphData = []
        teGraphData = []
        dstGraphData = []
        kGraphData = []
        
        for j in range(0, len(playerNames)):
            for i in range(0, len(playerNames[j])):
                file = 'C:\\Users\\Freew\\OneDrive\\Desktop\\Python Projects\\Fantasy Football\\players stats\\{} stats.json'.format(playerNames[j][i])
                data = eq.readEq(file)
                
                if(len(data) == 0):
                    print('Error Found with this Name: {}'.format(playerNames[j][i]))
                    
                    
                elif(data[0]['position'] == 'qb'):
                    player = data
                    name = player[0]['name']
                    position = player[0]['position']
                    team = player[0]['team']
                    
                    year = []
                    for i in range(0, len(player)):
                        year.append(player[i]['year'])
                    
                    year0 = year[0]
                    
                    week = []
                    rank = []
                    compPass = []
                    attPass = []
                    ydsPass = []
                    interceptions = []
                    sacked = []
                    attRush = []
                    ydsRush = []
                    tdRush = []
                    fl = []
                    for i in range(0, len(player)):
                        if year0 == year[i]:
                            week.append(player[i]['week'])
                            rank.append(player[i]['rank'])
                            compPass.append(player[i]['cmpPass'])
                            attPass.append(player[i]['attPass'])
                            ydsPass.append(player[i]['ydsPass'])
                            interceptions.append(player[i]['pic'])
                            sacked.append(player[i]['sacks'])
                            attRush.append(player[i]['attRush'])
                            ydsRush.append(player[i]['ydsRush'])
                            tdRush.append(player[i]['tdRush'])
                            fl.append(player[i]['fl'])
                            
                        else:
                            year0 = year[i]
                            
                            week.append(player[i]['week'])
                            rank.append(player[i]['rank'])
                            compPass.append(player[i]['cmpPass'])
                            attPass.append(player[i]['attPass'])
                            ydsPass.append(player[i]['ydsPass'])
                            interceptions.append(player[i]['pic'])
                            sacked.append(player[i]['sacks'])
                            attRush.append(player[i]['attRush'])
                            ydsRush.append(player[i]['ydsRush'])
                            tdRush.append(player[i]['tdRush'])
                            fl.append(player[i]['fl'])
                            
                    qbGraphData.append({'Name': name, 'team': team, 'week': week, 'rank': rank, 
                                        'compPass': compPass, 'attPass': attPass, 'ydsPass': ydsPass, 
                                        'interceptions': interceptions, 'sacks': sacked,
                                        'attRush': attRush, 'ydsRush': ydsRush, 'tdRush': tdRush, 'fl': fl})     
                        
                        
                    
                elif(data[0]['position'] == 'rb'):
                    player = data
                    name = player[0]['name']
                    position = player[0]['position']
                    team = player[0]['team']
                    
                    year = []
                    for i in range(0, len(player)):
                        year.append(player[i]['year'])
                    
                    year0 = year[0]
                    
                    week = []
                    rank = []
                    attRush = []
                    ydsRush = []
                    long = []
                    twtyPls = []
                    tdRush = []
                    rec = []
                    tgt = []
                    ydsPass = []
                    tdPass = []
                    fl = []
                    for i in range(0, len(player)):
                        if year0 == year[i]:
                            week.append(player[i]['week'])
                            rank.append(player[i]['rank'])
                            attRush.append(player[i]['attRush'])
                            ydsRush.append(player[i]['ydsRush'])
                            long.append(player[i]['long'])
                            twtyPls.append(player[i]['twtyPls'])
                            tdRush.append(player[i]['tdRush'])
                            rec.append(player[i]['rec'])
                            tgt.append(player[i]['tgt'])
                            ydsPass.append(player[i]['ydsPass'])
                            tdPass.append(player[i]['tdPass'])
                            fl.append(player[i]['fl'])
                            
                        else:
                            year0 = year[i]
                            
                            week.append(player[i]['week'])
                            rank.append(player[i]['rank'])
                            attRush.append(player[i]['attRush'])
                            ydsRush.append(player[i]['ydsRush'])
                            long.append(player[i]['long'])
                            twtyPls.append(player[i]['twtyPls'])
                            tdRush.append(player[i]['tdRush'])
                            rec.append(player[i]['rec'])
                            tgt.append(player[i]['tgt'])
                            ydsPass.append(player[i]['ydsPass'])
                            tdPass.append(player[i]['tdPass'])
                            fl.append(player[i]['fl'])
                            
                    rbGraphData.append({'Name': name, 'team': team, 'week': week, 'rank': rank, 
                                   'attRush': attRush, 'ydsRush': ydsRush, 'long': long, 'twtyPls': twtyPls, 'tdRush': tdRush,
                                   'receptions': rec, 'targets': tgt,
                                   'ydsPass': ydsPass, 'tdPass': tdPass, 'fl': fl})
                            
                        
                    
                elif(data[0]['position'] == 'wr' or data[0]['position'] == 'te'):
                    player = data
                    name = player[0]['name']
                    position = player[0]['position']
                    team = player[0]['team']
                    
                    year = []
                    for i in range(0, len(player)):
                        year.append(player[i]['year'])
                    
                    year0 = year[0]
                    
                    week = []
                    rank = []
                    receptions = []
                    targets = []
                    ydsPass = []
                    long = []
                    twtyPls = []
                    tdPass = []
                    attRush = []
                    ydsRush = []
                    tdRush = []
                    fl = []
                    for i in range(0, len(player)):
                        if year0 == year[i]:
                            week.append(player[i]['week'])
                            
                            rank.append(player[i]['rank'])
                            receptions.append(player[i]['rec'])
                            targets.append(player[i]['tgt'])
                            ydsPass.append(player[i]['ydsPass'])
                            long.append(player[i]['long'])
                            twtyPls.append(player[i]['twtyPls'])
                            tdPass.append(player[i]['tdPass'])
                            attRush.append(player[i]['attRush'])
                            ydsRush.append(player[i]['ydsRush'])
                            tdRush.append(player[i]['tdRush'])
                            fl.append(player[i]['fl'])
                            
                        else:
                            year0 = year[i]
                            
                            week.append(player[i]['week'])
                            rank.append(player[i]['rank'])
                            receptions.append(player[i]['rec'])
                            targets.append(player[i]['tgt'])
                            ydsPass.append(player[i]['ydsPass'])
                            long.append(player[i]['long'])
                            twtyPls.append(player[i]['twtyPls'])
                            tdPass.append(player[i]['tdPass'])
                            attRush.append(player[i]['attRush'])
                            ydsRush.append(player[i]['ydsRush'])
                            tdRush.append(player[i]['tdRush'])
                            fl.append(player[i]['fl'])
                    
                    if (position == 'wr'):
                        wrGraphData.append({'Name': name, 'team': team, 'week': week, 'rank': rank, 
                                           'receptions': receptions, 'targets': targets, 'ydsPass': ydsPass, 
                                           'long': long, 'twtyPls': twtyPls, 'tdPass': tdPass,
                                           'attRush': attRush, 'ydsRush': ydsRush, 'tdRush': tdRush, 'fl': fl})
                    
                    if (position == 'te'):
                        teGraphData.append({'Name': name, 'team': team, 'week': week, 'rank': rank, 
                                           'receptions': receptions, 'targets': targets, 'ydsPass': ydsPass, 
                                           'long': long, 'twtyPls': twtyPls, 'tdPass': tdPass,
                                           'attRush': attRush, 'ydsRush': ydsRush, 'tdRush': tdRush, 'fl': fl})
                
                elif(data[0]['position'] == 'dst'):
                    player = data
                    name = player[0]['name']
                    position = player[0]['position']
                    team = player[0]['team']
                    
                    year = []
                    for i in range(0, len(player)):
                        year.append(player[i]['year'])
                    
                    year0 = year[0]
                    
                    week = []
                    rank = []
                    sacks = []
                    interceptions = []
                    fumbleRecovery = []
                    fumbleForced = []
                    defTd = []
                    safty = []
                    specialTd = []
                    for i in range(0, len(player)):
                        if year0 == year[i]:
                            week.append(player[i]['week'])
                            
                            rank.append(player[i]['rank'])
                            sacks.append(player[i]['sacks'])
                            interceptions.append(player[i]['int'])
                            fumbleRecovery.append(player[i]['fr'])
                            fumbleForced.append(player[i]['ff'])
                            defTd.append(player[i]['defTD'])
                            safty.append(player[i]['sfty'])
                            specialTd.append(player[i]['spcTD'])
                            
                        else:
                            year0 = year[i]
                            
                            week.append(player[i]['week'])
                            rank.append(player[i]['rank'])
                            sacks.append(player[i]['sacks'])
                            interceptions.append(player[i]['int'])
                            fumbleRecovery.append(player[i]['fr'])
                            fumbleForced.append(player[i]['ff'])
                            defTd.append(player[i]['defTD'])
                            safty.append(player[i]['sfty'])
                            specialTd.append(player[i]['spcTD'])
                            
                    dstGraphData.append({'Name': name, 'team': team, 'week': week, 'rank': rank, 
                                        'sacks': sacks, 'interceptions': interceptions, 
                                        'fumbleRecovery': fumbleRecovery, 'fumbleForced': fumbleForced, 
                                        'defTd': defTd, 'safty': safty, 'secialTd': specialTd})
                    
                elif(data[0]['position'] == 'k'):
                    player = data
                    name = player[0]['name']
                    position = player[0]['position']
                    team = player[0]['team']
                    
                    year = []
                    for i in range(0, len(player)):
                        year.append(player[i]['year'])
                    
                    year0 = year[0]
                    
                    week = []
                    rank = []
                    fg = []
                    fga = []
                    long = []
                    u20 = []
                    u30 = []
                    u40 = []
                    u50 = []
                    p50 = []
                    xpt = []
                    xpa = []
                    for i in range(0, len(player)):
                        if year0 == year[i]:
                            week.append(player[i]['week'])
                            
                            rank.append(player[i]['rank'])
                            fg.append(player[i]['fg'])
                            fga.append(player[i]['fga'])
                            long.append(player[i]['long'])
                            u20.append(player[i]['u20'])
                            u30.append(player[i]['u30'])
                            u40.append(player[i]['u40'])
                            u50.append(player[i]['u50'])
                            p50.append(player[i]['p50'])
                            xpt.append(player[i]['xpt'])
                            xpa.append(player[i]['xpa'])
                            
                        else:
                            year0 = year[i]
                            
                            week.append(player[i]['week'])
                            
                            rank.append(player[i]['rank'])
                            fg.append(player[i]['fg'])
                            fga.append(player[i]['fga'])
                            long.append(player[i]['long'])
                            u20.append(player[i]['u20'])
                            u30.append(player[i]['u30'])
                            u40.append(player[i]['u40'])
                            u50.append(player[i]['u50'])
                            p50.append(player[i]['p50'])
                            xpt.append(player[i]['xpt'])
                            xpa.append(player[i]['xpa'])
                            
                    kGraphData.append({'Name': name, 'team': team, 'week': week, 'rank': rank, 
                                        'fg': fg, 'fga': fga, 'long': long, 
                                        '0-19': u20, '20-29': u30, '30-39': u40, '40-49': u50, '50-': p50,
                                        'xpt': xpt, 'xpa': xpa})
        
        eq.writeEq('C:\\Users\\Freew\\OneDrive\\Desktop\\Python Projects\\Fantasy Football\\Analytics\\Graphical\\qbGraphical.json', qbGraphData)
        eq.writeEq('C:\\Users\\Freew\\OneDrive\\Desktop\\Python Projects\\Fantasy Football\\Analytics\\Graphical\\rbGraphical.json', rbGraphData)
        eq.writeEq('C:\\Users\\Freew\\OneDrive\\Desktop\\Python Projects\\Fantasy Football\\Analytics\\Graphical\\wrGraphical.json', wrGraphData)
        eq.writeEq('C:\\Users\\Freew\\OneDrive\\Desktop\\Python Projects\\Fantasy Football\\Analytics\\Graphical\\teGraphical.json', teGraphData)
        eq.writeEq('C:\\Users\\Freew\\OneDrive\\Desktop\\Python Projects\\Fantasy Football\\Analytics\\Graphical\\dstGraphical.json', dstGraphData)
        eq.writeEq('C:\\Users\\Freew\\OneDrive\\Desktop\\Python Projects\\Fantasy Football\\Analytics\\Graphical\\kGraphical.json', kGraphData)