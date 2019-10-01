# premier_league_table.py - extracts current premier league table values from
# premier league website and displays to console in a table

import sys
from table_extractor import TableExtractor
from team import Team
from display import Display

# Extract and store premier league table data
tableEx = TableExtractor()
tableEx.extractTable() 

# Build 20 teams with stats data from extracted table
teams = {}
for n in range(len(tableEx.teamNames)):
    # Make a new team from tableEx lists with abreviated team name as key
    teams[tableEx.teamNames[n][1]] = Team(tableEx.teamNames[n][0],
                                          tableEx.positions[n],
                                          tableEx.played[n], 
                                          tableEx.wins[n], 
                                          tableEx.draws[n], 
                                          tableEx.losses[n], 
                                          tableEx.gf[n], 
                                          tableEx.ga[n], 
                                          tableEx.gd[n], 
                                          tableEx.points[n])

# Display large table is default
displaySmall = False
# Get command line arguemnts
if len(sys.argv) > 1:
    for i in range(1, len(sys.argv)):
        if sys.argv[i].lower() == 'small' or sys.argv[i].lower() == 's':
            displaySmall = True # Display small premier league instead

# Display premier league table
display = Display()
if displaySmall:
    display.displaySmallTable(teams)
else:
    display.displayLargeTable(teams)

input("Press enter to exit")
