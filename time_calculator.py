def add_time(start, duration, sday=None):

  dotw = {"Saturday" : 0,
          "Sunday" : 1,
          "Monday" : 2,
          "Tuesday" : 3,
          "Wednesday" : 4,
          "Thursday" : 5,
          "Friday" : 6,
         }

# splitting
  timing = start.split() # ['11:06', 'PM']
  timeh = timing[0]
  tod = timing[1]

#start time
  times = timeh.partition(":") #('11', ':', '06') 
  hourss = int(times[0]) 
  minutess = int(times[2])

  if tod == "PM": # 24 hr clock sys
    hourss += 12

#duration time
  timed = duration.partition(":")  #('2', ':', '02')
  hourd = int(timed[0]) 
  minuted = int(timed[2])

# % shows the remainder. // rounds down to nearest whole num
# adding the minutes nd hours
  total_minutes = int(minutess) + int(minuted)
  total_hours = hourss + hourd

# minutes cant be > 60
  if total_minutes >= 60:
    total_hours += 1

  days = total_hours // 24
  hours = (total_hours % 24)
  minutes = total_minutes % 60

# getting the correct am or pm
  am_pm = ""
  if (total_hours % 24) <= 11:
    am_pm = "AM"
  else:
    am_pm = "PM"

# adding a 0 to the minutes if <= 9
  if minutes <= 9:
    minutes = f'0{minutes}'
  else:
    minutes = minutes

# set everything to str
  new_times = []

  hrs = str((total_hours % 24) % 12)
  if hrs == "0":
    hrs = "12"
  new_times.append(hrs)
  
  mins = str(minutes)
  new_times.append(mins)

  dl = f'({days} days later)'
  nd = "(next day)"

  TIME = f'{new_times[0]}:{new_times[1]} {am_pm}'
  new_time = ""

  if sday == None:
    if days == 0:
      new_time = TIME
    if days == 1:
      new_time = TIME + " " + nd
    if days >= 2:
      new_time = TIME + " " + dl
  else:
    index_num = (dotw[sday.lower().capitalize()] + days) % 7
    for od, nd in dotw.items():
      if nd == index_num:
        index_num = od
        break
    if days == 0:
      new_time = f'{TIME}, {index_num}'
    if days == 1:
      new_time = f'{TIME}, {index_num} (next day)'
    if days >= 2:
      new_time = f'{TIME}, {index_num} ({days} days later)'

  return new_time
  