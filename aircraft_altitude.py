from aircraft import Aircraft

model = input("Enter aircraft model:\n")
plane = Aircraft(model)

while True:
    command = input("Enter command (A for ascent, D for descent, X to exit):\n")

    if command == "X":
        break

    parts = command.split()
    action = parts[0]
    feet = int(parts[1])

    if action == "A":
        plane.ascend(feet)
    elif action == "D":
        plane.descend(feet)

print(f"Final altitude: {plane.altitude} feet")