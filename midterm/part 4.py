class RoomSensor:
    def __init__(self, name, temperature, humidity, light):
        self.name = name
        self.temperature = temperature
        self.humidity = humidity
        self.light = light

    def __str__(self):
        return f"Sensor: {self.name} | Temp: {self.temperature}°C | Humidity: {self.humidity}%"

    def check_comfort(self):
        # A simple check: comfortable if temp is between 18 and 24
        if 18 <= self.temperature <= 24:
            return "Comfortable"
        return "Uncomfortable"

# Test it out
office_sensor = RoomSensor("Office", 21, 40, 500)
print(office_sensor)
print(f"Status: {office_sensor.check_comfort()}")