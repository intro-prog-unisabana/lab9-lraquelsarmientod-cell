from car_utils import create_car_from_input, display_cars
from car import Car

cars = {}

while True:
    print("\nMenu:")
    print("1. Add a new car")
    print("2. View all cars")
    print("3. Drive a car")
    print("4. Paint a car")
    print("5. Exit")

    choice = input("Enter your choice:\n")

    if choice == "1":
        # Crear carro
        car = create_car_from_input()
        cars[car.car_id] = car
        print(car)
        print("Car added.")

    elif choice == "2":
        display_cars(cars)

    elif choice == "3":
        car_id = input("Enter car ID:\n")
        miles = float(input("Enter miles driven:\n"))

        if car_id in cars:
            cars[car_id].drive(miles)
            print("Mileage updated.")
            print(cars[car_id])

    elif choice == "4":
        car_id = input("Enter car ID:\n")
        new_color = input("Enter new color:\n")

        if car_id in cars:
            cars[car_id].change_color(new_color)
            print("Color updated.")
            print(cars[car_id])

    elif choice == "5":
        print("Goodbye!")
        break