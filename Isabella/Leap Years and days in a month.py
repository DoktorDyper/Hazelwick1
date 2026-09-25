year = int(input("Enter a year: "))



if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0 and year % 100 != 0):
    print(year, "is a Leap Year.")

else:
    print(year, "is not a Leap Year.")

month = int(input("Enter a month number(1-12): "))

if month < 1 and month > 12:
    print("Error")

elif month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
    print(f"Month {month} of {year} has 31 days.")

elif month == 4 or month == 6 or month == 9 or month == 11:
    print(f"Month {month} of {year} has 30 days.")
    
