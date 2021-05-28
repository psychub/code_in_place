import numpy as np
import pandas as pd
from matplotlib import pyplot as plt





"""
This is my final project of Code in Place.
The user has the chance to enter a name of a country and get a line graph showing the development of the Corona cases.
"""


def main():
    Code_in_place()
    country = asking_for_country()
    while country:
        clean_data, provinces = preparing_data(country)
        if len(provinces) > 1:
            plotting_province(clean_data, provinces)
        else:
            plotting_country(clean_data)
        country = asking_for_country()





# creates a new column containing the dates with double digits for single digit dates EXAMPLE: (1 -> 01)
def match_country_dates(data):
    for days in data["day"]:
        if len(days) == 1:
            data["day"] = data["day"].replace(days, "0{}".format(days))
    for months in data["month"]:
        if len(months) == 1:
            data["month"] = data["month"].replace(months, "0{}".format(months))
    data["new_date"] = data["month"]+ "/"+ data["day"]+  "/20"+  data["year"]
    # data = data.set_index(keys="new_date")

    return data




# transforms the dates from the intervention.csv from Germany
def transform_dates(data):
    for date in data["date"]:
        new_date_d = date[0:2]
        new_date_m = date[3:5]
        new_date_y = date[6:]
        new_date = new_date_m+"/"+new_date_d+"/"+new_date_y
        data["date"] = data["date"].replace([date], new_date)
    return data





# creating markups for interventions
def adding_interventions(data_cases):
    index_matches = []
    with open("interventions.csv") as f:
        interventions = pd.read_csv(f)
        interventions_trans = transform_dates(interventions)
        inter_text = list(interventions_trans["interventions"])
        threshold = max(data_cases["cases"]) / 3
        for i in range(len(interventions["date"])):
            date = interventions_trans["date"].iloc[i]
            ind = data_cases.index[data_cases['new_date'] == date].to_list()
            index_matches.append(ind[0])
        for i in range(len(index_matches)):
            inter_pos = data_cases["cases"].loc[index_matches[i]]
            if inter_pos >= threshold:
                plt.annotate(inter_text[i], xy=(index_matches[i]-10,inter_pos), xytext=(index_matches[i]/2,inter_pos), arrowprops=dict(facecolor="black"))
            else:
                plt.annotate(inter_text[i], xy=(index_matches[i]-10,inter_pos), xytext=(index_matches[i]/2,inter_pos+1), arrowprops=dict(facecolor="black"))


# plots the different Provinces if there are more than one
def plotting_province(data, provinces):
    for province in provinces:
        filt = (data["Province/State"]==province)
        province_cases = list(data["cases"].loc[filt])
        province_dates = list(data["date"].loc[filt])
        year = list(data["year"].loc[filt])
        year_20 = year.count("20")
        year_21 = year.count("21")
        plt.xticks([0,year_20/2 , year_20], labels=["Jan-20", "July-20", "Jan-21"])
        plt.xlabel("Time (month-year)")
        plt.ylabel("Cases in millions")
        plt.title("Covid 19 cases in "+ province)
        plt.plot(province_dates, province_cases)
        plt.show()





# creating a line graph diplaying the development of corona cases in the country of interest
def plotting_country(data):
    X = list(data["date"])
    Y = list(data["cases"])
    year = list(data["year"])
    year_20 = year.count("20")
    year_21 = year.count("21")
    plt.xticks([0,year_20/2 , year_20], labels=["Jan-20", "July-20", "Jan-21"])
    plt.xlabel("Time (month-year)")
    plt.ylabel("Cases in millions")
    country = data["Country/Region"].iloc[1]
    plt.title("Covid 19 cases in "+ country)

    if country == "Germany":
        adding_interventions(data)
    plt.plot(X, Y)

    plt.show()





# creating a new nominal variable to be able to group by season
def creating_seasons(country_of_interest):
    country_of_interest[["month", "day", "year"]] = country_of_interest["date"].str.split("/", expand=True)
    country_of_interest["season"] = country_of_interest["month"]

    seasons = {
        "winter": [12, 1, 2],
        "spring": [3, 4, 5],
        "summer": [6, 7, 8],
        "autumn": [9, 10, 11]
    }

    for month in country_of_interest["season"]:
        for keys in seasons.keys():
            if month in str(seasons[keys]):
                country_of_interest['season'] = country_of_interest['season'].replace([month], keys)

    return country_of_interest








# filtering the country our user is interested in out
def preparing_data(Country):
    with open("time_series_covid19_confirmed_global.csv") as f:
        Covid = pd.read_csv(f)
        filt = (Covid["Country/Region"]==Country)
        country_of_interest = Covid.loc[filt]

        # handling NaNs
        country_of_interest = country_of_interest.fillna('Unknown Province')
        provinces = list(country_of_interest["Province/State"])

        # wide to long
        country_of_interest = pd.melt(country_of_interest, id_vars=["Country/Region","Province/State", "Long", "Lat"],var_name="date",value_name="cases")
        for cases in country_of_interest["cases"]:
            if cases != 0:
                country_of_interest['cases'] = country_of_interest['cases'].replace([cases], (cases/1000000))



        country_of_interest = creating_seasons(country_of_interest)
        country_of_interest = match_country_dates(country_of_interest)

    return country_of_interest, provinces







def asking_for_country():
    country = input("Please Enter the country you want to get info about: ")
    return country


def Code_in_place():
    print("Dear Chris, Mehran and all of the students and section leaders of Code in Place 2021,\n\n"
          "I want to thank you all for this awesome experience and the knowledge you provided for us. \n"
          "But I want to thank you specially for the enormous positive energy you conveyed every week of Code in Place.\n"
          "For me, coding now and always will be positively associated with community, fun and kindness.\n"
          "You didn't just provide and enhance knowledge, you ignited motivation\n"
          "that will help me far more in the future, than the knowledge I've obtained.\n"
          "So again thank you all and hopefully you all stay healthy and strong trough the last bits of this pandemic\n"
          "\nTill then Linus\n")


if __name__=="__main__":
    main()