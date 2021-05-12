YEAR = 365
DAY = 24
MINUTE = 60
SECOND = 60


def main():
    total = YEAR * DAY * MINUTE * SECOND
    print("There are 365 days in a year, 24 hours in a day, 60 minutes in an hour, and 60 seconds per minute.\n this equals: ", total,"seconds!")

    if __name__ == "__main__":
        main()