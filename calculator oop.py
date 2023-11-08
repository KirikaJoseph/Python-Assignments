from datetime import date

class Calculator:
    def add(self, num1, num2):
        return num1 + num2

    def subtract(self, num1, num2):
        return num1 - num2

    def multiply(self, num1, num2):
        return num1 * num2

    def divide(self, num1, num2):
        if num2 == 0:
            return "Error! Division by zero."
        else:
            return num1 / num2

    @staticmethod
    def calculate_age(year_of_birth):
        today = date.today()
        birth_year = int(year_of_birth)
        age = today.year - birth_year
        return age

# Instantiate the Calculator class
calculator = Calculator()

print("Choose an operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Calculate Age")
choice = input("Enter the operation number (1/2/3/4/5): ")

if choice == '5':
    year_of_birth = input("Enter your year of birth (e.g., 1990): ")
    age = Calculator.calculate_age(year_of_birth)
    print("Age in years: ", age)

    today = date.today()
    birth_date = date(int(year_of_birth), 1, 1)
    age_months = (today.year - birth_date.year) * 12 + (today.month - birth_date.month)
    age_days = (today - birth_date).days
    print("Age in months: ", age_months)
    print("Age in days: ", age_days)

elif choice in ['1', '2', '3', '4']:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    if choice == '1':
        result = calculator.add(num1, num2)
    elif choice == '2':
        result = calculator.subtract(num1, num2)
    elif choice == '3':
        result = calculator.multiply(num1, num2)
    elif choice == '4':
        result = calculator.divide(num1, num2)

    print("Result: ", result)
else:
    print("Invalid input! Please choose a valid operation (1/2/3/4/5).")
