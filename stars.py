def print_isosceles_triangle(height):
    for i in range(height):
        # Print spaces to center the stars
        for j in range(height - i - 1):
            print(" ", end="")
        # Print stars
        for k in range(2 * i + 1):
            print("*", end="")
        # Move to the next line after each row
        print()

# Example usage
height = 5
print_isosceles_triangle(height)
