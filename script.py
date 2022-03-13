import argparse

from teams import Teams
from player import Player

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    subparser = parser.add_subparsers(dest='command')
    
    # subparsers
    grouped_teams = subparser.add_parser('grouped-teams', help="Get all teams grouped in divisions")
    players_stats = subparser.add_parser('players-stats', help="Get players with name (first or last)\
     who is the tallest and is the heaviest")
    teams_stats = subparser.add_parser('teams-stats', help="Get statistics for a given season and optionally store it")

    # arguments
    players_stats.add_argument('--name', type=str, required=True, help="Provide first or last name of player to get "
                                                                       "their statistics")
    teams_stats.add_argument('--season', type=int, required=True, help="Seasons are represented by the year they began.\
     For example, 2018 represents season 2018-2019.")

    # optional arguments
    teams_stats.add_argument('--output', choices=['csv', 'json', 'sqlite', 'stdout'], default='stdout', type=str,
                             help="Choose output format. stdout is default")

    args = parser.parse_args()

    if args.command == 'grouped-teams':
        team = Teams()
        team.get_all_teams()
    
    elif args.command == 'players-stats':
        name = args.name
        player = Player()
        player.get_stats(name)
    
    elif args.command == 'teams-stats':
        season = args.season
        output = args.output
        team = Teams()
        team.teams_stats(season, output)

    else:
        parser.print_help()
