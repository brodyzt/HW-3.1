import math

class Bus:
    def __init__(self, numSeatsTotal, numSeatsFilled, depart, arrive):
        self.numSeatsTotal = numSeatsTotal
        self.numseatsFilled = numSeatsFilled
        self.depart = depart
        self.arrive = arrive

    def isFilled(self):
        return self.numseatsFilled == self.numSeatsTotal
class City:
    def __init__(self, name, latitude, longitude):
        self.name = name
        self.latitude = latitude
        self.longitude = longitude

def dis_bet_cities(city1, city2):
    lat1 = math.radians(city1.latitude)
    lat2 = math.radians(city2.latitude)
    long1 = math.radians(city1.longitude)
    long2 = math.radians(city2.longitude)
    a = math.sin((lat1 - lat2)/2) ** 2 + math.cos(lat1)*math.cos(lat2)*(math.sin((long2 - long1)/2) ** 2)
    c = 2 * math.atan2(math.sqrt(a),math.sqrt(1-a))
    return 3958.76 * c

cities = [City('Chicago',-41.8369,-87.6847),
          City('Boston',-42.3601,-71.0589),
          City('New York City',-40.7127,-74.0059),
          City('Toronto',-43.7000,-79.4000),
          City('Portland',-45.5200,-122.6819),
          City('Tokyo',-35.6833,139.6833)]


#print('The distance between {} and {} is {} miles'.format(portland.name,tokyo.name,dis_bet_cities(portland,tokyo)))