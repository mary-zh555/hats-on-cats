import requests
from urllib import parse
from random import randint
import os
from dotenv import load_dotenv
from os.path import join, dirname


dotenv_path = join(dirname(__file__), ".env.example")
load_dotenv(dotenv_path)

api_key = os.getenv("api_key", " ")


def send_request(lang: str, query: str, num: str):
    url = "http://api.giphy.com/v1/gifs/search"
    API_KEY = api_key
    params = parse.urlencode(
        {
            "q": query,
            "api_key": API_KEY,
            "limit": num,
            "lang": lang,
            "offset": randint(1, 4999),
            "bundle": "messaging_non_clips",
        }
    )

    req = requests.get(url, params=params)
    return req.json()


def return_urls(resp) -> list:
    original_url = title = ""
    my_list = list()
    for obj in resp["data"]:
        original_url = obj["images"]["original"]["url"]
        title = obj["title"] or "GIF"
        my_list.append([original_url, title])
    return my_list
