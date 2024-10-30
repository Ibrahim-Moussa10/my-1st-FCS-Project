class Driver:
    def __init__(self, id ,name,start_city):
        self.id = id
        self.name=name
        self.start_city=start_city

    def __str__(self):
        return f'ID: {self.id}, Name: {self.name}, Start City: {self.start_city}'

class Cities:
    def __init__(self):
        self.cities = {
            "Beirut": ["Jbeil", "Akkar"],
            "Jbeil": ["Beirut", "Akkar"],
            "Akkar": ["Jbeil", "Beirut"],
            "Sayda": ["Zahle"],
            "Zahle": ["Sayda"]
        }

    def show_cities(self):
        for city in self.cities.keys():
            print(city)

    def show_neighbors(self, city):
        if city in self.cities:
            neighbors = self.cities[city]
            print(f"Neighbors of '{city}': {' & '.join(neighbors) if neighbors else 'None'}")
        else:
            print(f"City {city} does not exist.")

    def add_city(self, city, neighbors=None):
        if city not in self.cities:
            self.cities[city] = neighbors if neighbors else[]
            print(f"City {city} was added")

    def __str__(self):
        return " & ".join(self.cities.keys())


class DeliverySystem:
      
    def __init__(self):
        self.drivers=[]
        self.cities = Cities()
        self.next_id = 1


    def add_driver(self, name,start_city):
        id = self.next_id
        driver = Driver(id ,name, start_city)
        self.drivers.append(driver)
        self.next_id +=1
        self.cities.add_city(start_city)
        

    def show_drivers(self):
        if not self.drivers:
            print("No Drivers available")
        else:
            for driver in self.drivers:
                print(f"Driver {driver} is available")

    def check_similar_drivers(self):
        pass

    def show_cities(self):
        self.cities.show_cities()

    def show_neighbors(self, city):
        self.cities.show_neighbors(city)

    def drivers_menu(self):
        while True:
            print("1. To view all the drivers")
            print("2. To add a driver")
            print("3. Check similar drivers")
            print("4. To go back to the main menu")
            choice = input('Enter your choice: ')
            if choice =='1':
                self.show_drivers()
            elif choice == '2':
                name= input('Enter new driver name: ')
                start_city=input("Enter driver start city: ")
                self.add_driver(name, start_city)
                print("Driver was added")
            elif choice =='3':
                start_city = input("Enter city to check for cimilar drivers: ")
                similar_driver = self.check_similar_drivers(start_city)
                if similar_driver:
                    print(f'Drivers starting from {start_city} are: ')
                    for driver in similar_driver:
                        print(driver)
                else:
                    print(f"No similar drivers start from {start_city}")
            elif choice =='4':
                break
            else:
                print("Invalid Choice.")
    
    def cities_menu(self):
        while True:
            print("1. show cities")
            print("2. search city")
            print("3. Print close cities")
            print("4. Print Drivers delivering to the city")
            print("5. To go back")
            choice = input('Enter your choice: ')
            if choice == '1':
                self.show_cities()
            elif choice =='2':
                pass
            elif choice == '3':
                city = input("Enter city name: ")
                self.show_neighbors(city)
            elif choice == '4':
                pass
            elif choice== '5':
                break
            else:
                print("Invalid Choice.")
                
    def main_menu(self):
        while True:
            print("Hello! Please enter: ")
            print("1. To go to the Drivers' Menu")
            print("2. To go to the Cities' Menu")
            print("3. To exit the System")
            choice = input('Enter your choice: ')
            if choice == '1':
                self.drivers_menu()
            elif choice =='2':
                self.cities_menu()
            elif choice == '3':
                print('Goodbye!')
                break
            else:
                print("Invalid Choice.")

if __name__ == "__main__":
    system = DeliverySystem()
    system.add_driver('Max Verstappen', 'Akkar')
    system.add_driver('Charies Leclerc', 'Saida')
    system.add_driver('Lando Norris', 'Jbeil')
    system.main_menu()