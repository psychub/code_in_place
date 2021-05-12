




# Change the number of ROWS and COLUMNS to edit the size of the world
ROWS = 10
COLUMNS = 10


# Starts in a FLAT EARTH (...) in the bottom left corner [1,1] facing east.
# the user gets to enter to commands: move and turn left
# the user can stop walking if he doesnt enter anything and presses ENTER
def main():
    facing = 0
    current_position = [1,1]
    answer = greetings()
    check_input(answer, current_position, facing)
    while answer:
        answer = question()
        facing = check_input(answer, current_position, facing)
    print("You ended up at row", current_position[0], "column", str(current_position[1]) + ".")


# Greets the user and asks him the first question
def greetings():
    print("Welcome to first person Karel!")
    answer = input("What would you like to do? ")
    return answer


# asks the question and gives back the answer
def question():
    answer = input("What would you like to do? ")
    return answer


# checks the answer and depending on it calls the move or turn left function
def check_input(answer, current_position , facing):
    if answer == "move":
        current_position = move(current_position, facing)
    elif answer == "turn left":
        facing = turn_left(facing)
    return facing


# the move function moves the user forward in the current direction hes facing
def move(current_position, facing):
    end_of_world = False
    end_of_world = check_flatearth(current_position, facing)
    if end_of_world == False:
        if facing == 0:
            current_position[1] += 1
            print("You moved one step forward and now you're at row", current_position[0], "column", str(current_position[1]) + ".")
        elif facing == 1:
            current_position[0] += 1
            print("You moved one step forward and now you're at row", current_position[0], "column", str(current_position[1]) + ".")
        elif facing == 2:
            current_position[1] -= 1
            print("You moved one step forward and now you're at row", current_position[0], "column", str(current_position[1]) + ".")
        elif facing == 3:
            current_position[0] -= 1
            print("You moved one step forward and now you're at row", current_position[0], "column", str(current_position[1]) + ".")
    return current_position

# checks whether or not you have reached the end of the WORLD......don't fall
def check_flatearth(current_position, facing):
    if current_position[1] == COLUMNS and facing == 0:
        print("You can't move forward. Because the world is flat.....")
        end_of_world = True
    elif current_position[0] == ROWS and facing == 1:
        print("You can't move forward. Because the world is flat.....")
        end_of_world = True
    elif current_position[1] == 0 and facing == 2:
        print("You can't move forward. Because the world is flat.....")
        end_of_world = True
    elif current_position[0] == 0 and facing == 3:
        print("You can't move forward. Because the world is flat.....")
        end_of_world = True
    else:
        end_of_world = False
    return end_of_world


# turns the user left and checks how often the user turned left
def turn_left(facing):
    if facing < 3:
        facing += 1
    else:
        facing = 0
    check_facing(facing)
    return facing


# gets the numeric value of facing and prints the cardinal direction
def check_facing(facing):
    if facing == 0:
        print("You turned left and are now facing East again.")
    elif facing == 1:
        print("You turned left and are now facing North.")
    elif facing == 2:
        print("You turned left and are now facing West.")
    elif facing == 3:
        print("You turned left and are now facing South.")





if __name__=="__main__":
    main()