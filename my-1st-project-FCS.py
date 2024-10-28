class Driver:
    def __init__(self, id ,name,start_city):
        self.id = id
        self.name=name
        self.start_city=start_city

    def __str__(self):
        return f'ID: {self.id}, Name: {self.name}, Start City: {self.start_city}'
class Cities:

    def __init__(self,city,path):
       self.city=city
       self.path=path

    def __str__(self) -> str:
        pass

class DeliverySystem:

    def __init__(self):
        self.drivers=[]

    def add_driver(self, id, name,start_city):
        driver = Driver(id ,name, start_city)
        self.drivers.append(driver)
        
    def show_drivers(self):
        if not self.drivers:
            print("No Drivers available")
        else:
            for driver in self.drivers:
                print(driver)

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
                id = input('Enter driver ID: ')
                name= input('Enter new driver name: ')
                start_city=input("Enter driver start city: ")
                self.add_driver(id, name, start_city)
                print("Driver was added")
            elif choice =='3':
                pass
            elif choice =='4':
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
                pass
            elif choice == '3':
                print('Goodbye!')
                break
            else:
                print("Invalid Choice.")

if __name__ == "__main__":
    system = DeliverySystem()
    system.main_menu()