import json
import sys

from teams import Teams
from player import Player

# print(f"Name of the script      : {sys.argv[0]=}")
# print(f"Arguments of the script : {sys.argv[1:]=}")

def print_r(data):
    print(json.dumps(data, indent=2))

if __name__ == '__main__':
    if sys.argv[1] == "grouped-teams":
        team = Teams()
        team.get_all_teams()
    
    elif sys.argv[1] == "players-stats":
        assert sys.argv[2] == "--name"
        # if sys.argv[2] != "--name":
            # raise Exception("--name parameter is required")

        player = Player()
        player.get_stats(sys.argv[3])

        # with open('out.json', 'r') as f:
        #     data = json.load(f)

        # tallest, heaviest = player.get_players_data(data)
        # print(tallest, '\n', 50 * '-')
        
        # print(heaviest, '\n', 50 * '-')

        # player.print_stats(tallest, heaviest)


    