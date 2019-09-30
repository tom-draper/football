# team.py - holds the data structures to represent a premier leagie team results

class Team():

    def __init__(self, position, played, won, drawn, lost, gf, ga, gd, points):
        self.stats = {}
        self.buildDict(position, played, won, drawn, lost, gf, ga, gd, points)

    # Add teams premier league values to its dictionary
    def buildDict(self, position, played, won, drawn, lost, gf, ga, gd, points):
        self.stats['position'] = position
        self.stats['played'] = played
        self.stats['won'] = won
        self.stats['lost'] = lost
        self.stats['drawn'] = drawn
        self.stats['gf'] = gf
        self.stats['ga'] = ga
        self.stats['gd'] = gd
        self.stats['points'] = points
        