class Team():
    
    def __init(self, number, teams, mainValues, goalValues):
        self.name = teams[number]
        self.stats = {'played': 0,'won': 0,'drawn': 0,'lost': 0,'gf': 0,'ga': 0,'gd': 0,'points': 0}

        buildDict(number, mainValues, goalValues)

    #def buildDict(self, number, mainValues, goalValues):
        
        

