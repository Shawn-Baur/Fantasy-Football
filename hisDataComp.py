from bs4 import BeautifulSoup as bs
import requests, re

class annualFantasyData:
    def historicalDataScraper(URL, position, year):
        data = requests.get(URL).text
        soup = bs(data, 'html.parser')
        
        #find elements
        text_table = soup.find('table').get_text()
        
        file = 'C:\\Users\\Freew\\OneDrive\\Desktop\\Python Projects\\Fantasy Football\\annual_raw\\{} {} stats.txt'.format(year, position)
        f = open(file, "a")
        f.truncate(0)
        doc = text_table
        print(doc, file=f)
        f.close()

    def tablePosition(position, year):
        URL = 'https://www.fantasypros.com/nfl/stats/{}.php?year={}'.format(position, year)
        return URL
    
    def formatData(table, position, year):
        text_file = open(table, 'r')
        old = text_file.read()
        
        #Split text file into array line by line
        modified = old.split('\n')
        
        #Remove unwanted data
        modified = [i for i in modified if i != '']
        modified = [i for i in modified if i != '\xa0']
        modified = [i for i in modified if i != '\d+']
        
        if position == 'qb':
            divisor = 16
        if position == 'rb':
            divisor = 16
        if position == 'wr' or position == 'te':
            divisor = 15
        if position == 'k':
            divisor = 15
        if position == 'dst':
            divisor = 11
        
        numPlayers = ((len(modified) // divisor)-1)
        
        #Different Stats accumulated
        unfilPlayers = []
        temp = []
        temp2 = []
        attPass = []
        pct = []
        ydsPass = []
        tdPass = []
        pic = []
        sacks = []
        attRush = []
        ydsRush = []
        tdRush = []
        long = []
        twtyPls = []
        fl = []
        receptions = []
        fg = []
        fga = []
        u20 = []
        u30 = []
        u40 = []
        p50 = []
        xpt = []
        xpa = []
        tgt = []
        fumbleR = []
        fumbleF = []
        defTD = []
        sfty = []
        list1 = []
        spcTD = []
        g = []
        
        for i in range(0, numPlayers):
            if position == 'qb':
                spaces = i*16
                unfilPlayers.append(modified[17 + spaces])
                attPass.append(modified[18 + spaces])
                pct.append(modified[19 + spaces])
                ydsPass.append(modified[20 + spaces])
                tdPass.append(modified[22 + spaces])
                pic.append(modified[23 + spaces])
                sacks.append(modified[24 + spaces])
                attRush.append(modified[25 + spaces])
                ydsRush.append(modified[26 + spaces])
                tdRush.append(modified[27 + spaces])
                fl.append(modified[28 + spaces])
                g.append(modified[29 + spaces])
            
            if position == 'rb':
                spaces = i*16
                unfilPlayers.append(modified[17 + spaces])
                ydsRush.append(modified[18 + spaces])
                long.append(modified[20 + spaces])
                twtyPls.append(modified[21 + spaces])
                tdRush.append(modified[22 + spaces])
                receptions.append(modified[23 + spaces])
                tgt.append(modified[24 + spaces])
                ydsPass.append(modified[25 + spaces])
                tdPass.append(modified[27 + spaces])
                fl.append(modified[28 + spaces])
                g.append(modified[29 + spaces])
            
            if position == 'wr' or position == 'te':
                spaces = i*15
                unfilPlayers.append(modified[16 + spaces])
                tgt.append(modified[17 + spaces])
                ydsPass.append(modified[18 + spaces])
                long.append(modified[20 + spaces])
                twtyPls.append(modified[21 + spaces])
                tdPass.append(modified[22 + spaces])
                attRush.append(modified[23 + spaces])
                ydsRush.append(modified[24 + spaces])
                tdRush.append(modified[25 + spaces])
                fl.append(modified[26 + spaces])
                g.append(modified[27 + spaces])
            
            if position == 'k':
                spaces = i*15
                unfilPlayers.append(modified[15 + spaces])
                fga.append(modified[16 + spaces])
                pct.append(modified[17 + spaces])
                long.append(modified[18 + spaces])
                u20.append(modified[19 + spaces])
                u30.append(modified[20 + spaces])
                u40.append(modified[21 + spaces])
                p50.append(modified[22 + spaces])
                xpt.append(modified[23 + spaces])
                xpa.append(modified[24 + spaces])
                g.append(modified[25 + spaces])
                
            if position == 'dst':
                spaces = i*11
                unfilPlayers.append(modified[11 + spaces])
                
                string = unfilPlayers[i]
                arr = string.split()
                exists = '49ers' in arr
                
                if exists == True:
                    arr.remove('49ers')

                sent = ' '.join(arr)
                list1.append(sent)
                
                unfilPlayers = list1[:]
                
                pic.append(modified[12 + spaces])
                fumbleR.append(modified[13 + spaces])
                fumbleF.append(modified[14 + spaces])
                defTD.append(modified[15 + spaces])
                sfty.append(modified[16 + spaces])
                spcTD.append(modified[17 + spaces])
                g.append(modified[18 + spaces])
        
        for i in range(0, numPlayers):
            res = re.split('(\d+)', unfilPlayers[i])
            temp.extend(res)
            
        temp = [i for i in temp if i != '']
        
        rank = []
        ufilName = []
        name = []
        cmp = []
        for i in range(0, numPlayers):
            rank.append(temp[i*3])
            ufilName.append(temp[1 + i*3])
            cmp.append(temp[2+ i*3])
            if position == 'rb':
                attRush = cmp
            if position == 'wr' or position == 'te':
                receptions = cmp
            if position == 'k':
                fg = cmp
            if position == 'dst':
                sacks = cmp
        
        temp = []
        team = []
        for i in range(0, numPlayers):
            temp.append(ufilName[i].split())
            lastEl = len(temp[i])-1
            team.append(temp[i][lastEl])
            temp[i].remove(team[i])
            name.append(temp[i][:])
    
        filPlayers = []
        file = '{} {} stats.csv'.format(year, position)
        if position == 'qb':
            for i in range(0, numPlayers):
                filPlayers.append([year, position, rank[i], name[i], team[i], cmp[i], attPass[i], pct[i], ydsRush[i], tdPass[i], pic[i], sacks[i], attRush[i], ydsRush[i], tdRush[i], fl[i], g[i]])
                
        if position == 'rb':
            for i in range(0, numPlayers):
                filPlayers.append([year, position, rank[i], name[i], team[i], attRush[i], ydsRush[i], long[i], twtyPls[i], tdRush[i], receptions[i], tgt[i], ydsPass[i], tdPass[i], fl[i], g[i]])
                
        if position == 'wr':
            for i in range(0, numPlayers):
                filPlayers.append([year, position, rank[i], name[i], team[i], receptions[i], tgt[i], ydsPass[i], long[i], twtyPls[i], tdPass[i], attRush[i], ydsRush[i], tdRush[i], fl[i], g[i]])
                
        if position == 'te':
            for i in range(0, numPlayers):
                filPlayers.append([year, position, rank[i], name[i], team[i], receptions[i], tgt[i], ydsPass[i], long[i], twtyPls[i], tdPass[i], attRush[i], ydsRush[i], tdRush[i], fl[i], g[i]])
                
        if position == 'k':
            for i in range(0, numPlayers):
                filPlayers.append([year, position, rank[i], name[i], team[i], fg[i], fga[i], pct[i], long[i], u20[i], u30[i], u40[i], p50[i], xpt[i], xpa[i], g[i]])
                
        if position == 'dst':
            for i in range(0, numPlayers):
                filPlayers.append([year, position, rank[i], name[i], team[i], sacks[i], pic[i], fumbleR[i], fumbleF[i], defTD[i], sfty[i], spcTD[i], g[i]])

        return filPlayers

    def createFile(playerData):
        position = ['qb', 'rb', 'wr', 'te', 'k', 'dst']
        
        for pos in range(0, 6):
            file = 'C:\\Users\\Freew\\OneDrive\\Desktop\\Python Projects\\Fantasy Football\\annual_pos_data\\{} data.txt'.format(position[pos])
            with open(file, 'w') as file:
                for item in playerData[pos]:
                    file.write("%s\n" % item)
        
        #Raw Data
        with open('raw data.txt', 'w') as file:
            for item in playerData:
                file.write("%s\n" % item)
                
        print('Done')