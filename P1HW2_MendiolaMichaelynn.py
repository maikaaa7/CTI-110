# Michaelynn Mendiola
# 11/07/2025
# P1HW2
# Calculating a travel budget using addition and subtraction 

print("This program calculates and displays travel expenses")
print()

budget = int(input("Enter Budget: "))
print()

destination = input("Enter your travel destination: ")
print()

gas = int(input("How much do you think you will spend on gas? "))
print()

hotel = int(input("Approximately, how much will you need for an accommodation/hotel? "))
print()

food = int(input("Last, how much do you need for food? "))
print()

total_expenses = gas + hotel + food
remaining_balance = budget - total_expenses

print("---------Travel Expenses---------")
print("Location:", destination)
print("Initial Budget:", budget)
print()

print("Fuel:", gas)
print("Accommodation:", hotel)
print("Food:", food)
print()

print("Remaining Balance:", remaining_balance)