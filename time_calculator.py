def add_time(start, duration, day=""):
  DAY_OF_WEEK = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
  day = day.capitalize()
  num_days = 0

  start_time, am_pm = start.split()
  start_hour, start_minute = start_time.split(":")
  end_hour, end_minute = duration.split(":")

  if am_pm == "PM":
    start_hour = int(start_hour) + 12

  new_hour = int(start_hour) + int(end_hour)
  new_minute = int(start_minute) + int(end_minute)

  
  while new_minute > 59:
    new_minute -= 60
    new_hour += 1

  while new_hour > 24:
    new_hour -= 24
    num_days += 1
  
  if new_hour > 12:
    am_pm = "PM" if am_pm == "AM" else "PM"
    new_hour -= 12
  else:
    am_pm = "AM" if am_pm == "PM" else "AM"

  if new_hour == 12:
    if new_minute > 0 and am_pm == "PM":
      num_days += 1
      am_pm = "AM"
    else:
      am_pm = "PM" if am_pm == "AM" else "PM"

  new_minute = str(new_minute).zfill(2)

  if day:
    new_day = DAY_OF_WEEK[(DAY_OF_WEEK.index(day) + num_days)%7] + " "
    if num_days == 1:
      return f"{new_hour}:{new_minute} {am_pm}, {new_day}(next day)" 
    if num_days > 1:
      return f"{new_hour}:{new_minute} {am_pm}, {new_day}({num_days} days later)"
    return f"{new_hour}:{new_minute} {am_pm}, {day}"
  else:
    if num_days == 1:
      return f"{new_hour}:{new_minute} {am_pm} (next day)"
    if num_days > 1:
      return f"{new_hour}:{new_minute} {am_pm} ({num_days} days later)"
  return f"{new_hour}:{new_minute} {am_pm}"
