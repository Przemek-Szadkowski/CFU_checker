from datetime import datetime, timedelta
from flight_search import check_flights
from sheet_manager import update_google_sheet

ORIGIN_CITY_IATA_LIST = ['WAW', 'POZ', 'KTW']
DESTINATION_IATA = 'CFU'

flights = []

today = datetime.now().strftime("%d/%m/%Y")
tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=6 * 30)


check_flights(ORIGIN_CITY_IATA_LIST, DESTINATION_IATA, tomorrow, six_month_from_today, flights)

update_google_sheet(flights, today)