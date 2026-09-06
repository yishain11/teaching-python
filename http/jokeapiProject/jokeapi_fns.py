import requests as req
import json
import os
import dotenv

dotenv.load_dotenv()


def get_joke_main():
    tries = 0
    max_tries = int(os.getenv("NUM_OF_TRIES"))
    valid_joke = None
    while tries < max_tries:
        tries += 1
        try:
            joke_json = send_joke_req()
            isValid = clean_validate_joke(joke_json) and content_validate_joke(
                joke_json
            )
            if not isValid:
                continue
            else:
                valid_joke = joke_json
                break
        except Exception as e:
            print(e)
            return False
    if valid_joke:
        joke_stats = process_joke(valid_joke["joke"])
        show_joke(valid_joke["joke"], joke_stats)
        return valid_joke["joke"]
    else:
        print("no joke to show")
        return


def send_joke_req():
    joke_base_url = os.getenv("JOKE_BASE_URL")
    if joke_base_url:
        r = req.get(joke_base_url)
        joke_json = r.json()
        return joke_json
    raise ValueError(
        "didnt find the base url env var. make sure you have .env and the key JOKE_BASE_URL"
    )


def clean_validate_joke(joke_json):
    flags_json = joke_json["flags"]
    for flag in flags_json:
        bool_value = flags_json[flag]
        if bool_value == True:
            return False
    if joke_json["safe"] == False:
        return False
    print("Joke is valid")
    return True


def content_validate_joke(joke_json):
    if "joke" not in joke_json:
        return False
    if not isinstance(joke_json["joke"], str) or len(joke_json["joke"].strip()) == 0:
        return False
    return True


def process_joke(joke):
    num_of_chars = 0
    num_of_words = len(joke.split(" "))
    for char in joke:
        num_of_chars += 1
    return (num_of_chars, num_of_words)


def show_joke(joke, stats):
    print("Joke is:\n", joke)
    print(f"num of chars: {stats[0]}\nnum of words: {stats[1]}")
