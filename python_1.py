keep_on = input("Do you want to keep playing? 'y' 'n'") == "y"



def main():
    while keep_on:
        getting_name()
        print("Hello " + username)
        keep_on



def getting_name():
    global username
    username = input("please enter your name ")




if __name__=="__main__":
    main()




