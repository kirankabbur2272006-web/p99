# bmi_calculator.py

# Input weight (kg) and height (m)
weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in meters: "))

# Calculate BMI
bmi = weight / (height ** 2)

# Display results
print(f"Weight: {weight} kg")
print(f"Height: {height} m")
print(f"BMI: {bmi:.1f}")
