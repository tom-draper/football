from table_extractor import TableExtractor
from team import Team
from display import Display

tableEx = TableExtractor()
tableEx.extractTable() 

# Build teams with stats data from extracted table
teams = {}
for position in range(len(tableEx.teams)): # 20 different teams
    teams[tableEx.teams[position]] = Team(tableEx.played[position], 
                                          tableEx.wins[position], 
                                          tableEx.draws[position], 
                                          tableEx.losses[position], 
                                          tableEx.gf[position], 
                                          tableEx.ga[position], 
                                          tableEx.gd[position], 
                                          tableEx.points[position])

display = Display()
# Display premier league table
display.displayTable(teams)

input("Press enter to exit")
