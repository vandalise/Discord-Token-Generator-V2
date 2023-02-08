from colorama import Fore
import tls_client
import websocket
import threading
import random
import base64
import httpx
import json
import time
import sys
import os

os.system("cls||clear")
print(f"{Fore.YELLOW}|/| Loading capmonster{Fore.RESET}")
try:
    captchaKey = json.loads(open("config.json", "r").read())["capkey"]
except:
    print(f"  {Fore.WHITE}|>|{Fore.RED} Error loading capmonster key from config.json")
    time.sleep(3)
    sys.exit()
try:
    get_balance_resp = httpx.post(f"https://api.capmonster.cloud/getBalance", json={"clientKey": captchaKey}).text
    CaptchaBalance = json.loads(get_balance_resp)["balance"]
except Exception as e:
    print(f"  {Fore.WHITE}|>|{Fore.RED} Capmonster API is down or the key is invalid!!")
    time.sleep(3)
    sys.exit()
print(f"{Fore.YELLOW}|/| Loading proxies{Fore.RESET}")
try:
    proxylist = []
    proxycount = 0
    for proxy in open("proxies.txt", "r").read().splitlines():
        proxylist.append(proxy)
        proxycount +=1
except:
    print(f"  {Fore.WHITE}|>|{Fore.RED} Error loading proxies from proxies.txt")
    time.sleep(3)
    sys.exit()

def getBanner():
    global CaptchaBalance, proxycount
    text = f"""
███████╗██╗   ██╗██████╗  ██████╗ ███████╗
██╔════╝██║   ██║██╔══██╗██╔════╝ ██╔════╝
███████╗██║   ██║██████╔╝██║  ███╗█████╗  
╚════██║██║   ██║██╔══██╗██║   ██║██╔══╝  
███████║╚██████╔╝██║  ██║╚██████╔╝███████╗
╚══════╝ ╚═════╝ ╚═╝  ╚═╝ ╚═════╝ ╚══════╝
      Captchas: [${CaptchaBalance}] Proxies: [{proxycount}]
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃                 SurgeCord               ┃
┃           Discord Token Generator       ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛

"""
    xbanner = ""
    banner = ""
    count = 100
    for line in text.splitlines():
        line = line.replace("═", "\u001b[37m═")
        line = line.replace("╝", "\u001b[37m}╝")
        line = line.replace("╚", "\u001b[37m╚")
        line = line.replace("║", "\u001b[37m║")
        line = line.replace("╗", "\u001b[37m╗")
        line = line.replace("╔", "\u001b[37m╔")
        line = line.replace("█", f"\033[38;2;0;{count};255m█")
        line = line.replace("{", "")
        line = line.replace("}", "")
        xbanner+=f"{line}\n"
        count = count -15
    for line in xbanner.splitlines():
        banner += ("                    " +line+"\n")
    return banner

