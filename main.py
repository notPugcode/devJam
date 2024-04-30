print("Hello World")


def main():
    while True:
        try:
            # Read a single character from the user
            char = input("Type a letter: ")[0]
            print("You typed:", char)
            
            # If the user types 'q', exit the loop
            if char.lower() == 'q':
                break
        except IndexError:
            print("Please type at least one character.")

if __name__ == "__main__":
    main()