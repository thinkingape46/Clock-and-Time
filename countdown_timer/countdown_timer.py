# Simple program that works like a countdown timer.
import time # importing time

h2 = int(input("Please enter hours (hh): "))                              # Requests hours from user.
m2 = int(input("Please enter minuues (mm): "))                            # Requests minutes from user.
s2 = int(input("Please enter seconds (ss): "))                            # Requests seconds from user.

# ct = time.ctime() # Assigns current time as a string "DAY MON DD HH:MM:SS YYYY"

# h1 = ct[11: 13]                                                             # Slices the hours from ct.
# m1 = ct[14: 16]                                                             # Slices the minutes from ct.
# s1 = ct[17:19]                                                              # Slices the seconds from ct

sleep_time = ((h2 * 3600) + (m2 * 60) + (s2))

time.sleep(sleep_time)

print("COUNTDOWN ENDED!")