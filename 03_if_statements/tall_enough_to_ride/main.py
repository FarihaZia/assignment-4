MINIMUM_HEIGHT: int = 50  # Minimum height required to ride

def tall_enough_extension():
    while True:
        height_input = input("How tall are you? (press Enter to quit) ")
        
        if height_input == "":
            print("Okay, goodbye!")
            break  # Exit the loop if input is empty
        
        height = float(height_input)  # Convert input to number

        if height >= MINIMUM_HEIGHT:
            print("You're tall enough to ride!\n")
        else:
            print("You're not tall enough to ride, but maybe next year!\n")

if __name__ == '__main__':
    tall_enough_extension()
