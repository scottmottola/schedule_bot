import os
import requests
import datetime

import discord
from dotenv import load_dotenv

BASE = "http://127.0.0.1:5000/"

load_dotenv()
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client()


def create_user(user, discord_user):
    data = user.split(";")
    data = data[1]
    data = data.split()
    userdata = {"user_name": data[0], "user_pass": data[1]}
    route = BASE + "users"
    response = requests.post(route, userdata)
    rdata = response.json()
    create_discord_user(discord_user, rdata["user_id"])
    return f"user_id: {rdata['user_id']}, user_name: {rdata['user_name']}"


def create_discord_user(discord_user, id):
    route = BASE + "discorduser"
    response = requests.post(route, {"user_id": id, "discord_user_name": discord_user})
    return response.json()


def create_discord_server(discord_server, discord_user):
    route = BASE + "discorduser"
    discorduser = requests.get(route, {"discord_user_name": discord_user})
    if discorduser.status_code != 200:
        return "Error no account"
    
    ruser = discorduser.json()

    route = BASE + "discordserver"
    response = requests.post(route, {"discord_user_id": ruser['discord_user_id'], "discord_server_name": discord_server, "discord_server_nickname": discord_user})
    return response.json()


def create_discord_channel(discord_channel, discord_server, discord_user):
    route = BASE + "discorduser"
    discorduser = requests.get(route, {"discord_user_name": discord_user})
    if discorduser.status_code != 200:
        return "Error no account"
    
    ruser = discorduser.json()
    
    rserver = ""

    route = BASE + "discordserver"
    discordserver = requests.get(route, {"discord_server_name": discord_server})
    if discordserver.status_code != 200:
        if discordserver.status_code == 404:
            discordserver = create_discord_server(discord_server, discord_user)
            "This user is not connected to this server. Created a connection to server. Please try again."
        else:
            return "Error with the server"
    for server in discordserver.json():
        jserver = server
        if jserver["discord_user_id"] == ruser["discord_user_id"]:
            rserver = jserver
    
    
    
    route = BASE + "discordchannel"
    response = requests.post(route, {"discord_server_id": rserver['discord_server_id'], "discord_channel_name": discord_channel, "discord_channel_mute": False})
    return response.json()


def create_planner(discord_user):
    route = BASE + "discorduser"
    discorduser = requests.get(route, {"discord_user_name": discord_user})
    if discorduser.status_code != 200:
        return "Error no account"
    
    ruser = discorduser.json()

    route = BASE + "planner"
    response = requests.post(route, {"user_id": ruser['user_id'], "planner_name": "Unnamed Planner"})
    return response.json()


