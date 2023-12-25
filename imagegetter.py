import requests
import json
import datetime

def get_last_week_snowflake():
    now = datetime.datetime.utcnow()
    week_ago = now - datetime.timedelta(days=7)
    timestamp = int((week_ago - datetime.datetime(1970, 1, 1)).total_seconds() * 1000)
    snowflake = (timestamp - 1420070400000) << 22
    return snowflake

def timestamp_to_snowflake(timestamp):
    dt = datetime.datetime.fromisoformat(timestamp.replace("Z", "+00:00"))
    timestamp = int(dt.timestamp() * 1000)
    snowflake = (timestamp - 1420070400000) << 22
    return snowflake

apikey = open("apikey.txt").read().replace("\n", "")
headers = {
    'Authorization': apikey,
}

channelid = 689739087581544556

lastmessagesnowflake = get_last_week_snowflake()

counter = 0

allimages = []

while True:
    url = f'https://discord.com/api/v9/channels/{str(channelid)}/messages?after={str(lastmessagesnowflake)}&limit=100'

    response = requests.get(url, headers=headers)

    messages = response.json()
    if("code" in messages):
        print(messages)
        print(messages["code"])
        print("too big! done")
        break

    for message in messages:
        if("attachments" in message and message["attachments"] != []):
            if("reactions" in message):
                for reaction in message["reactions"]:
                    if(reaction['emoji']['name'] == "⭐"):
                        allimages.append([message['author']['username'], message['timestamp'], message["attachments"][0]["url"], reaction['count']])

    if(timestamp_to_snowflake(messages[0]["timestamp"]) == lastmessagesnowflake):
        print("last message gotten")
        break
    lastmessagesnowflake = timestamp_to_snowflake(messages[0]["timestamp"])

allimages.sort(key=lambda x: int(x[3]) * -1)

for i in allimages:
    print(f"The author is {i[0]}, at {i[1]}")
    print(i[2])
    print(f"There are {i[3]} ⭐")

print(f"Total stars this week:{sum([i[3] for i in allimages])}")
