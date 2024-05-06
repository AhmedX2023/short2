from playwright.sync_api import Playwright, sync_playwright, expect
from time import sleep
import requests
import re
from base64 import b64decode
import random
from playwright_recaptcha import recaptchav2
from string import ascii_lowercase
from playwright_stealth import stealth_sync,StealthConfig
username = "uoqph5vvr3t2pez"
password = "iegnw755bxqn2lv"
proxy = "rp.proxyscrape.com:6060"

def devode(im):
    from base64 import b64decode
    print(im)
    rt= b64decode(im)
    return rt

def getcap():
        import easyocr
        reader = easyocr.Reader(['en'],gpu=False) # this needs to run only once to load the model into memory
        result = reader.readtext('D:\\hp\\desktop\\aa1.jpg',detail=0)
        if result == '' or result == ' ' or result == None:
            return 777
        try:
            rp=result[0]
            return rp
        except:
            return 14
from typing import Generator
from pathlib import Path
from playwright.sync_api import Playwright, BrowserContext
import pytest
from string import ascii_lowercase
from playwright.sync_api import Playwright, sync_playwright, expect
from time import sleep
from playwright_stealth import stealth_sync
from random import randint,choice 
import phonenumbers

import random
from string import ascii_lowercase
from phonenumbers import geocoder
names=open('names.txt').readlines()
proxyes=open('proxyes.txt').readlines()
numbers=open('numbers.txt').readlines()
password=''.join(choice(ascii_lowercase) for i in range(13))
bv=''
h=[]
def getcant(p):
    import pycountry , phonenumbers
    from phonenumbers.phonenumberutil import region_code_for_number
    
    pn = phonenumbers.parse('+'+p)
    
    country = pycountry.countries.get(alpha_2 = region_code_for_number(pn))
    
    return country.name


def run(playwright: Playwright) -> None:
    global browser,context
    for number in numbers:
        
        pro=random.choice(proxyes)
        print(f"{pro}:{random.randint(10000,10248)}")
        ignonumber=open('ignonum.txt','r')
        ignonumber2=ignonumber.readlines()
      #  print(ignonumber2)
        ignoproxy=open('ignopro.txt','r')
        ignoproxy2=ignoproxy.readlines()
        if number in ignonumber2:
            continue
        else:
        #  if pro in ignoproxy2:
        #     continue                  
            #h.append(number)
            ignonumber=open('ignonum.txt','a')
        
            ignoproxy=open('ignopro.txt','a')
            ignonumber.write(number)
            ignoproxy.write(pro)
            nam=random.choice(names)
            pasw=''.join(random.choice(ascii_lowercase) for iqq in range(13))
            email=''.join(random.choice(ascii_lowercase) for iqq in range(8))+"@gmail.com"
            #print(random.choice(proxyes))
            #import win32com.shell.shell as shell
        # commands = 'echo hi'
            #shell.ShellExecuteEx(lpVerb='runas', lpFile='cmd.exe', lpParameters='/c '+commands)
            number2=number
            
            ch_number = phonenumbers.parse(f'+{number}')
            #print(Fore.GREEN+f'Number Info: '+geocoder.description_for_number(ch_number,'en')+': '+str(i))
            cun=geocoder.description_for_number(ch_number,'en')
            if len(str(ch_number.country_code))==2 :
                number=number[2:]
            else:
                number=number[3:]
            bv=number
            browser = playwright.chromium.launch(headless=False,proxy={'server':pro})
            context = browser.new_context()
            page = context.new_page()
            stealth_sync(page=page,config=StealthConfig(webdriver=False,nav_platform=False,nav_user_agent=False,navigator_hardware_concurrency=False,chrome_runtime=False))
            '''
            page.goto("https://www.croxyproxy.rocks/",wait_until='domcontentloaded',timeout=4000)
            page.get_by_placeholder("Enter an URL or a search query to access").click()
            page.get_by_placeholder("Enter an URL or a search query to access").fill("hhttps://www.astrosage.com/")
            page.get_by_role("button", name="Go!").click()
            '''
            #sleep(400000)
            page.goto("https://www.astrosage.com/",wait_until='domcontentloaded',timeout=4000)
            #sleep(2222)
            selector = "#appNavbar > div.collapse.navbar-collapse > ul > li > button > a.ln"
            x_pos = page.evaluate(f"""document.querySelector('{selector}').getBoundingClientRect()['x']""".format(selector))
            y_pos = page.evaluate(f"""document.querySelector('{selector}').getBoundingClientRect()['y']""".format(selector))
            page.mouse.move(x=x_pos, y=y_pos, steps=100)
            page.hover(selector)

            page.click(selector)
            page.locator('xpath=/html/body/div[2]/div[3]/div[4]/div/div/div/div[2]/div[3]/div[1]/span').click()

            page.keyboard.press('Tab')
        
            page.keyboard.press('Enter')
            page.keyboard.press('Enter')
          #  page.locator("xpath=/html/body/div[1]/div[2]/ul/li/button/a[1]").click()
            page.locator("#countrycode").select_option(f"{ch_number.country_code}")
            page.get_by_placeholder("Mobile number").click()
            page.get_by_placeholder("Mobile number").fill(f"{number}")
            page.get_by_role("button", name="Get OTP").click()
            sleep(4)

            # --------------------- 
            context.close()
            browser.close()




while 1:
    try:
        with sync_playwright() as playwright:
            run(playwright)
    except Exception as e:
        print(e)
        
       # exit()
        pass
