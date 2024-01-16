#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData
from notification_manager import NotificationManager

# GET LIST OF CITY NAME
google_req = DataManager()
city_data = google_req.get_request(cell_range="prices!A1:C12")
city_list = [city[0] for city in city_data]

# GET IATA CODE
flight_req = FlightSearch()
code_data = flight_req.get_city_code(city_list)

# UPDATE CODE DATA
google_data = [[code] for code in code_data]
code_body = {
    'values': google_data
}
google_req.update_request(cell_range="prices!B2", body=code_body)

# SEARCH FLIGHT
dest_str = ','.join(code_data)
flight_data = flight_req.search_flight(dest_str)['data']
data_req = FlightData()
compressed_data = data_req.compressed(data=flight_data)
print(compressed_data)

# Get List of Lowest Price
price_dict = {item[0]: item[2] for item in city_data}

# Send Msg
# messages = NotificationManager()
# for flight in compressed_data:
#     for (place, price) in price_dict.items():
#         if flight['cityTo'] == place and flight['price'] <= int(price):
#             messages.send_message(flight)