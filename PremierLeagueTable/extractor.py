# extractor.py - scrapes premier league table website and locates table
# row values. Values are sorted into speficic list for display.
#
# Note: I found both html 'table' and 'tbody' attribute only enclosed the top 
# row when returned with beautiful soup but not when inspecting through web 
# browser. As a result, all table row attributes on the webpage are retrieved 
# from full website and only the first twenty are used.

import requests
from bs4 import BeautifulSoup

class Extractor:

    def __init__(self):
        self.teamNames = []
        self.teams = {}
        
    # Requests and returns html from a webpage 
    def requestWebpage(self, url):
        print('Requesting webpage...')

        res = requests.get(url)
        try:
            res.raise_for_status()
            res.status_code == requests.codes.ok
        except Exception as ex:
            print('There was a problem: %s' % (ex))

        return res.text
        
    # Sort all extracted table values list into separate ordered lists
    def sortTableValues(self, values):
        for idx in range(0, len(self.teamNames)):
            i = idx * 9; # Get index in values list current team data begins
            self.teams[self.teamNames[idx][1]] = {'name': self.teamNames[idx][0], 
                                                  'position': values[i], 
                                                  'played': values[i + 1], 
                                                  'won': values[i + 2], 
                                                  'lost': values[i + 3], 
                                                  'drawn': values[i + 4], 
                                                  'gf': values[i + 5], 
                                                  'ga': values[i + 6], 
                                                  'gd': values[i + 7], 
                                                  'points': values[i + 8]}

    # Extract premier league table values and sort into lists
    def extractTable(self):
        webpage = self.requestWebpage('https://www.premierleague.com/tables') # Get premier league table webpage html
        soup = BeautifulSoup(webpage, 'html.parser')
        
        # Get html table rows of for each team in premier league table 
        # Top team tableDark, next 3 tableMid, 5th tableLight, last 3 tableMid, rest empty
        tableRows = soup.find_all('tr', {'class': ['tableDark', 'tableMid', 'tableLight', '']})
        
        tableValues = []
        for row in tableRows[:20]: # Only first twenty rows
            # Add team name to main teams list
            teamLong = row.find('td', {'class': 'team'}).find('a').find('span', {'class', 'long'}).get_text()
            teamShort = row.find('td', {'class': 'team'}).find('span', {'class': 'short'}).get_text()
            # Save team name with abreviated version to list
            self.teamNames.append(tuple([teamLong, teamShort]))
            
            # Collect the html lines for the team's table values
            lines = []
            # Record the html containing team's position
            lines.append(row.find('td', {'id': 'Tooltip'}).find('span', {'class': 'value'}))
            # Add html table data line for played, wins, draws, losses and goal difference
            lines += row.find_all('td', {'class': None})
            # Add html table data line for goals for and goals against
            lines += row.find_all('td', {'class': 'hideSmall'})
            # Add html table data line for points
            lines += row.find_all('td', {'class': 'points'})
            # Extract raw data values and add to list
            for line in lines:
                tableValues.append(int(line.get_text().strip()))
                
        self.sortTableValues(tableValues)
        
        