
import json
import warnings
from os import system
from Wappalyzer import Wappalyzer, WebPage
import requests
import time


# ANSI escape codes for text colors
purple = '\033[95m'
blue = '\033[94m'
green = '\033[92m'
yellow = '\033[93m'
red = '\033[91m'
default = '\033[0m'
underline = '\033[4m'
orange = '\033[33m'

def analyze_website(url):
    start = time.time()
    try:
        webpage = WebPage.new_from_url(url)
        warnings.simplefilter("ignore")
        wappalyzer = Wappalyzer.latest()
        tech = wappalyzer.analyze_with_versions_and_categories(webpage)
        data = json.dumps(tech, indent=4)

        # Print the data with red text
        print(red + data + default)  
    except requests.exceptions.RequestException as e:
        # Print error message in red
        print('\033[91m' + f"[+] Error: {e}" + '\033[0m')
    except Exception as e:
        # Print unexpected error message in red
        print('\033[91m' + f"[+] Unexpected Error: {e}" + '\033[0m')

    end = time.time()
    print(f"\n[+] Total Execution Time: {end - start} seconds\n\n")

