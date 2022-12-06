# OIM Term Project - Web Scraping for Badminton Warehouse

1. Project Proposal [project_proposal](project_proposal.md). 

2. Libraries to install

- Signup for a Twilio account here because this application will use the Twilio messaging API to send messages to yourself or friends. After signing up, you need to download the **Twilio** library by typing "**pip3 install twilio**" in your command prompt.
- **Beautifulsoup** is a Python library for pulling data from HTML and XML files. Install Beautifulsoup by typing "**pip install beautifulsoup4**" in your command prompt.
- **SSL** is a wrapper for socket objects, and we used it because we had trouble requesting the URL for Badminton Warehouse and SSL solved our issue. Install by typing "**pip install ssl**" in your command prompt.
- **Schedule** is a simple API for scheduling or running Python functions (or any other callable) periodically using a friendly syntax. Install by typing "**pip install schedule**" in your command prompt.

3. How to run the code:
    1. You will first need to signup for your own **Twilio** account at https://www.twilio.com/try-twilio
    2. Then in the **Twilio Console**, you can find your own **SID** and **Authentication Token**.
    3. Create your own **credentials.py** or **config.py** to store your sensitive information including your **SID**, **Authentication Token** and **NUMBERS** which is a list of numbers you'd like to send the messages to. Format for **NUMBERS** should be [+0123XXXX890, +1234XXXX901, etc]
    4. Get product URL by picking a product you want to buy from https://www.badmintonwarehouse.com/ but is currently sold out.
    5. Copy and Paste the URL to **web_scraping.py** and name it whatever you'd like.
    6. Go down to the **send_text_if_available()** function and change the URL to the product URL you'd like to purchase once available.
    7. Run the program and the application will send you a text when product becomes available!

4. VOILA!!!!