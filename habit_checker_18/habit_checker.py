# -*- coding = utf-8 -*-
# Motto : Practice makes perfect.
# Time : 29/8/2023 11:32 am

from datetime import datetime
from dataclasses import dataclass

@dataclass
class Habit:
    name: str
    time_since: str
    remaining_days: str
    minutes_saved: float
    money_saved: float

def track_habit(name: str, start: datetime, cost: float, minutes_used: float) -> Habit:
    goal: int = 60
    hourly_wage: int = 30

    time_elapsed: float = (datetime.now() - start).total_seconds() #Compute the time elapsed since the habit started (in seconds).
    hours: float = round(time_elapsed / 60 / 60, 1)    # Convert time_elapsed into hours.
    #This function rounds the result to one decimal place
    days: float = round(hours / 24, 2)   # Convert the above hours into days.
    # #This function rounds the result to two decimal place


    money_saved: float = cost * days
    minutes_used: float = round(days * minutes_used)
    #Round to the nearest whole number.
    total_money_saved: str = f'${round(money_saved + (minutes_used / 60 * hourly_wage), 2)} '

    days_to_go: float | str = round(goal - days)

    remaining_days: str = 'Cleared!' if days_to_go <= 0 else f'{days_to_go}'
    time_since: str = f'{days} days ' if hours > 72 else f'{hours} hours.'

    return  Habit(name=name,
                  time_since=time_since,
                  remaining_days=remaining_days,
                  minutes_saved=minutes_used,
                  money_saved=total_money_saved)





