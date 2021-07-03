cars = {}

y_n = ""
    
while y_n != "n":
    if y_n != "n":
        car_name= input("Enter car's name: ")
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

for x in cars:
    if(x['name'] == race_choice1):
        print("Car 1 top speed is: ", x['car_top_speed'])
 
for y in cars:
    if(y['name'] == race_choice):
        print("Car 2 top speed is: ", y['car_top_speed'])
 
        if (x['car_top_speed']) < (y['car_top_speed']):
            print("Car 2 will win.")
        elif (x['car_top_speed']) > (y['car_top_speed']):
            print("Car 1 will win.")
        else: 
            print("Sorry")



    


    
