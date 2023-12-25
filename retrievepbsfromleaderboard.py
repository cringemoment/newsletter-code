import requests
from datetime import datetime, timedelta

def is_within_last_week(date_string):
    if("<td>" in date_string):
        date_string = date_string[5:]
    # Get the current date and time
    current_date = datetime.now()
    last_week_start = current_date - timedelta(days=7)
    currentdate = current_date - timedelta(days=0)

    # Parse the given date string into a datetime object
    given_date = datetime.strptime(date_string, "%Y-%m-%d %H:%M:%S")

    # Check if the given date is within the last week
    if given_date >= last_week_start and given_date <= current_date:
        return True
    return False

url = "https://jstris.jezevec10.com/PC-mode"
response = requests.get(url).text.splitlines()
print(response)

allpbs = []

for lineindex, line in enumerate(response):
    if("time-mil" in line):
        timestamp = response[lineindex + 4].strip("<td>/")
        username = response[lineindex - 3].replace("<a>", "").replace("</a>", "")
        pb = response[lineindex - 1].strip("<>/strongd")
        if is_within_last_week(timestamp):
            print(timestamp)
            allpbs.append([username, pb])

longestlength = 0
for pb in allpbs:
    if(len(pb[0]) > longestlength):
        longestlength = len(pb[0])

for pbindex, pb in enumerate(allpbs):
    spacer = " " * (longestlength - len(pb[0]))
    print(str(pbindex + 1) + ". " + pb[0] + " " + spacer + str(pb[1]) + " (Jstris)")
