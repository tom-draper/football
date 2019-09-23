class Team():

    def __init__(self, played, won, drawn, lost, gf, ga, gd, points):
        self.stats = {}

        self.buildDict(played, won, drawn, lost, gf, ga, gd, points)

    def buildDict(self, played, won, drawn, lost, gf, ga, gd, points):
        self.stats['played'] = played
        self.stats['won'] = won
        self.stats['lost'] = lost
        self.stats['drawn'] = drawn
        self.stats['gf'] = gf
        self.stats['ga'] = ga
        self.stats['gd'] = gd
        self.stats['points'] = points
        