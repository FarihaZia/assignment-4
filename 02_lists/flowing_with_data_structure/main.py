def add_three_copies(my_list, data):
    # Add the data to the list three times
    for i in range(3):
        my_list.append(data)

########## No need to edit code past this point

def main():
    message = input("Enter a message to copy: ")  # User types a message
    my_list = []  # Start with an empty list

    print("List before:", my_list)  # Show the empty list
    add_three_copies(my_list, message)  # Call the function that adds the message 3 times
    print("List after:", my_list)  # Show the updated list

if __name__ == "__main__":
    main()
