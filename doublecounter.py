import requests

def main():

    while True:
        code = input("[+] Please, insert a valid Double Counter verification link / code here: ").strip()

        if code.startswith("https://"):
            code = code[len("https://"):]
        if code.startswith("http://"):
            code = code[len("http://"):]
        if code.startswith("www."):
            code = code[len("www."):]

        if code.startswith("verify.doublecounter.gg/v/"):
            code = code[len("verify.doublecounter.gg/v/"):]

        if len(code) < 3:
            print("[+] Inserted link or code is not valid.")
            continue

        url = f"https://verify.doublecounter.gg/v/{code}"

        headers = {
            "Host": "verify.doublecounter.gg",
            "Connection": "keep-alive",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
            "Sec-Fetch-Site": "same-origin",
            "Sec-Fetch-Mode": "navigate",
            "Sec-Fetch-User": "?1",
            "Sec-Fetch-Dest": "document",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "en-US,en;q=0.9"
        }

        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            print("[+] Successfully Bypassed Double Counter.")
            break
        else:
            print(f"[+] Failed to verify. Status code: {response.status_code}. Please try again.")

if __name__ == "__main__":
    main()
