# -*- coding = utf-8 -*-
# Motto : Practice makes perfect.
# Time : 29/8/2023 12:21 pm

import pandas as pd
from tabulate import tabulate
from datetime import datetime
from habit_tracker import track_habit, Habit
def main():
    habits: list[Habit] = [
        track_habit('coffee', datetime(2023,5,12, 13), cost=1, minutes_used=5)]

    df = pd.DataFrame(habits)

    print(tabulate(df, headers='keys', tablefmt='psql'))

if __name__ == '__main__':
    main()