def get_ws():
    games = ['Minecraft', 'Rust', 'VRChat', 'reeeee', 'MORDHAU', 'Fortnite', 'Apex Legends', 'Escape from Tarkov', 'Rainbow Six Siege', 'Counter-Strike: Global Offense', 'Sinner: Sacrifice for Redemption', 'Minion Masters', 'King of the Hat', 'Bad North', 'Moonlighter', 'Frostpunk', 'Starbound', 'Masters of Anima', 'Celeste', 'Dead Cells', 'CrossCode', 'Omensight', 'Into the Breach', 'Battle Chasers: Nightwar', 'Red Faction Guerrilla Re-Mars-tered Edition', 'Spellforce 3', 'This is the Police 2', 'Hollow Knight', 'Subnautica', 'The Banner Saga 3', 'Pillars of Eternity II: Deadfire', 'This War of Mine', 'Last Day of June', 'Ticket to Ride', 'RollerCoaster Tycoon 2: Triple Thrill Pack', '140', 'Shadow Tactics: Blades of the Shogun', 'Pony Island', 'Lost Horizon', 'Metro: Last Light Redux', 'Unleash', 'Guacamelee! Super Turbo Championship Edition', 'Brutal Legend', 'Psychonauts', 'The End Is Nigh', 'Seasons After Fall', 'SOMA', 'Trine 2: Complete Story', 'Trine 3: The Artifacts of Power', 'Trine Enchanted Edition', 'Slime-San', 'The Inner World', 'Bridge Constructor', 'Bridge Constructor Medieval', 'Dead Age', 'Risk of Rain', "Wasteland 2: Director's Cut", 'The Metronomicon: Slay The Dance Floor', 'TowerFall Ascension + Expansion', 'Nidhogg', 'System Shock: Enhanced Edition', 'System Shock 2', "Oddworld:New 'n' Tasty!", 'Out of the Park Baseball 18', 'Hob', 'Destiny 2', 'Torchlight', 'Torchlight 2', 'INSIDE', 'LIMBO', "Monaco: What's Yours Is Mine", 'Tooth and Tail', 'Dandara', 'GoNNER', 'Kathy Rain', 'Kingdom: Classic', 'Kingdom: New Lands', 'Tormentor X Punisher', 'Chaos Reborn', 'Ashes of the Singularity: Escalation', 'Galactic Civilizations III', 'Super Meat Boy', 'Super Hexagon', 'de Blob 2', 'Darksiders II Deathinitive Edition', 'Darksiders Warmastered Edition', 'de Blob', 'Red Faction 1', 'Dungeon Defenders']
    mobile = {
        "op": 2,
        "d": {
            "token": "",
            "properties": {
                "$os": "Android",
                "$browser": "Discord Android",
                "$device": "Android 12"
            },
        }
    }
    game = random.choice(games)
    pc = {
        "op": 2,
        "d": {
            "token": "",
            "capabilities": 125,
            "properties": {
                "$os": "Windows",
                "$browser": "Chrome",
                "$device": "Windows Device",
                "system_locale": "en-US",
                "browser_user_agent":
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36",
                "browser_version": "96.0.4664.45",
                "os_version": "10",
                "referrer": "",
                "referring_domain": "",
                "referrer_current": "",
                "referring_domain_current": "",
                "release_channel": "stable",
                "client_build_number": 105691,
                "client_event_source": None
            },
            "presence": {
                "status": random.choice(["online", "idle"]),
                "game": {"name": game, "type": 0},
                "since": 0,
                "activities": [],
                "afk": False
            },
            "compress": False,
            "client_state": {
                "guild_hashes": {},
                "highest_last_message_id": "0",
                "read_state_version": 0,
                "user_guild_settings_version": -1,
                "user_settings_version": -1
            }
        },
        "s": None,
        "t": None
    }
    return pc, mobile


def WSLogin(token):
    while True:
        try:
            ws = websocket.WebSocket()
            ws.connect("wss://gateway.discord.gg/?encoding=json&v=6")
            pc, mobile = get_ws()
            mobile["d"]["token"] = token
            pc["d"]["token"] = token
            ws.send(json.dumps(random.choice([pc, mobile])))
            heartbeat = json.loads(ws.recv())['d']['heartbeat_interval']
            time.sleep(heartbeat / 1000)
            ws.send(json.dumps({"op": 1, "d": None}))
        except Exception as e:
            continue


def solve_cap():
        payload = {
            "clientKey": f"{captchaKey}",
            "task": {
                "type": "HCaptchaTaskProxyless",
                "userAgent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36 Edg/92.0.902.73",
                "websiteKey": f"4c672d35-0701-42b2-88c3-78380b0db560",
                "websiteURL": f"https://discord.com/"
            }
        }
        while True:
            try:
                tempreqx = httpx.post("https://api.capmonster.cloud/createTask", json=payload).text
                taskid = json.loads(tempreqx)["taskId"]
                break
            except:
                continue
        payload1 = {
            "clientKey": f"{captchaKey}",
            "taskId": taskid
        }
        while True:
            r = httpx.post(f"https://api.capmonster.cloud/getTaskResult", json=payload1).text
            status = json.loads(r)["status"]
            if status == "processing":
                continue
            elif status == "ready":
                data = json.loads(r)
                break
        return data["solution"]["gRecaptchaResponse"]

