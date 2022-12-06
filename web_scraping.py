import urllib.request
from bs4 import BeautifulSoup
import ssl
from twilio_text_message import twilio_text
import schedule
import time

#Test URLs: (AS50 Shuttlecocks are currently available, and "Victor Lightfighter Ultra Badminton Racket" is currently unavailable)
AS50_URL = 'https://www.badmintonwarehouse.com/products/yonex-as50-badminton-shuttles'
RACKET_URL = 'https://www.badmintonwarehouse.com/collections/deals-of-the-day/products/victor-light-fighter-ultra-badminton-racket'


def download_page(url):
    """downloads the website page"""
    context = ssl._create_unverified_context() #SSL is a temp fix to url request error on windows
    return urllib.request.urlopen(url, context = context)

# print(download_page(DOWNLOAD_URL).read())

def check_availability(html):
    """
    Analyze the html page, checks availability of product based on whether or not users can 'add to cart' or 'sold out'
    """
    soup = BeautifulSoup(html, features="html.parser")
    # print(soup.prettify())
    for atc_string in soup.find_all('span', attrs = {"class":"atc-button--text"}):
        atc_string = str(atc_string.text).replace(' ','').strip('\n')
        # print(point)
    if atc_string == 'Soldout':
        return 'Unavailable'
    else:
        return 'Available'

# check_availability(download_page(RACKET_URL).read())

def send_text_if_available():
    """Uses twilio text messaging API to send text to phone if available, otherwise prints 'unavailable for now'"""
    if check_availability(download_page(RACKET_URL)) == 'Available':
        twilio_text()
    else:
        print('Unavailable for now!')

# send_text_if_available()


def main():
    #In order to keep program running, we used the schedule and time module to keep the send_text_if_available() running
    schedule.every(5).seconds.do(send_text_if_available) #For testing purposes set to refresh 5 seconds, but when actual use probably once a day
    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == '__main__':
    main()