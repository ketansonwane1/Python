import argparse
import requests
import pyfiglet
import threading
from colorama import Fore

print("************************************************************************************************************************************************************")
print(Fore.CYAN)

print('''      
                        $$$$$$$\                       $$\                                                                      
                        $$  __$$\                      $$ |                                                                     
                        $$ |  $$ | $$$$$$\   $$$$$$\ $$$$$$\          $$$$$$$\  $$$$$$$\ $$$$$$\  $$$$$$$\   $$$$$$\   $$$$$$\ 
                        $$$$$$$  |$$  __$$\ $$  __$$\\_$$  _|        $$  _____|$$  _____|\____$$\ $$  __$$\ $$  __$$\ $$  __$$\ 
                        $$  ____/ $$ /  $$ |$$ |  \__| $$ |          \$$$$$$\  $$ /      $$$$$$$ |$$ |  $$ |$$$$$$$$ |$$ |  \__|
                        $$ |      $$ |  $$ |$$ |       $$ |$$\        \____$$\ $$ |     $$  __$$ |$$ |  $$ |$$   ____|$$ |       
                        $$ |      \$$$$$$  |$$ |       \$$$$  |      $$$$$$$  |\$$$$$$$\\$$$$$$$ |$$ |  $$ |\$$$$$$$\ $$ |      
                        \__|       \______/ \__|        \____/       \_______/  \_______|\_______|\__|  \__| \_______|\__|
                                                                                                |
|--------------------------------------------------------------------Coded by Ketan------------------------------------------------------------------------|
''') 

print("\n                                                    Github: https://github.com/ketansonwane1                                                          \n")

print("************************************************************************************************************************************************************")

print("Ports scanning is strated")
print(Fore.MAGENTA)
def check_status(domain):
    try:
        # Check Status for HTTP
        http_response = requests.head("http://" + domain, allow_redirects=True, timeout=10)
        http_status_code = http_response.status_code

        # Check HTTPS
        https_response = requests.head("https://" + domain, allow_redirects=True, timeout=10)
        https_status_code = https_response.status_code

        # Print status codes
        if http_status_code == 200:
            print(f"Domain: http://{domain}-Status Code: 200 (OK)")
        elif https_status_code in [301, 302]:
            print(f"Domain: https://{domain}-Status Code: {http_status_code} (Redirect)")
        elif http_status_code == 403:
            print(f"Domain: http://{domain}-Status Code: 403 (Forbidden)")
        else:
            print(f"Domain: http://{domain}-Status Code: {http_status_code}")
    except requests.RequestException as e:
        print(f"Domain: {domain} -Connectio Timeout ")

parser = argparse.ArgumentParser(description="Check status codes of HTTP and HTTPS domains.")
parser.add_argument("-f", help="enter Valid filename")
args = parser.parse_args()

# Read the domains from the file
file = open(args.f, "r")
domains = file.readlines()
file.close()
threads = []
for domain in domains:
    domain = domain.strip()
    thread = threading.Thread(target=check_status, args=(domain,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()
print("--------------------------------------------------------------------Thank-you------------------------------------------------------------------------------")
