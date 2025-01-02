def calculate_area():
    shape = input("Enter the shape (circle, rectangle, triangle): ").lower()

    if shape == "circle":
        radius = float(input("Enter the radius of the circle: "))
        area = 3.14159 * radius ** 2  # Area of circle = πr²
        print(f"The area of the circle is: {area:.2f}")

    elif shape == "rectangle":
        length = float(input("Enter the length of the rectangle: "))
        breadth = float(input("Enter the breadth of the rectangle: "))
        area = length * breadth  # Area of rectangle = l * b
        print(f"The area of the rectangle is: {area:.2f}")

    elif shape == "triangle":
        base = float(input("Enter the base of the triangle: "))
        height = float(input("Enter the height of the triangle: "))
        area = 0.5 * base * height  # Area of triangle = 0.5 * b * h
        print(f"The area of the triangle is: {area:.2f}")

    else:
        print("Invalid shape entered. Please enter circle, rectangle, or triangle.")

# Call the function to execute the program
calculate_area()