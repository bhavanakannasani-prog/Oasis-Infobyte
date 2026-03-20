def calculate_bmi(weight, height):
    return weight / (height ** 2)

def get_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 24.9:
        return "Normal weight"
    elif bmi < 29.9:
        return "Overweight"
    else:
        return "Obese"

def main():
    print("🧮 BMI Calculator (CLI)")

    try:
        weight = float(input("Enter weight (kg): "))
        height = float(input("Enter height (m): "))

        if weight <= 0 or height <= 0:
            print("❌ Values must be positive.")
            return

        bmi = calculate_bmi(weight, height)
        category = get_category(bmi)

        print(f"\n📊 Your BMI: {bmi:.2f}")
        print(f"📌 Category: {category}")

    except ValueError:
        print("❌ Please enter valid numbers.")

if __name__ == "__main__":
    main()