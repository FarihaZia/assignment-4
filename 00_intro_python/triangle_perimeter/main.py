def main():
    # Get the 3 side lengths from the user (as float, because it can be decimal)
    side1: float = float(input("What is the length of side 1? "))
    side2: float = float(input("What is the length of side 2? "))
    side3: float = float(input("What is the length of side 3? "))

    # Calculate the perimeter
    perimeter: float = side1 + side2 + side3

    # Print the result
    print("The perimeter of the triangle is " + str(perimeter))


if __name__ == '__main__':
    main()

