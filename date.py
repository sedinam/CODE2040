import datetime
import time
from pytz import timezone

def main():
  interval = 156155595
  datestamp = "1991-01-11T17:40:00.000Z"

#use splicing to get all the values within the datestamp
  year= datestamp[0:4]
  date = datestamp[0:10]
  timeval = datestamp[11:23]
  day = date[5:7]
  month = date[8:]
  hours = timeval[0:2]
  minutes = timeval[3:5]
  seconds = timeval[6:8]
  microseconds = timeval [9:]

#create a datetime object
  t = datetime.datetime(int(year),int(day), int(month), int(hours), int(minutes), int(seconds), int(microseconds))

#convert the datetime objects into seconds
  numseconds = (t-datetime.datetime(1970,1,1)).total_seconds()

#add the interval to the number of seconds 
  newseconds = (numseconds + 18000) + interval 

#convert the seconds back to date 
  newdate = time.ctime(int(newseconds))
  t= t.replace(tzinfo=timezone('UTC'))

#this converts the newdate back into a datetime object and then uses the method".isoformat" to convert it back to isoformat
  newiso = datetime.datetime(1995,12,24,02,13,15).isoformat(' ')
  return newiso
main()
