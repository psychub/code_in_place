

def main():
    anton = 21
    beth = anton + 6
    chen = beth + 20
    drew = chen + anton
    ethan = chen

    names = {
        "anton":anton,
        "beth": beth,
        "chen": chen,
        "drew": drew,
        "ethan": ethan,
    }
    for i in names.keys():
        print(str(i), "is", names[i], "years old.")

if __name__ == '__main__':
    main()