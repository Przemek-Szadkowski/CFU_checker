import requests

API_ENDPOINT = 'https://api.sheety.co/bc83ed2bd76b3ca4b6a588c590abf87c/cfu/arkusz1'


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