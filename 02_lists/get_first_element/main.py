def get_first_element(lst):
    """
    Prints the first element of a provided list.
    """
    print(lst[0])  # List ka pehla element print karo (0th index)

# --- Neeche ka code user se list input lene ke liye hai ---

def get_lst():
    """
    User se ek ek element poochh kar list banata hai.
    Jab user kuch na daale (empty enter kare), input band ho jata hai.
    """
    lst = []  # Khali list bana lo
    elem: str = input("Please enter an element of the list or press enter to stop. ")
    while elem != "":
        lst.append(elem)  # Jo bhi input mile, list mein daal do
        elem = input("Please enter an element of the list or press enter to stop. ")
    return lst  # List wapas return karo

def main():
    lst = get_lst()  # User se list lo
    get_first_element(lst)  # List ka pehla element print karo

if __name__ == '__main__':
    main()
