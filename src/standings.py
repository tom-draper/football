
class Table:
    def __init__(self):
        self.team_alias = {'Wolverhampton Wanderers FC': 'Wolves',
                           'Tottenham Horspur FC': 'Spurs',
                           'Brighton & Hove Albion FC': 'Brighton',
                           'West Bromwich Albion FC': 'West Brom'}
        self.initials = {'West Bromwich Albion FC': 'WBA',
                         'Brighton & Hove Albion FC': 'BHA',
                         'West Ham United FC': 'WHU',
                         'Sheffield United FC': 'SHU',
                         'Manchester United FC': 'MUN',
                         'Aston Villa FC': 'AVL',
                         'Manchester City FC': 'MCI'}

class CompactTable(Table):
    def __init__(self):
        Table.__init__(self)

    def _team_initials(self, name):
        if name in self.initials.keys():
            name = self.initials[name]
        else:
            name = name[:3].upper()
        return name

    @staticmethod
    def _display_table_divider():
        print(' ' + '—' * 33)
    
    @staticmethod
    def _display_column_headings():
        print(' │' + (' ' * 3) + 'TEAM' + (' ' * 3) + '|  Pl    GD   |   P  |')
    
    def _display_team_rows(self, teams):
        for team in teams:
            print(' │ ' +
                  (str(team['position'])).rjust(2, ' ') + '  ' +
                  self._team_initials(team['team']['name']).ljust(4, ' ') +
                  ' │  ' +
                  str(team['playedGames']).rjust(2, ' ') +
                  str(team['goalDifference']).rjust(6, ' ') +
                  ' │'.rjust(4, ' ') +
                  str(team['points']).rjust(4, ' ') +
                  '  │')

    def display(self, teams):
        self._display_table_divider()
        self._display_column_headings()
        self._display_table_divider()
        self._display_team_rows(teams)
        self._display_table_divider()


class StandardTable(Table):
    def __init__(self):
        Table.__init__(self)

    def _shorten_name(self, name):
        if name in self.team_alias.keys():
            name = self.team_alias[name]
        name = name.replace(' FC', '')
        name = name.replace(' AFC', '')
        return name

        
    @staticmethod
    def _display_table_divider():
        print(' ' + '—' * 73)
    
    @staticmethod
    def _display_column_headings():
        print(' |' + (' ' * 12) + 'TEAM' + (' ' * 12) +
              '|   P   W   D   L    GF   GA   GD   |   P  |')
    
    def _display_team_rows(self, teams: list):
        for team in teams:
            print(' │  ' +
                  (str(team['position'])).rjust(2, ' ') + '  ' +
                  self._shorten_name(team['team']['name']).ljust(22, ' ') +
                  '│  ' +
                  str(team['playedGames']).rjust(2, ' ') +
                  str(team['won']).rjust(4, ' ') +
                  str(team['draw']).rjust(4, ' ') +
                  str(team['lost']).rjust(4, ' ') +
                  str(team['goalsFor']).rjust(6, ' ') +
                  str(team['goalsAgainst']).rjust(5, ' ') +
                  str(team['goalDifference']).rjust(5, ' ') +
                  '│'.rjust(4, ' ') +
                  str(team['points']).rjust(4, ' ') +
                  '  │') 

    def display(self, teams):
        self._display_table_divider()
        self._display_column_headings()
        self._display_table_divider()
        self._display_team_rows(teams)
        self._display_table_divider()
