from datetime import date, timedelta
from prettytable import PrettyTable
from typing import List
# from pprint import pprint

today = date.today()
# today = date.weekday(date.today())
print(today)

# https://strftime.org/
print(date.strftime(today, "%Y %B %d %A"))

day_intervals = [0, 15, 30, 45, 60, 90, 183, 365]

# print(type(today))

op: List[List] = [
    [x, (today - timedelta(days=x)).strftime("%Y %B %d %A")] for x in day_intervals
]

table = PrettyTable(["Interval (Days)", "Date"])
table.add_rows(op)
table.align = "l"

print(table)
