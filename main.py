import requests
import os
import argparse
from dotenv import load_dotenv
from urllib.parse import urlparse, parse_qs

API_STATS_URL = 'https://api.vk.ru/method/utils.getLinkStats'
API_SHORTEN_URL = 'https://api.vk.ru/method/utils.getShortLink'
API_VERSION = '5.199'

def shorten_link(token, url):
    payload = {
        'url': url,
        'access_token': token,
        'v': API_VERSION,
    }
    response = requests.post(API_SHORTEN_URL, data=payload)
    response.raise_for_status()
    fetched_data = response.json()
    if 'error' in fetched_data:
        raise Exception(f"VK API Error: {fetched_data['error']}")
    return fetched_data['response']['short_url']

def count_clicks(token, parsed_url):
    key = parsed_url.path.strip('/')
    payload = {
        'key': key,
        'access_token': token,
        'v': API_VERSION,
        'interval': 'forever',
    }
    response = requests.post(API_STATS_URL, data=payload)
    response.raise_for_status()
    fetched_data = response.json()
    if 'error' in fetched_data:
        raise Exception(f"VK API Error: {fetched_data['error']}")
    return fetched_data['response']['stats'][0]['views']

def is_shorten_link(token, url):
    key = urlparse(url).path.strip('/')
    payload = {
        'key': key,
        'access_token': token,
        'v': API_VERSION,
        'interval': 'forever',
    }
    response = requests.post(API_STATS_URL, data=payload)
    response.raise_for_status()
    api_response = response.json()
    return 'error' not in api_response

def main():
    load_dotenv()
    token = os.environ['VK_API']
    parser = argparse.ArgumentParser(description="Получить информацию по укороченной ссылке или укоротить ссылку.")
    parser.add_argument("url", help="Введите ссылку.")
    args = parser.parse_args()
    url = args.url

    try:
        if is_shorten_link(token, url):
            parsed_url = urlparse(url)
            print(f"Кликов по ссылке: {count_clicks(token, parsed_url)}")
        else:
            print(f"Короткая ссылка: {shorten_link(token, url)}")
    except requests.exceptions.HTTPError as e:
        print(f"HTTP Error: {e}")
    except requests.exceptions.RequestException as e:
        print(f"Request Error: {e}")
    except ValueError as e:
        print(f"JSON Error: {e}")
    except Exception as e:
        print(f"Error: {e.args}")

if __name__ == "__main__":
    main()