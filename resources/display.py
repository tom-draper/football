# display.py - functions required to display the table to the command line
import datetime

class Display():
    def __init__(self):
        self.teamAlias = {'Wolverhampton Wanderers FC': 'Wolves',
                          'Tottenham Horspur FC': 'Spurs',
                          'Brighton & Hove Albion FC': 'Brighton',
                          'West Bromwich Albion FC': 'West Brom'}
        # Initials of teams that do not take their first three letters
        self.initials = {'West Bromwich Albion FC': 'WBA',
                         'Brighton & Hove Albion FC': 'BHA',
                         'West Ham United': 'WHU',
                         'Sheffield United': 'SHU',
                         'Manchester United': 'MUN',
                         'Aston Villa FC': 'AVL',
                         'Manchester City FC': 'MCI'}
                         
    
    # Get current premier league season date based on todays date
    def currentSeasonDate(self):
        now = datetime.datetime.now()
        if now.month >= 8:
            plDate = str(now.year) + '/' + str(now.year + 1)[2:]
        else:
            plDate = str(now.year - 1) + '/' + str(now.year)[2:]
            
        return plDate
        
    # Display table title
    def displayTitle(self):
        date = self.currentSeasonDate()
        print('Premier League Table ' + str(date))
    
    def shortenName(self, name):
        if name in self.teamAlias.keys():
            name = self.teamAlias[name]
        name = name.replace(' FC', '')
        name = name.replace(' AFC', '')
        return name

    def teamInitials(self, name):
        if name in self.initials.keys():
            name = self.initials[name]
        else:
            name = name[:3].upper()
        return name

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
        for team in teams:
            print('| ' + 
                  (str(team['position']) + '.').ljust(4, ' ') +
                  self.teamInitials(team['team']['name']).ljust(5, ' ') + 
                  '|  ' +
                  str(team['playedGames']).rjust(2, ' ') +
                  str(team['goalDifference']).rjust(6, ' ') +
                  '|'.rjust(4, ' ') + 
                  str(team['points']).rjust(4, ' ') +
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
        print('|' + (' ' * 13) + 'TEAM' + (' ' * 13) + '|   P   W   D   L  ' + '  GF   GA   GD   |   P  |')
        self.largeDivider()
        
        for team in teams:
            print('| ' + 
                  (str(team['position']) + '.').ljust(4, ' ') +
                  self.shortenName(team['team']['name']).ljust(25, ' ') + 
                  '|  ' +
                  str(team['playedGames']).rjust(2, ' ') +
                  str(team['won']).rjust(4, ' ') +
                  str(team['draw']).rjust(4, ' ') +
                  str(team['lost']).rjust(4, ' ') +
                  str(team['goalsFor']).rjust(6, ' ') +
                  str(team['goalsAgainst']).rjust(5, ' ') +
                  str(team['goalDifference']).rjust(5, ' ') +
                  '|'.rjust(4, ' ') + 
                  str(team['points']).rjust(4, ' ') +
                  '  |')
            
        self.largeDivider()
