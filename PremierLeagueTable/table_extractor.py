import requests
import re

class TableExtractor:

    teamsMatches = []
    mainValuesMatches = []
    goalValuesMatches = []

    def displayTeams(self):
        for team in self.teamsMatches:
            print(team)

    def displayMainValues(self):
        print('\n P  W  D  L')
        for i in range(4, len(self.mainValuesMatches) + 1, 4):
            print(self.mainValuesMatches[i-4:i])

    def displayGoals(self):
        print('\n GF GA')
        for i in range(2, len(self.goalValuesMatches) + 1, 2):
            print(self.goalValuesMatches[i-2:i])

    def requestWebpage(self):
        print('Requesting webpage...')

        res = requests.get('https://www.premierleague.com/tables')
        try:
            res.raise_for_status()
            res.status_code == requests.codes.ok
        except Exception as ex:
            print('There was a problem: %s' % (ex))

        return res.text

    def extractTable(self):
        webpage = self.requestWebpage() # Get premier league table webpage html

        teamRegex = re.compile(r'''(/clubs/\d+/([A-Za-z-]+)/overview)''')
        mainValuesRegex = re.compile(r'''(<td>(\d+)</td>)''')                          # Played,, won, drawn, lost
        goalValuesRegex = re.compile(r'''([ ]*<td class="hideSmall">(\d+)</td>)''')    # GF, GA              

        # Fill list with unique instances of teams found
        for groups in teamRegex.findall(webpage):
            team = groups[1].replace("-", " ") # Extract team name
            if team not in self.teamsMatches:
                self.teamsMatches.append(team) # Add new team to list
        self.teamsMatches = self.teamsMatches[:20]

        # Fill list with each table value found
        for groups in mainValuesRegex.findall(webpage):
            tableValue = groups[1]
            self.mainValuesMatches.append(int(tableValue)) # Add to list
        self.mainValuesMatches = self.mainValuesMatches[:80] # Only first 80 relevant
        
        # Fill list with each goal value found
        for groups in goalValuesRegex.findall(webpage):
            tableValue = groups[1]
            self.goalValuesMatches.append(int(tableValue)) # Add to list
        self.goalValuesMatches = self.goalValuesMatches[:40] # Only first 40 relevant

    
    