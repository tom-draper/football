from webpage_values import WebpageValues
from team import Team
from display import Display

wv = WebpageValues()
# Request PL website html and extract teams and table values into lists
wv.extractTable() 

teams = wv.teamsMatches # List of 20 PL teams
mainValues = wv.mainValuesMatches # List of all played, won, drawn, lost values 
                                  # in correct order
goalValues = wv.goalValuesMatches # List of all GF and GA values in correct order

teams = {}
for i in range(0, 20): # 20 different teams
    teams["team{0}".format(i)] = Team(i, wv.teamsMatches, wv.mainValuesMatches, wv.goalValuesMatches)

display = Display()
display.displayTable(teams)
