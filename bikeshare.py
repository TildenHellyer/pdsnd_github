import time
import calendar
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
    print('Hello! Let\'s explore some US bikeshare data!\n')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
   
    while True:
        city = input("Please enter city of interest: Chicago, New York City, Washington: ").lower()
        if city.lower() not in ('new york city', 'chicago', 'washington'):
            print("Not a valid city, please enter one from the list")
            continue
        else:
            break
# TO DO: get user input for month (all, january, february, ... , june)       
    while True:
        month = input("Please enter the month of interest, from January to June only or type 'all' : ").lower()
        if month.lower() not in ('all','january', 'february', 'march', 'april', 'may','june','july'):
            print("Not a valid month, please try again")
            continue
        else:
            break
# TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input("Please enter day of the week or type 'all': ").title()
        if day.lower() not in ('all','sunday', 'monday', 'tuesday','wednesday', 'thursday', 'friday','saturday'):
            print("Not a valid day of the week, please try again")
            continue
        else:
            break

   #print('-'*40)
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
    df = pd.read_csv(CITY_DATA[city])
    df["month"] = pd.DatetimeIndex(df["Start Time"]).month
    df["day_of_week"] = pd.DatetimeIndex(df["Start Time"]).weekday_name
    df["hour"] = pd.DatetimeIndex(df["Start Time"]).hour
    df["month"] = df["month"].apply(lambda x: calendar.month_name[x].lower())

    if month != 'all':
        df = df[df['month'] == month]
        
    if day != 'all':   
        df = df[df['day_of_week'] == day]
    
    return df

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    
def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    most_common_month = df['month'].mode()[0]
    print("The most common month: " + str(most_common_month.title()) )

    # TO DO: display the most common day of week
    most_common_day = df['day_of_week'].mode()[0]
    print('The most popular day of the week: ' + str(most_common_day.title()))       

    # TO DO: display the most common start hour
    most_common_hour = df['hour'].mode()[0]
    print('The most popular hour of the day: ' + str(most_common_hour))  

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    
def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_common_start_station = df['Start Station'].mode()[0]
    print('The most popular starting station: ' + str(most_common_start_station))

    # TO DO: display most commonly used end station
    most_common_end_station = df['End Station'].mode()[0]
    print('The most popular end station: ' + str(most_common_end_station))    

    # TO DO: display most frequent combination of start station and end station trip
    combination = (df['Start Station'] + " towards " +  df['End Station']).mode()[0]
    print('The most popular combination goes from station ' + str(combination))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    
def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    average_trip = df["Trip Duration"].sum()
    print('Total trips have taken ' + str(round(average_trip/3600/24)) + ' days')

    # TO DO: display mean travel time
    average_trip = df["Trip Duration"].mean()
    print('Average trip took ' + str(round(average_trip)) + ' seconds')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print('A breakdown of users:\n')
    print(user_types)

    # TO DO: Display counts of gender 
    if 'Gender' in df:
        gender = df['Gender'].fillna('No Gender given')
        print("A breakdown of genders:")
        print(gender.value_counts())
    else:
        print("\nNo gender data is available for this city")
        
    
    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df:
        birth_recent = df['Birth Year'].max()
        birth_earlist = df['Birth Year'].min()
        birth_most_common= df['Birth Year'].mode()[0]
        print('\nMost recent birth year: ' + str(birth_recent))
        print('\nEarlist year of birth: ' + str(birth_earlist))     
        print('\nMost common year of birth: ' + str(birth_most_common))
    else:
        print("\nNo birth data is available for this city")
          
   
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_bikeshare_data(df): 
    print('Last Thing!\n')
    

    line_lower = 0
    line_upper = 5
    while True:
        check_raw_data = input('\nWould you like to see 5 new lines of raw bikeshare data? Enter yes or no? \n')
        if check_raw_data in ('y', 'yes'):
            for i in range(line_lower,line_upper):
                print(df.iloc[line_lower:line_upper])
                line_lower += 5
                line_upper += 5
          #      check_raw_data = input('\nWould you like to another 5 lines of raw bikeshare data? Enter yes or no? \n') 
        elif check_raw_data in ('no', 'n'):
            return
        else:
            print("Please try again with either 'yes' or 'no'")

            
          #line_lower += 5
          #line_upper += 5
             
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_bikeshare_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
