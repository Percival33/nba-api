from data import Data
import requests

class Teams(Data):
    def __init__(self):
        pass
    

    def get_all_teams(self) -> None: 
        payload = {
            'per_page' : 30
        }

        teams = self.get_all_data("https://www.balldontlie.io/api/v1/teams", payload)
        
        divisions = dict()

        for team in teams:
            if not team['division'] in divisions:
                divisions[team['division']] = []

            divisions[team['division']].append({
                'full_name' : team['full_name'],
                'abbreviation' : team['abbreviation']
            })

        for div in divisions:
            print(div)
            for team in divisions[div]:
                print(f'\t{team["full_name"]} ({team["abbreviation"]})')


    def team_stats(self):
        pass