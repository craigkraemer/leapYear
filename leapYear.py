# -*- coding: utf-8 -*-
"""
Created on Sun Mar 13 18:10:30 2022

@author: craig
"""

year = int(input("Which year do you want to check? "))

year_mod_4 = year % 4
year_mod_100 = year % 100
year_mod_400 = year % 400
if year_mod_4 == 0 and year_mod_100 != 0 or year_mod_400 == 0:
    print("Leap year.")
else:
    print("Not leap year.")