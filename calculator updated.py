#Name : Joseph Amuyunzu Kirika
#Admission no: SCT211-0061/2022


from datetime import date

# Function to perform addition
print("Choose an operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Calculate Age")
choice = input("Enter the operation number (1/2/3/4/5): ")

def add(num1, num2):
    return num1 + num2

# Function to perform subtraction
def subtract(num1, num2):
    return num1 - num2

# Function to perform multiplication
def multiply(num1, num2):
    return num1 * num2

# Function to perform division
def divide(num1, num2):
    if num2 == 0:
        return "Error! Division by zero."
    else:
        return num1 / num2

# Function to calculate age
def calculate_age(year_of_birth):
    today = date.today()
    birth_year = int(year_of_birth)  # Convert the input to an integer
    age = today.year - birth_year
    return age

# Prompt the user to enter two numbers


# Prompt the user to choose an operation

# Perform the selected operation and display the result
if choice == '5':
    year_of_birth = input("Enter your year of birth (e.g., 1990): ")
    age = calculate_age(year_of_birth)
    print("Age in years: ", age)
    # Calculate age in months and days
    today = date.today()
    birth_date = date(int(year_of_birth), 1, 1)  # Convert to integer here
    age_months = (today.year - birth_date.year) * 12 + (today.month - birth_date.month)
    age_days = (today - birth_date).days
    print("Age in months: ", age_months)
    print("Age in days: ", age_days)

elif choice == '2':
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    result = subtract(num1, num2)
    print("Result: ", result)
elif choice == '3':
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    result = multiply(num1, num2)
    print("Result: ", result)
elif choice == '4':
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    result = divide(num1, num2)
    print("Result: ", result)
elif choice == '1':
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    result = add(num1, num2)
    print("Result: ", result)
else:
    print("Invalid input! Please choose a valid operation (1/2/3/4/5).")
