import requests
import whois
import datetime
import os
from urllib.parse import urlparse
import sys


def load_urls4check(path):
    if os.path.exists(path):
        with open(path) as file_with_urls:
            return file_with_urls.read().splitlines()


def is_server_respond_with_200(url):
    ok_status_code = 200
    return requests.head(url).status_code == ok_status_code


def get_proper_domain_name_for_whois(url):
    return urlparse(url).hostname[5:]


def get_domain_expiration_date(domain_name):
    return whois.whois(domain_name)['expiration_date'].date()


def check_if_expires_over_month_or_more(domain_expiration_date):
    month_days_quantity = 30
    return (((domain_expiration_date - datetime.date.today()).days) > month_days_quantity)

def output_sites_monitoring(urls):
    for url in urls:
        print(url)
        print('Server responds with 200 code:', is_server_respond_with_200(url))
        domain_name = get_proper_domain_name_for_whois(url)
        domain_expiration_date = get_domain_expiration_date(domain_name)
        print('Server expires over month:', check_if_expires_over_month_or_more(domain_expiration_date))
        print('--------')

if __name__ == '__main__':
    if len(sys.argv) == 1:
        urls = load_urls4check(input("Enter path to file with urls you wish to check: "))
    else:
        urls = load_urls4check(sys.argv[1])
    output_sites_monitoring(urls)


