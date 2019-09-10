import requests
import re

class WebpageValues:

    teamMatches = []
    mainTableValueMatches = []
    goalsTableValueMatches = []

    def displayTeams(self):
        for team in self.teamMatches:
            print(team)

    def displayMainValues(self):
        print('\nPlayed Won Drawn Lost')
        for i in range(4, 81, 4):
            print(self.mainTableValueMatches[i-4:i])

    def displayGoals(self):
        print('\n GF  GA')
        for i in range(2, 41, 2):
            print(self.goalsTableValueMatches[i-2:i])

    def requestWebpage(self):
        print('Requesting webpage...')

        res = requests.get('https://www.premierleague.com/tables')
        try:
            res.raise_for_status()
            res.status_code == requests.codes.ok
        except Exception as ex:
            print('There was a problem: %s' % (ex))

        return res.text

    def getTable(self):
        webpage = self.requestWebpage() # Get premier league table webpage html

        teamRegex = re.compile(r'''(/clubs/\d+/([A-Za-z-]+)/overview)''', re.VERBOSE)

        mainTableValueRegex = re.compile(r'''(<td>(\d+)</td>)''')                          # Played,, won, drawn, lost
        goalsTableValueRegex = re.compile(r'''([ ]*<td class="hideSmall">(\d+)</td>)''')    # GF, GA              

        # Fill list with unique instances of teams found
        for groups in teamRegex.findall(webpage):
            team = groups[1] # Extract team name
            if team not in self.teamMatches:
                self.teamMatches.append(team) # Add new team to list
        self.teamMatches = self.teamMatches[:20]

        # Fill list with each table value found
        for groups in mainTableValueRegex.findall(webpage):
            tableValue = groups[1]
            self.mainTableValueMatches.append(int(tableValue)) # Add to list
        self.mainTableValueMatches = self.mainTableValueMatches[:80] # Only first 80 relevant
        
        # Fill list with each goal value found
        for groups in goalsTableValueRegex.findall(webpage):
            tableValue = groups[1]
            self.goalsTableValueMatches.append(int(tableValue)) # Add to list
        #self.mainTableValueMatches = self.mainTableValueMatches[:40] # Only first 40 relevant

    
    