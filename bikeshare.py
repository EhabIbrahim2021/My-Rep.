import time
import pandas as pd
import numpy as np

CITY_DATA = { 'ch': 'chicago.csv',
              'ny': 'new_york_city.csv',
              'w': 'washington.csv' }

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
    city = input('Kindly specify a city to proceed, please type ch for Chicago, ny for New York, or w for Washington : \n').lower()
    while city not in CITY_DATA.keys():
        city = input('Please check your answer and specify a city to proceed, please type ch for Chicago, ny for New York, or w for Washington : \n').lower()
        
   

    # TO DO: get user input for month (all, january, february, ... , june)
    months = ['all','january' , 'february', 'march', 'april', 'may', 'june']
    month = input('Kindly specify the desired month to explore either january , february, march, april, may, june. OR all to explore all months : \n').lower()
    while month not in months:
          month = input('Please check your answer and specify a month to explore either january , february, march, april, may, june. OR all to explore all months : \n').lower()
                        
                  

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    days = ['all','saturday','sunday','monday','tuesday','wednesday','thursday','friday']
    day = input('Kindly specify the desired day to explore either saturday,sunday, monday,tuesday,wednesday,thursday,friday. OR all to explore all days : \n').lower()
    while day not in days:
        day = input('Please check your answer and specify a day to explore either saturday,sunday, monday,tuesday,wednesday,thursday,friday. OR all to explore all days : \n').lower()
          
     
        
               
        
        

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
    # load data file to data frame
    df = pd.read_csv(CITY_DATA[city])
    
    #Convert Start time to readable datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
    #Create month column
    df['month'] = df['Start Time'].dt.month
    
    #Create day column
    df['day'] = df['Start Time'].dt.weekday_name
    
    # Create hour column
    df['hour'] = df['Start Time'].dt.hour
    
    
        
    # Filter & data frame by month
    #indexing Month
    if month != 'all':      
        months = ['all','january' , 'february', 'march', 'april', 'may', 'june']
        month=months.index(month)
        
        df = df[df['month'] == month]
        
    
        
    #Filter & data frame by day
    if day != 'all':
        df = df[df['day'] == day.title()]
        

    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    
    # TO DO: display the most common month
    common_month= df['month'].mode()[0]
    print('The most common month is : ',common_month)

    # TO DO: display the most common day of week
    common_day= df['day'].mode()[0]
    print('The most common day is : ', common_day)

    # TO DO: display the most common start hour
    common_hour= df['hour'].mode()[0]
    print('The most common hour is : ', common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    print('The most common Start Station is : ', common_start_station)

    # TO DO: display most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    print('The most common End Station is : ', common_end_station)
    
    # TO DO: display most frequent combination of start station and end station trip
    df['route']=df['Start Station'] + '-' + df['End Station']
    common_combination_stations=df['route'].mode()[0]
    print('The most frequent combination of Start & End Stations is : ', common_combination_stations)
        

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum().sum()
    print('Total Travel Time is : ', total_travel_time, ' seconds')
    

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('Average of Travel Time is : ', mean_travel_time, ' seconds')
    

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_counts= df['User Type'].value_counts()
    print('The counts of user types are : \n',user_counts)
    
    # TO DO: Display counts of gender
    if city != 'w':
        gender_counts = df['Gender'].value_counts()
        print('The counts of user gender are : \n', gender_counts)
        # TO DO: Display earliest, most recent, and most common year of birth
        earliest_birth_year = df['Birth Year'].min()
        print('The oldest user was born in : ',earliest_birth_year)
        most_recent_birth_year = df['Birth Year'].max()
        print('The youngest user was born in : ' , most_recent_birth_year)
        common_birth_year = df['Birth Year'].mode()[0]
        print('The common birth year is : ', common_birth_year)
              

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    
    
def raw_data(df):
    print('Raw data is available for review \n')
    
    start=0
    display_opt= input('Please specify if you want to review the raw data in bulks, each bulk is of 5 rows. Please type yes to proceed or no to exit : \n').lower()
    answer=['yes','no']
    while display_opt not in answer :
        display_opt= input('Invalid entry, if you want to review the raw data in bulks, each bulk is of 5 rows. Please type yes to proceed or no to exit : \n').lower()
    
    
    if display_opt =='yes':
        while display_opt =='yes':
            print(df.iloc[start:start+5])
            start+=5
            display_opt = input('Do you want another 5 rows ? , Please type yes to proceed or no to exit : \n').lower()
            
       
        
    else:
        print('Thank you for using our application, hope we presented a helpful material')
        
        
 
    

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)
        raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
    
        

