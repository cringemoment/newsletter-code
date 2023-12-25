import requests
import json
import csv
import datetime

def snowflake_to_datetime(snowflake):
    timestamp = ((snowflake >> 22) + 1420070400000) / 1000.0
    return datetime.datetime.utcfromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')

def get_last_week_snowflake():
    now = datetime.datetime.utcnow()
    week_ago = now - datetime.timedelta(days=7)
    timestamp = int((week_ago - datetime.datetime(1970, 1, 1)).total_seconds() * 1000)
    snowflake = (timestamp - 1420070400000) << 22
    return snowflake

def get_current_snowflake():
    now = datetime.datetime.utcnow()
    week_ago = now - datetime.timedelta(days=0)
    timestamp = int((week_ago - datetime.datetime(1970, 1, 1)).total_seconds() * 1000)
    snowflake = (timestamp - 1420070400000) << 22
    return snowflake

import datetime

def timestamp_to_snowflake(timestamp):
    dt = datetime.datetime.fromisoformat(timestamp.replace("Z", "+00:00"))
    timestamp = int(dt.timestamp() * 1000)
    snowflake = (timestamp - 1420070400000) << 22
    return snowflake


apikey = open("apikey.txt").read().replace("\n", "")
headers = {
    'Authorization': apikey,
}

channelid = 577021222311821312

lastmessagesnowflake = get_last_week_snowflake()

counter = 0
runvalues = []
while True:
    url = f'https://discord.com/api/v9/channels/{str(channelid)}/messages?after={str(lastmessagesnowflake)}&limit=100'
    response = requests.get(url, headers=headers)

    messages = response.json()
    if("code" in messages):
        print(messages["code"])
        print("too big! done")
        break

    for message in messages:
        if("embeds" in message and message["embeds"] != []):
            if("PC Mode" in message["embeds"][0]["description"]):
                runvalues.append([message["embeds"][0]["title"].split(" - ")[0].replace("*", ""), int(message["embeds"][0]["fields"][4]["value"])])


    if(timestamp_to_snowflake(messages[0]["timestamp"]) == lastmessagesnowflake):
        print("last message gotten")
        break
    lastmessagesnowflake = timestamp_to_snowflake(messages[0]["timestamp"])
    if(lastmessagesnowflake > get_current_snowflake()):
        #break
        pass

runvalues.sort(key=lambda x: x[1], reverse = True)
runvalueswithoutrepeat = []
for i in runvalues:
    for j in runvalueswithoutrepeat:
        if(i[0] == j[0]):
            break
    else:
        runvalueswithoutrepeat.append(i)

print("Top runs")
[print(i) for i in runvalues]
longestlength = 0
longestpblength = 0

for i in range(5):
    if(len(runvalueswithoutrepeat[i][0]) > longestlength):
        longestlength = len(runvalueswithoutrepeat[i][0])
    if(len(str(runvalueswithoutrepeat[i][1])) > longestpblength):
        longestpblength = len(str(runvalueswithoutrepeat[i][1]))

for i in range(5):
    print(str(i + 1) + ". " + str(runvalueswithoutrepeat[i][0]) + (" " * (longestlength - len(runvalueswithoutrepeat[i][0]) + 2 + longestpblength - len(str(runvalueswithoutrepeat[i][1])))) + str(runvalueswithoutrepeat[i][1]) + " PC")
