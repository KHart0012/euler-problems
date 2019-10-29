month_dict = {
    'january' : 31,
    'february' : 28,
    'february-leap' : 29,
    'march' : 31,
    'april' : 30,
    'may' : 31,
    'june' : 30,
    'july' : 31,
    'august' : 31,
    'september' : 30,
    'october' : 31,
    'november' : 30,
    'december' : 31
}

def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0 and not year % 400 == 0:
            return False
        return True
    return False


days = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']
months = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december']
day_counter = 1
month_counter = 'january'
month_num = 0
year_counter = 1900

def next_day_week(day):
    idx = days.index(day)
    return days[idx + 1]

def next_month(month, year):
    if month == 'january' and is_leap_year(year):
        return 'february-leap'
    if month == 'february-leap':
        return months[2]
    idx = months.index(month)
    return months[idx + 1]

def increment_day(date):
    new_date = []

    # handle moving to next day of week
    if date[0] == days[6]:
        new_date.append(days[0])
    else:
        new_date.append(next_day_week(date[0]))
    
    # handle day of month and month change
    if date[1] + 1 > month_dict[date[2]]:
        # if it is the end of december, add january first and increment year
        if date[2] == months[11]:
            new_date.append(1)
            new_date.append(months[0])
            new_date.append(date[3] + 1)
            return new_date
        # end of month that is not december
        new_date.append(1)
        new_date.append(next_month(date[2], date[3]))
        new_date.append(date[3])
        return new_date
    # just add one to the day
    new_date.append(date[1] + 1)
    new_date.append(date[2])
    new_date.append(date[3])
    return new_date
    

date = [days[1], day_counter, month_counter, year_counter]
sundays = 0
while not (date[3] == 2000 and date[1] == 31 and date[2] == 'december'):
    date = increment_day(date)
    if date[1] == 1 and date[0] == days[0] and date[3] > 1900:
        sundays += 1

print(sundays)