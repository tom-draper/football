import requests
import json

class Extractor:
    def __init__(self):
        self.teamNames = []
        self.teams = {}
    
    def getXAuthToken(self):
        with open('resources/api_details.json', 'r') as f:
            data = f.read()
            obj = json.loads(data)
            return str(obj['x-auth-token'])
        print("Enter your X-Auth-Token from your football-data.org account into the api_details.json file.")
        return None

    """For possible endpoints visit: https://www.football-data.org/documentation/quickstart/
    """
    def requestWebpage(self, endpoint):
        url = "https://api.football-data.org/v2/"
        x_auth_token = self.getXAuthToken()
        headers = {'X-Auth-Token': x_auth_token}
        
        response = requests.get(url + endpoint, headers=headers)
        return json.loads(response.text)
    
    def writeJSON(self, data, filename):
        with open(filename, 'w') as f:
            json.dump(data, f, indent=4)
    
    def readJSON(self, filename):
        with open(filename) as f:
            data = json.load(f)
            return data
    
    def extractTableValues(self, refresh_data=True):
        endpoint = 'competitions/PL/standings'
        
        if refresh_data:
            json_data = self.requestWebpage(endpoint)
            standings = json_data['standings']
            for standing in standings:
                if standing['type'] == 'TOTAL':
                    standings = standing['table']
                    break
            self.writeJSON(json_data, 'data.json')
        else:
            json_data = self.readJSON('data.json')
            
        # Ensure standings sorted by position
        standings.sort(key=lambda x: x['position'])
            
        return standings