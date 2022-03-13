from data import Data
from typing import List, Tuple
import re
import sys


class Player(Data):
    def __init__(self) -> None:
        super().__init__()

    def get_tallest_and_heaviest(self, data: List[dict]) -> Tuple[List[dict], List[dict]]:
        """
            Function parses list of players and returns sorted lists by height and by weight.

            Parameters
            ----------
            data : List[dict]
                list of players

            Returns
            -------
            List[dict], List[dict] - list of players:
                sorted by height decreasingly, 
                sorted by weight decreasingly 
        """
        tallest, heaviest = [], []

        for player in data:
            if player['height_feet'] is not None:
                tallest.append({
                    'first_name': player['first_name'],
                    'last_name' : player['last_name'],
                    'height' : self.height_to_meters(player['height_feet'], player['height_inches'])
                })
            
            if player['weight_pounds'] is not None:
                heaviest.append({
                    'first_name': player['first_name'],
                    'last_name' : player['last_name'],
                    'weight' : self.weight_to_kg(player['weight_pounds'])
                })

        tallest.sort(key=self.height, reverse=True)
        heaviest.sort(key=self.weight, reverse=True)

        return tallest, heaviest

    @staticmethod
    def print_stats(tallest: List[dict], heaviest: List[dict]) -> None:
        """
            Function prints the tallest player and their height and the heaviest player and their weight.
            If no data are available it prints "Not found".

            Parameters
            ----------
            tallest: List[dict]
                List of players sorted by height decreasingly
            heaviest: List[dict]
                List of players sorted by weight decreasingly

            Returns
            -------
            None
        """

        tallest_str = "Not found"
        heaviest_str = "Not found"
        
        if tallest:
            tallest_str = f'{tallest[0]["first_name"]} {tallest[0]["last_name"]} {round(tallest[0]["height"],2)} meters'
            
        if heaviest:
            heaviest_str = f'{heaviest[0]["first_name"]} {heaviest[0]["last_name"]} {round(heaviest[0]["weight"])} '\
                    'kilograms'

        print("The tallest player: " + tallest_str)
        print("The heaviest player: " + heaviest_str)

    def get_stats(self, name: str) -> None:
        """
            Function prints tallest and heaviest players name and values. If no data is available prints "Not found"

            Parameters
            ----------
                name: str
                    name (first or last) of players to be searched for tallest and heaviest one.

            Returns
            -------
                None
        """
        
        if not re.findall('^[a-zA-Z]*$', name):
            print("Error occurred:\n\tName can not contain neither digit nor special chracter.")
            sys.exit(1)

        payload = {
            'search': name,
            'per_page': 50
        }

        data = self.get_all_data("https://balldontlie.io/api/v1/players", payload)

        tallest, heaviest = self.get_tallest_and_heaviest(data)
        self.print_stats(tallest, heaviest)    

    @staticmethod
    def height(player: dict) -> int:
        """
            Function returns players height

            Parameters
            ----------
                player: dict
                    dictionary representing player

            Returns
            -------
                player['height']: int
                    players height
        """
        return player['height']

    @staticmethod
    def weight(player: dict) -> int:
        """
            Function returns players weight

            Parameters
            ----------
                player: dict
                    dictionary representing player

            Returns
            -------
                player['weight']: int
                    players weight
        """
        return player['weight']
    
        