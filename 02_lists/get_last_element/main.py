def get_last_element(lst):
    """
    Prints the last element of the provided list.
    """
    print(lst[len(lst) - 1])  # Method 1: last element using length
    # OR just use this simpler line:
    # print(lst[-1])  # Method 2: using negative indexing (Python feature)


def get_lst():
    """
    Prompts the user to enter one element of the list at a time and returns the resulting list.
    """
    lst = []
    elem = input("Please enter an element of the list or press enter to stop. ")
    while elem != "":
        lst.append(elem)
        elem = input("Please enter an element of the list or press enter to stop. ")
    return lst


def main():
    lst = get_lst()             # User se list lo
    get_last_element(lst)       # List ka last element print karo


if __name__ == '__main__':      # Python script run hone par yeh call hota hai
    main()
