class RoomSensor:
    def __init__(self, name, temperature, humidity, light):
        """
        Initializes the RoomSensor with name, temperature, humidity, and light levels.
        """
        self.name = name
        self.temperature = temperature
        self.humidity = humidity
        self.light = light