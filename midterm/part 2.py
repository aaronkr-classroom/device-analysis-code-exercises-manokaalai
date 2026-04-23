class RoomSensor:
    def __init__(self, name, temperature, humidity, light):
        self.name = name
        self.temperature = temperature
        self.humidity = humidity
        self.light = light

    def __str__(self):
        return f"Sensor: {self.name} | Temp: {self.temperature}°C | Humidity: {self.humidity}%"