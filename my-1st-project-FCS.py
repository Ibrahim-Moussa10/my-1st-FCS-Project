class Driver:
    def __init__(self,id,name,start_city):
        self.id=id
        self.name=name
        self.start_city=start_city
class Cities:
    def __init__(self,city,path):
       self.city=city
       self.path=path
    def __str__(self):
        return (f"ID: {self.id}, Name: {self.name}, Start City: {self.start_city}")