# premierLeagueTable.py - extracts current premier league table values from
# premier league website and displays to console in a table

import sys
from extractor import Extractor
from display import Display

# Extract and store premier league table data
tableEx = Extractor()
tableEx.extractTable() 
# Get extracted team data
teams = tableEx.teams;

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
