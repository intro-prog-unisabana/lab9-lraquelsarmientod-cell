from aircraft import Aircraft

model = input("Enter aircraft model: ")
aircraft = Aircraft(model)

while True:
    user_input = input("Enter command (A for ascent, D for descent, X to exit): ")
    
    if user_input == "X":
        break
    
    parts = user_input.split()
    command = parts[0]
    value = int(parts[1])
    
    if command == "A":
        aircraft.ascend(value)
    elif command == "D":
        aircraft.descend(value)

print(f"Final altitude: {aircraft.altitude} feet")