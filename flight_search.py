import requests
from flight_data import FlightData


TEQUILA_ENDPOINT = "https://tequila-api.kiwi.com"
API_KEY = 'IWwL_djKw8s-vdgn8PRaKWoUvxXzVS_9'


def check_flights(origin_cities, destination, from_time, to_time, flights):
    for city in origin_cities:
        headers = {'apikey': API_KEY}
        query = {
            "fly_from": city,
            "fly_to": destination,
            "date_from": from_time.strftime("%d/%m/%Y"),
            "date_to": to_time.strftime("%d/%m/%Y"),
            "nights_in_dst_from": 6,
            "nights_in_dst_to": 8,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr": "PLN"
        }

        response = requests.get(
            url=f'{TEQUILA_ENDPOINT}/v2/search',
            headers=headers,
            params=query,
        )

        try:
            data = response.json()['data'][0]
        except IndexError:
            print('No flights!')
        else:
            flight_data = FlightData(
                price = data['price'],
                origin_city = data["route"][0]["cityFrom"],
                origin_airport = data["route"][0]["flyFrom"],
                destination = data["route"][1]["flyTo"],
                out_date = data["route"][0]["local_departure"].split("T")[0],
                return_date = data["route"][1]["local_departure"].split("T")[0],
            )

            flights.append(flight_data)