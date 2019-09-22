class Display():

    def divider(self):
        print("-------------------------------------------------------------------")

    def displayTable(self, teams):
        print('Premier League Table\n')
        self.divider()
        print("|          TEAM            |   P   W   D   L    GF  GA  GD     P  |")
        for key in teams.keys():
            self.divider()
            print('| ' +
                teams[key].name + 
                (25 - len(teams[key].name)) * ' ' + 
                '| ' + (3 - len(str(teams[key].stats['played']))) * ' ' +
                str(teams[key].stats['played']) +
                ' ' + (3 - len(str(teams[key].stats['won']))) * ' ' +
                str(teams[key].stats['won']) +
                ' ' + (3 - len(str(teams[key].stats['drawn']))) * ' ' +
                str(teams[key].stats['drawn']) +
                ' ' + (3 - len(str(teams[key].stats['lost']))) * ' ' +
                str(teams[key].stats['lost']) +
                3 * ' ' + (3 - len(str(teams[key].stats['gf']))) * ' ' +
                str(teams[key].stats['gf']) +
                ' ' + (3 - len(str(teams[key].stats['ga']))) * ' ' +
                str(teams[key].stats['ga']) +
                ' ' + (3 - len(str(teams[key].stats['gd']))) * ' ' +
                str(teams[key].stats['gd']) +
                3 * ' ' + (3 - len(str(teams[key].stats['points']))) * ' ' +
                str(teams[key].stats['points']) +
                '  |')
        self.divider()
