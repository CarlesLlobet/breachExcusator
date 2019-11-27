#!/usr/bin/env python
import sys
import random
from colorama import Fore, Style, init, deinit

threatActors = ["Russians", "NSA", "FBI", "North Koreans", "Chinese", "Anonymous collective", "teenage hacking prodigies", "Iranians", "KGB", "industrial spies", "competition", "Europeans", "Americans", "cyber terrorists", "advanced persistent threats", "state actors", "rogue AIs", "APTs", "Fancy Bears", "foreign assets", "master hackers", "technology whiz kids", "script kiddies", "hacking activists", "hacking people", "security community", "internet crowd"]
methods = ["0-day exploits", "unprecedented XSS vulnerabilities", "infiltrators", "overwhelming force", "botnets", "ransomware", "DDoS attacks", "IoT malware", "advanced techniques", "hacking drones", "cyborg bees", "digital nukes", "the open door in our basement", "that one vulnerability we were going to patch next Tuesday", "that other vulnerability we were going to patch next tuesday", "something something vulnerability", "vectors we really couldn't have prevented", "vulnerabilities in a 3rd party solution", "weaknesses in our vendors", "nefarious techniques", "an issue in Wordpress 1.0", "Heartbleed", "a vulnerability in Windows XP SP1", "pen and paper based social engineering", "an open window in the server room", "30 - 50 feral hogs"]
targets = ["gain access to some data", "cause a minor disturbance", "potentially access some customer data", "cause an undetermined amount of damage", "partially disrupt our services", "breach our high security servers", "glimpse into our database", "transfer 7 petabytes of data", "extract some private keys", "do something, but we aren't quite sure what it is", "make a mess", "make us look bad", "force us to release this report", "hack the coffee maker", "install a C99"]
mitigations = ["made everyone promise to be super super careful", "gotten ISO certified", "gotten PCI certified", "worked with industry leading specialists", "upskilled our cafeteria staff", "hired external consultants", "worked with law enforcement", "bought an IDS", "twiddled with our firewall", "been pretty good about security", "hired some people with 'CISSP' after their names", "watched a YouTube video on cyber security", "told them to not do it again", "said that we are very sorry", "copy-pasted a security policy we found on Google", "hired a Russian dude", "watched the movie Hackers 8 times back to back", "sent one of our guys to Defcon", "put a rotating lock GIF on our website"]

def printUsage():
    print("Usage: \n'python breachExcuse.py [-h/--help]' to print this Usage\n'python breachExcuse.py' to get a cool explanation of why you were breached")
    exit()

def selectRandomExcuse():
    print("The fucking " + Fore.RED + random.choice(threatActors) + Style.RESET_ALL + " used " + Fore.RED + random.choice(methods) + Style.RESET_ALL + " to " + Fore.RED + random.choice(targets) + Style.RESET_ALL + ".\nBut we have since " + Fore.RED + random.choice(mitigations) + Style.RESET_ALL + ", so it will never happen again!")

### MAIN ###
args = sys.argv[1:]

if len(args) > 1:
    print("ERROR: Too many arguments")
    printUsage()
else:
    if len(args) == 1:
        if str(args[0]) == "-h" or str(args[0]) == "--help":
            printUsage()
        else:
            print("ERROR: Bad argument")
            printUsage()
    else:
        init(autoreset=True)
        selectRandomExcuse()
        deinit()