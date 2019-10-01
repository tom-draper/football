# premier_league_table.py - extracts current premier league table values from
# premier league website and displays to console in a table

import sys
from table_extractor import TableExtractor
from display import Display

# Extract and store premier league table data
tableEx = TableExtractor()
tableEx.extractTable() 

# Build 20 teams with stats data from extracted table
teams = {}
for n in range(len(tableEx.teamNames)):
    # Make a new team from tableEx lists with abreviated team name as key
    teams[tableEx.teamNames[n][1]] = {'name': tableEx.teamNames[n][0], 
                                      'position': tableEx.positions[n], 
                                      'played': tableEx.played[n], 
                                      'won': tableEx.wins[n], 
                                      'lost': tableEx.losses[n], 
                                      'drawn': tableEx.draws[n], 
                                      'gf': tableEx.gf[n], 
                                      'ga': tableEx.ga[n], 
                                      'gd': tableEx.gd[n], 
                                      'points': tableEx.points[n]}

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
