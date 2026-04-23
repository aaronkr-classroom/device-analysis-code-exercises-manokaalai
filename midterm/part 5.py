# Create a list of sensors for different rooms
sensors = [
    RoomSensor("Office", 21, 40, 500),
    RoomSensor("Server Room", 16, 30, 100),
    RoomSensor("Greenhouse", 28, 85, 1000)
]

print("--- Room Status Report ---")
for sensor in sensors:
    print(f"{sensor} | Status: {sensor.check_comfort()}")