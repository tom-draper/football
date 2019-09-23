# premier_league_table.py - extracts current premier league table values from
# premier league website and displays to console in a table

import sys
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

# Display large table is default
displaySmall = False
# Get arguemnts
if len(sys.argv) > 1:
    for i in range(1, len(sys.argv)):
        if sys.argv[i].lower() == 'small' or sys.argv[i].lower() == 's':
            displaySmall = True

# Display premier league table
display = Display()
if displaySmall:
    display.displaySmallTable(teams)
else:
    display.displayBigTable(teams)

input("Press enter to exit")
