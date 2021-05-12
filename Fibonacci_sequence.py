def main():
    max_num = 10000
    Fibonacci_sequence(max_num)






def Fibonacci_sequence(max_num):
    x = 1
    number = 0
    num1 = 0
    num2 = 1
    while number < max_num:
        if x == 1:
            number = num1 + num2
            if number < max_num:
                print(number)
            num1 = number
            x += 1
        else:
            number = num1 + num2
            if number < max_num:
                print(number)
            num2 = number
            x -= 1






if __name__ == "__main__":
    main()

