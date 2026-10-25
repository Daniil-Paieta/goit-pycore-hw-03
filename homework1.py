# GoIT PyCore Homework 03

#TASK 1

from datetime import datetime


def get_days_from_today(date):
    try:
        given_date = datetime.strptime(date, "%Y-%m-%d").date()
        today = datetime.today().date()
        difference = today - given_date
        return difference.days
    except ValueError:
        return None


#TASK2 

import random


def get_numbers_ticket(min, max, quantity):
    
    if min < 1:
        return []

    if max > 1000:
        return []

    if min > max:
        return []

    if quantity < 1:
        return[]
    
    if quantity > max - min + 1:
        return[]

    possible_numbers = range(min, max + 1)
    selected_numbers = random.sample(possible_numbers, quantity)
    sorted_numbers = sorted(selected_numbers)

    return sorted_numbers


#TASK3 

import re 


def normalize_phone(phone_number):
    clean_number = re.sub(r"\D", "", phone_number)
    
    if clean_number.startswith("380"):
        return "+" + clean_number
    else:
        return "+38" + clean_number
     

#TASK4 

from datetime import datetime, timedelta


def get_upcoming_birthdays(users):
    today = datetime.today().date()
    next_week = today + timedelta(days = 7)
    upcoming_birthdays = []

    for user in users:
        birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()

        birthday_this_year = birthday.replace(year = today.year)

        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)
        
        if today <= birthday_this_year <= next_week:
            congratulation_date = birthday_this_year

            if congratulation_date.weekday() >= 5:
                days_to_monday = 7 - congratulation_date.weekday()
                congratulation_date += timedelta(days = days_to_monday)

            upcoming_birthdays.append(
                {
                    "name": user["name"],
                    "congratulation_date": congratulation_date.strftime("%Y.%m.%d"),
                }
            )
    return upcoming_birthdays


