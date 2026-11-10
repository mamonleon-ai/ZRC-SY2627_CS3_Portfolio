class Sensor(ABC):
    @abstractmethod
    def get_reading(self):
        pass


class PHSensor(Sensor):
    def get_reading(self):
        print("[pH Sensor] Reading: 7.2 pH (Neutral)")


class TempSensor(Sensor):
    def get_reading(self):
        print("[Temperature Sensor] Reading: 24.5°C")


print("--- Lab Inventory System ---")

my_sensors = [
    PHSensor(),
    TempSensor()
]

for sensor in my_sensors:
    sensor.get_reading()

try:
    my_sensor = Sensor()
except TypeError as e:
    print(type(e).__name__ + ": " + str(e))