import math
import os
import random
import re
import sys

# Complete the solve function below.

if __name__ == '__main__':
    meal_cost = float(input())
    tip_percent = meal_cost * int(input())/100
    tax_percent = meal_cost * int(input())/100
    tcost = meal_cost + tip_percent + tax_percent
    print(str(round(tcost)))
