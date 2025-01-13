import math
import datetime as dt

hourly_rate = int(input("Input your hourly rate: "))
hours_per_day = int(input("Input the number of hours you work per day: "))
how_many_days_per_week = int(input("Input the number of days you work per week: "))
goal = int(input("Input your goal: "))

amount_per_day =  hourly_rate * hours_per_day
amount_per_week = amount_per_day * how_many_days_per_week
estemated_amount_weeks  = round(goal / amount_per_week)
amount_per_month = estemated_amount_weeks / 4

print(f"the goal is ${goal} which would take {estemated_amount_weeks} weeks or {amount_per_month} months")
