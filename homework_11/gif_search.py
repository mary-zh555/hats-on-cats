import requests
from urllib import parse
import questionary
import credentials


def _encode(ukr_text: str) -> str:
    return parse.quote(ukr_text)


def choose_lang():
    languages = {
        "English": "eng",
        "Українська": "uk",
    }

    lang = questionary.select(
        "Choose language/Обери мову", choices=[*languages.keys()]
    ).ask()

    return languages[lang]


def get_user_input():
    lang: str = choose_lang()
    query: str = ""
    number: str = ""
    choice: dict = dict()
    min_num, max_num = 1, 50

    ENG_TEXT: dict = {
        "question": "What gif you want to find?",
        "limit": "How many do you want to see?",
        "instructions": f"Input a number in range {min_num}-{max_num}.",
        "num_error": "WRONG number. Please try again!",
    }

    UKR_TEXT: dict = {
        "question": "Яку гіфку ти шукаєш?",
        "limit": "Скільки ти хочеш побачити?",
        "instructions": f"Введіть число в діапазоні {min_num}-{max_num}.",
        "num_error": "НЕПРАВИЛЬНИЙ номер. Спробуйте ще раз!",
    }

    if lang == "eng":
        choice = ENG_TEXT
    if lang == "uk":
        choice = UKR_TEXT

    query = questionary.text(choice["question"]).ask()
    number = questionary.text(choice["limit"], instruction=choice["instructions"]).ask()

    if int(number) not in range(min_num, max_num):
        questionary.print(choice["num_error"], style="bold italic fg:darkred")

    print(query, lang, number)
    return (lang, query, number)


def send_request(lang: str, query: str, num: str):
    url = "http://api.giphy.com/v1/gifs/search"
    API_KEY = credentials.API_KEY
    params = parse.urlencode(
        {
            "q": query,
            "api_key": API_KEY,
            "limit": num,
            "lang": lang,
            "offset": 0,
            "bundle": "messaging_non_clips",
        }
    )

    req = requests.get(url, params=params)
    # print(req.url)
    return req.json()


def return_urls(resp):
    original_url = title = ""
    my_list = list()
    for obj in resp["data"]:
        original_url = obj["images"]["original"]["url"]
        title = obj["title"] if obj["title"] else "GIF"
        my_list.append([original_url, title])
    return my_list


def print_search_results(data_list: list):
    for img in data_list:
        url, title = img
        questionary.print(f"{title}:", style="bold fg:orange")
        questionary.print(f"    {url}\n", style="italic fg:#3366CC")


if __name__ == "__main__":
    input = get_user_input()
    request = send_request(*input)
    data = return_urls(request)
    print_search_results(data)
