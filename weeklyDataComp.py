from bs4 import BeautifulSoup as bs
from equation_sheet import equations as eq
import requests, re, json

class weeklyFantasyData:
    def weeklyDataScraper(URL, position, year, week):
        data = requests.get(URL).text
        soup = bs(data, 'html.parser')
        
        #find elements
        #text_table = soup.find('table').get_text()
        
        data = []
        table = soup.find('table')
        table_body = table.find('tbody')

        rows = table_body.find_all('tr')
        for row in rows:
            cols = row.find_all('td')
            cols = [ele.text.strip() for ele in cols]
            data.append([ele for ele in cols if ele]) # Get rid of empty values
        
        file = 'C:\\Users\\Freew\\OneDrive\\Desktop\\Python Projects\\Fantasy Football\\weekly_raw\\{} {} {} stats.json'.format(year, week, position)
        eq.writeEq(file, data)
        return data
    
    def tablePosition(position, year, week):
        URL = 'https://www.fantasypros.com/nfl/stats/{}.php?year={}&week={}&range=week'.format(position, year, week)
        return URL
    
    def formatData(table, position, year, week):
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
            filPlayers = []
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
                
                filPlayers.append([year, week, position, rank, name, team, cmpPass, attPass, ydsPass, tdPass, pic, sacks, attRush, ydsRush, tdRush, fl])
        
        if position == 'rb':
            filPlayers = []
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
        
                filPlayers.append([year, week, position, rank, name, team, attRush, ydsRush, long, twtyPls, tdRush, rec, tgt, ydsPass, tdPass, fl])
        
        if position == 'wr' or position == 'te':
            filPlayers = []
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
        
                filPlayers.append([year, week, position, rank, name, team, rec, tgt, ydsPass, long, twtyPls, tdPass, attRush, ydsRush, tdRush, fl])
        
        if position == 'k':
            filPlayers = []
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

                filPlayers.append([year, week, position, rank, name, team, fg, fga, long, u20, u30, u40, u50, p50, xpt, xpa])
                
        if position == 'dst':
            filPlayers = []
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

                filPlayers.append([year, week, position, rank, name, team, sacks, pic, fr, ff, defTD, sfty, spcTD])
        
        file = 'raw_week_data.json'
        eq.writeEq(file, filPlayers)
        
        return filPlayers