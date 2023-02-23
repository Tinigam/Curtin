class Emission():

    def __init__(self, year, make, model, engine_size, transmission, consumption_city, consumption_long_route, consumption_average, emission_CO2):
        self.year = int(year)
        self.make = make
        self.model = model
        self.engine_size = int(engine_size)
        self.transmission = transmission
        self.consumption_city = float(consumption_city)
        self.consumption_long_route = float(consumption_long_route)
        self.consumption_average = float(consumption_average)
        self.emission_CO2 = float(emission_CO2)

    def __str__(self):
        return str(self.year) + "|" + str(self.make) + "|" + str(self.model) + "|" + str(self.engine_size) + "|" + str(self.transmission) + "|" + str(self.consumption_city) + "|" + str(self.consumption_long_route) + "|" + str(self.consumption_average) + "|" + str(self.emission_CO2)
