import time
print(time.gmtime())#returns green wich time
print(time.time())#it returns time in seconds
print(time.ctime())#it returns time in current time format i.e day, month, date, time, year
print(time.gmtime())


print("-----------------------")

# for i in range( 1,4):
#     time.sleep(2)
#     print(i)

obj=time.gmtime()
print(time.asctime(obj))# it converts the argument and displays time in local time format
print(time.localtime())#it displays local time
print(time.time_ns())#it displays time in nano seconds
from time import gmtime, strftime
# s = strftime("%A, %D %B %y %H:%M:%S",
# 			gmtime(1627987508.6496193))
# print(s)

