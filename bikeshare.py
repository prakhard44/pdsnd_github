import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    citylist=[k for k in CITY_DATA]
    city=""
    while city not in citylist:
        if city!="":
            print("please enter a valid input")
        city=input("please enter the city you want to analyse data for: ").lower()

    # TO DO: get user input for month (all, january, february, ... , june)
    monthlist=["january","february","march","april","may","june","all"]
    month=""
    while month not in monthlist:
        if month!="":
            print("please enter a valid input")
        month=input("enter the month you want to analyse data for or enter all:").lower()


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    daylist=["monday","tuesday","wednesday","thursday","friday","saturday","sunday","all"]
    day=""
    while day not in daylist:
        if day!="":
            print("please enter a valid input")
        day=input("please enter weekday you want to analyse data for or enter all:").lower()

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    # load data file into a dataframe using inbuilt function
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]


    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month from the Start Time column to create an month column
    df['month'] = df['Start Time'].dt.month

    # find the most popular month
    popular_month = df['month'].mode()[0]

    print('Most Popular Start month:', popular_month)

    # TO DO: display the most common day of week
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month from the Start Time column to create a week column
    df['week'] = df['Start Time'].dt.weekday_name

    # find the most popular hour
    popular_week = df['week'].mode()[0]

    print('Most Popular Start weekday:', popular_week)

    # TO DO: display the most common start hour
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract hour from the Start Time column to create an hour column
    df['hour'] = df['Start Time'].dt.hour

    # find the most popular hour
    popular_hour = df['hour'].mode()[0]

    print('Most Popular Start Hour:', popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start_station=df['Start Station'].mode()[0]
    print('Most popular start station:',popular_start_station)
    # TO DO: display most commonly used end station
    popular_end_station=df['End Station'].mode()[0]
    print('Most common end station:',popular_end_station)
    # TO DO: display most frequent combination of start station and end station trip
    df['Popular Route']=df['Start Station']+" to "+df['End Station']
    popular_route=df['Popular Route'].mode()[0]
    print('Most common route:',popular_route)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)



def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time=df['Trip Duration'].sum()
    print("total travel time is:",total_travel_time)
    # TO DO: display mean travel time
    mean_travel_time=df['Trip Duration'].mean()
    print("mean travel time is:",mean_travel_time)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df,city):
    """Displays statistics on bikeshare users."""
    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types= df['User Type'].value_counts()
    print("count of user types: \n")
    print(user_types)


    # TO DO: Display counts of gender

    try:
        genders= df['Gender'].value_counts()
        print("\ncount of gender:")
        print(genders)

    # TO DO: Display earliest, most recent, and most common year of birth
        earliest_year=df['Birth Year'].min()
        print("the earliest birth year is:",earliest_year)
        recent_year=df['Birth Year'].max()
        print("the most recent birth year is:",recent_year)
        most_common_year=df['Birth Year'].mode()[0]
        print("the most common birth year is:",most_common_year)

    except:
        print("we don't have any further user data for {}".format(city))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def print_raw_input(df):
    """printing raw data till the user wants"""
    option=["y","n"]
    raw_input=input("do you want to look at the raw stats for your city, press y or n:").lower()
    while raw_input not in option:
        raw_input=input("please enter y or n:")

    i=0

    while i<=len(df):
        if raw_input=="y":
            print(df.iloc[i:i+5])
            i=i+5
            raw_input=input("do you want to contniue, press y or n:").lower()
            while raw_input not in option:
                raw_input=input("please enter y or n:")
        else:
            break





def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)
        df = load_data(city, month, day)
        print_raw_input(df)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
	main()
