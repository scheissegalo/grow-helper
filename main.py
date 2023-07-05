import datetime
import ephem

def calculate_suntime(latitude, longitude, date):
    observer = ephem.Observer()
    observer.lat = str(latitude)
    observer.lon = str(longitude)
    observer.elevation = 0  # Elevation is optional and set to 0 for simplicity

    sun = ephem.Sun()
    observer.date = date

    sunrise = observer.previous_rising(sun).datetime()
    sunset = observer.next_setting(sun).datetime()

    # Calculate daylight duration within a 24-hour period
    daylight_duration = (sunset - sunrise) % datetime.timedelta(days=1)

    return daylight_duration

# Example usage
latitude = 19.615087  # Finca latitude
longitude = -70.403280  # Finca longitude

growth_period = datetime.timedelta(weeks=8)  # Growth period of the plant

today = datetime.datetime.now().date()  # Current date

# Calculate the start date for growing the plant
start_date = today - growth_period

longest_suntime = datetime.timedelta()
best_start_date = None

# Iterate over each day of the growth period
for day in range(growth_period.days + 1):
    date = start_date + datetime.timedelta(day)
    suntime = calculate_suntime(latitude, longitude, date)

    if suntime > longest_suntime:
        longest_suntime = suntime
        best_start_date = date

# Calculate the target date within the last 2 weeks of the growth period
target_date = best_start_date + datetime.timedelta(weeks=6)

print("Best date to start growing the plant:", best_start_date)
print("Target date with the longest suntime within the last 2 weeks:", target_date)
