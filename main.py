from datetime import datetime, timedelta
from flight_search import check_flights
from sheet_manager import update_google_sheet
from notification_manager import send_message
from pandas import *
import smtplib

ORIGIN_CITY_IATA_LIST = ['WAW', 'POZ', 'KTW']
DESTINATION_IATA = 'CFU'

flights = []
cheapest_flights = []

today = datetime.now().strftime("%d/%m/%Y")
tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=6 * 30)


check_flights(ORIGIN_CITY_IATA_LIST, DESTINATION_IATA, tomorrow, six_month_from_today, flights)

update_google_sheet(flights, today)

flights_dict = [item.__dict__ for item in flights]

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
            message = f'Subject: New cheapest flight to Corfu!!!\n\nNew cheapest fly from {flights_dict[nr]["origin_airport"]} - ' \
                      f'{flights_dict[nr]["out_date"]} to {flights_dict[nr]["return_date"]} - price: {flights_dict[nr]["price"]}'
            send_message(message)
    pandas.DataFrame(flights_list).to_csv('cheapest_flights.csv')