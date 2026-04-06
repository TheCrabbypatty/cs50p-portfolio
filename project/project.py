import sys
from tabulate import tabulate
import re
import random

# Global dictonaries that nest lists, which represent different aspects of data.
# Mass list controls the display
global mass_list
mass_list = {i: ["Free"] * 7 for i in range(1, 25)}
# Event list stores all the event descriptions.
global event_list
event_list = {i: [""] * 7 for i in range(1, 25)}
# Time dict stores the events, and the specific time and date in which they occur.
global time_dict
time_dict = {}

# Main function


def main():
    # Seperator
    print("~" * 96)
    # Instructions
    print(
        f"Instructions: Free means free space, occupied means the time block is occupied"
    )
    while True:
        print("~" * 96)
        print(create_calendar())
        while True:
            # Loop that determines which of the 3 actions to do (create, delete, view).
            create_del = input(
                'Create, delete, or check a event? \n1. Only put "create" if you want to create an event.\n2. Only put "delete" if you want to delete an event.\n3. Only put "view" if you want to view a specfic event.\nAll other values will not be accepted.\nInput: '
            )
            if create_del.lower().strip() == "create":
                day = days()
                AM, PM = time()
                if is_valid_event(AM, PM, day) == False:
                    print(
                        "Event cannot be created. Overlapping events are not supported."
                    )
                    break
                else:
                    create_event(AM, PM, day)
                    print(create_calendar())
                    break
            elif create_del.lower().strip() == "delete":
                delete_event()
                print(create_calendar())
                break
            elif create_del.lower().strip() == "view":
                day = days()
                view_event(view_time(), day)
                break
            else:
                print("Invalid input given")

        while True:
            exit = input("Exit calendar? (Y/n): ")
            if exit.lower().strip() == "y":
                sys.exit()
            elif exit.lower().strip() == "n":
                break
            else:
                print("Invalid reponse, please enter Y for yes, or n for no")
                pass

# Specialized function validates the day.


def days():
    while True:
        days_list = [
            "monday",
            "tuesday",
            "wednesday",
            "thursday",
            "friday",
            "saturday",
            "sunday",
        ]
        print(
            "To add, delete or view events, specify the day in one word (e.g Monday or Tuesday).\nThis calendar does not support events that span over days."
        )
        event_day = input("Event Day: ")
        if event_day.lower().strip() in days_list:
            print(f"The event day is {event_day.lower().strip().title()}!")
            return event_day.lower().strip().title()
        else:
            print("Invalid day format")

# Specialized function that validates the time, using another function as a helper.


def time():
    while True:
        print(
            "To add, or delete events, specify the time in the format 'HH:MM (AM or PM) to HH:MM (AM or PM)'.\nThis calendar does not support events that span over days."
        )
        event_time = input("Event Time: ")
        if is_valid_time(event_time) == None:
            pass
        else:
            return is_valid_time(event_time)

# Specialized function that validates the time exclusively for the view action, using a helper function.


def view_time():
    while True:
        print(
            "To view events, specify the time in the format 'HH:MM (AM or PM)'.\nThis calendar does not support events that span over days."
        )
        event_time = input("Event Time: ")
        if is_valid_time_view(event_time) == None:
            pass
        else:
            return is_valid_time_view(event_time)

# Create event action.


def create_event(AM, PM, day):
    days_dict = {
        "monday": 0,
        "tuesday": 1,
        "wednesday": 2,
        "thursday": 3,
        "friday": 4,
        "saturday": 5,
        "sunday": 6,
    }
    day = day.lower().strip()
    day_num = days_dict[day]
    start = int(AM) // 60
    end = int(PM) // 60

    if start == 0:
        start = 24
    if end == 0:
        end = 24

    start = min(start, end)
    end = max(start, end)

    title = input("What is the title of the event? Input: ").strip().title()
    color_text = random_color("~")
    time_dict[f"{title}"] = [start, end, day_num]
    for i in range(start, end + 1):
        mass_list[i][day_num] = color_text * len(title)
    average = round((start + end) / 2)
    mass_list[average][day_num] = title
    event_description = input(f"What is the description of the event? {title}: ")
    for i in range(start, end + 1):
        event_list[i][day_num] = f"{title}: {event_description}"

# Delete event action.


def delete_event():
    while True:
        event = input(f"What event are you deleting?\nInput: ").lower().strip().title()
        if event in time_dict:
            start, end, day_num = time_dict[event]
            for i in range(start, end + 1):
                mass_list[i][day_num] = "Free"
                event_list[i][day_num] = ""
            del time_dict[event]
            print(f'Event "{event}" has been deleted.')
            break
        else:
            print("Unable to find event, please try again.")

