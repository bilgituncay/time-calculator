def add_time(start, duration, start_day=False):
    week = [
        'monday',
        'tuesday',
        'wednesday',
        'thursday',
        'friday',
        'saturday',
        'sunday'
    ]

    end_day = ''
    start_time = start.split()
    period = start_time[1]
    start_hm = start_time[0].split(':')
    start_min = int(start_hm[1])
    start_hour = int(start_hm[0])

    duration_hm = duration.split(':')
    duration_min = int(duration_hm[1])
    duration_hour = int(duration_hm[0])

    end_min = 0
    add_hour = 0
    total_min = start_min + duration_min
    if total_min < 60:
        end_min = total_min
    else:
        end_min = total_min % 60
        add_hour = total_min // 60
    end_hour = 0
    total_hour = start_hour + duration_hour + add_hour
    if total_hour < 13:
        end_hour = total_hour
    else:
        end_hour = total_hour % 12 or start_hour + 1

    days = 0
    while total_hour >= 12:
        if period == 'PM':
            period = 'AM'
            days +=1
        else:
            period = 'PM'
        total_hour -= 12

    new_time = f'{end_hour}:{end_min:02d} {period}'
    if start_day:
        start_day = start_day.lower()
        selected_day = int((week.index(start_day) + days) % 7)
        current_day = week[selected_day]
        new_time += f", {current_day.title()}"
    if days == 1:
        new_time += ' (next day)'
    elif days > 1:
        new_time += f' ({days} days later)'

    return (new_time)