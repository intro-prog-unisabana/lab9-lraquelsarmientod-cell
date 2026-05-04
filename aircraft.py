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
name = input()
altitude = 0

while True:
    command = input()

    if command == "X":
        break

    action, value = command.split()
    value = int(value)

    if action == "A":
        altitude += value
    elif action == "D":
        altitude -= value

print(f"{name}\n{altitude}")