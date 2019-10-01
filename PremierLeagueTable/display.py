# display.py - display teams values in formatted table

import datetime

class Display():
    
    # Get current premier league season date based on todays date
    def getPLDate(self):
        now = datetime.datetime.now()
        if now.month >= 8:
            plDate = str(now.year) + '/' + str(now.year + 1)[2:]
        else:
            plDate = str(now.year - 1) + '/' + str(now.year)[2:]
            
        return plDate
        
    # Display table title
    def displayTitle(self):
        plDate = self.getPLDate()
        print('Premier League Table ' + str(plDate))

    # Display small used by small table 
    def smallDivider(self):
        print('-' * 33)
        
    # Display team played, goal difference and points in a table
    def displaySmallTable(self, teams):
        self.displayTitle()
        # Print table
        self.smallDivider()
        print('|' + (' ' * 3) + 'TEAM' + (' ' * 3) + '|   P    GD   |   P  |')
        self.smallDivider()
        for team in teams.keys():
            print('| ' + (str(teams[team]['position']) + '.').ljust(4, ' ') +
                  team.ljust(5, ' ') + '|  ' +
                  str(teams[team]['played']).rjust(2, ' ') +
                  str(teams[team]['gd']).rjust(6, ' ') +
                  '|'.rjust(4, ' ') + 
                  str(teams[team]['points']).rjust(4, ' ') +
                  '  |')
        self.smallDivider()
        
    # Display large divider used by large table
    def largeDivider(self):
        print('-' * 75)

    # Display full team data in form of a table
    def displayLargeTable(self, teams):
        self.displayTitle()
        # Print table
        self.largeDivider()
        print('|' + (' ' * 13) + 'TEAM' + (' ' * 13) + '|   P   W   D   L  ' + 
              '  GF   GA   GD   |   P  |')
        self.largeDivider()
        for teamData in teams.values():
            print('| ' + (str(teamData['position']) + '.').ljust(4, ' ') +
                  teamData['name'].ljust(25, ' ') + '|  ' +
                  str(teamData['played']).rjust(2, ' ') +
                  str(teamData['won']).rjust(4, ' ') +
                  str(teamData['drawn']).rjust(4, ' ') +
                  str(teamData['lost']).rjust(4, ' ') +
                  str(teamData['gf']).rjust(6, ' ') +
                  str(teamData['ga']).rjust(5, ' ') +
                  str(teamData['gd']).rjust(5, ' ') +
                  '|'.rjust(4, ' ') + 
                  str(teamData['points']).rjust(4, ' ') +
                  '  |')
        self.largeDivider()
