# Original Author - Swastik2442 (https://github.com/Swastik2442)
# Python Program to send Latest Instagram Posts to Discord

from urllib.request import urlopen
from dotenv import load_dotenv, find_dotenv
import json, datetime, requests, time, os

load_dotenv(find_dotenv())
USERNAME = os.getenv("IG_USERNAME")
DISCORD_WEBHOOK = os.getenv("DISCORD_WEBHOOK")

def write_json(new_data):
    with open("log.json",'r+') as file:
        file_data = json.load(file)
        file_data["posts"].append(new_data)
        file.seek(0)
        json.dump(file_data, file, indent = 4)

def countdown(h=3, m=0, s=0):
    total_seconds = h * 3600 + m * 60 + s
    while total_seconds > 0:
        timer = datetime.timedelta(seconds = total_seconds)
        print(timer, end="\r")
        time.sleep(1)
        total_seconds -= 1

def discordsend(user, data):
    ilog = open("log.json", "r")
    ilogged = json.loads(ilog.read())
    oldmedcode = ilogged["posts"]
    newmedcode = ((list((((data["graphql"])["user"])["edge_owner_to_timeline_media"])["edges"])[0])["node"])["shortcode"]
    if newmedcode not in oldmedcode:
        rep = (data["graphql"])["user"]
        full_name = rep["full_name"]
        profileurl = rep["profile_pic_url_hd"]
        media = (rep["edge_owner_to_timeline_media"])["edges"]
        latestmed = (list(media)[0])["node"]
        medurl = "https://instagram.com/p/" + latestmed["shortcode"]
        medpreview = latestmed["display_url"]
        medcaption = ((((latestmed["edge_media_to_caption"])["edges"])[0])["node"])["text"]
        medepoch = latestmed["taken_at_timestamp"]
        medtime = time.strftime("%Y-%m-%dT%H:%M:00.000Z", time.localtime(medepoch-19800))

        #Template of Discord Webhooks from Python - https://gist.github.com/Bilka2/5dd2ca2b6e9f3573e0c2defe5d3031b2
        data = {
            "content" : "",
            "username" : "Social Media",
            "avatar_url" : "https://media.discordapp.net/attachments/839327846773162014/964543848200159302/ThisIsBusiness.png"
        }
        data["embeds"] = [
            {
                "author" : {
                    "name" : full_name + " (@"+ user +")",
                    "url" : "https://instagram.com/"+ user,
                    "icon_url" : profileurl
                },
                "color" : "12632256",
                "url" : medurl,
                "timestamp" : medtime,
                "image" : {
                    "url" : medpreview
                },
                "fields": [
                    {
                      "name": medurl,
                      "value": medcaption
                    }
                ],
                "footer" : {
                    "text" : "Instagram",
                    "icon_url" : "https://media.discordapp.net/attachments/839327846773162014/964711691571040357/instagram.png"
                }

            }
        ]

        result = requests.post(DISCORD_WEBHOOK, json = data)
        try:
            result.raise_for_status()
        except requests.exceptions.HTTPError as err:
            print(err)
        else:
            print("Payload for "+ user +" was delivered successfully, with code {}.".format(result.status_code))
        return latestmed["shortcode"]
    else:
        print("No new Media from " + user)
        return None

def main():
    while True:
        print(" "*5 + "Instagram to Discord" + " "*5)
        print("Getting Info for "+ USERNAME)
        try:
            url = "https://www.instagram.com/"+ USERNAME +"/?__a=1"
            response = urlopen(url)
            data_json = json.loads(response.read().decode())
            if (DISCORD_WEBHOOK==None) or (USERNAME==None):
                print("Correct Environment Variables not provided!")
                break
            else:
                retcode = discordsend(USERNAME, data_json)
                if retcode != None:
                    print("https://instagram.com/p/" + retcode)
                    write_json(retcode)
        except json.decoder.JSONDecodeError: #Prevention for the code to run if Instagram's Rate Limit has been hit
            print("Sussy Insta Bro")
            pass
        countdown() #Default is set to 3 hours, it can be changed by using countdown(h,m,s) providing the specific values

main()
