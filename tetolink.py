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

channelid = 569730957536395274

lastmessagesnowflake = get_last_week_snowflake()

now = datetime.datetime.utcnow()
week_ago = now - datetime.timedelta(days=7)

counter = 0
while True:
    url = f'https://discord.com/api/v9/channels/{str(channelid)}/messages?after={str(lastmessagesnowflake)}&limit=100'

    response = requests.get(url, headers=headers)

    messages = response.json()
    if("code" in messages):
        print(messages["code"])
        print("too big! done")
        break

    for message in messages:
        if("tetr.io" in message["content"]):
            print(f'From {message["author"]["username"]}:')
            print(message["content"])

    if(timestamp_to_snowflake(messages[0]["timestamp"]) == lastmessagesnowflake):
        print("last message gotten")
        break
    lastmessagesnowflake = timestamp_to_snowflake(messages[0]["timestamp"])
