#!/usr/bin/env python
#######################################################################
# Mission Description
#
# ##Description
#
# Then, make an HTTP POST request to the URL http://hdegip.appspot.com/challenge/003/endpoint 
# which contains the JSON string as a body part.
#
# * Content-Type: of the request must be "application/json".
# * The URL is protected by HTTP Basic Authentication, which is explained on Chapter 2 of RFC2617, so you have to provide an Authorization: header field in your POST request
# * For the "userid" of HTTP Basic Authentication, use the same email address you put in the JSON string.
# * For the "password", provide an 10-digit time-based one time password conforming to RFC6238 TOTP.
# 
# ** You have to read RFC6238 (and the errata too!) and get a correct one time password by yourself.
# ** TOTP's "Time Step X" is 30 seconds. "T0" is 0.
# ** Use HMAC-SHA-512 for the hash function, instead of the default HMAC-SHA-1.
# ** Token shared secret is the userid followed by ASCII string value "HDECHALLENGE003" (not including double quotations).
# 
# *** For example, if the userid is "ninja@example.com", the token shared secret is "ninja@example.comHDECHALLENGE003".
# *** For example, if the userid is "ninjasamuraisumotorishogun@example.com", the token shared secret is "ninjasamuraisumotorishogun@example.comHDECHALLENGE003"
#
# If your POST request succeeds, the server returns HTTP status code 200.
#
#######################################################################

import requests
import hmac
import hashlib
import time
import sys
import struct
import json

from requests.auth import HTTPBasicAuth

root = "https://api.challenge.hennge.com/challenges/003"
content_type = "application/json"
userid = "angelo.hizon27@gmail.com"
secret_suffix = "HENNGECHALLENGE003"
shared_secret = userid+secret_suffix

timestep = 30
T0 = 0

def HOTP(K, C, digits=10):
    """HTOP:
    K is the shared key
    C is the counter value
    digits control the response length
    """
    K_bytes = str.encode(K)
    C_bytes = struct.pack(">Q", C)
    hmac_sha512 = hmac.new(key = K_bytes, msg=C_bytes, digestmod=hashlib.sha512).hexdigest()
    return Truncate(hmac_sha512)[-digits:]

def Truncate(hmac_sha512):
    """truncate sha512 value"""
    offset = int(hmac_sha512[-1], 16)
    binary = int(hmac_sha512[(offset *2):((offset*2)+8)], 16) & 0x7FFFFFFF
    return str(binary)

# time based one time password
# K = shared secret where it includes the gmail and the secret code which is angelo.hizon27@gmail.comHENNGECHALLENGE003
# digits is equal to 10 that specifies the length
# timestep means change of password every 30 seconds
# timeref dictates the difference of the current time wherein it has the value of 0 therefore it takes the current time of the day as seconds
def TOTP(K, digits=10, timeref = 0, timestep = 30):
    C = int ( time.time() - timeref ) // timestep
    return HOTP(K, C, digits = digits)

data = { 
        "github_url": "https://gist.github.com/angelohizon-coder/3158c0d6092783f5bbc0e68cfbb73a15", 
        "contact_email": "angelo.hizon27@gmail.com",
        "solution_language": "python"
     }

#zfill is a function that fills the beggining of the string with 0 until it reaches the specified length
password = TOTP(shared_secret, 10, T0, timestep).zfill(10) 
print(password)

# resp = requests.post(root, auth=HTTPBasicAuth(userid, password), data=json.dumps(data))
# print(resp.json())