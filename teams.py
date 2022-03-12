from data import Data
from typing import List

class Teams(Data):
    def __init__(self) -> None:
        pass
    

    def get_all_teams(self) -> None:
        """
            Function prints all teams grouped by divisions.

            Parameters
            ----------
            None

            Returns
            -------
            None
        """
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
                print(f'\t{team["full_name"]} ({team["abbreviation"]})'.expandtabs(4))


    def add_team_result(self, team_data: dict, result: dict) -> dict:
        """
            Function updates and returns team_data acordingly to result of a game.


            Parameters
            ----------
                team_data: dict
                    dict representing team and their results
                
                result: dict
                    dict representing result of one game

            Returns
            -------
                team_data: dict
                    Updated dict representing team and their results
        """

        if 'team_name' not in team_data:
            team_data['team_name'] = result['team_name']

            team_data['won_games_as_home_team'] = 0
            team_data['won_games_as_visitor_team'] = 0
            team_data['lost_games_as_home_team'] = 0
            team_data['lost_games_as_visitor_team'] = 0


        if result['home']:
            if result['won']:
                team_data['won_games_as_home_team'] += 1
            else:
                team_data['lost_games_as_home_team'] += 1
        
        else:
            if result['won']:
                team_data['won_games_as_visitor_team'] += 1
            else:
                team_data['lost_games_as_visitor_team'] += 1

        return team_data


    def parse_games(self, data: List[dict]) -> List[dict]:
        """
            Function parses season data and returns list of dicts, where dict is result of specific team.

            len(teams_stats) = 30 as there are currently 30 NBA teams

            Parameters
            ----------
                data: List[dict]
                    List of dict where each dict represent one game

            Returns
            -------
                teams_stats: List[dict]
                    List of dict where each dict represent one team
        """
        teams_stats = [dict() for i in range(31)]

        for game in data:
            home_team_data = {
                'home': True,
                'team_id': game['home_team']['id'],
                'team_name': (f'{game["home_team"]["full_name"]}' 
                f' ({game["home_team"]["abbreviation"]})'),
                'won': game['home_team_score'] > game['visitor_team_score']
            }

            visitor_team_data = {
                'home': False,
                'team_id': game['visitor_team']['id'],
                'team_name': (f'{game["visitor_team"]["full_name"]}' 
                f' ({game["visitor_team"]["abbreviation"]})'),
                'won': game['visitor_team_score'] > game['home_team_score']
            }


            team_id = home_team_data['team_id']
            teams_stats[team_id] = self.add_team_result(teams_stats[team_id],home_team_data)

            team_id = visitor_team_data['team_id']
            teams_stats[team_id] = self.add_team_result(teams_stats[team_id],visitor_team_data)

        del teams_stats[0] # delete empty dict

        return teams_stats


    def teams_stats(self, season: int, output: str = "stdout") -> None:
        """
            Function takes season, optionally output option, and prints every team statistics in given season.

            Parameters
            ----------
                season: int
                    Seasons are represented by the year they began. For example, 2018 represents season 2018-2019.
                output: str
                    output method { csv | json | sqlite | stdout(default) }. Creates output.* file or just print results without saving it.

            Returns
            -------
                None            
        """
        
        payload = {
            'seasons[]': season,
            'per_page': 100,
        }

        data = self.get_all_data("https://www.balldontlie.io/api/v1/games", payload)

        teams_stats = self.parse_games(data)

        if output == 'json':
            self.to_json(teams_stats)
        elif output == 'csv':
            self.to_csv(teams_stats)
        elif output == 'sqlite':
            self.to_sqlite(teams_stats)
        else:
            for team in teams_stats:
                print(team['team_name'])
                print(f"\twon games as home team: {team['won_games_as_home_team']}".expandtabs(4))
                print(f"\twon games as visitor team: {team['won_games_as_visitor_team']}".expandtabs(4))
                print(f"\tlost games as home team: {team['lost_games_as_home_team']}".expandtabs(4))
                print(f"\tlost games as visitor team: {team['lost_games_as_visitor_team']}".expandtabs(4))

