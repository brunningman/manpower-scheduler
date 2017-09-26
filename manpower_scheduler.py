# '''
# Manpower Calculator
# Take the input from a user for multiple projects (jobs) and calculate the required manpower over time
# Will be used to visualize employee load over time, and calculate potential overtime costs
# '''

from datetime import datetime, date, timedelta
from math import ceil

# values input by user per job (this will be replaced by input functions)
project = []
project_name = "Test Job 1"
project_milestone1 = "Grid"
start_date = date(2017,1,1)
end_date = date(2017,1,10)
estimated_hours = 60*8
max_crew_size = 4

# value taken from total available employees. either by some database or input by user
manpower_pool = 10

# Calculate duration in total days
duration = int((end_date - start_date).days + 1)

def daterange(start_date, end_date):
	for date in range(int((end_date - start_date).days) + 1):
		yield start_date + timedelta(date)

def find_working_days(start_date,end_date):
	weekdays = 0
	saturdays = 0
	sundays = 0
	for single_date in daterange(start_date,end_date):
		if single_date.weekday() == 5:
			saturdays = saturdays + 1
		elif single_date.weekday() == 6:
			sundays = sundays + 1
		else:
			weekdays = weekdays + 1
	return {"weekdays":weekdays,"saturdays":saturdays,"sundays":sundays}
			

working_days = find_working_days(start_date,end_date)	
req_manpower = ceil(estimated_hours/8/working_days.get("weekdays"))

print("From " + str(start_date) + " to " + str(end_date))
print (working_days)
print(str(req_manpower))
