class Team():

    def __init__(self, number, teams, mainValues, goalValues):
        self.name = teams[number]
        self.stats = {'played': 0,'won': 0,'drawn': 0,'lost': 0,'gf': 0,'ga': 0,'gd': 0,'points': 0}

        self.buildDict(number, mainValues, goalValues)

    def buildDict(self, number, mainValues, goalValues):
        # Inset main values
        pointer = number * 4
        self.stats['played'] = mainValues[pointer]
        pointer += 1
        self.stats['won'] = mainValues[pointer]    
        pointer += 1
        self.stats['drawn'] = mainValues[pointer]  
        pointer += 1
        self.stats['lost'] = mainValues[pointer]

        # Insert goal values
        pointer = number * 2
        self.stats['gf'] = goalValues[pointer]
        pointer += 1
        self.stats['ga'] = goalValues[pointer]
        
        self.stats['gd'] = self.stats['gf'] - self.stats['ga'] # Calc goal difference
        self.stats['points'] = 3 * self.stats['won'] + 1 * self.stats['drawn'] # Calc points