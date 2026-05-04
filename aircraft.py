# FREEZE CODE BEGIN
class Aircraft:
    def __init__(self, model, altitude=0):
        self.model = model
        self.altitude = altitude

    def climb(self, feet):
        self.altitude += feet

    def descend(self, feet):
        self.altitude -= feet
# FREEZE CODE END
if __name__ == "__main__":
    model = input()
    aircraft = Aircraft(model)

    while True:
        command = input().strip()

        if command == "X":
            break

        parts = command.split()

        if len(parts) != 2:
            continue  

        action, value = parts
        value = int(value)

        if action == "A":
            aircraft.climb(value)
        elif action == "D":
            aircraft.descend(value)

    print(aircraft.altitude)