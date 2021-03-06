import math

#exception for empty seat found
class EmptySeatFound(Exception): pass

class Person:
    #counter to keep track of used person_ids
    counter = 0

    #initializes the person object with the inputted data
    def __init__(self, name=None, age=None, bus_id=None, personality=None):
        self.id = self.counter
        self.name = name
        self.age = age
        self.bus_id = bus_id
        self.personality = personality

    #packages the person data into a single list
    def get_data(self):
        list = []
        list.append(self.id)
        list.append(self.name)
        list.append(self.age)
        list.append(self.bus_id)
        list.append(self.personality)
        return list

class Seat:
    #initializes the seat object
    def __init__(self):
        self.is_filled = False
        self.sitting_person = None

    #formats the string version of the seat object
    def __str__(self):
        return 'Filled: {}, {}'.format(self.is_filled,self.sitting_person)

    #adds a person to the seat
    def seat_person(self, person):
        self.sitting_person = person
        self.is_filled = True

#bus class
class Bus:
    #initializes the bus class
    def __init__(self, id, seat_rows, seat_columns, departure_city, arrival_city):
        self.id = id
        self.departure_city = departure_city
        self.arrival_city = arrival_city
        temp_grid = []
        for y in range(seat_rows): # adds the seats to the bus object
            temp_row = []
            for x in range(seat_columns):
                temp_row.append(Seat())
            temp_grid.append(temp_row)
        self.seats = temp_grid
        self.num_seats = seat_columns * seat_rows

    # overrides the string version of the bus object
    def __str__(self):
        return "Bus ID:{}, #Seats:{}, #Empty Seats:{}, Departure City:{}, Arrival City:{}".format(self.id,self.num_seats,self.num_empty_seats(),self.departure_city,self.arrival_city)

    # determines whether the bus is filled or not
    def is_filled(self):
        for row in self.seats:
            for seat in row:
                if not seat.is_filled:
                    return False
        else:
            return True

    #seats a person on the bus
    def add_person(self, person):
        for row in self.seats:
            for seat in row:
                if not seat.is_filled:
                    seat.seat_person(person)
                    return None

    #returns the number of empty seats on the bus
    def num_empty_seats(self):
        counter = 0
        for row in self.seats:
            for seat in row:
                if not seat.is_filled:
                    counter += 1
        return counter

class City:
    #initializes the city object
    def __init__(self, name, state, latitude, longitude):
        self.name = name
        self.state = state
        self.latitude = latitude
        self.longitude = longitude

class ProgramStartup():

    #gets list of cities from file
    @staticmethod
    def get_cities():
        list = []
        file = open('Cities','r')
        contents = file.readlines()
        contents.pop(0)
        for line in contents:
            current_city = line.split(',')
            list.append(City(current_city[0],current_city[1],float(current_city[2]),float(current_city[3])))
        file.close()
        return list

    #gets list of people from file
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
            temp_person.bus_id = attributes[3].replace('\n','')
            list.append(temp_person)
            Person.counter += 1
        return list

    #gets list of buses from file
    @staticmethod
    def get_buses():
        list = []
        file = open('Buses','r')
        contents = file.readlines()
        contents.pop(0)
        for line in contents:
            temp_data = line.split(',')
            list.append(Bus(temp_data[0],int(temp_data[1]),int(temp_data[2]),temp_data[3],temp_data[4].replace('\n','')))
        return list

    #returns list of only open buses
    @staticmethod
    def get_open_buses():
        list = ProgramStartup.get_buses()
        new_list = []
        for x in range(len(list)):
            if list[x].is_filled:
                new_list.append(list[x])
        return new_list

    #seats all the people from the file on their corresponding bus
    @staticmethod
    def seat_people():
        for person in people:
            for bus in buses:
                if person.bus_id == bus.id:
                    bus.add_person(person)

#calculates distance between cities
def dis_bet_cities(city1, city2):
    lat1 = math.radians(city1.latitude)
    lat2 = math.radians(city2.latitude)
    long1 = math.radians(city1.longitude)
    long2 = math.radians(city2.longitude)
    a = math.sin((lat1 - lat2)/2) ** 2 + math.cos(lat1)*math.cos(lat2)*(math.sin((long2 - long1)/2) ** 2)
    c = 2 * math.atan2(math.sqrt(a),math.sqrt(1-a))
    distance = 3958.76 * c
    return round(distance, 1)

#prints a set number of blank lines
def print_lines(num):
    for x in range(num):
        print()

#prints a bunch of blank lines to clear the console output
def clear_screen():
    print_lines(100)

#asks the user whether they would like to continue and returns corresponding boolean
def will_continue():
    print('Would you like to continue using the system or are you finished?')
    print('\n1.Continue\n2.Finish')
    choice = input('\nChoice: ')
    clear_screen()
    if(choice == '1'):
        return True
    else:
        return False

