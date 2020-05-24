# Not practical, as it's made for fun and learning python.
# Only useful for 24 hours and date is not incorporated yet.

import time # Imports time module
h2 = int(input("Enter Hour in 24 hour format please: ")) # Requests the hour
m2 = int(input("Enter Minutes (MM format) please: "))  # Request the minute, should be in two digit.

# Remember when a character is entered, this code will give an ValueError.

class Alarm():

    def __init__(self):
        pass

    def ring(self, h2, m2):

        self.h2 = h2
        self.m2 = m2

        ct = time.ctime() # current time
        h1 = int(ct[11:13]) # slices the hour value and convterts to integer
        m1 = int(ct[14:16]) # slices the minute value and converts to integer
        diff_sec = ((h2 - h1) * 3600) + ((m2 - m1) * 60) # subtracts the current time from alarm time in seconds
        time.sleep(diff_sec-1)

        while True:

            n = 1

            ct = time.ctime() # current time
            h1 = int(ct[11:13]) # slices the hour value and convterts to integer
            m1 = int(ct[14:16]) # slices the minute value and converts to integer

            if (h2, m2) == (h1, m1): # Checks for a_hour and a_minute in time string, gotta be a better way.
                print("Alarm Rings!") # When it matches, prints the statement and breaks out.
                break

            n += 1

        pass

alarm1 = Alarm()
alarm1.ring(h2, m2)