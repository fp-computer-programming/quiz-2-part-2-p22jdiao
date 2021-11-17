# Author: JD 11/17/2021

ans = input("Enter the letter of the day: ")

day = ans.upper()

if day == "A" or day == "C" or day == "E":
    print("You have class today because it is {0} day.".format(day))
elif day == "B" or day == "D" or day == "F" or day == "G":
    print("You have no class today because it is {0} day.".format(day))
else:
    print("Day {0} is not a valid day.".format(day))