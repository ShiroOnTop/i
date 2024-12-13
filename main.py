# -*- coding: utf-8 -*-
from flask import Flask
from threading import Thread
from telethon import TelegramClient, errors
import asyncio

# Your API credentials
API_ID = '20658975'
API_HASH = '99a9c003635723dc91417afb83e6e17a'

# List of target groups, channels, or forum-style channels with topic IDs
TARGETS = [
    {"channel": -1002495894937},  # Channel: Discord Badge & Nitro Chat
    {"channel": -1002136187908},  # Channel: Badge Town Chat
    {"channel": -1002237087611},  # Channel: Discord wts/wtb
    {"channel": -1001718246645},  # Channel: The Stock
    {"channel": -1001935659628},  # Channel: DS wts-wtb
    {"channel": -1002089943475},  # Channel: Wts wtb discord stuffs
    {"channel": -1002236357366},  # Channel: Badge City Chat
    {"channel": -1002153182622},  # Channel: Discord Shop Wts wtb
    {"channel": -1002218150029},  # Channel: Badge shop wts/wtb
    {"channel": -1002044678462},  # Channel: Asteral wtb / wts
    {"channel": -1002354514183},  # Channel: Market'WTS
]

# Advertisement message
AD_MESSAGE = """
**Welcome To Shiro Shop**

**The Cheapest and Most Reliable Seller on the Market for All Your Discord Needs!**

**Level up your community engagement with Discord Server Boosts, Nitro Tokens, Aged Accounts, Botted Members, and more!**

**Discord Server Boost**
14x 1 month server boost = 3$
14x 3 month server boost = 6$

**Discord Acc Token With Nitro**
1 Month Nitro Token = 0.80$
3 Month Nitro Token = 2$

**Discord Botted Members**
Offline botted member = 2.50$/k
Online botted member = 4$/k

**Discord Aged Account**
2016-2022 (full access)

**Discord Nitro**
1 Month Nitro = 7$
1 Year Nitro = 20$

**Discord Decorations**
4.99$ → 3.49$
5.49$ → 3.84$
6.99$ → 4.89$
8.99$ → 5.29$
9.99$ → 6.99$
12.00$ → 8.40$

**Discord Bot**
Discord Auto Middleman Bot = 50$
MM Server Setup With Role & Channels = 3$
Custom Bot = 3$

Payment method: **LTC/BTC**

Dm @shiro_always_on_top On Discord / Here

MM✅
"""

# Flask app setup
app = Flask('')

@app.route('/')
def home():
    return "Bot is running and alive!"

def run_flask():
    app.run(host='0.0.0.0', port=8080)

# Telegram bot setup
client = TelegramClient('user_session', API_ID, API_HASH)

async def send_ads():
    for target in TARGETS:
        try:
            if "topic_id" in target:  # Check if the target has a topic ID
                await client.send_message(
                    target["channel"],
                    AD_MESSAGE,
                    link_preview=False,
                    reply_to=target["topic_id"]
                )
                print(f"Message sent to Topic ID: {target['topic_id']} in Channel: {target['channel']}")
            else:  # Regular channels/groups
                await client.send_message(target["channel"], AD_MESSAGE, link_preview=False)
                print(f"Message sent to Channel: {target['channel']}")
        except errors.FloodWaitError as e:
            print(f"Flood wait error: Sleeping for {e.seconds} seconds")
            await asyncio.sleep(e.seconds)
        except Exception as e:
            print(f"Failed to send message to {target}: {e}")

async def main():
    print("Logging in...")
    await client.start()
    print("Logged in successfully!")
    while True:
        await send_ads()
        print("Messages sent. Waiting for the next round...")
        await asyncio.sleep(3600)  # Wait 1 hour before sending again

# Run Flask and Telegram bot in parallel
if __name__ == "__main__":
    flask_thread = Thread(target=run_flask)
    flask_thread.start()

    with client:
        client.loop.run_until_complete(main())
