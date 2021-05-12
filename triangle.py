def main():
    side_sum = sides()
    print("The perimeter of the triangle is", side_sum)

def sides():
    triangle = 1
    side = []
    for i in range(3):
        text = "What is the length of side "+ str(triangle) +"? "
        side.append(float(input(text)))
        triangle += 1
    return sum(side)

if __name__ == "__main__":
    main()