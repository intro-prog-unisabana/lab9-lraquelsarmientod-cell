from aircraft import Aircraft

if __name__ == "__main__":
    model = input()
    aircraft = Aircraft(model)

    while True:
        command = input()

        if command == "X":
            break

        action, value = command.split()
        value = int(value)

        if action == "A":
            aircraft.climb(value)
        elif action == "D":
            aircraft.descend(value)

    print(aircraft.altitude)