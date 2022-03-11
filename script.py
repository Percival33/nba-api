import sys

from teams import Teams
from player import Player

if __name__ == '__main__':
    try:
        if sys.argv[1] == "grouped-teams":
            team = Teams()
            team.get_all_teams()

        elif sys.argv[1] == "players-stats":
            try:
                param = sys.argv[2]
                name = sys.argv[3]

                assert param == "--name"

            except IndexError as err:
                print("--name and 'player_name' parameters are required. 'player_name' can not be empty.")
                sys.exit(1)
            except AssertionError as err:
                print("--name parameter is required")
                sys.exit(1)

            player = Player()
            player.get_stats(name)
        
        elif sys.argv[1] == "team-stats":
            pass

        else:
            raise Exception("Given option is invalid. Available options: grouped-teams|players-stats|teams-stats")
    
    except IndexError:
        print("specify parameter to get desirable result.")
    except Exception as err:
        print(err)
    