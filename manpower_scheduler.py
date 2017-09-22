# '''
# Manpower Calculator
# Take the input from a user for multiple projects (jobs) and calculate the required manpower over time
# Entry will be gui-based, with output as either text or graph, filterable by job if necessary
# '''

from datetime import datetime, date, timedelta
from math import ceil

# values input by user per job
project = []
project_name = "Test Job 1"
project_milestone1 = "Grid"
start_date = date(2017,1,1)
end_date = date(2017,1,10)
estimated_hours = 60*8
max_crew_size = 4

# value taken from total available employees. either by some database or input by user
manpower_pool = 10

# starting values & duration calculation
duration = int((end_date - start_date).days + 1)
weekdays = 0
saturdays = 0
sundays = 0

def daterange(start_date, end_date):
	for date in range(int((end_date - start_date).days) + 1):
		yield start_date + timedelta(date)
		
for single_date in daterange(start_date,end_date):
	if single_date.weekday() == 5:
		saturdays = saturdays + 1
	elif single_date.weekday() == 6:
		sundays = sundays + 1
	else:
		weekdays = weekdays + 1

req_manpower = ceil(estimated_hours/8/weekdays)

print ("Weekdays: " + str(weekdays))
print ("Saturdays: " + str(saturdays))
print ("Sundays: " + str(sundays))

print(str(req_manpower))