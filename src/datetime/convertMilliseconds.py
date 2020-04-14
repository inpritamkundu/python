import time
from datetime import datetime

# convert given date time in milli
createdAt = '2019-12-11 16:46:48.145000'
dt_obj = datetime.strptime(createdAt,
                           '%Y-%m-%d %H:%M:%S.%f')
millisec = dt_obj.timestamp() * 1000

print(millisec)

# convert current date time in milli

millis = int(round(time.time() * 1000))
print(millis)

print(millis-millisec)


# convert millisecond to date time
dattimes = str(datetime.fromtimestamp(millis/1000.0))
l = dattimes.split()
print(dattimes)


# convert to date
