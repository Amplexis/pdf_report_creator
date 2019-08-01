import datetime
from datetime import timedelta

def current_week():
    week_dict = {'Tuesday': 1,
                 'Wednesday': 2,
                 'Thursday': 3,
                 'Friday': 4,
                 'Saturday': 5,
                 'Sunday': 6}

    #  Get current date and day
    x = datetime.datetime.now()
    day_of_week = x.strftime('%A')

    #  Weeks run Monday - Sunday
    #  Get the date of this week's Monday and Sunday
    if day_of_week != 'Monday':
        subtract_value = week_dict[day_of_week]
        start_date = x - timedelta(days=subtract_value)
        end_date = start_date + timedelta(days=6)
    else:
        start_date = x
        start_date = start_date - timedelta(days=7)
        end_date = start_date + timedelta(days=6)

    month1 = start_date.strftime('%B')
    day1 = start_date.day
    year1 = start_date.year
    month2 = end_date.strftime('%B')
    day2 = end_date.day
    year2 = end_date.year
    if year1 != year2:
        string = 'Week of {} {}, {} - {} {}, {}'.format(month1, day1,year1, month2, day2, year2)
    else:
        string = 'Week of {} {} - {} {}, {}'.format(month1, day1, month2, day2, year1)

    return string
