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
    #add a while loop here to check if cit given is in list of cities
    cities=['chicago','washington','new york city']
    while(1):
        city=input(print("Which city do you wish to filter by? chicago,new york city,washington"))
        if city in cities:
            print("You have selected ",city)
            break
        else:
            print("Please enter a valid choice")
            city=input()
            break
            
        
        
        

    # TO DO: get user input for month (all, january, february, ... , june)
    #adda while loop here as well
    months=['all','january','february','march','april','may','june']
    while(1):
        month=input(print("Which month do you wish to filter by? all,january,february,march,april,may,june"))
        if month in months:
            print("You have selected ",month)
            break
        else:
            print("Please enter a valid choice")
            month=input()
            break

    #add a while loop here as well
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    days=['all','monday','tuesday','wednesday','thursday','friday','saturday','sunday']
    day=input(print("Which day do you wish to filter by? all,monday,tuesday,wednesday,thursday,friday?"))

    while(1):
        if day in days:
            print("You have selected ",day)
            break
        else:
            print("Please enter a valid choice")
            day=input()
            break


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
    df=pd.read_csv(CITY_DATA[city])
    # convert the Start Time column to datetime
    df['Start Time']=pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] =df['Start Time'].dt.month
    df['day_of_week'] =df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month =months.index(month)+1
    
        # filter by month to create the new dataframe
        df=df[df['month']==month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df=df[df['day_of_week']==day.title()]
    
    return df
def display_data(df):
    print("Printing first five lines...")
    print(df.head())
    ch=input(print("Do you wish to view the next five lines? yes,no"))
    i=5
    while ch=='yes':
        print(df.iloc[i:i+5,:])
        i=i+5
        ch=input(print("Do you wish to view the next five lines? yes,no"))


    return df
    


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    df['Start Time']=pd.to_datetime(df['Start Time'])
    
    
    # TO DO: display the most common month
    df['month'] =df['Start Time'].dt.month
    popular_month =df['month'].mode()[0]
    print('Most Frequent Month:', popular_month)


    # TO DO: display the most common day of week
    df['day_of_week'] =df['Start Time'].dt.weekday_name
    popular_day=df['day_of_week'].mode()[0]
    print('Most Frequent Day of Week:', popular_day)


    # TO DO: display the most common start hour
    df['hour'] =df['Start Time'].dt.hour
    popular_hour =df['hour'].mode()[0]
    print('Most Frequent Start Hour:', popular_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start_station=df.loc[:,"Start Station"].mode()[0]
    print("Most Popular Start Station: ",popular_start_station)

    # TO DO: display most commonly used end station
    popular_end_station=df.loc[:,"End Station"].mode()[0]
    print("Most Popular End Station: ",popular_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    popular_trip=(df['Start Station']+','+df['End Station']).mode()[0]
    print("Most Popular Trip: ",popular_trip)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_trip_duration=df['Trip Duration'].sum()
    print("Total Travel Time: ",total_trip_duration)

    # TO DO: display mean travel time
    mean_trip_duration=df['Trip Duration'].mean()
    print("Average Travel Time: ",mean_trip_duration)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print(user_types)

    # TO DO: Display counts of gender
    if 'Gender' in df:
        gender_count=df['Gender'].value_counts()
        print("Gender types: ",gender_count)
    else:
        print("This dataset does not have a Gender column")   
    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df:
        earliest=df['Birth Year'].min()
        recent=df['Birth Year'].max()
        common=df['Birth Year'].mode()[0]
        print("Earliest Birth Year: ",int(earliest))
        print("Recent Birth Year: ",int(recent))
        print("Common Birth Year: ",int(common))
    else:
        print("This dataset does not have a BirthYear column")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break
#Write  a function to get the name of city that the user wants and display the list till they want you to stop

if __name__ == "__main__":
	main()
