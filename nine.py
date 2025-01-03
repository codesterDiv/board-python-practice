# Function to check if the number is odd or even
def check_odd_even(number):
    if number % 2 == 0:
        return "even"
    else:
        return "odd"

# Main program
def main():
    try:
        # Input a number from the user
        number = int(input("Enter a number: "))
        
        # Check if the number is odd or even
        result = check_odd_even(number)
        
        print(f"The number {number} is {result}.")
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

# Run the main program
if __name__ == "__main__":
    main()