def create_plan(plan, discord_user, discord_channel, discord_server):
    route = BASE + "discorduser"
    discorduser = requests.get(route, {"discord_user_name": discord_user})
    if discorduser.status_code != 200:
        return "Error no account"
    
    ruser = discorduser.json()
    
    rserver = ""
    print(discord_server)
    print(discord_channel)

    route = BASE + "discordserver"
    discordserver = requests.get(route, {"discord_server_name": discord_server})
    print(discordserver.json())
    if discordserver.status_code != 200:
        if discordserver.status_code == 404:
            discordserver = create_discord_server(discord_server, discord_user)
            "This user is not connected to this server. Created a connection to server. Please try again."
        else:
            return "Error with the server"
    for server in discordserver.json():
        jserver = server
        if jserver["discord_user_id"] == ruser["discord_user_id"]:
            rserver = jserver
    
    rchannel = ""

    route = BASE + "discordchannel"
    discordchannel = requests.get(route, {"discord_channel_name": discord_channel})
    if discordchannel.status_code != 200:
        if discordchannel.status_code == 404:
            discordchannel = create_discord_channel(discord_channel, discord_server, discord_user)
            "This user is not connected to this channel. Created a connection to channel. Please try again."
        else:
            return "Error with the channel"
    for channel in discordchannel.json():
        jchannel = channel
        if jchannel["discord_server_id"] == rserver["discord_server_id"]:
            rchannel = jchannel
    
    rplanner = ""

    route = BASE + "planner"
    planners = requests.get(route, {"user_id": ruser['user_id']})
    if planners.status_code != 200:
        if planners.status_code == 404:
            planners = create_planner(discord_user)
            "This user is not connected to this planner. Created a connection to planner. Please try again."
        else:
            return "Error with the planner"
    for planner in planners.json():
        jplanner = planner
        if jplanner["user_id"] == ruser["user_id"]:
            rplanner = jplanner

    data = plan.split(";")
    data = data[1]
    data = data.split("/")

    plan_name = data[0]
    plan_start = data[1]
    plan_end = data[2]
    # plan_start = datetime.datetime.strptime(data[1], '%y,%m,%d,%H,%M,%S')
    # plan_end = datetime.datetime.strptime(data[2], '%y,%m,%d,%H,%M,%S')
    # times1 = [int(time) for time in data[1].split(",")]
    # times2 = [int(time) for time in data[2].split(",")]
    # plan_start = datetime.datetime(times1[0], times1[1], times1[2], times1[3], times1[4], times1[5])
    # plan_end = datetime.datetime(times2[0], times2[1], times2[2], times2[3], times2[4], times2[5])
    repeat = bool(data[3])
    if data[4] != " ":
        repeat_frequency = data[1]
    else:
        repeat_frequency = data[4]
    
    if data[5] != " ":
        repeat_duration = data[1]
    else:
        repeat_duration = data[5]
    # if data[4] != " ":
    #     times3 = [int(time) for time in data[4].split(",")]
    #     # repeat_frequency = datetime.datetime.strptime(data[4], '%y,%m,%d,%H,%M,%S')
    #     repeat_frequency = datetime.datetime(times3[0], times3[1], times3[2], times3[3], times3[4], times3[5])
    # else:
    #     # repeat_frequency = datetime.datetime.strptime(data[1], '%y,%m,%d,%H,%M,%S')
    #     repeat_frequency = datetime.datetime(times1[0], times1[1], times1[2], times1[3], times1[4], times1[5])
    # if data[5] != " ":
    #     times4 = [int(time) for time in data[5].split(",")]
    #     # repeat_duration = datetime.datetime.strptime(data[5], '%y,%m,%d,%H,%M,%S')
    #     repeat_duration = datetime.datetime(times4[0], times4[1], times4[2], times4[3], times4[4], times4[5])
    # else:
    #     # repeat_duration = datetime.datetime.strptime(data[1], '%y,%m,%d,%H,%M,%S')
    #     repeat_duration = datetime.datetime(times1[0], times1[1], times1[2], times1[3], times1[4], times1[5])
    description = data[6]

    print(plan_start)
    print(data)

    route = BASE + "plan"
    response = requests.post(route, {"planner_id": rplanner["planner_id"], "plan_name": plan_name, "plan_start": plan_start, "plan_end": plan_end, "repeat": repeat,"repeat_frequency": repeat_frequency, "repeat_duration": repeat_duration, "description": description})
    rdata = response.json()

    print(response)

    create_announcement(rchannel["discord_channel_id"], rdata["plan_id"], plan_start)
    return response.json()


def create_announcement(discord_channel_id, plan_id, alert):
    route = BASE + "announcement"
    response = requests.post(route, {"discord_channel_id": discord_channel_id, "plan_id": plan_id, "announce": True, "alert": alert})
    return response.json()


def check_schedule(discord_user):
    route = BASE + "discorduser"
    discorduser = requests.get(route, {"discord_user_name": discord_user})
    if discorduser.status_code != 200:
        return "Error no account"
    
    rdiscorduser = discorduser.json()
    
    rplanner = ""
    plans_list = []

    route = BASE + "planner"
    planners = requests.get(route, {"user_id": rdiscorduser['user_id']})
    if planners.status_code != 200:
        if planners.status_code == 404:
            planners = create_planner(discord_user)
            "This user is not connected to this planner. Created a connection to planner. Please try again."
        else:
            return "Error with the planner"
    for planner in planners.json():
        print(planner)
        jplanner = planner
        if jplanner["user_id"] == rdiscorduser["user_id"]:
            rplanner = jplanner

            route = BASE + "plan"
            plans = requests.get(route, {"planner_id": rplanner["planner_id"]})
            for plan in plans.json():
                print(plan)
                if not plan:
                    return "No plans."
                plans_list.append(plan)
    return plans_list


