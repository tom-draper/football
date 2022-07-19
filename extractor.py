import requests
import json
from dotenv import load_dotenv
import os

class Extractor:
    def __init__(self):
        self.team_names = []
        self.teams = {}
    
    def _load_x_auth_token(self) -> str|None:
        load_dotenv()
        x_auth_token = os.getenv('X_AUTH_TOKEN')
        if x_auth_token is None:
            raise ValueError("X_AUTH_TOKEN variable not found. Please create an account with football-data.org and copy your personal X-Auth token into the .env file.")
        return x_auth_token

    def _request_webpage(self, endpoint: str) -> dict:
        url = "https://api.football-data.org/v2/"
        x_auth_token = self._load_x_auth_token()
        headers = {'X-Auth-Token': x_auth_token}
        
        response = requests.get(url + endpoint, headers=headers)
        return json.loads(response.text)
    
    def _write_json(self, data, filename):
        with open(filename, 'w') as f:
            json.dump(data, f, indent=4)
    
    def _read_json(self, filename):
        with open(filename) as f:
            data = json.load(f)
            return data
        
    def _extract_standings_from_json(self, json_data: dict) -> dict|None:
        try:
            standings = json_data['standings']
            for standing in standings:
                if standing['type'] == 'TOTAL':
                    standings = standing['table']
                    break
            return standings
        except KeyError:
            return None  # Standings could not be extracted - usually API key error
    
    def extract_standings(self, refresh_data=True) -> list:
        if refresh_data:
            
            json_data = self._request_webpage('competitions/PL/standings')
            standings = self._extract_standings_from_json(json_data)
            if standings is None:
                # Retry with saved data file
                json_data = self._read_json('standings.json')
                standings = self._extract_standings_from_json(json_data)
            self._write_json(json_data, 'standings.json')
        else:
            json_data = self._read_json('standings.json')
                        
        # Ensure standings sorted by position
        standings.sort(key=lambda x: x['position'])
            
        return standings