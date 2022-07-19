# premier_league_table.py - extracts current premier league table values from
# premier league website and displays to console in a table
import sys
from extractor import Extractor
from display import Display

# Extract and store premier league table data
e = Extractor()
teams = e.extract_standings() 

display = Display()
if 'compact'in sys.argv or 'c' in sys.argv:
    display.display_standings(teams, compact=True) # Display small premier league instead
else:
    display.display_standings(teams)