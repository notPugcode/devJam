def read_letter():
    try:
        # Read a single character from the user
        char = input("Type a letter: ")[0]
        return char
    except IndexError:
        print("Please type at least one character.")
        return None
