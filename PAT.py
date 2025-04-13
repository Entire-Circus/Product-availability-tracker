"""
PAT.py

Simple product availability tracker that scrapes the website and sends result to telegram bot if products are available

Autor: Lysenko Alexander
Date: 13-04-2025

"""

# Library imports
import asyncio  # To handle asynchronous tasks
import urllib.request  # For sending HTTP requests to fetch product pages
from bs4 import BeautifulSoup  # For parsing HTML content and extracting data
import random  # For generating random delays between checks
from telegram import Bot  # To send notifications to Telegram

# --- TELEGRAM CONFIG ---
TOKEN = "Your_token_here"
CHAT_ID = "Your_chatid_here"

bot = Bot(token=TOKEN)

# --- GLOBAL STATE VARIABLES ---
urls = []  # List to store URLs to monitor
running = True  # Flag to control while loop for continuous monitoring


# --- TELEGRAM NOTIFICATION ---
async def notify_telegram(message):
    try:
        # Send the message to the Telegram bot
        await bot.send_message(chat_id=CHAT_ID, text=message)
    except Exception as e:
        # In case of failure, print error for debugging
        print(f"[ERROR] Telegram send failed: {e}")

# --- USER INPUT (synchronously) ---
def get_user_input():
    global urls
    while True:
        # Ask the user for how many URLs they want to monitor
        amount_input = input("How many URLs do you want to monitor? Enter a number and press Enter: ")
        # Prevents user from breaking the script by enterning incorrect values
        if amount_input.isdigit() and int(amount_input) > 0:
            amount = int(amount_input)
            break
        else:
            print("Enter a valid positive number.\n")

    for _ in range(amount):
        while True:
            # Prompt the user to input the URL for monitoring
            url = input(f"Paste URL and press Enter ({amount} remaining): ")
            # Prevents user from breaking the script by enterning incorrect urls
            if url.startswith("http"):
                urls.append(url)
                amount -= 1
                break
            else:
                print("Enter a valid url.\n")

    print(f"Your URLs are: {urls}")

# --- AVAILABILITY CHECK ---
async def check_product_availability(url):
    while running:
        # try block allows the script to continue working even if scraping part crashes
        try:
            # Send a get request to URL and read the response
            request = urllib.request.urlopen(url).read()
            # Decode the bytes to str
            data = request.decode()
            # Parse the data with BeautifulSoup
            soup = BeautifulSoup(data, "html.parser")

            # Find the div that contains product's information
            code_wrap = soup.find("div", class_="product-item__code-wrap")
            # Find the product availability itself
            availability = code_wrap.find("div", class_="product-item__status green", id="product_enabled")
            # Extract the name of the product
            name = soup.find("span", class_="product-item__name")

            if availability:
                print(f"Product: {name.text} is available")
                # Send message trough telegram bot whe prodcut is available
                await notify_telegram(f"Product: {name.text} is available")
            else:
                print(f"Product: {name.text} is not available")

            # Sets up random delay to avoid overloading the site
            delay = random.randint(5, 30)
            interval = delay * 60 # convert delay to seconds
            print(f"Next check is in {delay} minutes / {interval} seconds")

            for _ in range(interval):
                if not running:
                    return
                await asyncio.sleep(1)
        # Returs error for easier debugging
        except Exception as e:
            print(f"[ERROR] Failed to check {url}: {e}")
            await asyncio.sleep(10)

# --- MONITOR USER INPUT TO STOP SCRIPT ---
# Waits for the user to press Enter to stop monitoring
async def wait_for_exit():
    global running
    # Moves input to separate thread to allow async functions to run simultaneously
    await asyncio.to_thread(input, "Press Enter to stop monitoring...\n")
    running = False
    print("Shutting down...")
    await notify_telegram("Shutting down...")

# --- MAIN EVENT LOOP ---
async def main():
    get_user_input()
    print("Monitoring products ...")
    # Create a list of tasks to check product availability for each UR
    tasks = [check_product_availability(url) for url in urls]
    # Add the wait_for_exit function to stop the script
    tasks.append(wait_for_exit())
    # Shedules coroutines to run concurently
    await asyncio.gather(*tasks)
# Starts the script
asyncio.run(main())