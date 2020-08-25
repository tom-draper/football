# premier_league_table.py - extracts current premier league table values from
# premier league website and displays to console in a table
import sys
from extractor import Extractor
from display import Display

# Extract and store premier league table data
e = Extractor()
teams = e.extractTableValues() 

display = Display()
if 'small'in sys.argv or 's' in sys.argv:
    display.displaySmallTable(teams) # Display small premier league instead
else:
    display.displayLargeTable(teams)
    
input("Press enter to exit")
