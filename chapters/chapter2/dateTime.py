import datetime

current_date = datetime.date.today()

print(current_date)

print(current_date.year)

print(current_date.month)

print(current_date.day)


""" Changing date format  """


print(current_date.strftime("%d - %b - %Y "))

# %d for date
# %b for month
# %Y for year in digit 2020
# %B for month
# %y for year 16,15,20, etc..

# website --> strftime.org
