Weekdays = ["Monday","Tuesday","Wednesday","Thursday","Friday"]
Weekend = ["Saturday","Sunday"]

DayEntered = str(input('Enter the day'))

if DayEntered in Weekdays:
    print('Weekday')
elif DayEntered in Weekend:
    print('Weekend')
else:
    print('Error')
