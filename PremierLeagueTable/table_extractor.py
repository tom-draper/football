# table_extractor.py - scraps premier league table website and locates table
# row values. Values are sorted into speficic list for display.
#
# Note: I found both html 'table' and 'tbody' attribute only enclosed the top 
# row when returned with beautiful soup but not when inspecting through web 
# browser. As a result, all table row attributes on the webpage are retrieved 
# from full website and only the first twenty are used.

import requests
from bs4 import BeautifulSoup

class TableExtractor:

    def __init__(self):
        self.teams = []
        self.played = []
        self.wins = []
        self.draws = []
        self.losses = []
        self.gf = []
        self.ga = []
        self.gd = []
        self.points = []
    
    # Sort all values list into separate ordered lists
    def sortValues(self, values):
        for i in range(0, len(values), 8):
            self.played.append(values[i])
            self.wins.append(values[i + 1])
            self.draws.append(values[i + 2])
            self.losses.append(values[i + 3])
            self.gd.append(values[i + 4])
            self.gf.append(values[i + 5])
            self.ga.append(values[i + 6])
            self.points.append(values[i + 7])

    # Requests premier 
    def requestPLWebpage(self):
        print('Requesting webpage...')

        res = requests.get('https://www.premierleague.com/tables')
        try:
            res.raise_for_status()
            res.status_code == requests.codes.ok
        except Exception as ex:
            print('There was a problem: %s' % (ex))

        return res.text

    # Extract premier league table values and sort into lists
    def extractTable(self):
        webpage = self.requestPLWebpage() # Get premier league table webpage html
        soup = BeautifulSoup(webpage, 'html.parser')
        
        # Write to html debug file
        fileObj = open('debug.html', 'w')
        fileObj.write(str(soup.prettify))
        
        # Get html table rows of for each team in premier league table 
        # Top team tableDark, next 3 tableMid, 5th tableLight, last 3 tableMid, rest empty
        tableRows = soup.find_all('tr', {'class': ['tableDark', 'tableMid', 'tableLight', '']})
        
        values = []
        for row in tableRows[:20]: # Only first twenty
            # Add team name to main teams list
            self.teams += row.find('td', {'class': 'team'}).find('a').find('span', {'class', 'long'})
            
            # Add html table data line for played, wins, draws, losses and goal difference
            temp = row.find_all('td', {'class': None})
            # Add html table data line for goals for and goals against
            temp += row.find_all('td', {'class': 'hideSmall'})
            # Add html table data line for points
            temp += row.find_all('td', {'class': 'points'})
            # Add raw data values to list
            for line in temp:
                values.append(line.get_text().strip())
                
        self.sortValues(values)