# display.py - display teams values in formatted table

class Display():

    def smallDivider(self):
        print('-' * 53)
        
    # Display team played, goal difference and points in a table
    def displaySmallTable(self, teams):
        print('Premier League Table')
        self.smallDivider()
        print('|' + (' ' * 13) + 'TEAM' + (' ' * 13) + '|   P    GD   |   P  |')
        self.smallDivider()
        for team in teams.keys():
            print('| ' + (str(teams[team].stats['position']) + '.').ljust(4, ' ') +
                  team.ljust(25, ' ') + '|  ' +
                  str(teams[team].stats['played']).rjust(2, ' ') +
                  str(teams[team].stats['gd']).rjust(6, ' ') +
                  '|'.rjust(4, ' ') + 
                  str(teams[team].stats['points']).rjust(4, ' ') +
                  '  |')
        self.smallDivider()
        
    def bigDivider(self):
        print('-' * 75)

    # Display full team data in form of a table
    def displayBigTable(self, teams):
        print('Premier League Table')
        self.bigDivider()
        print('|' + (' ' * 13) + 'TEAM' + (' ' * 13) + '|   P   W   D   L  ' + 
              '  GF   GA   GD   |   P  |')
        self.bigDivider()
        for team in teams.keys():
            print('| ' + (str(teams[team].stats['position']) + '.').ljust(4, ' ') +
                  team.ljust(25, ' ') + '|  ' +
                  str(teams[team].stats['played']).rjust(2, ' ') +
                  str(teams[team].stats['won']).rjust(4, ' ') +
                  str(teams[team].stats['drawn']).rjust(4, ' ') +
                  str(teams[team].stats['lost']).rjust(4, ' ') +
                  str(teams[team].stats['gf']).rjust(6, ' ') +
                  str(teams[team].stats['ga']).rjust(5, ' ') +
                  str(teams[team].stats['gd']).rjust(5, ' ') +
                  '|'.rjust(4, ' ') + 
                  str(teams[team].stats['points']).rjust(4, ' ') +
                  '  |')
        self.bigDivider()
