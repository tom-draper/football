import requests
import re

class WebpageValues:

    teamMatches = []
    tableValueMatches = []

    def requestWebpage(self):
        print('Requesting webpage')

        res = requests.get('https://www.premierleague.com/tables')
        try:
            res.raise_for_status()
            res.status_code == requests.codes.ok
        except Exception as ex:
            print('There was a problem: %s' % (ex))

        return res.text

    def getTable(self):
        webpage = self.requestWebpage() # Get premier league table webpage html

        print(webpage[48000:100000])

        teamRegex = re.compile(r'''(/clubs/\d+/([A-Za-z-]+)/overview)''', re.VERBOSE)

        tableValueRegex = re.compile(r'''
        (<td>([-+]?\d+)</td>)|                # Played,, won, drawn, lost
        ([ ]*<td class="hideSmall">(\d+)</td>)|   # GF, GA              
        ([ ]*<td class="points">(\d+)</td>)       # Points
        ''')

        # Fill list with unique instances of teams found
        for groups in teamRegex.findall(webpage):
            team = groups[1] # Extract team name
            if team not in self.teamMatches:
                print(team)
                self.teamMatches.append(team) # Add new team to list

        # Fill list with each table value found
        for groups in tableValueRegex.findall(webpage):
            tableValue = groups[1]
            print(groups[0])
            print(groups)
            self.tableValueMatches.append(int(tableValue)) # Add to list

        # Print result
        print(self.teamMatches)
        #print(self.tableValueMatches[:160])

        for i in range(4, 161, 4):
            print(self.tableValueMatches[i-4:i])