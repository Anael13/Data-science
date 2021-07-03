cars = {}

y_n = ""

while y_n != "n":
    if y_n != "n":
        car_name = input("Enter car's name: ")
        car_top_speed = int(input("Enter car's top speed: "))
        car = {}
        car['name'] = car_name
        car['top_speed'] = car_top_speed
        cars[car_name] = car
        y_n = input("Do you want to add another car(y/n): ")
        if y_n == 'n':
            break


race_choice1 = input("\nPleass tell the first car you want to race: ")
race_choice2 = input("Pleass tell the second car you want to race: ")

top_speed1 = 0
top_speed2 = 0

for x, y in cars.items():
    if(x == race_choice1):
        print("Car 1 top speed is: ", y['top_speed'])
        top_speed1 = y['top_speed']

for x, y in cars.items():
    if(x == race_choice2):
        print("Car 2 top speed is: ", y['top_speed'])
        top_speed2 = y['top_speed']


if (top_speed1 < top_speed2):
    print("Car 2 will win.")
elif (top_speed1 > top_speed2):
    print("Car 1 will win.")
else:
    print("Sorry")
