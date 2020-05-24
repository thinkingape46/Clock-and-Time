# Not practical, as it's made for fun and learning python.
# Only useful for 24 hours and date is not incorporated yet.

import time # Imports time module
a_hour = (input("Enter Hour in 24 hour format please: ")) # Requests the hour
a_minute = (input("Enter Minutes (MM format) please: "))  # Request the minute, should be in two digit.

while True:
    n = 1
    x = time.ctime() # time is assigned to x
    if a_hour + ':' + a_minute in x: # Checks for a_hour and a_minute in time string, gotta be a better way.
        print("Alarm Rings!") # When it matches, prints the statement and breaks out.
        break
    n += 1