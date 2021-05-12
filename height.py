THRESHOLD = 50

def main():
    size = input("How tall are you (in cm)? ")
    while size:
        if int(size) > THRESHOLD:
            print("You are big enough for riding")
            size = input("How tall are you (in cm)? ")
        else:
            print("sorry you are too small! next person.")
            size = input("How tall are you (in cm)? ")


if __name__ == "__main__":
    main()