#from flask import g
#import mymodule
#print(mymodule.generate_full_name('Kamran', 'Habib'))

import Functions
print(Functions.add_two_numbers())

import Functions
print(Functions.area_circle(4))

#When one file has many functions and we want to import several funtions(like done in above) it can be done by this single command
from Functions import add_two_numbers, area_circle
print(add_two_numbers())
print(area_circle(4))

#Importing and Renaming
from Functions import print_full_name as full_name, sum_two_numbers as sum, calculate_age as current_age, weight_object as w
print(full_name('Kamran', 'Habib'))
print(sum(4,5))
print(current_age(2022,1996))
print(w(100,9.8))

#Built-in Modules

from statistics import *
ages = [20, 20, 4, 24, 25, 22, 26, 20, 23, 22, 26]
print(mean(ages))
print(median(ages))
print(mode(ages))
print(stdev(ages))

import math
print(math.pi)
print(math.sqrt(2))
print(math.pow(2,3))
print(math.floor(9.81)) #Rounding to the lowest
print(math.ceil(9.81)) #Rounding to the highest
print(math.log10(100)) #Logarithmic with 10 as base

from math import pi #For importing a specific function
print(pi)

from math import pi, sqrt, pow, floor as chatt, ceil as zameen, log10 #we can also use from math import *
print(pi)
print(sqrt(100))
print (pow(3,4))
print(chatt(4.89))
print(zameen(3.89))
print(log10(1000))

import string
print(string.ascii_letters)
print(string.digits)
print(string.punctuation)

from random import random, randint
print(random())
print(randint(5,20))
