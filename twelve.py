# Function to check license eligibility based on age
def check_license_eligibility(age):
    if age < 18:
        return "You are not eligible to get a license. You must be at least 18 years old."
    elif age > 70:
        return "You are not eligible to get a license. The maximum age limit is 70 years."
    else:
        return "You are eligible to get a license."

# Main program
def main():
    try:
        # Input age from the user
        age = int(input("Enter your age: "))
        
        # Check if the user is eligible for a license
        eligibility_message = check_license_eligibility(age)
        
        # Print the eligibility message
        print(eligibility_message)
    except ValueError:
        print("Invalid input. Please enter a valid integer for your age.")

# Run the main program
if __name__ == "__main__":
    main()