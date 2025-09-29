"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?   When the user inputs a value that cannot be converted to an integer
2. When will a ZeroDivisionError occur?   When the user enters 0 for the denominator
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
"""
total_fraction = 0.0
try:
    count = int(input("Please enter the number of fractions to calculate: "))
    if count <= 0:
        print("Number must be a positive integer!")
    else:
        for i in range(count):
            print(f"\nFraction {i + 1}:")
            try:
                numerator = int(input("Please enter the numerator: "))
                denominator = int(input("Please enter the denominator: "))
                if denominator == 0:
                    print("Error: Denominator cannot be zero, this fraction will be skipped")
                    continue
                current_fraction = numerator / denominator
                total_fraction += current_fraction
                print(f"Current fraction value: {current_fraction}, cumulative total: {total_fraction}")
            except ValueError:
                print("Error: Numerator and denominator must be integers, this fraction will be skipped")
    print(f"\nThe sum of all valid fractions is: {total_fraction}")
except ValueError:
    print("Error: The number of fractions must be an integer!")
print("Program finished.")