import requests
import json
import sys


# print(f"Name of the script      : {sys.argv[0]=}")
# print(f"Arguments of the script : {sys.argv[1:]=}")

def print_r(data):
    print(json.dumps(data, indent=2))


class Data:
    def __init__(self):
        pass

    def __str__(self):
        pass

    def json(self):
        pass

    def handle_error(self, http_code):
        if http_code == 400:
            raise Exception("Your request is invalid")
        elif http_code == 404:
            raise Exception("Specified resourse could not be found")
        elif http_code == 406:
            raise Exception("Balldontlie could not send format different than json")
        elif http_code == 429:
            raise Exception("You sent too many requests! Stop bombarding!")
        elif http_code == 500:
            raise Exception("Balldontlie has problem with their server. Try again later.")
        elif http_code == 503:
            raise Exception("Balldontlie is offline for maintenance. Please try again later.")


class Teams(Data):
    def __init__(self):
        pass

    def get_all_teams(self):
        res = requests.get("https://www.balldontlie.io/api/v1/teams")

        if res.ok:
            #FIXME: try and except with json ?
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
            super().handle_error(res.status_code)


if __name__ == '__main__':
    if sys.argv[1] == "grouped-teams":
        Teams().get_all_teams()
    
    