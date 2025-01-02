# Function to calculate incremented salary
def calculate_incremented_salary(salary):
    if salary > 100000:
        increment = salary * 0.10  # 10% increment
    else:
        increment = salary * 0.07  # 7% increment
    
    incremented_salary = salary + increment
    return incremented_salary

# Main program
try:
    # Input salary from user
    salary = float(input("Enter the salary of the employee: "))
    
    # Calculate incremented salary
    incremented_salary = calculate_incremented_salary(salary)
    
    # Print the incremented salary
    print(f"The incremented salary is: {incremented_salary:.2f}")
except ValueError:
    print("Please enter a valid number for the salary.")
