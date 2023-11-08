
# Name : Joseph Amuyunzu Kirika
# Admission no: SCT211-0061/2022

def calculate_bmi(weight_kg, height_m):
    bmi = weight_kg / (height_m ** 2)
    return bmi

def determine_weight_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    else:
        return "Overweight"

weight_kg = float(input("Enter your weight in kilograms: "))

height_m = float(input("Enter your height in meters: "))

# Calculate BMI
bmi = calculate_bmi(weight_kg, height_m)

# Determining and display the weight category
weight_category = determine_weight_category(bmi)
print(f"Your BMI is: {bmi:.2f}")
print(f"You are in the {weight_category} category.")
