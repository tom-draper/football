import sys
from src.extractor import Extractor
from src.display import Display

# Extract and store premier league table data
e = Extractor()
teams = e.extract_standings() 

display = Display()
if 'compact'in sys.argv or 'c' in sys.argv:
    display.standings(teams, compact=True) # Display small premier league instead
else:
    display.standings(teams)