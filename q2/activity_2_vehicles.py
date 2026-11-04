class Car:
    def move(self):
        print("The car drives on the road.")

class Boat:
    def move(self):
        print("The boat sails on water.")

class Drone:
    def move(self):
        print("The drone flies in the sky.")


def start_trip(vehicle):
    vehicle.move()


car_obj = Car()
boat_obj = Boat()
drone_obj = Drone()

start_trip(car_obj)
start_trip(boat_obj)
start_trip(drone_obj)