def add_time(start, duration, day="Today"):
    days = {"today":-1,"monday":0, "tuesday":1, "wednesday":2, "thursday":3, "friday":4, "saturday":5, "sunday":6}
    reverse_days = {value: key for key, value in days.items()}
    hour, the_rest = start.split(":")
    minutes, meridiem = the_rest.split()
    minutes = int(minutes)
    hour= int(hour)
    added_hour, added_minutes = duration.split(":")
    added_hour = int(added_hour)
    added_minutes =int(added_minutes)
    if meridiem.upper() == "PM" and hour != 12:
        hour += 12
    if meridiem.upper() == "AM" and hour == 12:
        hour = 0
    sum_of_hour = hour + added_hour
    sum_of_minutes = minutes + added_minutes
    sum_of_hour += sum_of_minutes // 60
    sum_of_minutes = sum_of_minutes % 60
    days_later = sum_of_hour // 24
    sum_of_hour = sum_of_hour % 24
    week_day = (days.get(day.lower()) + days_later) % 7
    final_week_day = reverse_days.get(week_day)
    if sum_of_hour == 0:
        new_hour = 12
        new_meridiem = "AM"
    elif sum_of_hour < 12:
        new_hour = sum_of_hour
        new_meridiem = "AM"
    elif sum_of_hour == 12:
        new_hour = 12
        new_meridiem = "PM"
    else:
        new_hour = sum_of_hour - 12
        new_meridiem = "PM"

    if day != "Today":
        new_time = f"{new_hour}:{sum_of_minutes:02d} {new_meridiem}, {final_week_day.title()}"
    else:
        new_time = f"{new_hour}:{sum_of_minutes:02d} {new_meridiem}"

    if days_later == 1:
            new_time += " (next day)"
    elif days_later > 1:
            new_time += f" ({days_later} days later)"

    return new_time


#print(add_time('2:59 AM', '24:00', "saturday"))