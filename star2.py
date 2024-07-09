def print_right_angle_triangle(height):
    for i in range(1, height + 1):
        # Print stars for the current row
        for j in range(i):
            print("*", end="")
        # Move to the next line after each row
        print()

# Example usage
height = 5
print_right_angle_triangle(height)
