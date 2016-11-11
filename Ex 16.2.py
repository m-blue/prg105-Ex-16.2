class Time():
    """attributes: hour, minute, second"""


def is_after(t1,t2):
    return time_to_sec(t1) > time_to_sec(t2)


def time_to_sec(x):
    minu = x.hour * 60 + x.minute
    sec = minu * 60 + x.minute
    return sec


time1 = Time()
time1.hour = 3
time1.minute = 45
time1. second = 30

time2 = Time()
time2.hour = 5
time2.minute = 25
time2.second = 35

print is_after(time1,time2)
