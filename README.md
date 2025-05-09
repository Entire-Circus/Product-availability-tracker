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
How many URLs do you want to monitor? Enter a number and press Enter: 4

Paste URL and press Enter (4 remaining): https://makeup.com.ua/ua/product/3608/

Paste URL and press Enter (3 remaining): https://makeup.com.ua/ua/product/488791/#/option/2000573/

Paste URL and press Enter (2 remaining): https://eva.ua/ua/pr477887/

Paste URL and press Enter (1 remaining): https://eva.ua/ua/pr1535891/

Your URLs are: ['https://makeup.com.ua/ua/product/3608/', 'https://makeup.com.ua/ua/product/488791/#/option/2000573/', 'https://eva.ua/ua/pr477887/', 'https://eva.ua/ua/pr1535891/']

Monitoring products ...

Product: Rabanne 1 Million is available from https://makeup.com.ua/ua/product/3608/

Next check is in 17 minutes / 1020 seconds

Product: Kiko Milano Long Lasting Colour Lip Marker is not available

Next check is in 13 minutes / 780 seconds

Product: Ліфтинг-крем для обличчя Medi-Peel Peptide-Tox Bor Cream з пептидним комплексом, 1.5 мл is available  from https://eva.ua/ua/pr477887/

Next check is in 17 minutes / 1020 seconds

Product: Фотоепілятор Philips Lumea Series 9000 BRI973/00 is available  from https://eva.ua/ua/pr1535891/

Next check is in 20 minutes / 1200 seconds

Press Enter to stop monitoring...

Shutting down...

Telegram Bot Notification:

"Product: Rabanne 1 Million is available from https://makeup.com.ua/ua/product/3608/"

"Product: Ліфтинг-крем для обличчя Medi-Peel Peptide-Tox Bor Cream з пептидним комплексом, 1.5 мл is available  from https://eva.ua/ua/pr477887/"

"Product: Фотоепілятор Philips Lumea Series 9000 BRI973/00 is available  from https://eva.ua/ua/pr1535891/"

"Shutting down..."
