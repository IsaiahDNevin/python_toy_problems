import math
import datetime as dt

hourly_rate = 15
hours_per_day = 6
how_many_days_per_week = 5
goal = 555

amount_per_day =  hourly_rate * hours_per_day
amount_per_week = amount_per_day * how_many_days_per_week
estemated_amount_weeks  = round(goal / amount_per_week)
amount_per_month = estemated_amount_weeks / 4

print(f"the goal is ${goal} which would take about {estemated_amount_weeks} weeks or {amount_per_month} months")
