# team.py - holds the data structures to represent a premier leagie team results

class Team():

    def __init__(self, name, position, played, won, drawn, lost, gf, ga, gd, points):
        self.data = {'name': name, 'position': position, 'played': played,
                     'won': won, 'lost': lost, 'drawn': drawn,
                     'gf': gf, 'ga': ga, 'gd': gd, 'points': points}
        