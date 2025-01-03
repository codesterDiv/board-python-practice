# Function to determine the section based on the standard
def determine_section(standard):
    if 1 <= standard <= 3:
        return "Foundation Stage"
    elif 4 <= standard <= 5:
        return "Preparatory Stage"
    elif 6 <= standard <= 8:
        return "Middle Stage"
    elif 9 <= standard <= 12:
        return "Senior Stage"
    else:
        return "Invalid standard. Please enter a standard between 1 and 12."

# Main program
def main():
    try:
        # Input the standard from the user
        standard = int(input("Enter the standard of the child (1-12): "))
        
        # Determine the section
        section = determine_section(standard)
        
        # Print the result
        print(f"The section for standard {standard} is: {section}")
    except ValueError:
        print("Invalid input. Please enter a valid integer for the standard.")

# Run the main program
if __name__ == "__main__":
    main()