class Team():
    
    def __init(self, name):
        self.name = name
        self.stats = {'played': 0,'won': 0,'drawn': 0,'lost': 0,'gf': 0,'ga': 0,'gd': 0,'points': 0}

    def buildTeam(self, first, goals):
        # hello
        self.stats['played'] = 0

