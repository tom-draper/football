# team.py - holds the data structures to represent a premier leagie team results

class Team():

    def __init__(self, name, position, played, won, drawn, lost, gf, ga, gd, points):
        self.data = {}
        self.buildDict(name, position, played, won, drawn, lost, gf, ga, gd, points)

    # Add teams premier league values to its dictionary
    def buildDict(self, name, position, played, won, drawn, lost, gf, ga, gd, points):
        self.data['name'] = name
        self.data['position'] = position
        self.data['played'] = played
        self.data['won'] = won
        self.data['lost'] = lost
        self.data['drawn'] = drawn
        self.data['gf'] = gf
        self.data['ga'] = ga
        self.data['gd'] = gd
        self.data['points'] = points
        