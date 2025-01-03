# Function to determine the output based on the number
def process_number(number):
    if number > 1000:
        return number * 3  # Return triple value
    elif number > 100:
        return number * 2  # Return double value
    else:
        return number  # Return the number itself

# Main program
def main():
    try:
        # Input a number from the user
        number = float(input("Enter a number: "))
        
        # Process the number and get the result
        result = process_number(number)
        
        # Print the result
        print(f"The result is: {result}")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

# Run the main program
if __name__ == "__main__":
    main()