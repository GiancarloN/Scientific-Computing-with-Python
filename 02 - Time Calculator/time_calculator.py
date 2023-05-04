def add_time(start, duration, day = ""):
    new_time = ""
    new_hour = 0
    new_minutes = 0
    new_day_cycle = ""
    number_days = 0
    day_cycle = list()
    additional_hour = 0
    day_cycle_changes = 0
    day_index = 0
    days = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"] 

    if len(day) > 0:
        day_index = days.index(day.lower())

    # Separates the starting time into a list
    start_time = list()
    tmp = start.split()
    for object in tmp:
        if ":" in object:
            tmp_time = object.split(":")
            start_time.append(int(tmp_time[0]))
            start_time.append(int(tmp_time[1]))
        else:
            day_cycle.append(object)
    
    # Separates the duration into a list
    added_time = duration.split(":")
    added_time[0] = int(added_time[0])
    added_time[1] = int(added_time[1])
    
    #Creates the AM/PM list
    if day_cycle[0] == "AM":
        day_cycle.append("PM")
    else:
        day_cycle.append("AM")

    # Calculate minutes
    new_minutes = start_time[1] + added_time[1]
    if new_minutes >= 60:
        additional_hour = 1
        new_minutes = new_minutes % 60
    new_minutes = str(new_minutes)
    if len(new_minutes) < 2:
        new_minutes = f"0{new_minutes}"

    # Calculate hours
    new_hour = start_time[0] + (added_time[0] % 12) + additional_hour
    if new_hour >= 12:
        day_cycle_changes = day_cycle_changes + 1
    if new_hour > 12:
        new_hour = new_hour % 12
    
    # Calculates the number of AM/PM cycles and the total number of additional days
    day_cycle_changes = day_cycle_changes + int(added_time[0] / 12)
    number_days = int(day_cycle_changes/ 2)
    if day_cycle[0] =="PM" and day_cycle_changes > 0:
        number_days = number_days + 1
    
    # Calculate PM or AM
    if day_cycle_changes % 2 == 0:
        new_day_cycle = day_cycle[0]
    else:
        new_day_cycle = day_cycle[1]
    
    # Calculate new day index
    new_day_index = day_index
    for _ in range(number_days):
        new_day_index = new_day_index + 1
        if number_days > 6:
            new_day_index = 0

    if len(day) == 0:
        if number_days == 0:
            new_time =f"{new_hour}:{new_minutes} {new_day_cycle}"
        elif number_days == 1:
            new_time =f"{new_hour}:{new_minutes} {new_day_cycle} (next day)"
        else:
            new_time =f"{new_hour}:{new_minutes} {new_day_cycle} ({number_days} days later)"
    else:
        if number_days == 0:
            new_time =f"{new_hour}:{new_minutes} {new_day_cycle}, {days[day_index].title()}"
        elif number_days == 1:
            new_time =f"{new_hour}:{new_minutes} {new_day_cycle}, {days[new_day_index].title()} (next day)"
        else:
            new_time =f"{new_hour}:{new_minutes} {new_day_cycle}, {days[new_day_index].title()} ({number_days} days later)"

    return new_time
