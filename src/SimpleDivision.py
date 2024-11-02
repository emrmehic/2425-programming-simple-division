# SimpleDivision.py

def simple_division():
    try:
        # Prompt the user to enter two numbers
        numerator = float(input("Enter the numerator: "))
        denominator = float(input("Enter the denominator: "))

        # Perform the division
        result = numerator / denominator

        # Display the result
        print("Result:", result)

    except ZeroDivisionError:
        # Handle division by zero
        print("Error: Cannot divide by zero.")

    except ValueError:
        # Handle invalid input that cannot be converted to float
        print("Error: Please enter a valid number.")

# Run the simple division function
if __name__ == "__main__":
    simple_division()
