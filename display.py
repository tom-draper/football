from standings import StandardTable, CompactTable

class Display:
    def standings(self, teams: list, compact=False):
        if compact:
            standings = CompactTable()
        else:
            standings = StandardTable()
        
        standings.display(teams)