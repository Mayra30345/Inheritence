class vehicle:
    def __init__(self,name,max_speed,mileage):
          self.name=name
          self.max_speed=max_speed
          self.mileage=mileage
class bus(vehicle):
    def __init__(self,brand,color,name,max_speed,mileage):
        self.brand=brand
        self.color=color
        vehicle.__init__(self,name,max_speed,mileage)
school_bus=bus("Royal Cruiser","white","School Volvo",180,12)
print("Vehicle name:  ",school_bus.name,"Speed: ",school_bus.max_speed,"mileage: ",school_bus.mileage)
