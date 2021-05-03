

def main():
    getting_name()
    print("Hello " + username)


def getting_name():
    global username
    username = input("please enter your name ")


if __name__=="__main__":
    main()




