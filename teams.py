from data import Data
import requests

class Teams(Data):
    def __init__(self):
        pass
    
    def get_all_teams(self) -> None: 
        res = requests.get("https://www.balldontlie.io/api/v1/teams")

        if res.ok:
            teams = res.json()['data']
            
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

        else:
            self.handle_error(res.status_code)



    def team_stats(self):
        pass