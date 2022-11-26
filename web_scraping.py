import csv
import urllib.request
from bs4 import BeautifulSoup


DOWNLOAD_URL = 'https://www.badmintonwarehouse.com/products/yonex-as50-badminton-shuttles'


def download_page(url):
    return urllib.request.urlopen(url)

print(download_page(DOWNLOAD_URL).read())

# def parse_html(html):
#     """
#     Analyze the html page, find the information and return the move list of tuples (movie_name, year)
#     """
#     soup = BeautifulSoup(html, features="html.parser")
#     print(soup.prettify())

# # parse_html(download_page(DOWNLOAD_URL).read())

# def main():
#     url = DOWNLOAD_URL
    


# if __name__ == '__main__':
#     main()