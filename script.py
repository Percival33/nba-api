import argparse

from teams import Teams
from player import Player

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    subparser = parser.add_subparsers(dest='command')
    
    grouped_teams = subparser.add_parser('grouped-teams', help="get all teams grouped in divisions")
    players_stats = subparser.add_parser('players-stats', help="get players with name (first or last) who is the tallest and is the heaviest")
    team_stats = subparser.add_parser('team-stats', help="TODO") #TODO: write some help command

    players_stats.add_argument('--name', type=str, required=True)
    
    args = parser.parse_args()

    if args.command == 'grouped-teams':
        team = Teams()
        team.get_all_teams()
    
    elif args.command == 'players-stats':
        name = args.name
        player = Player()
        player.get_stats(name)
    
    elif args.command == 'team-stats':
        pass

    else:
        parser.print_help()
