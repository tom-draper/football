class Display():

    def divider(self):
        print("-----------------------------------------------------------------------")

    def displayTable(self, teams):
        print('Premier League Table\n')
        self.divider()
        print("|          TEAM            |   P   W   D   L    GF   GA   GD   |   P  |")
        for team in teams.keys():
            self.divider()
            print('| ' + team.ljust(25, ' ') + '|  ' +
                  teams[team].stats['played'].rjust(2, ' ') +
                  teams[team].stats['won'].rjust(4, ' ') +
                  teams[team].stats['drawn'].rjust(4, ' ') +
                  teams[team].stats['lost'].rjust(4, ' ') +
                  teams[team].stats['gf'].rjust(6, ' ') +
                  teams[team].stats['ga'].rjust(5, ' ') +
                  teams[team].stats['gd'].rjust(5, ' ') +
                  '|'.rjust(4, ' ') + 
                  teams[team].stats['points'].rjust(4, ' ') +
                  '  |')
        self.divider()
