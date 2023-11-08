#Name : Joseph Amuyunzu Kirika
#Admission no: SCT211-0061/2022

# Function to check if a year is a leap year
def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

# Prompt the user to enter a year
year = int(input("Enter a year: "))

# Check if it's a leap year and display the result
if is_leap_year(year):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")