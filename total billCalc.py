#Name : Joseph Amuyunzu Kirika
#Admission no: SCT211-0061/2022


# Function to calculate the total amount to pay per person
def calculate_per_person(total_bill, tip_percentage, num_people):
    tip_amount = (tip_percentage / 100) * total_bill
    total_amount = total_bill + tip_amount
    per_person_amount = total_amount / num_people
    return per_person_amount

total_bill = float(input("Enter the total bill amount: "))

print("Select a tip percentage:")
print("1. 10%")
print("2. 12%")
print("3. 15%")
tip_choice = input("Enter the tip percentage (1/2/3): ")

tip_percentages = [10, 12, 15]
if tip_choice in ['1', '2', '3']:
    tip_percentage = tip_percentages[int(tip_choice) - 1]
else:
    print("Invalid tip percentage choice. Using default 10%.")
    tip_percentage = 10
num_people = int(input("Enter the number of people splitting the bill: "))

per_person_amount = calculate_per_person(total_bill, tip_percentage, num_people)


print(f"Each person should pay: ${per_person_amount:.2f}")
