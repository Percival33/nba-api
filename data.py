import requests
import time
import csv
import json
import sqlite3
from progress.bar import Bar
from typing import List


class Data:
    def __init__(self) -> None:
        pass

    @staticmethod
    def handle_error(http_code: int) -> None:
        """
            Function raises exception accordingly to error code.

            Parameters
            ----------
                http_code: int
                    http code returned by request

            Returns
            -------
                None
        """
        if http_code == 400:
            raise Exception("Your request is invalid")
        elif http_code == 404:
            raise Exception("Specified resource could not be found")
        elif http_code == 406:
            raise Exception("Balldontlie could not send format different than json")
        elif http_code == 429:
            raise Exception("You sent too many requests! Stop bombarding!")
        elif http_code == 500:
            raise Exception("Balldontlie has problem with their server. Try again later.")
        elif http_code == 503:
            raise Exception("Balldontlie is offline for maintenance. Please try again later.")

    def get_all_data(self, url: str, payload: dict = None) -> List[dict]:
        """
            Function makes GET request to given url with payload parameters. If there are multiple pages,
            they are merged to list of dicts. On error handle_error() is called and adequate exception is raised.

            Parameters
            ----------
                url: str
                    url to GET request
                payload: dict
                    parameters of GET request

            Returns
            -------
                data: List[dict]
                    list of results from JSON response

        """
        res = requests.get(url, params=payload)
        data = {}

        try:
            if res.ok:
                total_pages = res.json()['meta']['total_pages']

                with Bar('Processing...', max=total_pages) as bar:

                    data = res.json()['data']
                    if data:
                        bar.next()

                    for page in range(2, total_pages + 1):
                        payload['page'] = page

                        res = requests.get(url, params=payload)

                        if res.ok:
                            data = [*data, *res.json()['data']]
                        else:
                            self.handle_error(res.status_code)

                        time.sleep(res.elapsed.total_seconds())

                        bar.next()

                    bar.finish()

            else:
                self.handle_error(res.status_code)

        except Exception as err:
            print(err)

        return data

    @staticmethod
    def to_json(data: List[dict], filename: str = 'output') -> None:
        """
            Function dumps data to JSON file (output.json)

            Parameters
            ----------
                data: List[data]
                    data to be dumped to JSON file

                filename: str
                    name of created file

            Returns
            -------
                None
        """
        with open(f'{filename}.json', 'w') as f:
            json.dump(data, f, indent=2)

        print(f'File {filename}.json was successfully created')

    @staticmethod
    def to_csv(data: List[dict], filename: str = 'output') -> None:
        """
            Function saves data to csv file (output.csv) with default fieldnames.
            fieldnames = Team name, Won games as home team, Won games as visitor team, Lost games as home team,
            Lost games as visitor team

            Parameters
            ----------
                data: List[data]
                    data to be saved to csv file

                filename: str
                    name of created file

            Returns
            -------
                None
        """

        with open(f"{filename}.csv", 'w') as new_file:
            fieldnames = ['Team name', 'Won games as home team', 'Won games as visitor team', 'Lost games as home team',
                          'Lost games as visitor team']

            csv_writer = csv.DictWriter(new_file, fieldnames=fieldnames)

            csv_writer.writeheader()

            for team in data:
                line = {
                    'Team name': team['team_name'],
                    'Won games as home team': team["won_games_as_home_team"],
                    'Won games as visitor team': team["won_games_as_visitor_team"],
                    'Lost games as home team': team["lost_games_as_home_team"],
                    'Lost games as visitor team': team["lost_games_as_visitor_team"]
                }

                csv_writer.writerow(line)

        print(f'File {filename}.csv was successfully created')

    @staticmethod
    def to_sqlite(data: List[dict], filename: str = 'output') -> None:
        """
            Function creates table teams_stats, inserts data into it and save it to (output.sqlite) file.
            teams_stats (Team name: text, Won games as home team: integer, Won games as visitor team: integer,
            Lost games as home team: integer, Lost games as visitor team: integer)

            Parameters
            ----------
                data: List[data]
                    data to be saved to sqlite file

                filename: str
                    name of created file

            Returns
            -------
                None
        """
        conn = sqlite3.connect(f'{filename}.sqlite')

        c = conn.cursor()

        c.execute("""CREATE TABLE teams_stats (
                    team_name text,
                    won_games_as_home_team integer,
                    won_games_as_visitor_team integer,
                    lost_games_as_home_team integer,
                    lost_games_as_visitor_team integer
                    )""")

        conn.commit()

        for team in data:
            # shorcuts tn = team_name, take only first letters
            value = {
                'tn': team['team_name'],
                'wght': team['won_games_as_home_team'],
                'wgvt': team['won_games_as_visitor_team'],
                'lght': team['lost_games_as_home_team'],
                'lgvt': team['lost_games_as_visitor_team']
            }

            c.execute("INSERT INTO teams_stats VALUES "
                      "(:team_name, :won_games_as_home_team,:won_games_as_visitor_team, :lost_games_as_home_team,"
                      " :lost_games_as_visitor_team)",
                      {
                          'team_name': value['tn'],
                          'won_games_as_home_team': value['wght'],
                          'won_games_as_visitor_team': value['wgvt'],
                          'lost_games_as_home_team': value['lght'],
                          'lost_games_as_visitor_team': value['lgvt'],
                      })

        conn.commit()
        conn.close()
        print(f'File {filename}.sqlite was successfully created')

    @staticmethod
    def height_to_meters(feet: float, inch: float) -> float:
        """
            Function converts feet and inches values to metric system
            Parameters
            ----------
                feet: float
                    Length in feet
                inch: float
                    Length in inches
            
            Returns
            -------
                height: int
                    Length in metric system
        """
        if feet is None:
            return 0.0
        return (float(feet) * 30.48 + float(inch) * 2.54) / 100

    @staticmethod
    def weight_to_kg(pounds: float) -> float:
        """
            Function converts pounds to kilograms
            Parameters
            ----------
                pounds: float
                    weight in pounds
            
            Returns
            -------
                weight: float
                    weight in metric system
        """
        if pounds is None:
            return 0.0
        return float(pounds) * 0.453
