from table_extractor import TableExtractor
from team import Team
from display import Display

te = TableExtractor()
# Request PL website html and extract teams and table values and
#  store 
# in lists for teams, main values (played, win, drawn, loss) and goal values
# (GF and GA)
te.extractTable() 

teams = te.teamsMatches # List of extracted 20 PL teams
mainValues = te.mainValuesMatches # List of all played, won, drawn, lost data 
                                  # values in order
goalValues = te.goalValuesMatches # List of all GF and GA data values in order

# Build teams with stats data from extracted table
teams = {}
for position in range(0, 20): # 20 different teams
    teams["team{0}".format(position)] = Team(position, te.teamsMatches, te.mainValuesMatches, te.goalValuesMatches)

display = Display()
# Display premier league table
display.displayTable(teams)

input("Press enter to exit")
