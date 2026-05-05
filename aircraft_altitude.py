from aircraft import Aircraft

model = input("Enter aircraft model: ")
plane = Aircraft(model)

while True:
    command = input("Enter command (A for ascent, D for descent, X to exit): ")

    if command == "X":
        break

    parts = command.split()

    if len(parts) != 2:
        continue  # evita crash

    action = parts[0]
    
    try:
        feet = int(parts[1])
    except ValueError:
        continue  # evita crash si no es número

    if action == "A":
        plane.ascend(feet)
    elif action == "D":
        plane.descend(feet)

print(f"Final altitude: {plane.altitude} feet")