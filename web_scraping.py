import csv
import urllib.request
from bs4 import BeautifulSoup
import ssl
from twilio_text_message import twilio_text
import schedule
import time
import string


AS50_URL = 'https://www.badmintonwarehouse.com/products/yonex-as50-badminton-shuttles'
RACKET_URL = 'https://www.badmintonwarehouse.com/collections/deals-of-the-day/products/victor-light-fighter-ultra-badminton-racket'


def download_page(url):
    context = ssl._create_unverified_context() #SSL is a temp fix to url request error on windows
    return urllib.request.urlopen(url, context = context)

# print(download_page(DOWNLOAD_URL).read())

def check_availability(html):
    """
    Analyze the html page, find the information and return the move list of tuples (movie_name, year)
    """
    soup = BeautifulSoup(html, features="html.parser")
    # print(soup.prettify())
    for atc_string in soup.find_all('span', attrs = {"class":"atc-button--text"}):
        atc_string = str(atc_string.text).replace(' ','').strip('\n')
        # print(point)
    if atc_string == 'Soldout':
        return 'Unvailable'
    else:
        return 'Available'

# check_availability(download_page(RACKET_URL).read())

def send_text_if_available():
    if check_availability(download_page(AS50_URL)) == 'Available':
        twilio_text()
    else:
        print('Unavailble for now')

# send_text_if_available()


def main():
    schedule.every(1).hour.do(send_text_if_available)
    while True:
        schedule.run_pending()
        time.sleep(1)
    


if __name__ == '__main__':
    main()