'''
Created on Oct 25, 2021

@author: Darius
'''
from fractions import Fraction
def read_float():
    num = 0.
    while True:
        try:
            num = Fraction(input())
        except ValueError:
            print("Please enter a number!")
            continue
        else:
            return num

def read_int():
    num = 0
    while True:
        try:
            num = int(input())
        except ValueError:
            print("Please enter an integer!: ")
            continue
        else:
            return num
            