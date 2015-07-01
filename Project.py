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

def list_of_cities():
    list = []
    file = open('Cities','r')
    contents = file.readlines()
    for line in contents:
        currentCity = line.split(',')
        list.append(City(currentCity[0],float(currentCity[1]),float(currentCity[2])))
    file.close()
    return list
def dis_bet_cities(city1, city2):
    lat1 = math.radians(city1.latitude)
    lat2 = math.radians(city2.latitude)
    long1 = math.radians(city1.longitude)
    long2 = math.radians(city2.longitude)
    a = math.sin((lat1 - lat2)/2) ** 2 + math.cos(lat1)*math.cos(lat2)*(math.sin((long2 - long1)/2) ** 2)
    c = 2 * math.atan2(math.sqrt(a),math.sqrt(1-a))
    distance = 3958.76 * c
    return round(distance, 1)
def print_lines(num):
    for x in range(num):
        print()
def clear_screen():
    print_lines(100)
def will_continue():
    print('Would you like to continue using the system or are you finished?')
    print('\n1.Continue\n2.Finish')
    choice = input('\nChoice: ')
    if(choice == '1'):
        return True
    else:
        return False
def add_city(new_city):
    temp_cities = list_of_cities()
    temp_cities.append(new_city)
    cities.append(new_city)
    file = open('Cities','w')
    for city in temp_cities:
        file.write('{},{},{}\n'.format(city.name,city.latitude,city.longitude))
    file.close()
def delete_city(name):
    temp_cities = list_of_cities()
    file = open('Cities','w')
    for city in temp_cities:
        if(city.name != name):
            file.write('{},{},{}\n'.format(city.name,city.latitude,city.longitude))
    file.close()
    return list(city for city in cities if city.name != name)

cities = list_of_cities()

running = True

while(running):
    print('Welcome to the bus network. What would you like to do?')
    print('\n1.Calculate distance\n2.Add City\n3.Delete City\n')
    choice = input('Choice: ')
    clear_screen()

    if(choice == '1'):
        print('The following list are cities with bus stops. Please select a departure city and an arrival city.\n')
        for x in range(len(cities)):
            print(str(x+1) + '.' + cities[x].name)
        city1 = cities[int(input('\nDeparture city: ')) - 1]
        city2 = cities[int(input('Arrival city: ')) - 1]
        distance = dis_bet_cities(city1,city2)
        clear_screen()
        print('\nThe distance between {} and {} is {} miles'.format(city1.name,city2.name,dis_bet_cities(city1,city2)))
        print_lines(5)
        running = will_continue()

    if(choice == '2'):
        print('Please enter the details of the city you would like to add\nIf the coordinates are in the Northern or Western hemispheres, don\'t forget the negative sign\n')
        name = input('Name: ')
        latitude = float(input('Latitude: '))
        longitude = float(input('Longitude: '))
        add_city(City(name,latitude,longitude))
        clear_screen()

    if(choice == '3'):
        print('Please select which city you would like to delete\n')
        for x in range(len(cities)):
            print(str(x+1) + '.' + cities[x].name)
        choice = input('\nChoice: ')
        if(choice.isnumeric() == True and 0 < int(choice) <= len(cities)):
            city_name = cities[int(choice) - 1].name
            cities = delete_city(city_name)
        clear_screen()





#print('The distance between {} and {} is {} miles'.format(portland.name,tokyo.name,dis_bet_cities(portland,tokyo)))