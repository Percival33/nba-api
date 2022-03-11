import requests
import time
import csv, json, sqlite3

class Data:
    def __init__(self):
        pass

    def to_json(self):
        pass

    def to_csv(self):
        pass

    def to_sqlite(self):
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


    def get_all_data(self, url, payload = None):
        res = requests.get(url, params=payload)
        data = {}

        try:
            if res.ok:
                total_pages = res.json()['meta']['total_pages']

                data = res.json()['data']

                for page in range(2, total_pages + 1):
                    payload['page'] = page

                    res = requests.get(url, params=payload)
                    if res.ok:
                        data = [*data, *res.json()['data']]
                    else:
                        self.handle_error(res.status_code)
                    
                    time.sleep(res.elapsed.total_seconds())

            else:
                self.handle_error(res.status_code)

        except Exception as err:
            print(err)

        return data


    @staticmethod
    def height_to_meters(feet, inch):
        if feet == None:
            return None
        return (float(feet) * 30.48 + float(inch) * 2.54) / 100


    @staticmethod
    def weight_to_kg(pounds):
        if pounds == None:
            return None
        return float(pounds) * 0.453