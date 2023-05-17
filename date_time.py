from datetime import datetime

start_date = datetime(2020, 1, 1)

end_date = datetime(2022, 12, 5)

difference = end_date - start_date

years = (difference.days + (difference.seconds/86400))/365.25

print(years)

time = datetime.now().time()
print(time)

date1 = datetime.now()

print(date1.month)
print(date1.day)
print(date1.year)