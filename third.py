# Function to calculate total marks, percentage, and grade
def calculate_results(marks):
    total_marks = sum(marks)
    percentage = total_marks / len(marks)
    
    # Determine grade based on percentage
    if percentage >= 91:
        grade = 'A'
    elif percentage >= 71:
        grade = 'B'
    elif percentage >= 51:
        grade = 'C'
    elif percentage >= 33:
        grade = 'D'
    else:
        grade = 'E'
    
    return total_marks, percentage, grade

# Main program
def main():
    # Input student details
    roll_no = input("Enter Roll No: ")
    name = input("Enter Name: ")
    student_class = input("Enter Class: ")
    section = input("Enter Section: ")
    
    # Input marks for 5 subjects
    marks = []
    for i in range(1, 6):
        while True:
            try:
                mark = float(input(f"Enter marks for Subject {i}: "))
                if 0 <= mark <= 80:  # Assuming marks are out of 80
                    marks.append(mark)
                    break
                else:
                    print("Please enter marks between 0 and 80.")
            except ValueError:
                print("Invalid input. Please enter a number.")

    # Calculate results
    total_marks, percentage, grade = calculate_results(marks)

    # Print report card
    print("\n--- Report Card ---")
    print(f"Roll No: {roll_no}")
    print(f"Name: {name}")
    print(f"Class: {student_class}")
    print(f"Section: {section}")
    print(f"Total Marks: {total_marks}")
    print(f"Percentage: {percentage:.2f}%")
    print(f"Grade: {grade}")

# Run the main program
if __name__ == "__main__":
    main()