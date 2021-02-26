import requests

API_ENDPOINT = 'https://api.sheety.co/e5f66404da94946abb43041a21970d92/cfu/arkusz1'


def update_google_sheet(flight_data, date):
    for flight in flight_data:
        new_flight = {
            'arkusz1': {
                'wylot': flight.origin_airport,
                'dataWylotu': flight.out_date,
                'dataPowrotu': flight.return_date,
                'cena': flight.price,
                'dataWyszukiwania': date,
            }
        }

        response = requests.post(
            url=API_ENDPOINT,
            json=new_flight
        )

        print(response.text)