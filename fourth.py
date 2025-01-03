# Function to determine pass or fail
def check_pass_fail(marks):
    total_marks = sum(marks)
    percentage = total_marks / len(marks)
    
    # Check if the student has passed
    if percentage > 33:
        return True, percentage
    else:
        return False, percentage

# Main program
def main():
    # Input marks for 3 subjects
    marks = []
    subjects = ['English', 'Mathematics', 'Social Studies']
    
    for subject in subjects:
        while True:
            try:
                mark = float(input(f"Enter marks for {subject} (out of 100): "))
                if 0 <= mark <= 100:  # Assuming marks are out of 100
                    marks.append(mark)
                    break
                else:
                    print("Please enter marks between 0 and 100.")
            except ValueError:
                print("Invalid input. Please enter a number.")

    # Check pass or fail
    passed, percentage = check_pass_fail(marks)

    # Print result
    if passed:
        print(f"\nThe student has passed with a percentage of {percentage:.2f}%.")
    else:
        print(f"\nThe student has failed with a percentage of {percentage:.2f}%.")

# Run the main program
if __name__ == "__main__":
    main()