def seconds_difference(time_1, time_2):
    """ (number, number) -> number

    Return the number of seconds later that a time in seconds
    time_2 is than a time in seconds time_1.
        
    >>> seconds_difference(1800.0, 3600.0)
    1800.0
    >>> seconds_difference(3600.0, 1800.0)
    -1800.0
    >>> seconds_difference(1800.0, 2160.0)
    360.0
    >>> seconds_difference(1800.0, 1800.0)
    0.0
    """
    return time_2 - time_1

def hours_difference(time_1, time_2):
    """ (number, number) -> float

    Return the number of hours later that a time in seconds
    time_2 is than a time in seconds time_1.
        
    >>> hours_difference(1800.0, 3600.0)
    0.5
    >>> hours_difference(3600.0, 1800.0)
    -0.5
    >>> hours_difference(1800.0, 2160.0)
    0.1
    >>> hours_difference(1800.0, 1800.0)
    0.0
    """
    seconds_in_hour = 3600
    return (time_2 - time_1)/seconds_in_hour


def to_float_hours(hours, minutes, seconds):
    """ (int, int, int) -> float

    Return the total number of hours in the specified number
    of hours, minutes, and seconds.

    Precondition: 0 <= minutes < 60  and  0 <= seconds < 60

    >>> to_float_hours(0, 15, 0)
    0.25
    >>> to_float_hours(2, 45, 9)
    2.7525
    >>> to_float_hours(1, 0, 36)
    1.01
    """
    #converting minutes to hours' decimals
    minutes_to_float = minutes/60
    #converting seconds to hours' decimals
    seconds_to_float = seconds/3600
    #adding everything together
    return hours + minutes_to_float + seconds_to_float


def to_24_hour_clock(hours):
    '''(number) -> number

    hours is a number of hours since midnight. 
    Return the hour as seen on a 24-hour clock.

    Precondition: hours >= 0

    >>> to_24_hour_clock(24)
    0
    >>> to_24_hour_clock(48)
    0
    >>> to_24_hour_clock(25)
    1
    >>> to_24_hour_clock(4)
    4
    >>> to_24_hour_clock(28.5)
    4.5
    '''

    return hours % 24

### Write your get_hours function definition here:
def get_hours(seconds):
    '''(number) -> int
    Seconds is the number of seconds since midnight.
    
    Return hour equivalent of provided seconds since midnight 
    as seen on 24-hour clock

    >>> get_hours(4200)
    1
    >>> get_hours(72000)
    20
    >>> get_hours(86399)
    23
    >>> get_hours(87000)
    0
    '''
    #calculates up to 23, resets @ 86400(seconds a day) 
    #number of given second //int div by number of seconds in hour 
    return to_24_hour_clock(seconds//3600)

### Write your get_minutes function definition here:
def get_minutes(seconds):
    ''' (number) -> int
    Seconds is the number of seconds since midnight.
    
    Return minutes not included into full hours that passed since midnight.
    
    >>> get_minutes(4200)
    10
    >>> get_minutes(72000)
    0
    >>> get_minutes(86399)
    59
    >>> get_minutes(87000)
    10
    '''
    #get the reminder of the division - number of seconds not included into full hour
    #int divide the remainder by 60 s to get minutes
    return (seconds%3600)//60

### Write your get_seconds function definition here:
def get_seconds(seconds):
    '''(number) -> number
    Seconds is the number of seconds since midnight.
    
    Return seconds left that are not included into full hours and minutes
    >>> get_seconds(4200)
    0
    >>> get_seconds(86399)
    59
    >>> get_seconds(86514)
    54
    '''
    #(seconds%86400)%3600 = seconds left after hours
    # = seconds left after minutes
    return (seconds%86400)%3600 - (get_minutes(seconds)*60)
    


def time_to_utc(utc_offset, time):
    """ (number, float) -> float

    Return time at UTC+0, where utc_offset 
    is the number of hours away from UTC+0.

    >>> time_to_utc(+0, 12.0)
    12.0
    >>> time_to_utc(+1, 12.0)
    11.0
    >>> time_to_utc(-1, 12.0)
    13.0
    >>> time_to_utc(-11, 18.0)
    5.0
    >>> time_to_utc(-1, 0.0)
    1.0
    >>> time_to_utc(-1, 23.0)
    0.0
    """
    return to_24_hour_clock((time-utc_offset))



def time_from_utc(utc_offset, time):
    """ (number, float) -> float

    Return UTC time in time zone utc_offset.

    >>> time_from_utc(+0, 12.0)
    12.0
    >>> time_from_utc(+1, 12.0)
    13.0
    >>> time_from_utc(-1, 12.0)
    11.0
    >>> time_from_utc(+6, 6.0)
    12.0
    >>> time_from_utc(-7, 6.0)
    23.0
    >>> time_from_utc(-1, 0.0)
    23.0
    >>> time_from_utc(-1, 23.0)
    22.0
    >>> time_from_utc(+1, 23.0)
    0.0
    """
    return to_24_hour_clock((time+utc_offset))


