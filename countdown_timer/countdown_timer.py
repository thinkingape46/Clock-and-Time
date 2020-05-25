# Simple program that works like a countdown timer.
import time
# imports time module

hr = int(input("Please enter hours (hh): "))
# Requests hours from user.
min = int(input("Please enter minuues (mm): "))
# Requests minutes from user.
sec = int(input("Please enter seconds (ss): "))
# Requests seconds from user.

t1 = round(time.time())
# Current time in seconds.


ct_time = (hr * 3600) + (min * 60) + sec
# Countdown time in seconds
t2 = t1 + ct_time
# time in seconds since epoch when countdown ends.

while True:

    n = 1

    t1 = round(time.time())
    h_rem = 0
    m_rem = 0
    s_rem = t2-t1

    if (t2 - t1) > 0:

        time_rem = t2-t1

        if time_rem > 59:
            m_rem = time_rem / 60
            s_rem = time_rem - (int(m_rem) * 60)
            if m_rem > 59:
                h_rem = 1+ ((m_rem - 60) / 60)

        print(f"Time remaining: {(h_rem)}:{int(m_rem)}:{(s_rem)}")
        time.sleep(1)

    else:
        print(f"Time remaining: {(h_rem)}:{int(m_rem)}:{(s_rem)}")
        print("Countdown Ends!")
        break
    
    n += 1
