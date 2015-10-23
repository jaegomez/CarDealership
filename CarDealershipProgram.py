#!/usr/bin/python
#
#JulioGomez
#this is car delership program
#


import CarDealership

def main():
    """
    this is the main function
    :return:
    """
    #These are my cars
    Car1 = CarDealership.Car (240, 11, "black", "Lamborghini", "Murcielago", 350000)
    Car2 = CarDealership.Car (220, 10, "red", "Porsche", "GT3", 290000)
    Car3 = CarDealership.Car (230, 12, "yellow", "Chevrolet", "Corvette Z06", 180000)
    Car4 = CarDealership.Car (160, 9, "black", "Infiniti", "G35 Coupe", 48000)
    Car5 = CarDealership.Car (180, 10, "silver", "Nissan", "370Z Coupe", 59000)
    Car6 = CarDealership.Car (220, 11, "blue", "Ferrari", "F12 Berlinetta", 200000)
    Car7 = CarDealership.Car (200, 10, "green", "Lamborghini", "Gallardo", 108000)
    Car8 = CarDealership.Car (180, 9, "white", "Range Rover", "Supercharged", 100000)
    Car9 = CarDealership.Car (260, 14, "orange", "Buggati", "Veyron", 1600000)
    Car10 = CarDealership.Car (140, 8, "gold", "Toyota", "Camry", 27000)

    car_lot = [Car1, Car2, Car3, Car4, Car5, Car6, Car7, Car8, Car9, Car10]
    print "This is an Exotic Car Dealership \nWe have " + str(len(car_lot)) + " cars on our lot!"

    yes_or_no = ""
    while yes_or_no.lower() != "yes" and yes_or_no.lower() != "no":
        yes_or_no = raw_input("Would you like to proceed? Yes or No: ")

    if yes_or_no == "no".lower():
        print "Okay bye"
        quit()

    min_price = input("Whats the minimum you want to spend on a vehicle today? ")
    max_price = input("What is the maximum you want to spend on a vehicle today? ")

    found_a_car = False
    for dream_car in car_lot:
        if dream_car.car_price >= min_price and dream_car.car_price <= max_price:
            print dream_car.car_make
            found_a_car = True

    if found_a_car == True:

        buyer_pick = raw_input("Which one of those cars are you interested in? ").title()

        valid_choice = False
        for dream_car in car_lot:
            if dream_car.car_make == buyer_pick:
                valid_choice = True
                break

        if valid_choice == True:
            print "These are the specs for the " + dream_car.car_make
            print "The top speed is " + str(dream_car.car_speed) + " MPH."
            print "The acceleration is " + str(dream_car.car_acceleration) + " RPM."
            print "The colour is " + dream_car.car_colour + "."
            print "The make is " + dream_car.car_make + "."
            print "The model is " + dream_car.car_model + "!"
            print "The asking price is " + str(dream_car.car_price) + " dollars!"

            buyer_purchase = raw_input("Would you like to go ahead and purchase the car? ")

            if buyer_purchase == "yes":
                print "Congratulations you have purchased your new " + buyer_pick + " hope you enjoy it!"
            elif buyer_purchase == "no":
                print "Okay thank you!"
        else:
            print "Thats not a valid car choice."
    else:
        print "No vehicle available in that price range."


main()
