import math

CONSTANT = 6.56784



def main():
    print(test([1, 2, 3, 4, 5, 6]))
    getting_name()



def test(numbers):
    return [num for num in numbers if not num % 2]



def getting_name():
    username = input("please enter your name: ")
    return [username]



if __name__=="__main__":
    main()




