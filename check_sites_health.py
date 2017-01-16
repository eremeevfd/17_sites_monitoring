import requests
import pythonwhois
import datetime
import os
from urllib.parse import urlparse
import logging
import argparse
from collections import defaultdict


logging.basicConfig(level='INFO')
logger = logging.getLogger(__name__)


def create_arguments_parser():
    parser = argparse.ArgumentParser(description='Load file with urls.')
    parser.add_argument('input', help='path to file to load')
    return parser


def load_urls4check(path):
    if os.path.exists(path):
        with open(path) as file_with_urls:
            return file_with_urls.read().splitlines()


def is_server_respond_with_200(url):
    return requests.get(url).status_code == requests.codes.ok


def get_proper_domain_name_for_whois(url):
    return urlparse(url).netloc


def get_domain_expiration_date(domain_name):
    return pythonwhois.get_whois(domain_name).get('expiration_date')[0]


def check_if_expires_over_month_or_more(domain_expiration_date):
    month_days_quantity = 30
    return ((domain_expiration_date - datetime.datetime.today()).days) > month_days_quantity


def check_sites_health(urls):
    sites_health = defaultdict(dict)
    for url in urls:
        sites_health[url]['Response_200'] = is_server_respond_with_200(url)
        sites_health[url]['Expires_over_month'] = check_if_expires_over_month_or_more(
                get_domain_expiration_date(
                    get_proper_domain_name_for_whois(
                        url)
            )
        )
    return sites_health


def output_sites_monitoring(sites_health):
    for site, health in sites_health.items():
        print('{0}: Responds with code 200: {1} | Domain is paid for over a month: {2}'.format(
            site,
            'Yes' if health['Response_200'] else 'No',
            'Yes' if health['Expires_over_month'] else 'No')
        )


if __name__ == '__main__':
    parser = create_arguments_parser()
    arguments = parser.parse_args()
    urls = load_urls4check(arguments.input)
    sites_health = check_sites_health(urls)
    output_sites_monitoring(sites_health)