def mute_me(discord_user ,discord_channel):
    route = BASE + "discorduser"
    discorduser = requests.get(route, {"discord_user_name": discord_user})
    if discorduser.status_code != 200:
        return "Error no account"
    
    ruser = discorduser.json()

    route = BASE + "discordserver"
    discordserver = requests.get(route, {"discord_user_id": ruser["discord_user_id"]})
    if discordserver.status_code != 200:
        if discordserver.status_code == 404:
            "No server connected to this user."
        else:
            return "Error with the server"

    rserver = discordserver.json()

    route = BASE + "discordchannel"
    discordchannel = requests.get(route, {"discord_channel_name": discord_channel})
    if discordchannel.status_code != 200:
        if discordchannel.status_code == 404:
            "No channel connected to this user."
        else:
            return "Error with the channel"

    rchannel = discordchannel.json()

    
    if rchannel["discord_server_id"] == rserver["discord_server_id"]:
        route = BASE + "announcement"
        announcement = requests.get(route, {"discord_channel_id": rchannel["discord_channel_id"]})
        if announcement.status_code != 200:
            if announcement.status_code == 404:
                "No announcement connected to this user and channel."
            else:
                return "Error with the announcements"

        rannouncement = announcement.json()
        for announce in rannouncement:
            requests.patch(BASE + "announcement", {"search_id": announce["announce_id"], "announce": False})

    return f"Muted {discord_user}."


def mute_channel(discord_channel):
    route = BASE + "discordchannel"
    discordchannel = requests.get(route, {"discord_channel_name": discord_channel})
    if discordchannel.status_code != 200:
        if discordchannel.status_code == 404:
            "No channel connected to this user."
        else:
            return "Error with the channel"

    rchannel = discordchannel.json()

    route = BASE + "announcement"
    announcement = requests.get(route, {"discord_channel_id": rchannel["discord_channel_id"]})
    if announcement.status_code != 200:
        if announcement.status_code == 404:
            "No announcement connected to this user and channel."
        else:
            return "Error with the announcements"

    rannouncement = announcement.json()
    for announce in rannouncement:
        requests.patch(BASE + "announcement", {"search_id": announce["announce_id"], "announce": False})

    return f"Muted {discord_channel}."


@client.event
async def on_ready():
    print(
        f'{client.user} has connected to discord!' + '\n'
        )


@client.event
async def on_message(message):

    msg = message.content

    if message.author == client.user:
        return
    
    if msg.startswith('/hello'):
        await message.channel.send(f'Hello {message.author.name}')
    
    if msg.startswith('/help'):
        await message.channel.send('''These are the actions you can use.  (To create an account please go to ...)
        /add plan;(plan-name)/[plan start](2012-01-01T23:30:00)[yyyy-mm-ddThh:mm:ss]/[plan end](2012-01-01T23:30:00)[yyyy-mm-ddThh:mm:ss]/
            [does it repeat](False)/[if so when does it repeat](WIP)/[when does it stop repeating](WIP)/(description) - adds a plan for everyone in this channel.  
            you do not need to input anything in brackets including the brackets and you do not need the parentheses, colons and semicolons are needed. WIP
        /remove plan;(plan-name) - removes a plan for everyone in this channel. WIP
        /check schedule - checks the schedule that is identical for every one in this channel. WIP
        /mute channel - will no longer announce in this channel. WIP
        /mute me - will no longer @ the user when announcing. WIP
        /create account - will prompt the user in a private channel to create an account.
        ''')
    
    if msg.startswith('/add plan'):
        await message.channel.send(create_plan(msg, message.author.name, message.channel.name, message.guild.name))
    
    if msg.startswith('/remove plan'):
        await message.channel.send('What plan do you want to remove? WIP')
    
    if msg.startswith('/check schedule'):
        await message.channel.send(check_schedule(message.author.name))
    
    if msg.startswith('/mute channel'):
        await message.channel.send(mute_channel(message.channel.name))
    
    if msg.startswith('/mute me'):
        await message.channel.send(mute_me(message.author.name, message.channel.name))
    
    if msg.startswith('/create user; '):
        await message.author.send(create_user(msg, message.author.name))
    
    if msg.startswith('/create account'):
        await message.author.send("Type (/create user; (user_name) (user_pass)) to create an account. without the parentheses no spaces in name or pass")
    
    if msg.startswith('/respond'):
        await message.author.send("Hi")


client.run(os.getenv('DISCORD_TOKEN'))