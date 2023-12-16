
import os
import sys
import pyfiglet
from infogather.namp import nmap
from webanalyzer.gitbot import gitusers, gitemails
from webanalyzer.linkextractor import extract
from infogather.bannergrap import banner
from infogather.subdomains import sub
from infogather.geoip import geo
from webanalyzer.wayback import waybackurl, waybackrobots, waybackjson
from webanalyzer.ghosdork import ghosdork
from infogather.dnslookup import dnslookup
from infogather.subnetlookup import subnet_lookup
from infogather.httpheaders import httpheader
from webanalyzer.techanalyzer import analyze_website

# ANSI escape codes for text colors
purple = '\033[95m'
blue = '\033[94m'
green = '\033[92m'
yellow = '\033[93m'
red = '\033[91m'
default = '\033[0m'
underline = '\033[4m'
orange = '\033[33m'

def print_banner():
    font = pyfiglet.Figlet()
    art = font.renderText("GhostHunter")
    print(yellow + art + default)

def main_menu():
    print_banner()
    print(yellow + "[!] Please note that ANSI escape codes may not work in all environments." + default)
    print(blue + "[1] Information Gathering")
    print("[2] Web Analysis")
    print("[0] Exit" + default)

def main():
    #print_banner()

    while True:
        main_menu()
        choice = input(blue + "Enter the option number (or 0 to exit): " + default)

        if choice == '0':
            sys.exit()

        if choice == '1':
            information_gathering_menu()

        elif choice == '2':
            web_analysis_menu()

        else:
            print(red + "[-] Invalid option. Please enter a valid option number." + default)

def information_gathering_menu():
    os.system('clear')
    font = pyfiglet.Figlet()
    art = font.renderText("SpectraProbe")
    print(purple + art + default)
    print(blue + "[1] Httpheaders of target url")
    print("[2] Dnslookup of target domain")
    print("[3] Subdomain lookup of target domain")
    print("[4] Nmapscan of target domain")
    print("[5] Cidr for subnetlookup of target")
    print("[6] Banner grabbing of target ip address")
    print("[7] GeoIP lookup of target ip address")
    print("[0] Back" + default)

    choice = input(blue + "Enter the option number (or 0 to go back): " + default)

    if choice == '0':
        os.system('clear')
        return

    execute_information_gathering(choice)

def execute_information_gathering(choice):
    if choice == '1':
        target_url = input("Enter the target URL: ")
        print(green + "[+] Extracting http headers of target url" + default)
        httpheader(target_url)

    elif choice == '2':
        target_domain = input("Enter the target domain: ")
        print(green + "[+] DNS lookup of target domain" + default)
        dnslookup(target_domain)

    elif choice == '3':
        target_domain = input("Enter the target domain: ")
        print(blue + "[+] Subdomain lookup from target domain" + default)
        sub(target_domain)

    elif choice == '4':
        target_domain = input("Enter the target domain: ")
        print(green + "[+] Port scanning of target domain" + default)
        nmap(target_domain)

    elif choice == '5':
        cidr = input("Enter the CIDR for subnetlookup of target: ")
        subnet_lookup(cidr)

    elif choice == '6':
        target_ip = input("Enter the target IP address: ")
        print(green + "[+] Banner Grabbing from target ip address" + default)
        banner(target_ip)

    elif choice == '7':
        target_ip = input("Enter the target IP address: ")
        print(green + "[+] Geoip lookup of target Ip address" + default)
        geo(target_ip)

    else:
        print(red + "[-] Invalid option. Please enter a valid option number." + default)

def web_analysis_menu():
    os.system('clear')
    font = pyfiglet.Figlet()
    art = font.renderText("GhostWebAnalyzer")
    print(purple + art + default)
    print(blue + "[1] Github username of target")
    print("[2] Web Detail detect with headers url of target")
    print("[3] Extract links from target url (https/http)")
    print("[4] Internet Archive Crawling of target domain")
    print("[5] Google Dorking")
    print("[0] Back" + default)

    choice = input(blue + "Enter the option number (or 0 to go back): " + default)

    if choice == '0':
        os.system('clear')
        return

    execute_web_analysis(choice)

def execute_web_analysis(choice):
    if choice == '1':
        github_username = input("Enter the Github username: ")
        gitusers(github_username)
        gitemails(github_username)

    elif choice == '2':
        target_url = input("Enter the target URL: ")
        print(green + "[+] Detecting Web Detail with Identified Technologies and Custom Headers from target url" + default)
        analyze_website(target_url)

    elif choice == '3':
        target_url = input("Enter the target URL (https/http): ")
        print(green + "[+] Extracting all hidden and visible links from target url" + default)
        extract(target_url)

    elif choice == '4':
        target_domain = input("Enter the target domain: ")
        print(green + "[+] Dumping and Crawling Internet Archive Machine With Ashok" + default)
        waybackurl(target_domain)
        waybackrobots(target_domain)
        waybackjson(target_domain)

    elif choice == '5':
        ghosdork()
        
    else:
        print(red + "[-] Invalid option. Please enter a valid option number." + default)

if __name__ == "__main__":
    main()