def CheckUnformatted(auth):
    try:
        halfauth = auth[:len(auth)//2]
        x = httpx.get('https://discord.com/api/v9/users/@me', headers={'Authorization': auth})
        if x.status_code == 200:
            y = httpx.get('https://discord.com/api/v9/users/@me/affinities/users', headers={'Authorization': auth})
            json = x.json()
            if y.status_code == 200:
                print(Fore.GREEN + f'VALID: {halfauth}***** {json["username"]}#{json["discriminator"]}')
                open("valid.txt", "a").write(auth+"\n")
                open("unformat.txt", "a").write(auth+"\n")
            elif y.status_code == 403:
                print(Fore.YELLOW + f'LOCKED: {halfauth}***** {json["username"]}#{json["discriminator"]}')
            elif y.status_code == 429:
                print(Fore.YELLOW + f"You're being rate limited")
                time.sleep(y.headers['retry-after'])
            elif x.status_code == 429:
                print(Fore.YELLOW + f"You're being rate limited")
                time.sleep(y.headers['retry-after'])
            else:
                print(Fore.RED + f'INVALID: {halfauth}')
    except Exception as e:
        print(e)
        pass


def xprop():
    xpropheader = str("""{"os":"Windows","browser":"Chrome","device":"","system_locale":"en-US","browser_user_agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36","browser_version":"105.0.0.0","os_version":"10","referrer":"","referring_domain":"","referrer_current":"","referring_domain_current":"","release_channel":"stable","client_build_number":151638,"client_event_source":null}""")
    xprops = base64.b64encode(xpropheader.encode('utf-8')).decode('utf-8')
    return xprops

def cookie():
    proxy = random.choice(proxylist)
    proxies = f"http://{proxy}"
    Client = tls_client.Session(
        ja3_string="771,4865-4866-4867-49195-49199-49196-49200-52393-52392-49171-49172-156-157-47-53,0-23-65281-10-11-35-16-5-13-18-51-45-43-27-17513,29-23-24,0",
        h2_settings={
            "HEADER_TABLE_SIZE": 65536,
            "MAX_CONCURRENT_STREAMS": 1000,
            "INITIAL_WINDOW_SIZE": 6291456,
            "MAX_HEADER_LIST_SIZE": 262144
        },
        h2_settings_order=[
            "HEADER_TABLE_SIZE",
            "MAX_CONCURRENT_STREAMS",
            "INITIAL_WINDOW_SIZE",
            "MAX_HEADER_LIST_SIZE"
        ],
        supported_signature_algorithms=[
            "ECDSAWithP256AndSHA256",
            "PSSWithSHA256",
            "PKCS1WithSHA256",
            "ECDSAWithP384AndSHA384",
            "PSSWithSHA384",
            "PKCS1WithSHA384",
            "PSSWithSHA512",
            "PKCS1WithSHA512",
        ],
        supported_versions=["GREASE", "1.3", "1.2"],
        key_share_curves=["GREASE", "X25519"],
        cert_compression_algo="brotli",
        pseudo_header_order=[
            ":method",
            ":authority",
            ":scheme",
            ":path"
        ],
        connection_flow=15663105,
            header_order=[
                "accept",
                "user-agent",
                "accept-encoding",
                "accept-language"
            ]
        )
    return dict(Client.get("https://discord.com/register", proxy=proxies).cookies)

def join_vc(token, guildid, channelid):
    while True:
        try:
            ws = websocket.WebSocket()
            ws.connect("wss://gateway.discord.gg/?v=9&encoding=json")
            ws.send(json.dumps({"op": 2,"d": {"token": token, "properties": {"$os": "windows","$browser": "Discord","$device": "desktop"}}}))
            ws.send(json.dumps({"op": 4,"d": {"guild_id": guildid,"channel_id": channelid, "self_mute": True,"self_deaf": True}}))
            ws.close()
        except:
            continue

def gen(username, invite):
    while True:
        try:
            proxy = random.choice(proxylist)
            proxies = f"http://{proxy}"
            Client = tls_client.Session(
                ja3_string="771,4865-4866-4867-49195-49199-49196-49200-52393-52392-49171-49172-156-157-47-53,0-23-65281-10-11-35-16-5-13-18-51-45-43-27-17513,29-23-24,0",
                h2_settings={
                    "HEADER_TABLE_SIZE": 65536,
                    "MAX_CONCURRENT_STREAMS": 1000,
                    "INITIAL_WINDOW_SIZE": 6291456,
                    "MAX_HEADER_LIST_SIZE": 262144
                },
                h2_settings_order=[
                    "HEADER_TABLE_SIZE",
                    "MAX_CONCURRENT_STREAMS",
                    "INITIAL_WINDOW_SIZE",
                    "MAX_HEADER_LIST_SIZE"
                ],
                supported_signature_algorithms=[
                    "ECDSAWithP256AndSHA256",
                    "PSSWithSHA256",
                    "PKCS1WithSHA256",
                    "ECDSAWithP384AndSHA384",
                    "PSSWithSHA384",
                    "PKCS1WithSHA384",
                    "PSSWithSHA512",
                    "PKCS1WithSHA512",
                ],
                supported_versions=["GREASE", "1.3", "1.2"],
                key_share_curves=["GREASE", "X25519"],
                cert_compression_algo="brotli",
                pseudo_header_order=[
                    ":method",
                    ":authority",
                    ":scheme",
                    ":path"
                ],
                connection_flow=15663105,
                header_order=[
                    "accept",
                    "user-agent",
                    "accept-encoding",
                    "accept-language"
                ]
            )
            cap = solve_cap()
            payload = {
                "captcha_key": cap,
                "consent": True,
                "fingerprint": "",
                "gift_code_sku_id": "",
                "invite": invite,
                "username": username,
                            }
            cookiex = cookie()
            cookiez = f"__dcfduid={cookiex['__dcfduid']}; __sdcfduid={cookiex['__sdcfduid']};"
            headers = {
                "accept":"*/*",
                "accept-encoding": "gzip, deflate, br",
                "accept-language": "en-US,en;q=0.9",
                "content-type": "application/json",
                "cookie": cookiez,
                "origin": "https://discord.com",
                "referer": f"https://discord.com/invite/{invite}",
                "sec-ch-ua": 'Google Chrome";v="105", "Not)A;Brand";v="8", "Chromium";v="105',
                "sec-ch-ua-mobile": "?0",
                "sec-ch-ua-platform": "Windows",
                "sec-fetch-dest": "empty",
                "sec-fetch-mode": "cors",
                "sec-fetch-site": "same-origin",
                "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36",
                "x-debug-options": "bugReporterEnabled",
                "x-discord-locale": "en-US",
                "x-fingerprint": "",
                "x-super-properties": xprop()
            }
            x = Client.post("https://discord.com/api/v9/auth/register", headers=headers, json=payload, proxy=proxies)
            if "token" in x.text:
                token = json.loads(x.text)["token"]
                halfauth = token[:len(token)//2]
                print(f"{Fore.WHITE}> {Fore.BLUE}Generated: {Fore.WHITE}{halfauth}*****")
                open("tokens.txt", "a").write(token+"\n")
                threading.Thread(target=WSLogin, args=(token,)).start()
                pass
            elif "retry_after" in x.text:
                delay = json.loads(x.text)["retry_after"]
                print(f"{Fore.WHITE}> {Fore.RED}Proxy ratelimited for {Fore.WHITE}{delay}{Fore.RED} seconds")
                continue
            elif "invalid-response" or "invalid-input-response" in x.text:
                print(f"{Fore.WHITE}> {Fore.RED}Captcha error: {cap}")
                continue
            else:
                print(x.text)
        except Exception as e:
            continue

def main():
    os.system("cls||clear")
    print(getBanner())
    username = input(f"{Fore.WHITE}> {Fore.BLUE}Username{Fore.WHITE}: ")
    invite = input(f"{Fore.WHITE}> {Fore.BLUE}Input Invite{Fore.WHITE}: {Fore.BLUE}https://discord.gg/{Fore.WHITE}")
    threads = int(input(f"{Fore.WHITE}> {Fore.BLUE}Threads{Fore.WHITE}: "))
    for i in range(threads):
        threading.Thread(target=gen, args=(username, invite, )).start()

main()
