from datetime import datetime, timedelta
from flight_search import check_flights
from sheet_manager import update_google_sheet
from pandas import *

ORIGIN_CITY_IATA_LIST = ['WAW', 'POZ', 'KTW']
DESTINATION_IATA = 'CFU'

flights = []
cheapest_flights = []

today = datetime.now().strftime("%d/%m/%Y")
tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=6 * 30)


check_flights(ORIGIN_CITY_IATA_LIST, DESTINATION_IATA, tomorrow, six_month_from_today, flights)

update_google_sheet(flights, today)

# flights_dict = [item.__dict__ for item in flights]
flights_dict = [{'price': 370, 'origin_city': 'Warsaw', 'origin_airport': 'WMI', 'destination': 'WMI', 'out_date': '2021-05-27', 'return_date': '2021-06-03'}, {'price': 252, 'origin_city': 'Poznań', 'origin_airport': 'POZ', 'destination': 'POZ', 'out_date': '2021-05-16', 'return_date': '2021-05-23'}, {'price': 516, 'origin_city': 'Katowice', 'origin_airport': 'KTW', 'destination': 'KTW', 'out_date': '2021-06-16', 'return_date': '2021-06-23'}]

try:
    flights_frame = pandas.read_csv('cheapest_flights.csv')
except FileNotFoundError:
    new_flights = pandas.DataFrame(flights_dict)
    new_flights.to_csv('cheapest_flights.csv')
else:
    flights_list = flights_frame.to_dict(orient='records')
    for nr in range(0, 3):
        if flights_dict[nr]['price'] < flights_list[nr]['price']:
            flights_list[nr] = flights_dict[nr]
    pandas.DataFrame(flights_list).to_csv('cheapest_flights.csv')