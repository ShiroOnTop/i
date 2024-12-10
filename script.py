from telethon import TelegramClient, errors
import asyncio

# Your API credentials
API_ID = '20831568'
API_HASH = '4194de5006d5a4e37b58d4c2971ff75d'

# List of target groups or channels
TARGETS = [
    {"channel": -1002287228750},  # Regular channel
    {"channel": '@instaempiremarket'},  # Public channel with username
    {"channel": -1001718246645, "topic_id": 12345},  # Forum-style channel with a specific topic
]

# Advertisement message
AD_MESSAGE = """
**Welcome To Shiro Shop**

**The Cheapest and Most Reliable Seller on the Market for All Your Discord Needs!**

**Level up your community engagement with Discord Server Boosts, Nitro Tokens, Aged Accounts, Botted Members, and more!**

**Discord Server Boost**
`14x 1 month server boost = 3$`
`14x 3 month server boost = 6$`

**Discord Acc Token With Nitro**
`1 Month Nitro Token = 0.80$`
`3 Month Nitro Token = 2$`

**Discord Botted Members**
`Offline botted member = 2.50$/k`
`Online botted member = 4$/k`

**Discord Aged Account**
`2016-2022 (full access)`

**Discord Nitro**
`1 Month Nitro = 7$`
`1 Year Nitro = 20$`

**Discord Decorations**
`4.99$ → 3.49$`
`5.49$ → 3.84$`
`6.99$ → 4.89$`
`8.99$ → 5.29$`
`9.99$ → 6.99$`
`12.00$ → 8.40$`

**Discord Bot**
`Discord Auto Middleman Bot = 50$`
`MM Server Setup With Role & Channels = 3$`
`Custom Bot = 3$`

Payment method: **LTC/BTC**

Dm @shiro_always_on_top On Discord / Here

MM✅
"""

# List of SOCKS5 proxies (proxy_type, host, port)
PROXIES = [
    ('socks5', '54.37.78.53', 27606),
    ('socks5', '174.64.199.79', 4145),
    ('socks5', '68.71.249.158', 4145),
    # Add more proxies here
]

# Function to send advertisements
async def send_ads(client):
    for target in TARGETS:
        try:
            if "topic_id" in target:  # Forum-style channel with a specific topic
                await client.send_message(
                    target["channel"],
                    AD_MESSAGE,
                    link_preview=False,
                    reply_to=target["topic_id"]
                )
                print(f"Message sent to Topic ID: {target['topic_id']} in Channel: {target['channel']}")
            else:  # Regular channel or group
                await client.send_message(target["channel"], AD_MESSAGE, link_preview=False)
                print(f"Message sent to Channel: {target['channel']}")
        except errors.FloodWaitError as e:
            print(f"Flood wait error: Sleeping for {e.seconds} seconds")
            await asyncio.sleep(e.seconds)
        except Exception as e:
            print(f"Failed to send message to {target}: {e}")

# Main function
async def main():
    for idx, proxy in enumerate(PROXIES):
        try:
            session_name = f'user_session_{idx}'  # Unique session for each proxy
            print(f"Trying proxy {proxy[1]}:{proxy[2]} with session {session_name}...")

            # Create the Telegram client with the proxy
            client = TelegramClient(session_name, API_ID, API_HASH, proxy=proxy)
            await client.start()
            print(f"Connected successfully via proxy {proxy[1]}:{proxy[2]}")
            await send_ads(client)
            await client.disconnect()
            break  # Exit the loop if successful
        except Exception as e:
            print(f"Failed to connect via proxy {proxy[1]}:{proxy[2]}: {e}")
            continue  # Try the next proxy

    print("All proxies attempted.")

# Run the script
asyncio.run(main())
