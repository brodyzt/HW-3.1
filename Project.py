import math

class EmptySeatFound(Exception): pass

class Person:
    def __init__(self, id=None, name=None, age=None, departure_city=None, arrival_city=None, personality=None):
        self.id = id
        self.name = name
        self.age = age
        self.departure_city = departure_city
        self.arrival_city = arrival_city
        self.personality = personality

    def get_data(self):
        list = []
        list.append(self.id)
        list.append(self.name)
        list.append(self.age)
        list.append(self.departure_city)
        list.append(self.arrival_city)
        list.append(self.personality)
        return list
class Seat:
    def __init__(self):
        self.is_filled = False
        self.sitting_person = None

    def seat_person(self, person):
        self.sitting_person = person
class Bus:
    def __init__(self, seat_rows, seat_columns, departure_city, arrival_city):
        self.departure_city = departure_city
        self.arrival_city = arrival_city
        temp_grid = []
        for y in range(seat_rows):
            temp_row = []
            for x in range(seat_columns):
                temp_row.append(Seat())
            temp_grid.append(temp_row)
        self.seats = temp_grid

    def is_filled(self):
        for row in self.seats:
            for seat in row:
                if not seat.is_filled:
                    return False
        return True

    def add_person(self, person):
        for row in self.seats:
            for seat in row:
                if not seat.is_filled:
                    seat.seat_person(person)
                    return None

    def string_format(self):
        pass
class City:
    def __init__(self, name, latitude, longitude):
        self.name = name
        self.latitude = latitude
        self.longitude = longitude

class ProgramStartup():

    @staticmethod
    def get_cities():
        list = []
        file = open('Cities','r')
        contents = file.readlines()
        contents.pop(0)
        for line in contents:
            current_city = line.split(',')
            list.append(City(current_city[0],float(current_city[1]),float(current_city[2])))
        file.close()
        return list

    @staticmethod
    def get_people():
        list = []
        file = open('People','r')
        contents = file.readlines()
        contents.pop(0)
        for line in contents:
            temp_person = Person()
            attributes = line.split(',')
            temp_person.id = int(attributes[0])
            temp_person.name = attributes[1]
            temp_person.age = int(attributes[2])
            temp_person.departure_city = attributes[3]
            temp_person.arrival_city = attributes[4]
            temp_person.personality = int(attributes[5])
            list.append(temp_person)
        return list

    @staticmethod
    def get_seats():
        pass

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
    clear_screen()
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
def print_cities(list_of_cities):
    for x in range(len(list_of_cities)):
            print(str(x+1) + '.' + list_of_cities[x].name)
def city_with_name(city_name, list_input):
    for city in list_input:
        if(city_name == city.name):
            return city



def bus_network():
    cities = ProgramStartup.get_cities()
    people = ProgramStartup.get_people()

    print(people[0].get_data())

    running = True
    while(running):
        print('Welcome to the bus network. What would you like to do?')
        print('\n1.Calculate distance\n2.List Current City Options\n3.Add City\n4.Delete City\n')
        choice = input('Choice: ')
        clear_screen()

        if choice == '1':
            print('The following list are cities with bus stops. Please select a departure city and an arrival city.\n')
            print_cities(cities)
            city1 = cities[int(input('\nDeparture city: ')) - 1]
            city2 = cities[int(input('Arrival city: ')) - 1]
            distance = dis_bet_cities(city1,city2)
            clear_screen()
            print('\nThe distance between {} and {} is {} miles'.format(city1.name,city2.name,dis_bet_cities(city1,city2)))
            print_lines(5)
            running = will_continue()

        if choice == '2':
            print_cities(cities)
            input('\nHit enter when done')
            clear_screen()
            running = will_continue()

        if choice == '3':
            print('Please enter the details of the city you would like to add\nIf the coordinates are in the Northern or Western hemispheres, don\'t forget the negative sign\n')
            name = input('Name: ')
            latitude = float(input('Latitude: '))
            longitude = float(input('Longitude: '))
            add_city(City(name,latitude,longitude))
            clear_screen()
            running = will_continue()

        if choice == '4':
            print('Please select which city you would like to delete\n')
            for x in range(len(cities)):
                print(str(x+1) + '.' + cities[x].name)
            choice = input('\nChoice: ')
            if choice.isnumeric() == True and 0 < int(choice) <= len(cities):
                city_name = cities[int(choice) - 1].name
                cities = delete_city(city_name)
            clear_screen()
            running = will_continue()

bus_network()  # runs the main program



#print('The distance between {} and {} is {} miles'.format(portland.name,tokyo.name,dis_bet_cities(portland,tokyo)))
