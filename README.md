Product Availability Tracker (PAT)
A simple Python script to monitor product availability on websites and send notifications via Telegram when a product is available.
Constructed specifically for site https://www.makeup.com (Makeup.com)

Author: Lysenko Alexander
Date: 13-04-2025

Description

Script gathers urls of products provided by user and continioulsy checks part of the code responsible for availabilty.

It used random intervals set from 5 to 30 seconds to avoid overloading the site.

When product becomes available it messages the user via telegram bot 

Features

Scrapes product pages for availability.

Sends real-time notifications via Telegram.

Customizable monitoring intervals with random delays.

Simple command-line interface to add URLs.

Continuous monitoring until stopped manually.

Usage

The script wil promt you to enter number of ulrs you want to monitor

Enter the urls pressinf Enter after each one

Once all URLs are entered, the script will start monitoring them and will notify you via Telegram when a product becomes available.

Configuration

Before running the script, configure it to use your Telegram bot token and chat ID.

Create a Telegram bot and obtain your bot token from BotFather.

Replace the placeholders in the script with your actual TOKEN and CHAT_ID.
