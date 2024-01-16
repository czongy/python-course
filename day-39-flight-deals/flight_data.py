class FlightData:
    def __init__(self):
        self.flight_list = []

    def compressed(self, data):
        for flight in data:
            flight_dict = {
                "cityFrom": flight['cityFrom'],
                "cityCodeFrom": flight['cityCodeFrom'],
                "cityTo":  flight['cityTo'],
                "cityCodeTo": flight['cityCodeTo'],
                "local_departure": flight['local_departure'][:10],
                "local_departure_2": flight["route"][1]['local_departure'][:10],
                "price": flight['price']
            }
            self.flight_list.append(flight_dict)
        return self.flight_list
