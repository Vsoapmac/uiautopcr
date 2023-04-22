from datetime import datetime


start_timer = "12:31"
now = datetime.now()
year_month_day = now.strftime("%Y-%m-%d")
end = datetime.strptime(year_month_day + " " + start_timer,"%Y-%m-%d %H:%M")
print(now)
print(end)
d = end - now
print(d.seconds)