#adds city to the cities file
def add_city(new_city):
    temp_cities = ProgramStartup.get_cities()
    temp_cities.append(new_city)
    ProgramStartup.get_cities().append(new_city)
    file = open('Cities','w')
    file.write('Name,Latitude,Longitude\n')
    for city in temp_cities:
        file.write('{},{},{},{}\n'.format(city.name,city.state,city.latitude,city.longitude))
    file.close()

#deletes city from cities file
def delete_city(name):
    temp_cities = ProgramStartup.get_cities()
    file = open('Cities','w')
    file.write('Name,Latitude,Longitude\n')
    for city in temp_cities:
        if(city.name != name):
            file.write('{},{},{},{}\n'.format(city.name,city.state,city.latitude,city.longitude))
    file.close()
    return list(city for city in ProgramStartup.get_cities() if city.name != name)

#prints a list of the current cities
def print_cities(list_of_cities):
    for x in range(len(list_of_cities)):
            print(str(x+1) + '.' + list_of_cities[x].name + ', ' + list_of_cities[x].state)

#returns the city object with a name matching the input
def city_with_name(city_name, list_input):
    for city in list_input:
        if(city_name == city.name):
            return city

#adds person to people file
def add_person(new_person):
    temp_people = ProgramStartup.get_people()
    temp_people.append(new_person)
    file = open('People','w')
    file.write('PersonID,Name,Age,BusID\n')
    for person in temp_people:
        file.write('{},{},{},{}\n'.format(person.id,person.name,person.age,person.bus_id))
    file.close()
    ProgramStartup.seat_people()

#Program begins

#gets saved data
cities = ProgramStartup.get_cities()
people = ProgramStartup.get_people()
buses = ProgramStartup.get_buses()
ProgramStartup.seat_people()

running = True
while(running):
    #asks user which function they would like to perform
    print('Welcome to the bus network. What would you like to do?')
    print('\n1.Calculate distance\n2.List Current City Options\n3.Add City\n4.Delete City\n5.List Current Buses\n6.Add Person To Bus\n')
    choice = input('Choice: ')
    clear_screen()

    if choice == '1':
        #finds the distance between cities
        print('The following list are cities with bus stops. Please select a departure city and an arrival city.\n')
        print_cities(cities)
        city1 = cities[int(input('\nDeparture city: ')) - 1]
        city2 = cities[int(input('Arrival city: ')) - 1]
        distance = dis_bet_cities(city1,city2)
        clear_screen()
        print('\nThe distance between {} and {} is {} miles'.format(city1.name,city2.name,dis_bet_cities(city1,city2)))
        print_lines(5)

    if choice == '2':
        #lists the current cities
        print_cities(cities)
        input('\nHit enter when done')
        clear_screen()

    if choice == '3':
        #asks the user the details of the new city
        print('Please enter the details of the city you would like to add\nIf the coordinates are in the Northern or Western hemispheres, don\'t forget the negative sign\n')
        name = input('Name: ')
        latitude = float(input('Latitude: '))
        longitude = float(input('Longitude: '))
        add_city(City(name,latitude,longitude))
        clear_screen()

    if choice == '4':
        #asks the user which city they want to delete
        print('Please select which city you would like to delete\n')
        for x in range(len(cities)):
            print(str(x+1) + '.' + cities[x].name)
        temp_choice = input('\nChoice: ')
        if temp_choice.isnumeric() == True and 0 < int(temp_choice) <= len(cities):
            city_name = cities[int(temp_choice) - 1].name
            cities = delete_city(city_name)
        clear_screen()

    if choice == '5':
        #lists the current buses
        print('These are the following buses and their info:\n')
        for bus in buses:
            print(bus)

    if choice == '6':
        #allow the user to create a new person
        print('First, enter the details of the person you would like to create.')
        temp_name = input('Name: ')

        temp_age = None
        while True:
            try:
                temp_age = int(input('Age: '))
                break
            except ValueError:
                print("You didn't enter a valid age. Please try again.")

        print('\nPlease select from one of the following buses for the person to join.')
        temp_bus_list = ProgramStartup.get_open_buses()
        for bus in temp_bus_list:
            print('{}. Departure City: {}, Arrival City: {}'.format(bus.id,bus.departure_city,bus.arrival_city))

        bus_choice = input('\nChoice: ')
        while not bus_choice in list(bus.id for bus in temp_bus_list):
            print("You didn't enter a valid option. Please try again")
            bus_choice = input('Choice: ')
        add_person(Person(temp_name, temp_age, bus_choice))

    #asks the user whether they would like to continue or not
    running = will_continue()

