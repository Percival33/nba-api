from data import Data
import requests

class Player(Data):
    def __init__(self):
        pass
    

    @staticmethod
    def height(player) -> int:
        return player['height']


    @staticmethod
    def weight(player) -> int:
        return player['weight']
    

    def get_players_data(self, data):
        tallest, heaviest = [], []

        for player in data:
            if player['height_feet'] != None:
                tallest.append({
                    'first_name': player['first_name'],
                    'last_name' : player['last_name'],
                    'height' : self.height_to_meters(player['height_feet'], player['height_inches'])
                })
            
            if player['weight_pounds'] != None:
                heaviest.append({
                    'first_name': player['first_name'],
                    'last_name' : player['last_name'],
                    'weight' : self.weight_to_kg(player['weight_pounds'])
                })

        tallest.sort(key=self.height, reverse=True)
        heaviest.sort(key=self.weight, reverse=True)

        return tallest, heaviest


    def print_stats(self, tallest, heaviest) -> None:
        tallest_str = "Not found"
        heaviest_str = "Not found"
        
        if tallest:
            tallest_str = f'{tallest[0]["first_name"]} {tallest[0]["last_name"]} {round(tallest[0]["height"],2)} meters'
            
        if heaviest:
            heaviest_str = f'{heaviest[0]["first_name"]} {heaviest[0]["last_name"]} {round(heaviest[0]["weight"])} kilograms'

        print("The tallest player: " + tallest_str)
        print("The heaviest player: " + heaviest_str)


    def get_stats(self, name: str):
        payload = {
            'search' : name,
        }

        data = self.get_all_data("https://balldontlie.io/api/v1/players",payload)

        tallest, heaviest = self.get_players_data(data)
        self.print_stats(tallest, heaviest)    
        