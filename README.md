# Product Availability Tracker (PAT)
A simple Python script to monitor product availability on websites and send notifications via Telegram when a product becomes available. Constructed specifically for the site https://makeup.com.ua (MAKEUP) and https://eva.ua/ (eva.ua).

Author: Lysenko Alexander
Date: 13-04-2025

---

# Description:
The script gathers URLs of products provided by the user and continuously checks the code responsible for availability. It uses random intervals (5 to 30 minutes) to avoid overloading the site. When a product becomes available, the script sends a notification via Telegram.

---

# Features:

- Scrapes product pages for availability.

- Sends real-time notifications via Telegram.

- Customizable monitoring intervals with random delays.

- Simple command-line interface for adding URLs.

- Continuous monitoring until manually stopped.

---

# Usage:

The script will prompt you to enter the number of URLs you want to monitor.

Enter the URLs, pressing Enter after each one.

Once all URLs are entered, the script will begin monitoring them and notify you via Telegram when a product becomes available.

---

# Configuration:

Before running the script, configure it with your Telegram bot token and chat ID:

Create a Telegram bot and obtain your bot token from BotFather.

Replace the placeholders in the script with your actual TOKEN and CHAT_ID.

---

# Example Output:

Use existing config? (y/n): n

How many URLs do you want to monitor? Enter a number and press Enter: 2

Paste URL and press Enter (2 remaining): https://eva.ua/ua/pr1431541/

Paste URL and press Enter (1 remaining): https://makeup.com.ua/ua/product/1120231/#/option/2649605/

Your URLs are: ['https://eva.ua/ua/pr1431541/', 'https://makeup.com.ua/ua/product/1120231/#/option/2649605/']

Monitoring products ...

Product: Гель для душу Green Way Чорна орхідея, жіночий, 750 мл is available

Product: Освітлювальна ампульна сироватка для обличчя is not available

Next check is in 18 minutes / 1080 seconds

Next check is in 29 minutes / 1740 seconds

Press Enter to stop monitoring...

Telegram Bot Notification:

"Product: Гель для душу Green Way Чорна орхідея, жіночий, 750 мл is available from https://eva.ua/ua/pr1431541/"

"Product: Освітлювальна ампульна сироватка для обличчя is not available from https://makeup.com.ua/ua/product/1120231/#/option/2649605/"

"Shutting down..."
