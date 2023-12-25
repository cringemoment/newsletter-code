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
        if("jstris.jezevec10.com" in message["content"]):
            testlink = message["content"].split()
            for i in testlink:
                if("jstris.jezevec10.com" in i):
                    testlink = i
                    break
            response = requests.get(testlink.replace("[", "").replace("<", "")).text.splitlines()

            keepgoing = True

            for i in response:
                try:
                    if('meta name="description"' in i):
                        description = i.split('<meta name="description" content="')[1].split(' ">')[0]
                        gamemode = ' '.join(description.split("A replay of ")[1].split()[:3])
                        username = description.split("by ")[1].split(' on Jstris')[0]
                        break
                except:
                    keepgoing = False
                    break

            if(keepgoing):
                if(gamemode == "PC Mode PC"):
                    userlink = f"https://jstris.jezevec10.com/PC-mode?display=5&user={username}"
                    response = requests.get(userlink).text.splitlines()
                    currentpb = False
                    for line in response:

                        if("<td><strong>" in line):
                            currentpb = True

                        if(currentpb):
                            if("href" in line):
                                pblink = line.split('<a href="')[1].split('" target="_blank">')[0]

                                if(pblink == testlink):
                                    print(f"From {username}:")
                                    print(message["content"])
                                break

    if(timestamp_to_snowflake(messages[0]["timestamp"]) == lastmessagesnowflake):
        print("last message gotten")
        break
    lastmessagesnowflake = timestamp_to_snowflake(messages[0]["timestamp"])
