#!/usr/bin/python
#
#JulioGomez
#this is a program of a car dealership and helping a CONSUMER pick out a car without any help of any annoying employees
#

class Car:

    car_speed = None
    car_acceleration = None
    car_colour = None
    car_make = None
    car_model = None
    car_price = None

    def __init__(self, speed, acceleration, colour, make, model, price):
        """
        :param speed:
        :param acceleration:
        :param colour:
        :param make:
        :param model:
        :param price:
        :return:
        """
        self.car_speed = speed
        self.car_acceleration = acceleration
        self.car_colour = colour
        self.car_make = make
        self.car_model = model
        self.car_price = price