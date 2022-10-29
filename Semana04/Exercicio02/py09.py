import sys, datetime, os, calendar, antigravity
sys.path.append('/home/rodrigo/'Área de Trabalho'/SEII-RodrigoFariaArgondizo/My-Modules')

import my_module as mm
from my_module import find_index as fi, test
from my_module import *

import math

courses = ['History', 'Math', 'Physics', 'CompSci']

print(mm.find_index(courses, 'Math'))
print(fi(courses, 'Math'))
print(test)
print(sys.path)

print(math.radians(90), math.sin(math.radians(90)))

print(datetime.date.today())
print(calendar.isleap(2017))
print(calendar.isleap(2020))

print(os.getcwd())
print(os.__file__)