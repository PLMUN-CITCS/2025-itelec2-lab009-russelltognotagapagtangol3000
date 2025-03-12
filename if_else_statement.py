# Get input from the user
user_input = input("Enter a number: ")

try:
    # Convert input to an integer
    number = int(user_input)

    # Check if the number is even or odd using if...else
    if number % 2 == 0:
        print(f"The number {number} is Even.")
    else:
        print(f"The number {number} is Odd.")

except ValueError:
    print("Invalid input. Please enter an integer.")
