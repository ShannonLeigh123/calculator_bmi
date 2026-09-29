# -*- coding: utf-8 -*-
"""

BODY MASS INDEX Calculator
Metric and Imperial unit of measures calculated.
@author: shannon
"""

def bmi_calc(weight,height,measure = 'm'):
    if measure == "m":
        bmi = weight / (height **2)
    elif measure == "i":
        bmi = (weight / (height **2)) * 703
    else:
        raise ValueError("Invalid measure. Please enter either metric or imperial")
    return  bmi

def classify_bmi(bmi):
    if bmi < 18.5:
        return "You might be Underweight"
    elif 18.5 <= bmi <= 24.9:
        return "You are in the range considered to be normal"
    elif 25 <= bmi <= 29.9:
        return "You are in the range considered to be overweight"
    elif 30 <= bmi <= 40:
        return "You are in the range considered to be obese"
    else:
        return "You are obese"

def get_height(measure):
    if measure == "m":
        return float(input("Please enter your height in meters: "))
    elif measure == "i":
        feet = float(input("Please enter your height in feet: "))
        inches = float(input("Please enter your height in inches: "))
        return (feet * 12) + inches

def greet_user():
    print("Welcome the to BMI Calculator")
    measure = input("Please enter 'm' for metric or 'i' for imperial: ").strip().lower()
    if measure == "m":
        weight = float(input("Please enter your weight in kilograms: "))
        height = get_height(measure)
    elif measure == "i":
        weight = float(input("Please enter your weight in pounds: "))
        height = get_height(measure)
    else:
        print('Invalid input. Please re-enter your answers')
        greet_user()

    bmi = bmi_calc(weight, height, measure)
    classification = classify_bmi(bmi)
    print(f'\nYour Body Mass Index: {bmi:.2f}')
    print(f'Classification: {classification}')

    another_calc = input("Would you like to calculate another BMI (y/n)? ")
    if another_calc == "n":
        print("Thank you for using BMI Calculator")
    else:
        greet_user()


greet_user()















