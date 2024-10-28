class Driver:
    def __init__(self,id,name,start_city):
        self.id=id
        self.name=name
        self.start_city=start_city
    def driverInfo(self):
        print(f'ID:{self.id}, Name: {self.name},Start City: {self.start_city}')
class Cities:
    def __init__(self,city,path):
       self.city=city
       self.path=path
    def deliverInfo(self):
        print(f'Cities: {self.city} Path: {self.path}')

def main_menu():
    while True:
        print("Hello! Please enter: ")
        print("1. To go to the Drivers' Menu")
        print("2. To go to the Cities' Menu")
        print("3. To exit the System")
        choice = input('Enter your choice: ')
        if choice == '1':
            pass
        if choice =='2':
            pass
        if choice == '3':
            print('Goodbye!')
            break
        else:
            print("Invalid Choice.")