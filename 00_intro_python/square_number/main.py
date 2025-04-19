def main():
    # Ask the user for a number and convert it to float
    num: float = float(input("Type a number to see its square: "))

    # Calculate the square and display the result
    print(str(num) + " squared is " + str(num ** 2))


if __name__ == '__main__':
    main()
