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
