# Simple program that works like a countdown timer.
import time # imports time module

hr = int(input("Please enter hours (hh): "))                              # Requests hours from user.
min = int(input("Please enter minuues (mm): "))                            # Requests minutes from user.
sec = int(input("Please enter seconds (ss): "))                            # Requests seconds from user.

# ct = time.ctime() # Assigns current time as a string "DAY MON DD HH:MM:SS YYYY"

t1 = time.time()                                                              # Current time in seconds.

# h1 = ct[11: 13]                                                             # Slices the hours from ct.
# m1 = ct[14: 16]                                                             # Slices the minutes from ct.
# s1 = ct[17:19]                                                              # Slices the seconds from ct


ct_time = (hr * 3600) + (min * 60) + sec                                             # Countdown time in seconds
t2 = t1 + ct_time                                                                    # time in seconds since epoch when countdown ends.

while True:

    t1 = time.time()
    n = 1

    if (t2 - t1) > 0:        

        print(f"Time remaining: {round(t2-t1)} seconds")
        time.sleep(1)

    else:
        print(f"time remaining: {round(t2-t1)} seconds")
        print("Countdown Ends!")
        break
    
    n += 1



# h2 = hr + int(h1)                                                                # hour at which countdown should stop.
# m2 = min + int(m1)                                                               # minute of h2 at which countdown should stop.
# s2 = sec + int(s1)                                                               # second of h2 and m2 at which countdown should stop.

# delta_h = h2 - int(h1)                                                           # time in hours left for countdown.
# delta_m = m2 - int(m1)                                                           # time in minutes left for countdown.
# delta_s = s2 - int(s1)                                                           # time in seconds left for countdown.


# while True:
    
#     n = 1

#     if (t2 -t1)> 1:                                 # Checks if time left is more that one sec.

#         ct = time.ctime()                                                           # Assigns current time as a string "DAY MON DD HH:MM:SS YYYY"
#         h1 = ct[11: 13]                                                             # Slices the hours from ct.
#         m1 = ct[14: 16]                                                             # Slices the minutes from ct.
#         s1 = ct[17:19]                                                              # Slices the seconds from ct

#         delta_h = h2 - int(h1)                                                           # time in hours left for countdown.
#         delta_m = m2 - int(m1)                                                           # time in minutes left for countdown.
#         delta_s = s2 - int(s1)                                                           # time in seconds left for countdown.

#         print(f"Time Remaining: {delta_h}:{delta_m}:{delta_s}")

#         time.sleep(1)

#     else:
#         delta_s -= 1
#         print(f"Time Remaining: {delta_h}:{delta_m}:{delta_s}")
#         print("Countdown Ended!")
#         break

    n += 1