# View event action.


def view_event(time, day):
    days_dict = {
        "monday": 0,
        "tuesday": 1,
        "wednesday": 2,
        "thursday": 3,
        "friday": 4,
        "saturday": 5,
        "sunday": 6,
    }
    day = day.lower().strip()
    day_num = days_dict[day]
    event_time = int(int(time) / 60)
    if event_list[event_time][day_num] == "":
        print("Nothing seems to be there, did you want to schedule an event?")
    else:
        n = len(event_list[event_time][day_num])
        if n > 146:
            n = 146
        else:
            n = n

        print("~" * n)
        print(f"{event_list[event_time][day_num]}")
        print("~" * n)

# Converts hours, minutes, and period to a more understandable and a form that is easier to implment calculations in.


def get_military_minutes(hour, minutes, period):
    hour = int(hour)
    minutes = int(minutes)
    period = period.upper()
    if hour == 12:
        if period == "AM":
            hour = 0
        else:
            hour = 12
    elif period == "PM":
        hour += 12
    return (hour * 60) + minutes

# Validates the time using regex and helper functions to convert the time.


def is_valid_time(time):
    if time := re.search(
        r"^\s*([1-9]|10|11|12):([0-5][0-9])\s*(AM|PM)\s*to\s*([1-9]|10|11|12):([0-5][0-9])\s*(AM|PM)$",
        time,
        flags=re.IGNORECASE,
    ):
        start_time = get_military_minutes(time.group(1), time.group(2), time.group(3))
        end_time = get_military_minutes(time.group(4), time.group(5), time.group(6))
        if start_time >= end_time:
            print(
                "Invalid time format. Start time must be earlier than end time. Overnight events are not supported."
            )
            return None
        else:
            return start_time, end_time
    else:
        print("Invalid time format. Example: 9:00 AM to 11:30 AM")
        return None

# Validates the time exclusively for the view action, which uses another helper function to convert the time.


def is_valid_time_view(time):
    if time := re.search(
        r"^\s*([1-9]|10|11|12):([0-5][0-9])\s*(AM|PM)$", time, flags=re.IGNORECASE
    ):
        total_time = get_military_minutes(time.group(1), time.group(2), time.group(3))
        if total_time == 0:
            return 1440
        return total_time
    else:
        print("Invalid time format. Example: 9:00 AM to 11:30 AM")
        return None

# Validates events to see if they are overlapping with other events or not.


def is_valid_event(AM, PM, day):
    days_dict = {
        "monday": 0,
        "tuesday": 1,
        "wednesday": 2,
        "thursday": 3,
        "friday": 4,
        "saturday": 5,
        "sunday": 6,
    }
    day = day.lower().strip()
    day_num = days_dict[day]
    start = int(AM) // 60
    end = int(PM) // 60

    if start == 0:
        start = 24
    if end == 0:
        end = 24

    start = min(start, end)
    end = max(start, end)

    for i in range(start, end + 1):
        if event_list[i][day_num] != "":
            return False
    return True

# Gives a random color code.


def random_color(text):
    color_code = random.randint(1, 255)
    return f"\033[38;5;{color_code}m{text}\033[0m"

# Creates the UI for the user.


def create_calendar():
    # List within a list of all of the times (standard time), and the status of a given time.
    table = [
        ["1:00AM", *mass_list[1]],
        ["2:00AM", *mass_list[2]],
        ["3:00AM", *mass_list[3]],
        ["4:00AM", *mass_list[4]],
        ["5:00AM", *mass_list[5]],
        ["6:00AM", *mass_list[6]],
        ["7:00AM", *mass_list[7]],
        ["8:00AM", *mass_list[8]],
        ["9:00AM", *mass_list[9]],
        ["10:00AM", *mass_list[10]],
        ["11:00AM", *mass_list[11]],
        ["12:00PM", *mass_list[12]],
        ["1:00PM", *mass_list[13]],
        ["2:00PM", *mass_list[14]],
        ["3:00PM", *mass_list[15]],
        ["4:00PM", *mass_list[16]],
        ["5:00PM", *mass_list[17]],
        ["6:00PM", *mass_list[18]],
        ["7:00PM", *mass_list[19]],
        ["8:00PM", *mass_list[20]],
        ["9:00PM", *mass_list[21]],
        ["10:00PM", *mass_list[22]],
        ["11:00PM", *mass_list[23]],
        ["12:00AM", *mass_list[24]],
    ]
    # List that contains the days of the week
    headers = [
        "Time",
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday",
    ]
    return tabulate(table, headers, tablefmt="double_grid")


if __name__ == "__main__":
    main()